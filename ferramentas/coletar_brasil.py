"""Baixa as séries do Brasil: dólar (BCB, PTAX venda, SGS 1) e exportações para os EUA e a China (ComexStat).

Grava o bruto em dados/brutos/, as tabelas leves em dados/derivados/ e o hash em dados/MANIFESTO.json.
Uso: python ferramentas/coletar_brasil.py
"""
import csv
import datetime as dt
import hashlib
import json
import ssl
import time
import urllib.request
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
BRUTOS = RAIZ / "dados" / "brutos"
DERIVADOS = RAIZ / "dados" / "derivados"
MANIFESTO = RAIZ / "dados" / "MANIFESTO.json"
BRUTOS.mkdir(parents=True, exist_ok=True)
DERIVADOS.mkdir(parents=True, exist_ok=True)
CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE
PAISES = {"EUA": 249, "China": 160}


def registrar(nome, url, corpo):
    (BRUTOS / nome).write_bytes(corpo)
    m = json.loads(MANIFESTO.read_text(encoding="utf-8")) if MANIFESTO.exists() else {}
    m[nome] = {
        "url": url,
        "hora": dt.datetime.now().isoformat(timespec="seconds"),
        "bytes": len(corpo),
        "sha256": hashlib.sha256(corpo).hexdigest(),
    }
    MANIFESTO.write_text(json.dumps(m, ensure_ascii=False, indent=1), encoding="utf-8")


def baixar(url, dados=None):
    h = {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json"}
    r = urllib.request.Request(url, data=dados, headers=h)
    for tentativa in range(8):
        try:
            with urllib.request.urlopen(r, context=CTX, timeout=120) as f:
                return f.read()
        except Exception as e:  # BCB devolve 502 e ComexStat 429 quando apressados
            print("espera", url[:60], e, flush=True)
            time.sleep(20 * (tentativa + 1))
    raise SystemExit("falhou " + url)


def dolar():
    # A API do BCB limita a janela a 10 anos por pedido: baixa em blocos.
    linhas = []
    for ini, fim in [(1994, 2003), (2004, 2013), (2014, 2023), (2024, 2026)]:
        url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados?formato=json&dataInicial=01/07/{ini}&dataFinal=31/12/{fim}"
        corpo = baixar(url)
        registrar(f"bcb_sgs1_{ini}_{fim}.json", url, corpo)
        linhas += json.loads(corpo)
        time.sleep(1)
    with open(DERIVADOS / "dolar_ptax.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["data", "dolar"])
        for l in linhas:
            d = dt.datetime.strptime(l["data"], "%d/%m/%Y").date().isoformat()
            w.writerow([d, l["valor"]])
    print("dolar", len(linhas))


def comex():
    url = "https://api-comexstat.mdic.gov.br/general"
    saida = []
    for pais, cod in PAISES.items():
        for de, ate, rotulo in [("1997-01", "2026-09", "ano"), ("2025-01", "2025-09", "jan-set"), ("2026-01", "2026-09", "jan-set")]:
            q = {
                "flow": "export",
                "monthDetail": False,
                "period": {"from": de, "to": ate},
                "filters": [{"filter": "country", "values": [cod]}],
                "details": ["country"],
                "metrics": ["metricFOB"],
            }
            corpo = baixar(url, json.dumps(q).encode())
            registrar(f"comex_{pais}_{de}_{ate}.json", url + " " + json.dumps(q), corpo)
            for l in json.loads(corpo)["data"]["list"]:
                saida.append({"pais": pais, "ano": l.get("year"), "periodo": rotulo, "fob_usd": l["metricFOB"]})
            time.sleep(15)
    with open(DERIVADOS / "exportacoes_brasil.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["pais", "ano", "periodo", "fob_usd"])
        w.writeheader()
        w.writerows(saida)
    print("comex", len(saida))


if __name__ == "__main__":
    dolar()
    comex()
