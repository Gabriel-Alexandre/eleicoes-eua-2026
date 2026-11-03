"""Refaz os números centrais por outro caminho, sem importar analise.py nem pandas, e compara com o RESUMO.

Uso: python ferramentas/validacao_independente.py  (grava resultados/validacao_independente.csv)
"""
import csv
import glob
import json
import statistics as st
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
R = json.loads((RAIZ / "resultados" / "RESUMO.json").read_text(encoding="utf-8"))
L = []


def conf(nome, calc, pub, tol=0.051):
    L.append({"numero": nome, "refeito": round(calc, 2), "publicado": pub, "passou": abs(calc - pub) <= tol})


e = list(csv.DictReader(open(RAIZ / "dados" / "e1_midterms.csv", encoding="utf-8-sig")))
cam = [int(x["camara_variacao_partido_presidente"]) for x in e]
conf("midterms com perda", sum(c < 0 for c in cam), R["historia"]["camara_perdeu_cadeiras"])
conf("média Câmara", sum(cam) / len(cam), R["historia"]["camara_media"])
ab = [int(x["camara_variacao_partido_presidente"]) for x in e if float(x["aprovacao_gallup"]) < 50]
conf("média abaixo de 50", sum(ab) / len(ab), R["historia"]["camara_media_abaixo_50"])
conf("trocas da Câmara", sum(x["camara_maioria_antes"] != x["camara_maioria_depois"] for x in e), len(R["historia"]["camara_trocou"]))
# Regressão pela fórmula fechada de uma variável, em vez de álgebra matricial.
m = [x for x in e if x["generic_ballot_final_oposicao_menos_presidente"]]
xs = [float(x["aprovacao_gallup"]) for x in m]
ys = [float(x["camara_variacao_partido_presidente"]) for x in m]
mx, my = st.mean(xs), st.mean(ys)
b = sum((a - mx) * (c - my) for a, c in zip(xs, ys)) / sum((a - mx) ** 2 for a in xs)
conf("modelo aprovação, previsão 2026", my + b * (R["historia"]["aprovacao_2026"] - mx), R["historia"]["modelos"]["aprovacao"]["previsao_2026"])
# Exportações direto do bruto do ComexStat.
for pais, chave in (("EUA", "jan_set_eua"), ("China", "jan_set_china")):
    a = float(json.load(open(RAIZ / "dados" / "brutos" / f"comex_{pais}_2025-01_2025-09.json", encoding="utf-8"))["data"]["list"][0]["metricFOB"])
    d = float(json.load(open(RAIZ / "dados" / "brutos" / f"comex_{pais}_2026-01_2026-09.json", encoding="utf-8"))["data"]["list"][0]["metricFOB"])
    conf(f"variação jan-set {pais}", (d / a - 1) * 100, R["brasil"][chave][2])
# Dólar direto do bruto do BCB.
ptax = json.load(open(RAIZ / "dados" / "brutos" / "bcb_sgs1_2024_2026.json", encoding="utf-8"))
conf("PTAX 30/10/2026", float(next(l["valor"] for l in ptax if l["data"] == "30/10/2026")), R["brasil"]["dolar_30_10_2026"], 0.0001)
# Previsões direto dos JSON.
rod = [json.load(open(a, encoding="utf-8")) for a in glob.glob(str(RAIZ / "dados" / "previsoes" / "rodada_b" / "*.json"))]
pub = {p["id"]: p for p in R["previsoes"]["perguntas"]}
for q in ("B01", "B06", "T01", "T03", "W03"):
    conf(f"mediana {q} DD", st.median(r["perguntas"][q]["DD"] for r in rod), pub[q]["DD"])
g = [abs(st.median(r["perguntas"][q]["DD"] for r in rod) - st.median(r["perguntas"][q]["RR"] for r in rod)) for q in pub if pub[q]["grupo"] == "trump"]
conf("efeito grupo Trump", st.mean(g), R["previsoes"]["efeito_por_grupo"]["trump"])
# Votos, da lista, sem filtro de pandas.
v = {x["id"]: x for x in csv.DictReader(open(RAIZ / "dados" / "e4_votos_congresso.csv", encoding="utf-8-sig"))}
conf("S.J.Res. 81, sim", int(v["sjres81"]["sim"]), 52)
conf("H.Con.Res. 86, Câmara, sim", int(v["h2026_199"]["sim"]), 215)
with open(RAIZ / "resultados" / "validacao_independente.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(L[0]))
    w.writeheader()
    w.writerows(L)
ruim = [x for x in L if not x["passou"]]
print(f"{len(L) - len(ruim)} de {len(L)} passaram")
for x in ruim:
    print(x)
sys.exit(1 if ruim else 0)
