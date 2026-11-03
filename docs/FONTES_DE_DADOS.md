# Fontes de dados

| Dado | Fonte | Arquivo |
|---|---|---|
| Cadeiras e aprovação, 1946 a 2022 | American Presidency Project (UCSB), Brookings, Gallup, Câmara e Senado | `dados/e1_midterms.csv`, com divergências em `nota` |
| Chances de 02/nov | Midterm Forecast, Decision Desk HQ, Silver Bulletin e RacetotheWH (via Newsweek), Polymarket, Kalshi | `dados/e2_chances.csv` |
| Vetos | UCSB, conferidos com Câmara e Senado | `dados/e3_vetos_por_congresso.csv` |
| Uso da força | CRS R42738, versão de jun/2023 | `dados/e3_forca_por_ano.csv` |
| Tarifa média | USITC, Penn Wharton, Tax Foundation | `dados/e3_tarifa_media.csv` |
| Impeachment e intimações | Câmara, Ballotpedia, fontes por caso | `dados/e3_impeachment_e_oversight.csv` |
| Paralisações | CRS RS20348 | `dados/e3_shutdowns_por_ano_fiscal.csv` |
| Votos de 2025 e 2026 | Clerk da Câmara (XML), API do congress.gov, imprensa no Senado | `dados/e4_votos_congresso.csv` |
| Mecanismos | texto da lei, CRS | `dados/e4_mecanismos.csv` |
| Mundo | Reuters, AFP, centros de pesquisa | `dados/e5_mundo.csv`, `docs/PESQUISA_MUNDO.md` |
| Falas do Trump | transcrições e matérias, conferidas por script | `dados/e6_falas_trump.csv`, `docs/PESQUISA_TRUMP.md` |
| Dólar | Banco Central, série 1 do SGS | `dados/derivados/dolar_ptax.csv` |
| Exportações | ComexStat | `dados/derivados/exportacoes_brasil.csv` |

**Fontes secundárias, ditas como tal:** Silver Bulletin e RacetotheWH lidos via Newsweek; Kalshi via Cryptonews; Reuters, Politico e Jefferies em republicação; 2025 da tarifa em republicação da tabela da USITC. Fora do alcance deste computador: `senate.gov`, `congress.gov` em página, Cook Political Report, Crystal Ball e RealClearPolitics.
