# Pesquisa: o que uma Câmara ou um Senado de oposição consegue fazer

Levantamento feito em 02/nov/2026, às 21h de Brasília, antes das eleições de 03/nov. Nada aqui depende do resultado.

**Selos.** ✅ lido em documento primário ou em 2 fontes independentes. ⚠️ uma fonte só, fonte com lado, ou inferência minha marcada. ❌ o que circula e o texto não sustenta. ❓ não encontrado ou não lido.

**Datas.** Cada achado traz o fato (F) e a publicação (P).

**Onde estão os textos.** O slug é o arquivo em `documentacao/referencias-conteudo/roteiros/videos-longos/VIDEO_024_ELEICOES_EUA_2026/referencias/textos/congresso/<slug>.txt`, com a URL na 1ª linha. Os votos brutos estão em `dados/brutos/clerk/` (XML da Câmara, 676 votos de 2025 e 2026) e `dados/brutos/congresso_api/` (API do congress.gov).

**Três limites do acesso, e isso conta na leitura.**
1. `senate.gov` e todo subdomínio (`kaine.`, `foreign.`, `rickscott.`) recusaram este computador com 403, também no navegador. Os votos do Senado saíram do texto de ação do congress.gov, que traz número e placar, mas o voto de cada senador vem de imprensa.
2. `congress.gov` em página também deu 403. Usei a API dele e o espelho everycrsreport.com para os relatórios do CRS.
3. `federalregister.gov` pede CAPTCHA a automação. Não resolvi o CAPTCHA: li o PDF oficial na govinfo.gov.

---

## A. Brasil

### A1. A resolução do Senado contra as tarifas de 2025 ✅
- **S.J.Res. 81**, de Tim Kaine. **Aprovada por 52 a 48, voto 594, em 28/10/2025.** Fonte: `dados/brutos/congresso_api/acoes_sjres81.json`, `sjres81-cbs` (F e P 28/10/2025).
- **Republicanos a favor (5):** Collins, Murkowski, Tillis, McConnell, Paul (`sjres81-cbs`; lista oficial do Senado não lida).
- **Na Câmara:** recebida em 31/10/2025 e "Held at the desk" desde então. Nunca foi votada. A tentativa própria da Câmara, H.J.Res. 117, morreu antes: **moção de arquivar a retirada da comissão aprovada por 200 a 198 em 15/09/2025**, com Bacon e Massie contra arquivar (`clerk roll 265/2025`). Existe ainda a H.J.Res. 147, referida à comissão em 02/02/2026, sem voto.
- **Base legal:** Lei de Emergências Nacionais, 50 USC 1622: a emergência termina se for "enacted into law a joint resolution" (`lei-50usc1622`). Antes o texto aceitava resolução concorrente; o Congresso mudou depois da decisão sobre veto legislativo (`crs-lsb11281-pdf`, P abr/2025). Logo, mesmo aprovada nas 2 casas, iria ao veto.
- **Como a Câmara bloqueava:** a H.Res. 211 (11/03/2025, 216 a 214) fez cada dia do resto da sessão não contar como "calendar day" para essas resoluções (`crs-lsb11281-pdf`; o CRS diz "março de 2025" sem o número, e casei a H.Res. 211 pela data ⚠️). O bloqueio caiu em 10/02/2026, com a **H.Res. 1042 rejeitada por 214 a 217** e 3 republicanos com os democratas (`clerk roll 60/2026`, `tar-canada-cbc`).

### A2. A Suprema Corte, 20/02/2026 ✅
- *Learning Resources v. Trump*, com *V.O.S. Selections*: **a IEEPA não autoriza tarifas.** 6 a 3. Maioria de Roberts com Sotomayor, Kagan, Gorsuch, Barrett e Jackson nas partes centrais; dissidência de Kavanaugh com Thomas e Alito, e de Thomas (`scotus-thomsonreuters`, P 20/02/2026; `scotus-wiki`).
- Não ordenou prazo de devolução do dinheiro (`scotus-thomsonreuters`).
- O texto da decisão em supremecourt.gov não foi capturado ❓. Usei resumo jurídico e Wikipédia.

