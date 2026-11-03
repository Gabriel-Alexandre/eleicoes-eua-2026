import json
from pathlib import Path

R = json.loads((Path(__file__).resolve().parent.parent / "resultados" / "RESUMO.json").read_text(encoding="utf-8"))


def test_pesos_somam_100():
    assert abs(sum(R["previsoes"]["pesos_mundos"].values()) - 100) < 0.2


def test_probabilidades_validas():
    for p in R["previsoes"]["perguntas"]:
        for w in ("DD", "DR", "RR"):
            assert 0 <= p[w] <= 100


def test_impeachment_coerente():
    # Sem maioria democrata na Câmara, impeachment não pode ser mais provável.
    q = {p["id"]: p for p in R["previsoes"]["perguntas"]}
    assert q["T03"]["RR"] < q["T03"]["DR"] <= q["T03"]["DD"]


def test_historia():
    assert R["historia"]["n"] == 20
