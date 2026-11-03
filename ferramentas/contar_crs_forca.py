"""Conta as entradas do relatório do CRS "Instances of Use of United States Armed Forces Abroad" (R42738) por ano.

Fonte: PDF da versão de 07/jun/2023, capturado de everycrsreport.com
(arquivo no repositório documentacao: VIDEO_024_ELEICOES_EUA_2026/assets/prints/historico/crs-r42738-pdf.pdf).

Como conta: no PDF o ano fica na coluna da esquerda (x < 120) e cada entrada começa na coluna do texto com um rótulo
em itálico terminado em ponto ("Trieste, Italy."). Uma entrada = linha do corpo (fonte GillSans; notas de rodapé usam
outra fonte) que abre parágrafo novo com esse rótulo. Título de obra em itálico no meio do parágrafo não conta.

Saída: dados/e3_forca_por_ano.csv
  episodios_iniciados: entradas listadas sob o ano de início (episódio longo conta 1 vez, no ano em que começa)
  episodios_ativos: as mesmas entradas contadas em todo ano do intervalo do cabeçalho (ex.: 1950-1953 conta em 4 anos)

Uso: python ferramentas/contar_crs_forca.py <caminho do PDF> [--listar]
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

import fitz  # PyMuPDF

RAIZ = Path(__file__).resolve().parents[1]
SAIDA = RAIZ / "dados" / "e3_forca_por_ano.csv"
ANO = re.compile(r"^(\d{4})(?:\s*[-–]\s*(\d{4})?)?(?:\s*\w*)?\s*$")


def ler_entradas(pdf: Path) -> list[dict]:
    entradas: list[dict] = []
    atual = None
    doc = fitz.open(pdf)
    comecou = False
    for num, pagina in enumerate(doc):
        y_anterior = None  # posição da linha anterior do corpo: entre parágrafos o salto é de 13 a 14; dentro, de 10,5
        for bloco in pagina.get_text("dict")["blocks"]:
            for linha in bloco.get("lines", []):
                spans = [s for s in linha["spans"] if s["text"].strip()]
                if not spans:
                    continue
                x, y = linha["bbox"][0], linha["bbox"][1]
                fonte = spans[0]["font"]
                if y < 60 or y > 740 or "GillSans" not in fonte:  # cabeçalho, rodapé e notas (outra fonte)
                    continue
                texto = spans[0]["text"].strip()
                m = ANO.match(texto)
                if x < 120 and m and 1790 <= int(m.group(1)) <= 2030:
                    comecou = True
                    ini = int(m.group(1))
                    fim = int(m.group(2)) if m.group(2) else ini
                    atual = (ini, fim, bool(re.search(r"[-–]\s*$", texto)), texto)
                    y_anterior = None
                    continue
                if comecou and atual is not None and "Italic" in fonte and x < 165:
                    novo_paragrafo = y_anterior is None or y - y_anterior > 11.5
                    seguinte = spans[1]["text"].lstrip() if len(spans) > 1 else ""
                    fecha_rotulo = texto.endswith((".", ":")) or seguinte.startswith((".", ":"))
                    if novo_paragrafo and fecha_rotulo and texto[:1].isupper():
                        entradas.append({"ini": atual[0], "fim": atual[1], "aberto": atual[2], "cabecalho": atual[3],
                                         "rotulo": texto, "pagina": num + 1})
                y_anterior = y
    return entradas


def main() -> None:
    pdf = Path(sys.argv[1])
    entradas = ler_entradas(pdf)
    if "--listar" in sys.argv:
        for e in entradas:
            if e["ini"] >= 1946:
                print(e["cabecalho"], "|", e["rotulo"], "| p.", e["pagina"])
    anos = range(1946, 2024)
    iniciados = {a: 0 for a in anos}
    ativos = {a: 0 for a in anos}
    for e in entradas:
        if e["ini"] in iniciados:
            iniciados[e["ini"]] += 1
        fim = 2023 if e["aberto"] else e["fim"]
        for a in range(e["ini"], fim + 1):
            if a in ativos:
                ativos[a] += 1
    SAIDA.parent.mkdir(exist_ok=True)
    with SAIDA.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["ano", "episodios_iniciados", "episodios_ativos", "fonte", "nota"])
        for a in anos:
            nota = "parcial: o relatorio cobre ate abril/2023" if a == 2023 else ""
            if a >= 1980:  # palavras do próprio CRS: "Most occurrences listed since 1980 are summaries [...] War Powers Resolution"
                nota = (nota + "; " if nota else "") + "desde 1980 a lista e sobretudo resumo de relatorios da War Powers Resolution, inclusive de operacao ja em curso"
            w.writerow([a, iniciados[a], ativos[a], "CRS R42738 (07/jun/2023)", nota])
    print("entradas 1946-2023:", sum(iniciados.values()))


if __name__ == "__main__":
    main()
