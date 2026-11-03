"""Gera os CSVs históricos da etapa E1/E3 a partir das páginas capturadas (textos no repositório documentacao).

Nenhum número vem digitado de memória: tudo é lido dos .txt capturados por coletar-fonte.py, menos as linhas descritivas
(medidas tarifárias, impeachment, intimações), que trazem o arquivo de origem na coluna de fonte e são conferidas por
assert contra o texto capturado.

Uso: python dados/gerar_historico.py
Saídas: dados/e1_midterms.csv, e3_vetos_por_congresso.csv, e3_tarifa_media.csv, e3_impeachment_e_oversight.csv,
        e3_shutdowns_por_ano_fiscal.csv. Imprime as médias de perda de cadeiras.
"""
from __future__ import annotations

import csv
import json
import re
import statistics as st
from pathlib import Path

DADOS = Path(__file__).resolve().parent
TXT = Path(r"C:/Users/Gabriel/Downloads/repositorios/documentacao/referencias-conteudo/roteiros/videos-longos"
           r"/VIDEO_024_ELEICOES_EUA_2026/referencias/textos/historico")


def ler(nome: str) -> str:
    return (TXT / f"{nome}.txt").read_text(encoding="utf-8")


def confere(nome: str, trecho: str) -> str:
    """Trava: o trecho citado tem de estar no texto capturado. Devolve o nome da fonte."""
    if " ".join(trecho.split()) not in " ".join(ler(nome).split()):
        raise SystemExit(f"Trecho não está em {nome}: {trecho}")
    return nome


def achatar(t: str) -> str:
    return re.sub(r"\s+", " ", t)


# ---------- UCSB: aprovação e variação de cadeiras ----------
PRESIDENTES = {}
CEL = r"(--|nd|\d+)"
RE_UCSB = re.compile(
    r"\b(19[3-9]\d|20[0-2]\d) (?:(?:LD\*?|†|±) )?([A-Z][A-Za-z\.\-,\(\) ]+?) ([DR]) "
    + " ".join([CEL] * 6) + r" (\d+) (\d+) ([+-]\d+) ([+-]?\d+)")


def ler_ucsb() -> dict:
    t = achatar(ler("ucsb-seats-midterm"))
    saida = {}
    for m in RE_UCSB.finditer(t):
        ano = int(m.group(1))
        cels = [m.group(i) for i in range(4, 10)]
        num = [int(c) for c in cels if c.isdigit()]
        saida[ano] = {"presidente": m.group(2).strip(), "partido": m.group(3), "aprov": num[-1] if num else None,
                      "camara": int(m.group(12)), "senado": int(m.group(13))}
    return saida


# ---------- Gallup 2018: 2ª fonte da aprovação ----------
def ler_gallup_aprov() -> dict:
    t = ler("gallup-midterm-seat-loss-2018")
    return {int(a): (int(p), int(s)) for a, p, s in
            re.findall(r"^\s*(19\d\d|20\d\d)\t[^\t]+\t(\d+)\t([+-]\d+)", t, flags=re.M)}


# ---------- Brookings: voto popular e perdas ----------
def ler_brookings() -> tuple[dict, dict]:
    t = achatar(ler("brookings-vitalstats-cap2-2026"))
    votos = {}
    for m in re.finditer(r"\b(19[4-9]\d|20[0-2]\d) (\d\d\.\d) (\d\d\.\d) (\d\d\.\d) (\d\d\.\d) (\d+\.\d)([DR])", t):
        votos.setdefault(int(m.group(1)), (float(m.group(2)), float(m.group(4))))
    perdas = {}
    ini = t.find("Losses by the President's Party in Midterm Elections", t.find("Table 2-4") if "Table 2-4" in t else 0)
    corpo = ler("brookings-vitalstats-cap2-2026")
    bloco = achatar(corpo[corpo.rfind("Popular Vote and House Seats Won by Party"):])
    for m in re.finditer(r"\b(19[4-9][2468]|19[5-9][02468]|20[0-2][02468]) ([DR]) (\+?-?\d+)[a-z]? (\+?-?\d+)[a-z]?(?= |$)", bloco):
        perdas[int(m.group(1))] = (m.group(2), int(m.group(3)), int(m.group(4)))
    return votos, perdas


