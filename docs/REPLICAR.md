# Como refazer

```bash
pip install -r requirements.txt
python ferramentas/coletar_brasil.py        # PTAX do BCB e exportações do ComexStat, com hash em dados/MANIFESTO.json
python dados/gerar_historico.py             # refaz e1 e e3 a partir dos textos capturados (pasta do vídeo, no repositório documentacao)
python ferramentas/analise.py               # resultados/RESUMO.json
python ferramentas/agregar_previsoes.py     # resultados/previsoes.csv
python ferramentas/graficos.py              # resultados/figuras/
python ferramentas/gerar_relatorio.py       # RELATORIO.md, RESUMO_SIMPLES.md, docs/LEITURA_DA_IA.md
python ferramentas/validacao_independente.py
python ferramentas/conferir_linguagem.py
python -m pytest -q
```

`dados/brutos/` fica fora do git. Os textos e prints de cada fonte ficam no repositório de documentação, `referencias-conteudo/roteiros/videos-longos/VIDEO_024_ELEICOES_EUA_2026/`, com endereço e hora de captura.