### A3. A tarifa atual de 25%, e o ponto central ✅ no texto, ⚠️ na conclusão
- **Base:** memorando presidencial de 15/07/2026 e aviso do USTR, ambos no Federal Register de 20/07/2026 (`s301-fr-pres-14654`, `s301-fr-aviso-14542`; determinação em `s301-fr-determ-11158`, P 04/06/2026). 25% adicional sobre "all goods of Brazil", valendo de 22/07/2026, 12h01 de Washington.
- **Base citada:** comércio digital e pagamento eletrônico, tarifas preferenciais, anticorrupção, propriedade intelectual, etanol e desmatamento ilegal. A audiência teve mais de 360 comentários e 77 testemunhas.
- **Exceções, lidas na nota 50 do anexo:** itens da lista (a)(ii), onde aparecem carne (0201, 0202), petróleo (2709), gasolina (2710.12), suco de laranja (2009.11, 2009.12, 2009.19), castanha-do-pará (0801.2x), café (0901) e café solúvel (2101.11); aeronaves civis e peças; informação, doações e bagagem; e tudo que já paga Seção 232. O USTR acrescentou hidróxido de alumínio, antiguidades, couro, frutos do mar, ferro-gusa, mel orgânico e roupa usada, entre outros.
- **Por que carne ficou de fora:** o aviso responde a quem queria tirar a isenção por ligação com desmatamento: "There remains limited availability of these products outside of Brazil".
- **Soma:** desde 24/07/2026 há outra 301, de trabalho forçado, em 60 economias. A DHL diz que o Brasil pode pagar 25% mais 12,5% (`s301-dhl`, P 20/08/2026). ⚠️ uma fonte; o aviso dessa 301 não foi lido.

**O caminho da resolução de 2025 ainda existe contra a 301? Pelo texto, não.**
1. A 50 USC 1622 só termina "national emergency". Procurei "national emergenc" nos 3 documentos da 301 do Brasil: **0 ocorrências**. A tarifa não está apoiada em emergência.
2. Procurei "joint resolution" no texto de 19 USC 2411, 2412, 2414, 2415, 2416 e 2417: **0 ocorrências**. As seções 2413, 2418, 2419 e 2420 não foram lidas ❓.
3. O rito de desaprovação da lei de comércio, 19 USC 2192, só cobre as ações da seção 203 e os relatórios de 402(b) e 409(b) (`lei-19usc2192`). Não cita a 301.
4. O CRS, atualizado em 02/07/2026, diz que o Congresso "may debate whether to maintain, limit, or expand the scope of the authority" e cita projetos de revisão como H.R. 2665/S. 1272 (`crs-if11346-everycrs`). Em nenhum trecho lido oferece rito de desaprovação.
5. **Conclusão, minha:** contra a 301 sobra lei comum, com maioria na Câmara, 60 votos para encerrar o debate no Senado (CBS cita o patamar como regra da "most legislation") e sanção, ou 2/3 contra o veto. A S.J.Res. 81 passou com 52 por ter rito próprio; esse rito não se aplica aqui. Nenhum advogado de comércio foi lido dizendo isso com todas as letras: o alerta é ⚠️.
6. **A trava do relógio:** a 301 termina em 4 anos se ninguém da indústria beneficiada pedir continuação (`lei-19usc2417`). O USTR também pode modificar ou encerrar, sujeito à direção do presidente, e tem de relatar ao Congresso.
7. **Ação judicial contra a 301 do Brasil:** ❓ não pesquisado.

### A4. O embaixador ✅ no Senado, ⚠️ no que vem depois
- **Daniel Perez**, então presidente da Câmara da Flórida. Indicado em 01/06/2026, audiência em 16/07, **confirmado por 51 a 47 em 07/08/2026** (`perez-cartacapital`, `perez-bloomberg`, `perez-wiki`). Registro da votação no Senado não lido ❓.
- **Agrément:** não concedido até 29/10/2026. CNN Brasil (P 29/10): o Planalto avalia esperar a fuga de Flávio "decantar" e também "qual será a estratégia da Casa Branca" depois das eleições americanas (`perez-cnnbrasil`). SBT (P 29/10) diz o mesmo sentido (`perez-sbt`). Outra matéria, de 17/10, dizia que sairia até o fim do ano (`perez-brasilemfolhas`, veículo menor) ⚠️. Portanto a previsão mudou.
- **O visto da embaixadora:** o governo Trump revogou o de Maria Luiza Viotti em agosto; Meeks e Kamlager-Dove, com mais 10, cobraram em 07/10/2026 (`carta-kamlager-release-1007`).
- **O que muda conforme o Senado, inferência ⚠️:** nada para Perez, que já tem a confirmação; quem falta é o Brasil. Um Senado democrata afetaria indicados futuros. Nenhuma fonte lida trata de outra coisa.