# ---------- Divisões partidárias ----------
def ler_camara() -> dict:
    t = achatar(ler("house-party-divisions"))
    saida = {}
    for m in re.finditer(r"\b(\d{2,3})(?:st|nd|rd|th) \((\d{4})[–-](\d{4})\) (\d+) (\d+) (\d+)", t):
        c = int(m.group(1))
        if 79 <= c <= 119:
            d, r = int(m.group(5)), int(m.group(6))
            if not 420 <= d + r <= 437:
                raise SystemExit(f"Camara {c}: D {d} R {r} fora da faixa (nota colada?)")
            saida[c] = {"D": d, "R": r}
    return saida


def ler_senado() -> dict:
    corpo = ler("senate-party-division")
    saida = {}
    blocos = re.split(r"\n(?=\d{1,3}(?:st|nd|rd|th) Congress \()", corpo)
    for b in blocos:
        m = re.match(r"(\d{1,3})(?:st|nd|rd|th) Congress", b)
        if not m:
            continue
        c = int(m.group(1))
        ms = re.findall(r"Majority Party[^:]*: (Democrats|Republicans) \((\d+)", b)
        if ms:
            saida[c] = "D" if ms[-1][0] == "Democrats" else "R"
            if c == 107:
                saida[c] = "D"  # conferir nota abaixo: 107º mudou duas vezes; na eleição de 2002 a maioria era democrata
    return saida


# ---------- Generic ballot ----------
def ler_gallup_generic() -> tuple[dict, dict]:
    """Devolve {ano: R%} do poll final e {ano: R% real}, ambos dois partidos, da tabela do Gallup."""
    t = achatar(ler("gallup-13879"))
    i = t.find("Gallup Accuracy in Forecasting")
    final, real = {}, {}
    for a, re_, p, _e in re.findall(r"\b(19\d\d|20\d\d) (\d\d\.\d) (\d\d\.\d) (-?\d\.\d)", t[i:t.find("However, since the House", i)]):
        final[int(a)] = float(p)
        real[int(a)] = float(re_)
    j = t.find("Gallup Final Pre-Election Generic Ballot")
    tabela2 = {}
    for a, d, r in re.findall(r"\b(19\d\d|20\d\d) (\d\d\.\d) (\d\d\.\d) [+-]?\d\.\d", t[j:i]):
        tabela2[int(a)] = (float(d), float(r))
    return (final, real, tabela2)


def margem(txt: str) -> float:
    """'D+7' -> -7 (R menos D); 'R+7' -> +7; 'EVEN' -> 0."""
    txt = txt.strip()
    if txt == "EVEN":
        return 0.0
    return float(txt[2:]) * (1 if txt[0] == "R" else -1)


def ler_538() -> tuple[dict, dict]:
    t = ler("538-best-tool-presidencial-arquivo")
    final = {int(a): margem(g) for a, g, h, e in re.findall(r"^(19\d\d|20\d\d)\t([RDEVN+0-9]+)\t([RDEVN+0-9]+)\t(\d+)$", t, flags=re.M)
             if int(a) % 4 == 2}
    t2 = ler("538-best-tool-2022-arquivo")
    real = {int(a): margem(h) for a, h in re.findall(r"^(19\d\d|20\d\d)\t\w+\t[RD]\+\d+\.\d\t([RD]\+\d+\.\d)\t", t2, flags=re.M)}
    return final, real


def opos_menos_pres(r_menos_d: float, partido: str) -> float:
    return round(r_menos_d if partido == "D" else -r_menos_d, 1)


