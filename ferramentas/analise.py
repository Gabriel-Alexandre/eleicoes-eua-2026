"""Análise central: história das midterms, modelo de cadeiras, antes e depois de perder uma casa, e Brasil.

Grava resultados/RESUMO.json e as tabelas. Nenhum número do relatório sai de outro lugar.
Uso: python ferramentas/analise.py
"""
import json
from pathlib import Path

import numpy as np
import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent
D = RAIZ / "dados"
R = RAIZ / "resultados"
R.mkdir(exist_ok=True)

# Entradas de hoje, todas de dados/e2_chances.csv e docs/PESQUISA_TRUMP.md (média de 44 pesquisas, PollCheck; FiftyPlusOne).
APROVACAO_2026 = 37.9
GENERIC_2026 = round(52.7 - 44.1, 1)
PERDA_MINIMA_2026 = 218  # cadeiras republicanas hoje, BPMoney; a maioria é 218


def ols(x, y):
    X = np.column_stack([np.ones(len(x)), x])
    b, *_ = np.linalg.lstsq(X, y, rcond=None)
    return b


def loo(x, y):
    erros = []
    for i in range(len(y)):
        m = np.ones(len(y), bool)
        m[i] = False
        b = ols(x[m], y[m])
        erros.append(float(y[i] - np.r_[1, x[i]] @ b))
    return erros


def historia():
    e = pd.read_csv(D / "e1_midterms.csv")
    cam = "camara_variacao_partido_presidente"
    sen = "senado_variacao_partido_presidente"
    gen = "generic_ballot_final_oposicao_menos_presidente"
    apr = "aprovacao_gallup"
    casa_trocou = e[e.camara_maioria_antes != e.camara_maioria_depois]
    sen_trocou = e[e.senado_maioria_antes != e.senado_maioria_depois]
    s = {
        "n": len(e),
        "camara_perdeu_cadeiras": int((e[cam] < 0).sum()),
        "camara_media": round(e[cam].mean(), 1),
        "camara_media_abaixo_50": round(e[e[apr] < 50][cam].mean(), 1),
        "n_abaixo_50": int((e[apr] < 50).sum()),
        "camara_media_50_ou_mais": round(e[e[apr] >= 50][cam].mean(), 1),
        "camara_media_abaixo_40": round(e[e[apr] < 40][cam].mean(), 1),
        "n_abaixo_40": int((e[apr] < 40).sum()),
        "senado_perdeu_cadeiras": int((e[sen] < 0).sum()),
        "senado_media": round(e[sen].mean(), 1),
        "camara_trocou": casa_trocou.ano.tolist(),
        "senado_trocou": sen_trocou.ano.tolist(),
        "ultimas_6_camara": e.tail(6)[["ano", cam]].values.tolist(),
        "senado_ganhou_com_aprovacao_ate_45": e[(e[apr] <= 45) & (e[sen] > 0)].ano.tolist(),
    }
    # Modelos: variação de cadeiras explicada por aprovação; por voto genérico; pelos dois.
    m = e.dropna(subset=[gen, apr])
    y = m[cam].to_numpy(float)
    out = {}
    specs = {"aprovacao": [apr], "generic": [gen], "os_dois": [apr, gen]}
    entrada = {apr: APROVACAO_2026, gen: GENERIC_2026}
    for nome, cols in specs.items():
        x = m[cols].to_numpy(float)
        b = ols(x, y)
        err = loo(x, y)
        prev = float(np.r_[1, [entrada[c] for c in cols]] @ b)
        out[nome] = {
            "coef": [round(float(v), 2) for v in b],
            "erro_medio_absoluto_fora_da_amostra": round(float(np.mean(np.abs(err))), 1),
            "n": len(y),
            "previsao_2026": round(prev, 1),
            "maior_erro": {
                "ano": int(m.ano.iloc[int(np.argmax(np.abs(err)))]),
                "cadeiras": round(float(err[int(np.argmax(np.abs(err)))]), 1),
            },
            "acertou_lado_da_maioria_prevista": None,
        }
    # Base ingênua: repetir a média.
    media_loo = [float(y[i] - np.delete(y, i).mean()) for i in range(len(y))]
    out["media_simples"] = {
        "erro_medio_absoluto_fora_da_amostra": round(float(np.mean(np.abs(media_loo))), 1),
        "previsao_2026": round(float(e[cam].mean()), 1),
    }
    s["modelos"] = out
    s["aprovacao_2026"] = APROVACAO_2026
    s["generic_2026"] = GENERIC_2026
    return s, e


def forca_antes_depois(e):
    f = pd.read_csv(D / "e3_forca_por_ano.csv").set_index("ano")["episodios_iniciados"]
    linhas = []
    for ano in e[e.camara_maioria_antes != e.camara_maioria_depois].ano:
        if ano + 2 > f.index.max():
            continue
        antes = f.loc[ano - 1 : ano].sum()
        depois = f.loc[ano + 1 : ano + 2].sum()
        linhas.append({"midterm": int(ano), "dois_anos_antes": int(antes), "dois_anos_depois": int(depois)})
    t = pd.DataFrame(linhas)
    t.to_csv(R / "forca_antes_depois.csv", index=False)
    pos_1980 = t[t.midterm >= 1980]
    return {
        "casos": linhas,
        "soma_antes": int(t.dois_anos_antes.sum()),
        "soma_depois": int(t.dois_anos_depois.sum()),
        "subiu": int((t.dois_anos_depois > t.dois_anos_antes).sum()),
        "caiu": int((t.dois_anos_depois < t.dois_anos_antes).sum()),
        "igual": int((t.dois_anos_depois == t.dois_anos_antes).sum()),
        "desde_1980_soma_antes": int(pos_1980.dois_anos_antes.sum()),
        "desde_1980_soma_depois": int(pos_1980.dois_anos_depois.sum()),
    }