### A5. A carta dos 25 ✅ (texto original lido)
- **Documento:** `carta-original-pdf`, 29/10/2026, publicada em 30/10 (`carta-kamlager-release-1030`). 15 perguntas, resposta por escrito **até 13/11/2026** e pedido de reunião com assessores.
- **Assinam (25, contei no PDF):** Kamlager-Dove, Titus, Casar, Ivey, Crockett, J. Jackson, Jayapal, Velázquez, Grijalva, Tlaib, Norton, McGovern, Quigley, Pocan, Stanton, Chuy García, Ansari, Ross, Lynch, Frankel, Casten, Pingree, Amo, Ramirez, Castro. Norton é delegada sem voto em plenário.
- ❌ **Meeks e Raskin não assinam.** Quem vincular a carta aos 2 presidentes prováveis erra.
- **É carta, não intimação** (`carta-riotimes`, produzida por sistema automático da redação, conferida no PDF). Rubio disse que os EUA "not directly involved" (`carta-rubio-batimes`, P 01/11).
- **Base da entrada em disputa:** DHS diz que foi inspecionado e liberado pela CBP (Politico em `carta-yahoo-politico`); o NYT, citado em `carta-msnow` (fonte com lado), fala em *parole*. A carta fala em visto. ❓ Ninguém do governo explicou a base.
- **Quem presidiria:** Meeks é o principal democrata em Relações Exteriores (`carta-kamlager-release-1007`) e Raskin em Judiciário (`intim-judiciary-dem`). Presidir depende da votação na bancada: ⚠️ é expectativa por antiguidade. Raskin disse em 05/10/2026 que usaria intimações, sobre pardons e família Trump, não sobre o Brasil (`intim-raskin-political`, veículo menor).
- **Poder de intimação:** só comissões têm; a maioria das regras da Câmara deixa o presidente da comissão emitir sozinho (`intim-mondaq`, escritório de advocacia, P 17/04/2026; `intim-lasher`, democrata). **O limite:** contra autoridade do executivo o desacato criminal "will likely prove unavailing" e o Departamento de Justiça tende a não processar sob privilégio (`crs-rl34097-everycrs`).
- **Deportar:** o Congresso não pode (`carta-dcm`, professores citados, veículo com lado) ⚠️.

### A6. Falas de congressistas
**Democratas**
- Kaine, 28/10/2025: a emergência é "unusual and extreme" e veio da "decision to prosecute Donald Trump's friend" (`sjres81-cbs`, `falas-cnn-5-republicans`) ✅.
- Shaheen, Kaine e Welch a Rubio, 28/09/2026: pedem compromisso de "reconhecer o resultado certificado" (`falas-senadores-sbt`) ⚠️ tradução; original em senate.gov recusado.
- Sanders e 30 deputados, liderados por Ramirez, 24/09/2026 (`falas-deputados-truthout`) ⚠️ fonte com lado.

**Republicanos**
- Salazar (Flórida), 09/07/2025: pede Magnitsky contra Moraes, "radical judge"; 30/07/2025 comemora (`falas-salazar-x-pedido`, `falas-salazar-x-magnitsky`, posts dela) ✅ como fala.
- Salazar, ago/2025: Lula quer "turn Brazil into another Cuba" (`falas-salazar-2025-cibercuba`) ⚠️.
- Salazar, Giménez, McCormick, Smith e Rick Scott pediram em 18/09/2024 a revogação de vistos de ministros do STF (`falas-salazar-2024-house`) ✅.
- Chris Smith presidiu audiência em 07/05/2024: "under attack by Lula government" (`falas-smith-audiencia-2024`) ✅.
- McConnell, contra a tarifa: "The economic harms of trade wars are not the exception to history, but the rule" (`sjres81-cbs`) ✅.

❓ **Não encontrei fala de 2026 de Salazar, Giménez, Díaz-Balart ou Scott sobre Flávio, a eleição do Brasil ou a 301.** Portanto "republicanos da Flórida defendem endurecer" está sustentado até 2025 e não em 2026. Os 5 republicanos do Senado que votaram contra a tarifa não incluem nenhum da Flórida. Não li o voto a voto, mas CBS os nomeia.

