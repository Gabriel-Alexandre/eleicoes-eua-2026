"""Junta as previsões: mediana por pergunta e mundo, efeito do resultado, efeito de ler a história, e a média ponderada pelos mundos.

Grava resultados/previsoes.csv e a chave "previsoes" de resultados/RESUMO.json.
Uso: python ferramentas/agregar_previsoes.py
"""
import csv
import glob
import json
import statistics as st
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
P = RAIZ / "dados" / "previsoes"
RES = RAIZ / "resultados"
MUNDOS = ("DD", "DR", "RR")
FAIXAS = [(5, "quase nenhuma chance"), (20, "muito improvável"), (45, "improvável"), (55, "chance parecida"), (80, "provável"), (95, "muito provável"), (100, "quase certo")]


def faixa(p):
    return next(n for lim, n in FAIXAS if p <= lim)


def ler(pasta):
    return [json.load(open(a, encoding="utf-8")) for a in sorted(glob.glob(str(P / pasta / "*.json")))]


def mediana(rodada, q, w):
    v = [r["perguntas"][q][w] for r in rodada if q in r["perguntas"]]
    return st.median(v) if v else None


def main():
    A, B = ler("rodada_a"), ler("rodada_b")
    perguntas = list(csv.DictReader(open(P / "perguntas.csv", encoding="utf-8")))
    resumo_path = RES / "RESUMO.json"
    R = json.loads(resumo_path.read_text(encoding="utf-8"))
    # Pesos dos mundos: mediana dos mercados e modelos (dados/e2_chances.csv), reescalados para somar 100.
    c = R["chances"]
    rr = st.median(c["rr"])
    soma = c["dd_mediana"] + c["dr_mediana"] + rr
    pesos = {"DD": c["dd_mediana"] / soma, "DR": c["dr_mediana"] / soma, "RR": rr / soma}
    linhas = []
    for q in perguntas:
        i = q["id"]
        m = {w: mediana(B, i, w) for w in MUNDOS}
        a = {w: mediana(A, i, w) for w in MUNDOS}
        minmax = {w: (min(r["perguntas"][i][w] for r in B), max(r["perguntas"][i][w] for r in B)) for w in MUNDOS}
        linhas.append({
            "id": i, "grupo": q["grupo"], "pergunta": q["pergunta"], "prazo": q["prazo"],
            **{f"{w}": m[w] for w in MUNDOS},
            "faixa_DD": faixa(m["DD"]), "faixa_DR": faixa(m["DR"]), "faixa_RR": faixa(m["RR"]),
            "efeito_DD_RR": round(m["DD"] - m["RR"], 1),
            "efeito_DR_RR": round(m["DR"] - m["RR"], 1),
            "ponderada": round(sum(pesos[w] * m[w] for w in MUNDOS), 1),
            "discordancia_DD": minmax["DD"][1] - minmax["DD"][0],
            **{f"A_{w}": a[w] for w in MUNDOS},
        })
    with open(RES / "previsoes.csv", "w", newline="", encoding="utf-8") as f:
        w_ = csv.DictWriter(f, fieldnames=list(linhas[0]))
        w_.writeheader()
        w_.writerows(linhas)
    comuns = [l for l in linhas if l["A_DD"] is not None]
    efeito_hist = round(st.mean(abs(l[w] - l[f"A_{w}"]) for l in comuns for w in MUNDOS), 1)
    R["previsoes"] = {
        "pesos_mundos": {k: round(v * 100, 1) for k, v in pesos.items()},
        "p_mundos_a": {r["modelo"]: r["p_mundos"] for r in A},
        "p_mundos_b": {r["modelo"]: r["p_mundos"] for r in B},
        "efeito_medio_de_ler_a_historia": efeito_hist,
        "discordancia_media_DD": round(st.mean(l["discordancia_DD"] for l in linhas), 1),
        "efeito_por_grupo": {g: round(st.mean(abs(l["efeito_DD_RR"]) for l in linhas if l["grupo"] == g), 1) for g in ("brasil", "mundo", "trump")},
        # Corte que importa: o que depende do voto do Congresso contra o resto.
        "efeito_brasil_depende_do_congresso": round(st.mean(abs(l["efeito_DD_RR"]) for l in linhas if l["id"] in ("B04", "B05", "B06")), 1),
        "efeito_brasil_nao_depende": round(st.mean(abs(l["efeito_DD_RR"]) for l in linhas if l["grupo"] == "brasil" and l["id"] not in ("B04", "B05", "B06")), 1),
        "maior_efeito_brasil": max((l for l in linhas if l["grupo"] == "brasil"), key=lambda l: abs(l["efeito_DD_RR"]))["id"],
        "perguntas": linhas,
    }
    resumo_path.write_text(json.dumps(R, ensure_ascii=False, indent=1), encoding="utf-8")
    for l in linhas:
        print(l["id"], l["DD"], l["DR"], l["RR"], "| efeito", l["efeito_DD_RR"], "| pond", l["ponderada"], "| A", l["A_DD"], l["A_DR"], l["A_RR"], "| disc", l["discordancia_DD"], "|", l["pergunta"][:58])
    print(R["previsoes"]["pesos_mundos"], efeito_hist, R["previsoes"]["discordancia_media_DD"], R["previsoes"]["p_mundos_b"])


if __name__ == "__main__":
    main()