def vetos():
    v = pd.read_csv(D / "e3_vetos_por_congresso.csv")
    v["dividido"] = v.governo_dividido != "nenhum"
    # 2 presidentes no 88º e no 93º: soma por Congresso para a média.
    g = v.groupby(["congresso", "dividido"], as_index=False)[["vetos_total", "vetos_derrubados"]].sum()
    desde = g[g.congresso >= 97]  # 1981 em diante
    res = {}
    for nome, b in {"desde_1947": g, "desde_1981": desde}.items():
        res[nome] = {
            "media_dividido": round(b[b.dividido].vetos_total.mean(), 1),
            "media_unificado": round(b[~b.dividido].vetos_total.mean(), 1),
            "total_vetos": int(b.vetos_total.sum()),
            "total_derrubados": int(b.vetos_derrubados.sum()),
            "pct_derrubados": round(100 * b.vetos_derrubados.sum() / b.vetos_total.sum(), 1),
        }
    tr = v[v.presidente.str.contains("Trump")]
    res["trump"] = tr[["congresso", "governo_dividido", "vetos_total", "vetos_derrubados"]].to_dict("records")
    return res


def impeachment():
    # Das 5 vezes em que a Câmara trocou de mãos desde 1994, com o que está em e3_impeachment_e_oversight.csv.
    t = pd.read_csv(D / "e3_impeachment_e_oversight.csv")
    t = t[t.midterm >= 1994]
    aberto = t.inquerito_impeachment.str.startswith("sim")
    return {"casos": len(t), "inquerito_aberto": int(aberto.sum()), "anos": t[aberto].midterm.tolist(), "presidente_impedido_na_camara": ["Clinton", "Trump"], "condenado_no_senado": 0}


def tarifa():
    t = pd.read_csv(D / "e3_tarifa_media.csv")
    a = t[t.tipo == "taxa_anual"].set_index("ano").valor_pct
    return {str(k): float(v) for k, v in a.items()}


def brasil():
    d = pd.read_csv(D / "derivados" / "dolar_ptax.csv", parse_dates=["data"]).set_index("data")["dolar"]
    datas = {1998: "1998-11-03", 2002: "2002-11-05", 2006: "2006-11-07", 2010: "2010-11-02", 2014: "2014-11-04", 2018: "2018-11-06", 2022: "2022-11-08"}
    linhas = []
    for a, s in datas.items():
        t = pd.Timestamp(s)
        p = d[:t].iloc[-1]
        linhas.append({"ano": a, "ptax": float(p), **{f"d{k}": round(float((d[: t + pd.Timedelta(days=k)].iloc[-1] / p - 1) * 100), 1) for k in (30, 90, 180)}})
    td = pd.DataFrame(linhas)
    td.to_csv(R / "dolar_depois_das_midterms.csv", index=False)
    e = pd.read_csv(D / "derivados" / "exportacoes_brasil.csv")
    x = e[e.periodo == "ano"].pivot(index="ano", columns="pais", values="fob_usd").sort_index() / 1e9
    x_comp = x.loc[:2025]
    v = x_comp["EUA"].pct_change() * 100
    pos = [a + 1 for a in range(1998, 2023, 4)]
    fora = [a for a in v.dropna().index if a not in pos]
    js = e[e.periodo == "jan-set"].pivot(index="ano", columns="pais", values="fob_usd")
    return {
        "dolar": linhas,
        "dolar_mediana_d30": float(td.d30.median()),
        "dolar_mediana_d180": float(td.d180.median()),
        "dolar_30_10_2026": float(d["2026-10-30"]),
        "export_eua_ano_pos_midterm_mediana": round(float(v.loc[pos].median()), 1),
        "export_eua_outros_anos_mediana": round(float(v.loc[fora].median()), 1),
        "export_2018_2019": [round(float(x.loc[2018, "EUA"]), 1), round(float(x.loc[2019, "EUA"]), 1)],
        "export_2022_2023": [round(float(x.loc[2022, "EUA"]), 1), round(float(x.loc[2023, "EUA"]), 1)],
        "jan_set_eua": [round(js.loc[2025, "EUA"] / 1e9, 1), round(js.loc[2026, "EUA"] / 1e9, 1), round((js.loc[2026, "EUA"] / js.loc[2025, "EUA"] - 1) * 100, 1)],
        "jan_set_china": [round(js.loc[2025, "China"] / 1e9, 1), round(js.loc[2026, "China"] / 1e9, 1), round((js.loc[2026, "China"] / js.loc[2025, "China"] - 1) * 100, 1)],
    }


def chances():
    c = pd.read_csv(D / "e2_chances.csv")
    bal = c.dropna(subset=["DD"])
    return {
        "dd_mediana": float(bal.DD.median()),
        "dr_mediana": float(bal.DR.median()),
        "rr": bal.RR.dropna().tolist(),
        "senado_d_faixa": [float(c.senado_d.min()), float(c.senado_d.max())],
        "camara_d_cadeiras_faixa": [float(c.cadeiras_camara_d.min()), float(c.cadeiras_camara_d.max())],
    }


def main():
    h, e = historia()
    res = {
        "historia": h,
        "forca": forca_antes_depois(e),
        "vetos": vetos(),
        "impeachment": impeachment(),
        "tarifa": tarifa(),
        "brasil": brasil(),
        "chances": chances(),
    }
    (R / "RESUMO.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps(res, ensure_ascii=False, indent=0))


if __name__ == "__main__":
    main()