### A7. PCC e CV ✅
- **Fato:** SDGT em 28/05/2026; FTO com efeito em 05/06/2026 (`pcc-state`, `pcc-fr-pdf`, `pcc-whitecase`).
- **Papel do Congresso, 8 USC 1189:** aviso sigiloso 7 dias antes aos líderes e às comissões; a designação "shall cease to have effect upon an Act of Congress"; "The Congress, by an Act of Congress, may block or revoke" (`lei-8usc1189`). Sendo lei, passa por veto (inferência ⚠️).
- ❓ **Não encontrei projeto que bloqueie a designação.** Quem assina o aviso é o Secretário de Estado; não há voto do Congresso no caminho.

---

## B. Geral

### B1. Poderes de guerra ✅
Lista completa em `dados/e4_votos_congresso.csv`. O resumo:

| Assunto | Câmara | Senado | Resultado |
|---|---|---|---|
| Irã 2025 | | S.J.Res. 59: 47 a 53 (27/06/2025) | morreu |
| Barcos | H.Con.Res. 61: 210 a 216 (17/12/2025) | S.J.Res. 83: 48 a 51 (08/10/2025) | morreu |
| Venezuela | H.Con.Res. 64: 211 a 213; H.Con.Res. 68: 215 a 215 | S.J.Res. 90: 49 a 51; S.J.Res. 98: 52 a 47 e depois 51 a 50 contra, com Vance | morreu |
| Irã 2026, concorrente | H.Con.Res. 86: **215 a 208** (03/06) | **50 a 48** (23/06) | **passou nas 2 casas** |
| Irã 2026, outras | H.Con.Res. 89: 214 a 208; H.Con.Res. 93: 220 a 204, 7 republicanos | H.Con.Res. 89: 49 a 50 (24/09); 11 votos em resoluções conjuntas de 2026 com placar lido, todos perdidos | morreu |

- **Veto:** ❌ **nenhum veto de poderes de guerra neste mandato**, porque nada do tipo chegou à mesa dele. A que passou é concorrente: não vai ao presidente. "A Casa Branca efetivamente ignorou", argumentando que a lei é inconstitucional (`wp-cnbc-setembro`, P 24/09/2026; `wp-asil-junho`).
- **PBS** escreve em 06/06 que o Senado precisaria de 60 (`wp-pbs-politifact`). ❌ A H.Con.Res. 86 passou com 50 a 48. A CNBC fala em patamar de 50 votos na concorrente.
- Voto de 19/05/2026, 50 a 47 (`wp-pbs-politifact`), ainda não localizado no congresso.gov ⚠️.
- A H.Con.Res. 86 veio depois do prazo de 60 dias: Trump declarou a ação "terminated" em 01/05 por causa do cessar-fogo (`wp-pbs-politifact`) ⚠️.

### B2. Vetos ✅
**2 vetos, 0 derrubados** até a página lida: H.R. 131 e H.R. 504, em 29/12/2025 (`vetos-ballotpedia`). Câmara em 08/01/2026: **248 a 177** e **236 a 188**, ambos abaixo de 2/3 (`clerk roll 9 e 8`). A página oficial do Senado recusou o acesso ❓, e a data de atualização da Ballotpedia não é clara. Nenhuma votação com "Objections of the President" apareceu no restante do índice da Câmara até o voto 314, de 16/09/2026.

### B3. Resoluções de tarifa ✅
| Medida | Casa | Placar | Data |
|---|---|---|---|
| S.J.Res. 37, Canadá | Senado | 51 a 48 | 02/04/2025 |
| S.J.Res. 49, global | Senado | rejeitada (voto 225); placar 49 a 49 ⚠️ | 30/04/2025 |
| S.J.Res. 81, Brasil | Senado | 52 a 48 | 28/10/2025 |
| S.J.Res. 77, Canadá | Senado | 50 a 46 | 29/10/2025 |
| S.J.Res. 88, global | Senado | 51 a 47 | 30/10/2025 |
| H.J.Res. 72, Canadá | Câmara | 219 a 211 | 11/02/2026 |

A H.J.Res. 72 parou na Comissão de Finanças do Senado em 12/02/2026. Nove dias depois a Suprema Corte tirou a base. **Nenhuma virou lei.**

