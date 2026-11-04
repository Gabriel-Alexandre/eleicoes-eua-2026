"""Compara o resultado de 03/11 (projeções da imprensa, 04/11 de manhã) com o que foi gravado antes da votação.

Grava resultados/RESULTADO.json. Nenhuma previsão gravada é alterada.
Uso: python ferramentas/conferir_resultado.py
"""
import json
from pathlib import Path

import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent
R = json.loads((RAIZ / "resultados" / "RESUMO.json").read_text(encoding="utf-8"))
res = json.loads((RAIZ / "dados" / "resultado_03nov.json").read_text(encoding="utf-8"))
REPUBLICANOS_ANTES = 218  # dados/e2 e docs/PESQUISA_CONGRESSO.md B4

cam = res["camara"]
perda_estimada = cam["estimativa_nbc_r"] - REPUBLICANOS_ANTES
modelos = {k: v["previsao_2026"] for k, v in R["historia"]["modelos"].items()}
erro_modelos = {k: round(v - perda_estimada, 1) for k, v in modelos.items()}

c = pd.read_csv(RAIZ / "dados" / "e2_chances.csv")
por_distrito = c.dropna(subset=["cadeiras_camara_d"])[["fonte", "cadeiras_camara_d"]].to_dict("records")

# Nota de Brier dos 3 mundos: quem deu mais chance ao que aconteceu.
def brier(p):
    total = sum(p[w] for w in ("DD", "DR", "RR"))
    return round(sum((p[w] / total - (1 if w == res["mundo"] else 0)) ** 2 for w in ("DD", "DR", "RR")), 3)

pv = R["previsoes"]
notas = {"mercados_e_modelos": brier(pv["pesos_mundos"])}
for cond in ("a", "b"):
    for m, p in pv[f"p_mundos_{cond}"].items():
        notas[f"ia_{cond}_{m}"] = brier(p)

veto = {"camara_republicanos_para_2_tercos": 290 - cam["estimativa_nbc_d"], "senado_republicanos_para_2_tercos": 67 - res["senado"]["d"]}

saida = {
    "mundo": res["mundo"],
    "perda_republicana_estimada": perda_estimada,
    "previsao_dos_modelos_de_historia": modelos,
    "erro_dos_modelos_de_historia": erro_modelos,
    "previsoes_por_distrito_cadeiras_d": por_distrito,
    "estimativa_nbc_d": cam["estimativa_nbc_d"],
    "brier_3_mundos": notas,
    "veto": veto,
    "abertas": ["T01 (prazo 03/01/2027): até 04/11 ele disse que aceita o resultado", "T02 (prazo 05/01/2027)", "todas as outras perguntas"],
}
(RAIZ / "resultados" / "RESULTADO.json").write_text(json.dumps(saida, ensure_ascii=False, indent=1), encoding="utf-8")
print(json.dumps(saida, ensure_ascii=False, indent=1))