# ---------- E1 ----------
def gerar_e1() -> list[dict]:
    uc = ler_ucsb()
    ga = ler_gallup_aprov()
    votos, perdas = ler_brookings()
    cam = ler_camara()
    sen = ler_senado()
    gf, gr, gt = ler_gallup_generic()
    f538, r538 = ler_538()
    linhas = []
    for ano in range(1946, 2023, 4):
        u = uc[ano]
        c_dep = 80 + (ano - 1946) // 2
        c_ant = c_dep - 1
        notas = []
        # aprovação
        if ano in ga and ga[ano][0] != u["aprov"]:
            notas.append(f"aprovacao: UCSB (ultima leitura Gallup da tabela) {u['aprov']}; artigo Gallup 2018 {ga[ano][0]}")
        if ano not in ga:
            notas.append("aprovacao: sem 2a fonte independente capturada (artigo Gallup 2018 vai ate 2014)")
        # cadeiras
        if ano in ga and ga[ano][1] != u["camara"]:
            notas.append(f"camara: UCSB {u['camara']:+d}; Gallup {ga[ano][1]:+d}")
        if ano in perdas:
            _p, pc, ps = perdas[ano]
            if pc != u["camara"]:
                notas.append(f"camara: UCSB {u['camara']:+d}; Brookings {pc:+d}")
            if ps != u["senado"]:
                notas.append(f"senado: UCSB {u['senado']:+d}; Brookings {ps:+d}")
        else:
            notas.append("Brookings nao lido neste ano")
        calc = cam[c_dep][u["partido"]] - cam[c_ant][u["partido"]]
        if calc != u["camara"]:
            notas.append(f"camara: diferenca direta na tabela House {calc:+d}")
        # generic
        gen = ""
        fg = ""
        if ano in gf:
            gen = opos_menos_pres(2 * gf[ano] - 100, u["partido"])
            fg = "Gallup final (dois partidos; gallup-13879)"
            if ano in f538 and abs(f538[ano] - (2 * gf[ano] - 100)) >= 1:
                notas.append(f"generic: Gallup {2 * gf[ano] - 100:+.1f} (R-D); 538 {f538[ano]:+.0f} (R-D)")
        elif ano in f538:
            gen = opos_menos_pres(f538[ano], u["partido"])
            fg = "final RCP arredondado (tabela 538)"
        elif ano == 2022:
            confere("breitbart-rcp-final-2022", "the party led by 2.5% in the final RealClearPolitics average")
            gen = opos_menos_pres(2.5, u["partido"])
            fg = "final RCP (Breitbart cita RCP; pagina da RCP recusou captura)"
        if ano == 1998 and ano not in gf and 1998 in gt:
            pass
        if ano in gt and ano in f538 and ano not in gf:
            pass
        if gen == "":
            notas.append("generic: sem fonte capturada")
        # voto
        d, r = votos[ano]
        mv = opos_menos_pres(r - d, u["partido"])
        if ano in r538 and abs(r538[ano] - (r - d)) > 0.5:
            notas.append(f"voto: Brookings {r - d:+.1f} (R-D); 538 {r538[ano]:+.1f}")
        if ano in gr:
            margem2 = 2 * gr[ano] - 100
            if abs(margem2 - (r - d)) > 1.0:
                notas.append(f"voto: Brookings {r - d:+.1f} (todos os votos); Gallup dois partidos {margem2:+.1f}")
        if ano == 2022:
            confere("ballotpedia-news-generic", "when Republicans won by 2.8%")
            notas.append(f"voto: Brookings {r - d:+.1f} (R-D); Ballotpedia R+2.8")
        if ano == 2002:
            notas.append("senado: maioria antes = democratas em nov/2002 (senate.gov: mudou em jun/2001)")
        linhas.append({
            "ano": ano, "presidente": u["presidente"], "partido_presidente": u["partido"],
            "aprovacao_gallup": u["aprov"] if u["aprov"] is not None else "",
            "camara_variacao_partido_presidente": u["camara"], "senado_variacao_partido_presidente": u["senado"],
            "camara_maioria_antes": "D" if cam[c_ant]["D"] > cam[c_ant]["R"] else "R",
            "camara_maioria_depois": "D" if cam[c_dep]["D"] > cam[c_dep]["R"] else "R",
            "senado_maioria_antes": sen[c_ant], "senado_maioria_depois": sen[c_dep],
            "generic_ballot_final_oposicao_menos_presidente": gen,
            "voto_nacional_camara_margem": mv,
            "fonte1": "UCSB American Presidency Project (ucsb-seats-midterm); House History (house-party-divisions); Senate (senate-party-division)",
            "fonte2": "Brookings Vital Statistics cap.2 2026 (brookings-vitalstats-cap2-2026)"
                      + ("; Gallup 2018 (gallup-midterm-seat-loss-2018)" if ano in ga else "")
                      + (f"; generic: {fg}" if fg else ""),
            "nota": " | ".join(notas),
        })
    with (DADOS / "e1_midterms.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(linhas[0]))
        w.writeheader()
        w.writerows(linhas)
    return linhas


# ---------- Vetos ----------
def gerar_vetos() -> None:
    cam = ler_camara()
    sen = ler_senado()
    t = ler("ucsb-vetoes")
    t = t[t.find("Harry S. Truman"):t.find("Last Updated")]
    linhas = []
    pres, partido = None, None
    partidos = {"Harry S. Truman": "D", "Dwight D. Eisenhower": "R", "John F. Kennedy": "D", "Lyndon B. Johnson": "D",
                "Richard Nixon": "R", "Gerald R. Ford": "R", "Jimmy Carter": "D", "Ronald Reagan": "R", "George Bush": "R",
                "William J. Clinton": "D", "George W. Bush": "R", "Barack Obama": "D", "Donald J. Trump - I": "R",
                "Joseph R. Biden, Jr.": "D", "Donald J. Trump - II": "R"}
    for ln in t.splitlines():
        for nome in partidos:
            if ln.startswith(nome):
                pres, partido = nome, partidos[nome]
        m = re.match(r"\s*(\d{2,3})(?:st|nd|rd|th)\s*\d?\s+(\d+\.?\d*)%\s+(\d+\.?\d*)%\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)", ln)
        if not m:
            continue
        c = int(m.group(1))
        if c < 80:
            continue
        oposta = "R" if partido == "D" else "D"
        cam_op = cam[c]["D" if oposta == "D" else "R"] > cam[c]["R" if oposta == "D" else "D"]
        sen_op = sen.get(c) == oposta
        div = "ambos" if cam_op and sen_op else "Camara" if cam_op else "Senado" if sen_op else "nenhum"
        nota = []
        if c == 119:
            nota.append("parcial: UCSB com dados ate 08/jan/2026")
        if c == 107:
            nota.append("Senado mudou de maioria duas vezes no 107o; classificacao usa a maioria em nov/2002")
        if c == 117:
            nota.append("Senado 50-50 com democratas organizando")
        if int(m.group(5)) + int(m.group(6)) != int(m.group(4)):
            nota.append(f"inconsistencia na UCSB: total {m.group(4)}, regular {m.group(5)} + pocket {m.group(6)}; total por presidente bate")
        if c in (88, 93):
            nota.append("Congresso com dois presidentes; uma linha por presidente")
        linhas.append({"congresso": c, "presidente": pres, "partido_presidente": partido, "governo_dividido": div,
                       "vetos_total": int(m.group(4)), "vetos_derrubados": int(m.group(7)),
                       "fonte": "UCSB (ucsb-vetoes); totais por presidente conferidos com House History (house-vetoes) e Senate (senate-vetoes)",
                       "nota": " | ".join(nota)})
    # conferência: soma por presidente contra a tabela do Senado (arquivada em jan/2025) e da House
    with (DADOS / "e3_vetos_por_congresso.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(linhas[0]))
        w.writeheader()
        w.writerows(linhas)
    somas = {}
    for x in linhas:
        s = somas.setdefault(x["presidente"], [0, 0])
        s[0] += x["vetos_total"]
        s[1] += x["vetos_derrubados"]
    print("vetos por presidente (UCSB, 80o em diante):", somas)


# ---------- Tarifas ----------
def gerar_tarifa() -> None:
    t = ler("usitc-ave-1891-2024")
    linhas = []
    davemanuel = json.loads((DADOS / "brutos" / "davemanuel-tariffs.json").read_text(encoding="utf-8"))
    xs = davemanuel["x"]
    serie_all = next(s for s in davemanuel["series"] if s["n"] == "Duties as % of all imports")
    valores = dict(zip(xs, serie_all["v"]))
    for ano in range(2017, 2025):
        # Só a Tabela 1: a linha do ano é seguida de oito números, e o último é tarifa arrecadada / total importado.
        m = re.search(rf"^{ano}\s*\n\s*([\d,]+)\s+([\d.]+)\s+([\d,]+)\s+([\d.]+)\s+([\d,]+)\s+([\d,]+)\s+([\d.]+)\s+([\d.]+)\s", t, flags=re.M)
        if not m:
            raise SystemExit(f"USITC sem linha para {ano}")
        pct = float(m.group(8))
        dm = valores.get(str(ano))
        nota = ""
        if dm is not None and abs(float(dm) - pct) > 0.051:
            nota = f"divergencia: republicacao {dm}"
        linhas.append({"tipo": "taxa_anual", "ano": ano, "data": "", "valor_pct": pct,
                       "metrica": "tarifas arrecadadas / total importado (imports for consumption)",
                       "descricao": "", "posicao_em_relacao_a_nov2018": "",
                       "fonte1": "USITC Table 1 (usitc-ave-1891-2024)", "fonte2": "davemanuel.com/an/tariffs.json (republica USITC, edicao mar/2026)", "nota": nota})
    d25 = valores.get("2025")
    fred_d = float(re.search(r"2025: ([\d.,]+)", ler("fred-customs-duties")).group(1).replace(",", ""))
    fred_m = float(re.search(r"2025: ([\d.,]+)", ler("fred-imports-goods")).group(1).replace(",", ""))
    linhas.append({"tipo": "taxa_anual", "ano": 2025, "data": "", "valor_pct": d25,
                   "metrica": "tarifas arrecadadas / total importado",
                   "descricao": "", "posicao_em_relacao_a_nov2018": "",
                   "fonte1": "davemanuel.com/an/tariffs.json (USITC Table 1, edicao mar/2026; PDF oficial de 2025 nao disponivel)",
                   "fonte2": "FRED/BEA customs duties e imports of goods (fred-customs-duties; fred-imports-goods)",
                   "nota": f"conta com FRED/BEA: {fred_d}/{fred_m} = {100 * fred_d / fred_m:.2f}% (base contabil diferente)"})
    confere("wharton-tarifa-2026-07-13", "As of May 2026, the effective tariff rate stood at 7.2 percent")
    confere("taxfoundation-tariff-tracker", "raise the effective tariff rate (reflecting revenues collected) to 7.2 percent for calendar year 2026")
    confere("yale-tariffs-2026-04-08", "The average statutory tariff rate now stands at 11.0%")
    linhas.append({"tipo": "taxa_anual", "ano": 2026, "data": "2026-05", "valor_pct": 7.2,
                   "metrica": "taxa efetiva observada em maio/2026 (ano incompleto)",
                   "descricao": "", "posicao_em_relacao_a_nov2018": "",
                   "fonte1": "Penn Wharton Budget Model (wharton-tarifa-2026-07-13)",
                   "fonte2": "Tax Foundation (taxfoundation-tariff-tracker): estimativa 7,2% para o ano de 2026",
                   "nota": "Yale Budget Lab em 24/ago/2026: taxa ESTATUTARIA 11,0% (mede outra coisa; yale-tariffs-2026-04-08)"})
    medidas = [
        ("2018-02-07", "Salvaguarda Sec. 201: paineis solares e lavadoras em vigor", "1/23/2018—President proclaims actions on solar cells/modules and large residential washers, effective February 7, 2018."),
        ("2018-03-23", "Sec. 232: aco e aluminio em vigor", "3/23/2018—United States imposes steel and aluminum duties."),
        ("2018-07-06", "Sec. 301 China, etapa 1: 25% sobre US$ 34 bi", "7/6/2018—United States imposes stage 1 tariffs (25% tariff on $34 billion of U.S. imports)."),
        ("2018-08-23", "Sec. 301 China, etapa 2: 25% sobre US$ 16 bi", "8/23/2018—United States imposes stage 2 tariffs (25% tariff on $16 billion of U.S. imports)."),
        ("2018-09-24", "Sec. 301 China, etapa 3: 10% sobre US$ 200 bi", "9/24/2018—In response to Chinese retaliatory tariffs, United States imposes stage 3 tariffs (10% tariffs on $200 billion of U.S. imports)."),
        ("2018-12-01", "Anuncio de novas negociacoes com a China", "12/1/2018—President announces new negotiations with China to resolve U.S. concerns."),
        ("2019-05-10", "Sec. 301 China: etapa 3 sobe para 25%", "5/10/2019—United States imposes stage 3 tariff increase to 25%."),
        ("2019-05-17", "Sec. 232: veiculos declarados ameaca; negociacao ordenada, sem tarifa", "5/17/2019—President proclaims motor vehicle and parts imports a national security threat"),
        ("2019-05-19", "Sec. 232: Canada e Mexico isentos de aco e aluminio", "5/19/2019—President exempts Canada and Mexico from steel and aluminum duties."),
        ("2019-05-30", "IEEPA: anuncio de 5% sobre o Mexico; suspenso em 07/jun/2019, sem entrar em vigor", "5/30/2019—President announces intent to invoke IEEPA authorities to impose 5% tariff on all imports from Mexico"),
        ("2019-09-01", "Sec. 301 China, etapa 4A: 15%", "9/1/2019—United States imposes stage 4A tariffs of 15%."),
        ("2019-10-11", "Suspensao da alta prevista para outubro; anuncio da fase 1", "10/11/2019—President Trump suspends the proposed October tariff increases"),
        ("2019-12-15", "USTR suspende a etapa 4B antes de entrar em vigor", "12/15/2019—USTR suspends potential stage 4B tariffs of 15% before they take effect."),
        ("2020-01-15", "Acordo fase 1 assinado; etapa 4A cairia de 15% para 7,5% em 14/fev/2020", "1/15/2020—USTR issues a notice to reduce stage 4A tariffs from 15% to 7.5%, effective February 14, 2020."),
        ("2020-02-08", "Sec. 232: derivados de aco e aluminio em vigor", "1/24/2020—President proclaims certain derivative products of steel and aluminum"),
    ]
    for data, desc, trecho in medidas:
        confere("crs-in10943-tarifas", trecho)
        nota = ""
        if data == "2020-01-15":
            nota = "o CRS IN10943 datou a assinatura como 1/15/2019, erro evidente de digitacao; a nota do USTR no mesmo texto e 1/15/2020"
        linhas.append({"tipo": "medida", "ano": int(data[:4]), "data": data, "valor_pct": "", "metrica": "",
                       "descricao": desc,
                       "posicao_em_relacao_a_nov2018": "antes" if data < "2018-11-06" else "depois",
                       "fonte1": "CRS IN10943 (crs-in10943-tarifas)", "fonte2": "PIIE (piie-us-china-chart), so para China" if "China" in desc or "Sec. 301" in desc else "",
                       "nota": nota})
    with (DADOS / "e3_tarifa_media.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(linhas[0]))
        w.writeheader()
        w.writerows(linhas)


# ---------- Shutdowns ----------
def ler_shutdowns() -> list[dict]:
    t = ler("crs-rs20348-funding-gaps")
    bloco = t[t.find("Table 1. Appropriations Funding Gaps Since FY1977", t.find("A majority of the funding gaps")):t.find("Source: Compiled by CRS.")]
    tokens = [x.strip() for x in bloco.split("\n") if x.strip()]
    linhas, ano = [], None
    i = 0
    while i < len(tokens):
        tk = tokens[i]
        if re.fullmatch(r"(19|20)\d\d", tk):
            ano = int(tk)
            i += 1
            continue
        if re.match(r"\w+day, \d+/\d+/\d+", tk) and i + 2 < len(tokens) and tokens[i + 1].isdigit():
            linhas.append({"ano_fiscal": ano, "inicio_expira": tk.split(", ")[1], "dias": int(tokens[i + 1]),
                           "fim": tokens[i + 2].split(", ")[1]})
            i += 3
            continue
        i += 1
    return linhas


def gerar_shutdowns() -> list[dict]:
    gaps = ler_shutdowns()
    with (DADOS / "e3_shutdowns_por_ano_fiscal.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["ano_fiscal", "inicio_expira", "dias", "fim", "fonte", "nota"])
        w.writeheader()
        for g in gaps:
            w.writerow({**g, "fonte": "CRS RS20348 (crs-rs20348-funding-gaps)",
                        "nota": "funding gap; antes de FY1982 quase sem paralisacao (CRS/GAO)" if g["ano_fiscal"] < 1982 else ""})
    return gaps


def gerar_oversight(gaps: list[dict]) -> None:
    def fy(*anos):
        out = [f"FY{g['ano_fiscal']}: {g['dias']} dias" for g in gaps if g["ano_fiscal"] in anos]
        return "; ".join(out) if out else "nenhum funding gap listado"

    confere("coequal-subpoena", "Dan Burton issued 1,089 subpoenas")
    confere("coequal-subpoena", "the Committee issued 34 subpoenas as part of an investigation into the White House Travel Office")
    confere("cummings-issa-subpoena", "issued a combined total of 78 subpoenas")
    confere("cummings-issa-subpoena", "Issa has issued 96 subpoenas")
    confere("coequal-subpoena", "Darrell Issa issued over 100 subpoenas")
    confere("mayerbrown-118", "House and Senate committees have issued at least 129 subpoenas")
    confere("cap-jordan-subpoenas", "has issued at least 91 subpoenas")
    confere("wiki-clinton-impeachment", "On October 8, 1998, the United States House of Representatives voted to authorize a broad impeachment inquiry")
    confere("house-impeachment-list", "Impeached December 19, 1998")
    confere("house-impeachment-list", "Impeached December 18, 2019")
    confere("house-impeachment-list", "Impeached February 13, 2024")
    confere("ballotpedia-trump-impeachment", "first announced the House would pursue an inquiry into Trump on September 24, 2019")
    confere("wiki-biden-inquiry", "On September 12, 2023, Kevin McCarthy")
    confere("wiki-biden-inquiry", "voted 221–212 to formalize the inquiry")

    linhas = [
        (1946, "80o", "R", "Truman", "", "", "sem fonte de inquerito encontrada; nao consta na lista de impeachments da House", "fora da serie: a lista do CRS comeca em FY1977", "house-impeachment-list", "intimacoes sem fonte"),
        (1954, "84o", "D", "Eisenhower", "", "", "sem fonte de inquerito encontrada; nao consta na lista de impeachments da House", "fora da serie: a lista do CRS comeca em FY1977", "house-impeachment-list", "intimacoes sem fonte"),
        (1994, "104o", "R", "Clinton", "34 no caso Travel Office (1995-96, comite de Reforma do Governo); 1.089 de Dan Burton (1997-2002)", "coequal-subpoena", "sim: autorizado 08/out/1998 (105o Congresso); impeachment 19/dez/1998", f"{fy(1996)} (a maioria seguiu no 105o e 106o: {fy(1997, 1998, 1999, 2000, 2001)})", "wiki-clinton-impeachment; house-impeachment-list; crs-rs20348-funding-gaps", "contagens de um comite, nao da Camara inteira; Burton cobre tambem anos alem do mandato de Clinton"),
        (2006, "110o", "D", "G.W. Bush", "78 somados pelos presidentes do comite de Fiscalizacao em 2003-2010 (Davis, Waxman, Towns); sem corte por Congresso", "cummings-issa-subpoena", "nao consta inquerito aberto na lista de impeachments da House", fy(2008, 2009), "house-impeachment-list; crs-rs20348-funding-gaps", "numero mistura maiorias e vem de nota da minoria democrata"),
        (2010, "112o", "R", "Obama", "96 de Issa ate jul/2014; mais de 100 no mandato inteiro (2011-2014), um comite so", "cummings-issa-subpoena; coequal-subpoena", "nao consta inquerito aberto na lista de impeachments da House", f"{fy(2012, 2013)}; ainda com a mesma maioria, {fy(2014)}", "house-impeachment-list; crs-rs20348-funding-gaps", "96 vem de nota da minoria democrata; 113o Congresso incluido pela FY2014"),
        (2018, "116o", "D", "Trump", "", "", "sim: anunciado 24/set/2019; impeachment 18/dez/2019", f"{fy(2019)} (comecou antes da posse da nova maioria, em 21/dez/2018); {fy(2020, 2021)}", "ballotpedia-trump-impeachment; house-impeachment-list; crs-rs20348-funding-gaps", "contagem de intimacoes do 116o sem fonte"),
        (2022, "118o", "R", "Biden", "pelo menos 129 de Camara e Senado de jan/2023 a mar/2024; pelo menos 91 de Jim Jordan", "mayerbrown-118; cap-jordan-subpoenas", "sim: anunciado 12/set/2023, votacao 221-212 em 13/dez/2023, sem impeachment do presidente; Mayorkas impeached 13/fev/2024", fy(2024, 2025), "wiki-biden-inquiry; house-impeachment-list; crs-rs20348-funding-gaps", "Mayer Brown soma as duas casas; CAP e centro de centro-esquerda"),
    ]
    campos = ["midterm", "congresso", "nova_maioria_camara", "presidente", "intimacoes", "fonte_intimacoes",
              "audiencias_fiscalizacao", "inquerito_impeachment", "shutdowns_no_periodo", "fontes", "nota"]
    with (DADOS / "e3_impeachment_e_oversight.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=campos)
        w.writeheader()
        for l in linhas:
            w.writerow(dict(zip(campos, (*l[:6], "sem fonte", *l[6:]))))


def medias(e1: list[dict]) -> None:
    v = [(int(l["camara_variacao_partido_presidente"]), l["aprovacao_gallup"]) for l in e1]
    camara = [x for x, _ in v]
    perdeu = sum(1 for x in camara if x < 0)
    print(f"midterms: {len(camara)}; media da variacao: {st.mean(camara):.1f}; perdeu cadeiras em {perdeu}; ganhou em {sum(1 for x in camara if x > 0)}")
    for corte in (50, 40):
        s = [x for x, a in v if a != "" and int(a) < corte]
        print(f"aprovacao < {corte}: n={len(s)}; media {st.mean(s):.1f}; anos: {[l['ano'] for l in e1 if l['aprovacao_gallup'] != '' and int(l['aprovacao_gallup']) < corte]}")
    a50 = [x for x, a in v if a != "" and int(a) >= 50]
    print(f"aprovacao >= 50: n={len(a50)}; media {st.mean(a50):.1f}")
    # sensibilidade: troca a aprovação da UCSB pela do artigo Gallup de 2018, onde ele existe
    ga = ler_gallup_aprov()
    alt = [(int(l["camara_variacao_partido_presidente"]), ga[int(l["ano"])][0] if int(l["ano"]) in ga else int(l["aprovacao_gallup"]),
            int(l["ano"])) for l in e1]
    for corte in (50, 40):
        s = [(x, y) for x, a, y in alt if a < corte]
        print(f"sensibilidade Gallup 2018, aprovacao < {corte}: n={len(s)}; media {st.mean(x for x, _ in s):.1f}; anos {[y for _, y in s]}")
    # sensibilidade: mesmas contas com as cadeiras da Brookings
    _v, perdas = ler_brookings()
    br = [(perdas[int(l["ano"])][1], l["aprovacao_gallup"]) for l in e1]
    print(f"Brookings: media {st.mean(x for x, _ in br):.1f}; perdeu em {sum(1 for x, _ in br if x < 0)}; "
          f"<50: {st.mean(x for x, a in br if int(a) < 50):.1f}; <40: {st.mean(x for x, a in br if int(a) < 40):.1f}")


def main() -> None:
    e1 = gerar_e1()
    gerar_vetos()
    gerar_tarifa()
    gaps = gerar_shutdowns()
    gerar_oversight(gaps)
    medias(e1)


if __name__ == "__main__":
    main()