### B4. Derrubar veto e composição
- 2/3 dos presentes; com casa cheia, **290 na Câmara e 67 no Senado** (conta minha; regra em `vetos-ballotpedia`).
- **Câmara hoje:** 218 republicanos, 214 democratas, 1 independente (Kiley), 2 vagas (`camara-congresscountdown`, data 02/11; `camara-ballotpedia` 218 e 2 vagas) ⚠️ não vem da Clerk.
- **Senado hoje:** 53 a 47 (`camara-congresscountdown`, `senado-ballotpedia`).
- **Conta:** o maior número de republicanos que cruzou em tarifa foi 6 na Câmara e 5 no Senado; em guerra, 7 e 4. Com 47 democratas, 67 pedem 20 republicanos. Com 51 democratas, 16.

### B5. Senado em jogo ✅
35 cadeiras: 33 normais (20 republicanas, 13 democratas) e 2 especiais, Flórida e Ohio, ambas republicanas. Republicanos defendem 22 e democratas 13. Democratas precisam de **4 líquidas**, porque Vance desempata; republicanos podem perder 2 (`senado-ballotpedia`, `senado-wiki`). Cassidy e Cornyn perderam primárias (`senado-wiki`).

### B6. Redesenho ⚠️ (são potenciais, não resultados)
Ballotpedia, set/2026: Alabama +1 R, Califórnia +5 D, Flórida +4 R, Louisiana +1 R, Carolina do Norte +1 R, Ohio +2 R, Tennessee +1 R, Texas +5 R, Utah +1 D. **Líquido +9 R** (15 menos 6, conferi; `redis-ballotpedia`). A Wikipédia e a MultiState contam de outro jeito (`redis-wiki`, `redis-multistate`). Missouri voltou ao mapa antigo para a eleição geral, depois de idas e vindas (`redis-multistate`, `redis-ballotpedia`). Virgínia: passou em referendo e foi questionada na corte estadual (`redis-votingrightslab`); resultado final não conferido em 2 fontes ❓.

### B7. Impeachment ✅
- **Votos, todos moções de arquivar:** H.Res. 537, **344 a 79** (24/06/2025); H.Res. 939, **237 a 140, 47 presente** (11/12/2025); H.Res. 1486, **232 a 147, 47 presente** (15/09/2026). Autor da última ❓.
- **O movimento:** Jeffries, Clark e Aguilar foram de sim para presente. Raskin foi de sim para não, em 12/2025. Meeks foi de sim para presente e para não, em 09/2026 (lido nos XML).
- **Trump:** em janeiro disse aos republicanos da Câmara que será impedido se perderem (`imp-hill-jeffries`, P 26/04) ⚠️ 1 fonte; disse à Punchbowl que seria "very unfair" (`imp-couric`, P 28/10); e "if we wanted to play that game, we could play it just as well" (`imp-rawstory`, fonte com lado).
- **Jeffries:** "of course not" como prioridade (`imp-hill-jeffries`); não é foco "at this moment" (`imp-cnbc-jeffries`, 02/06); "We haven't ruled anything in, and we haven't ruled anything out", setembro (`imp-couric`).
- **A conta:** impeachment pede maioria simples; condenar, 2/3 do Senado. Dos 7 republicanos que condenaram em 2021, Collins e Murkowski ficam em 2027 (`imp-couric`).

### B8. Orçamento ✅
- **Paralisações:** 43 dias, de 01/10 a 12/11/2025, a maior geral; 3 dias em 01/2026; **75 dias no DHS, 14/02 a 30/04/2026**, a maior parcial (`crs-r49491-everycrs`). Brookings confirma os 43 (`shutdown-brookings`). A contagem de 76 dias vista em buscador não foi lida no texto ❓.
- **Rescisão de bolso:** a lei dá 45 dias para o Congresso aprovar; sem aprovação, o dinheiro "shall be made available" (`lei-2usc683-ica`). Em ago/2025, quase US$ 5 bi em ajuda externa; em 25/09/2026, **US$ 810 milhões**. O GAO disse em 29/09/2026 que é ilegal; "unlikely to have any practical effect unless the GAO takes the administration to court"; Vought respondeu que o órgão é "hyper partisan" (`pocket-rollcall`, `pocket-hill`).
- **O freio:** a Suprema Corte suspendeu a ordem de gastar em 26/09/2025, dizendo que o governo mostrou, "at this early stage", que a lei de 1974 impede a ação de terceiros. Jackson, Kagan e Sotomayor discordaram (`pocket-wiki-avac`) ⚠️ Wikipédia transcrevendo a ordem. Decisão de mérito ❓.
- **Conclusão minha:** o Congresso de oposição segura dinheiro novo, mas perto do fim do ano fiscal o presidente segura dinheiro já aprovado, e a saída é judicial e lenta.

---

## C. Academia

| Obra | O que mediu | Número | Selo |
|---|---|---|---|
| Howell e Pevehouse, *Presidents, Congress, and the Use of Force*, IO 2005, base do livro de 2007 | "clear connection" entre composição do Congresso e frequência trimestral de grandes usos da força, 1945 a 2000; **nada nos pequenos** | efeito ❓ | ✅ resumo `ac-howell-io-repec` |
| Howell e Pevehouse, *While Dangers Gather*, 2007 | a probabilidade de envio cresce com o apoio partidário; crítica: o alvo pode reagir a isso e o autor não testou | efeito ❓ | ⚠️ resenha `ac-howell-unb`, `ac-howell-erudit` |
| Kriner, *After the Rubicon*, 2010 | projetos, audiências e debate pesam no custo político que o presidente calcula | ❓ não lido | ⚠️ editora `ac-kriner-chicago` |
| Milner e Tingley, *Sailing the Water's Edge*, 2015 | o poder do presidente varia por instrumento: menos onde há interesse material e divisão ideológica | ❓ não lido | ⚠️ `ac-milner-niehaus`, `ac-milner-hv` |
| Mayhew, *Divided We Govern*, 2005 | governo dividido "no less productive of important legislation", mas associado a investigações | os 267 ❓ só no buscador | ⚠️ blurb `ac-mayhew-yale` |
| Binder, APSR 1999 | "intrabranch conflict, perhaps more than interbranch rivalry", explica o bloqueio, 1947 a 1996 | ❓ | ✅ resumo `ac-binder-econpapers` |
| Canes-Wrone, Howell e Lewis, JoP 2008 | presidentes têm "considerably greater influence over foreign policy", em orçamento e criação de agências | ❓ | ✅ `dados/brutos/academia/canes_openalex.json` |
| Tufte, APSR 1975 | 10 pontos de aprovação = 1,3 ponto no voto; US$ 100 de renda real = 3,5 pontos; explica **91,2%** da variância; 1938 a 1970, sem 1942 | sim | ✅ `ac-tufte-pdf` |
| Abramowitz; Bafumi, Erikson e Wlezien; Campbell | previsões de 2010: 49, 50 e 51 cadeiras a partir de cédula genérica ou cadeiras em risco | sim, de 2010 | ⚠️ blog de cientistas políticos `ac-modelos-monkeycage` |
| Bendekgey 2018 | repete os modelos em 2018: "a weakening of many traditional forecasting indicators" | | ⚠️ `ac-modelos-arxiv`, trabalho sem revista |

**A leitura junto:** o Congresso pesa mais no começo e no custo do que no final, e pesa mais em tarifa e ajuda (interesse material) que em força. O caso de 2025 e 2026 confirma parte: um Congresso republicano estreito levou a votos que não mudaram a guerra, e a queda da IEEPA veio da Corte, não de lei. Isso é interpretação minha, não resultado dos autores.

---

## Em aberto

1. Voto a voto do Senado (`senate.gov` recusado), inclusive Perez.
2. Placar de S.J.Res. 49, voto de 19/05/2026 e outras etapas: as listas da API só dão a última ação. Faltam chamadas, porque a chave pública de teste esgotou.
3. Texto da decisão da Suprema Corte, do aviso da 301 de trabalho forçado e dos relatórios de 2 CRS no original.
4. Opinião jurídica explícita sobre a falta de rito contra a 301, e ação judicial contra ela.
5. Falas de 2026 de republicanos da Flórida sobre o Brasil.
6. Tamanho de efeito de Howell e Pevehouse, Kriner e Milner e Tingley. Os livros não foram lidos, só resumos e resenhas.
7. Resultado final de Virgínia e números finais do redesenho.
8. Qualquer resposta de Rubio à carta: até o texto mais novo lido, nenhuma.
