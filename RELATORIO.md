# Relatório: eleições dos EUA de 2026, o que muda em cada resultado

**Rodada 1, 02/nov/2026, antes da votação de 03/nov.** Análise feita pelo Claude, com fontes capturadas e número saído de script (`resultados/RESUMO.json`). Comece pelo `RESUMO_SIMPLES.md`.

## O que este projeto não consegue dizer

- **O resultado.** Este relatório foi escrito antes da votação. As chances dos 3 mundos são de terceiros, não uma previsão própria.
- **Causa.** As comparações de antes e depois têm poucos casos, cada um com a sua história. Mostram o que veio depois, sem provar que veio por causa.
- **Intenção.** O que o Trump pretende não dá para ler de fora. O relatório separa o que ele disse do que fez.
- **As probabilidades de IA** são de 4 modelos da mesma empresa, com o mesmo texto: concordar entre eles não confirma nada, e modelos ainda perdem de previsores humanos treinados. Abaixo de 5%, o número é mais piso do que medida. A discordância média entre eles foi de 17,3 pontos no mundo DD.
- **Acesso:** `senate.gov` recusou este computador; o voto a voto do Senado vem de imprensa. Não há Gallup de 2026, porque a Gallup encerrou a medição em fevereiro.
- **Lei:** a conclusão de que não há rito rápido contra a tarifa da Seção 301 é leitura do texto da lei feita pela IA, sem parecer de advogado lido; as seções 2413 e 2418 a 2420 não foram lidas.

## 1. A resposta

**O resultado muda muito dentro dos Estados Unidos e pouco no que o Trump faz sozinho.** Entre democratas nas 2 casas e republicanos nas 2, a chance muda em média 28,2 pontos nas perguntas sobre Trump e Congresso, 10,1 nas do mundo e 6,2 nas do Brasil. Dentro do Brasil, 18,3 pontos no que depende de voto do Congresso (audiência, intimação, votação contra a tarifa) e 2,1 no resto (tarifa de fato, sanção, embaixador, encontro, ataque, exportação, dólar).

## 2. A história

- Nas 20 midterms de 1946 a 2022, o partido do presidente perdeu cadeiras na Câmara em 18, em média 25,6 (contando as 2 em que ganhou). Com aprovação abaixo de 50% (11 casos), 34,7; com 50% ou mais, 14,6.
- No Senado perdeu em 13 de 20, em média 3,6, e ganhou cadeiras com aprovação até 45% em 1982, 2018, 2022: o Senado depende de quais cadeiras estão em jogo.
- A Câmara trocou de mãos em 7 eleições (1946, 1954, 1994, 2006, 2010, 2018, 2022) e o Senado em 7 (1946, 1954, 1986, 1994, 2002, 2006, 2014).
- **Modelo simples:** com aprovação de 37,9% e voto genérico de D+8,6, a perda republicana seria de 31,8 cadeiras pelo voto genérico, 37,6 pela aprovação e 41,4 pelos dois.
- **Teste do passado**, deixando uma eleição de fora por vez (18 eleições): erro médio de 17,8 cadeiras pela aprovação, 15,9 pelo voto genérico, 15,2 pelos dois, contra 18,7 de só repetir a média. O modelo ajuda pouco e erra por muito. Maior erro do modelo dos dois: 1966, 33,1 cadeiras. Serve de ordem de grandeza.
- ⚠️ A aprovação de 2026 vem de outra fonte (média PollCheck), porque a Gallup parou. Ela varia de 31% a 40% conforme o instituto.

## 3. As chances, em 02/nov

Democratas nas 2 casas 75,1%, democratas só na Câmara 18,6%, republicanos nas 2 6,3% (mediana de Midterm Forecast, Polymarket e Kalshi, reescalada). Senado democrata de 76% a 80,1% nos modelos; cadeiras democratas na Câmara de 236 a 241. Tabela: `dados/e2_chances.csv`. **O que a IA errou sem ler nada:** sem a pesquisa, os 4 modelos deram de 18% a 30% ao mundo DD, contra perto de 75% dos modelos eleitorais e mercados.

## 4. O que o Congresso consegue e o que não consegue

Tabela: `dados/e4_mecanismos.csv`. Votos: `dados/e4_votos_congresso.csv`. Detalhe com fontes: `docs/PESQUISA_CONGRESSO.md`.

| Assunto | O que aconteceu | Leitura |
|---|---|---|
| Tarifa do Brasil de 2025 | Senado 52 a 48 pelo fim da emergência; parou na Câmara; a Suprema Corte derrubou a base em 20/02/2026 | quem tirou a tarifa foi a Corte, e o governo trocou de lei |
| Tarifa do Brasil de hoje | Seção 301, 25%, desde 22/07/2026; somada a 12,5% da 301 de trabalho forçado, segundo DHL e Reuters | pelo texto da lei, sem rito rápido: lei comum, 60 no Senado e veto |
| Lei Graham | 86 a 11, 262 a 159, sancionada em 18/09/2026; dispensada na parte da Rússia em 16/10, 28 dias depois | a lei deu ao presidente o poder de dispensar |
| Guerra do Irã | resolução concorrente passou nas 2 casas (215 a 208; 50 a 48); a Casa Branca ignorou | aprovar não obrigou |
| Veto | 290 e 67 com casa cheia; recorde de republicanos cruzando: 6 e 5 em tarifa, 7 e 4 em guerra | com 236 e 53 democratas, faltariam 54 e 14 |
| Embaixador | Perez confirmado por 51 a 47 em 07/08/2026 | quem falta é o Brasil; o Senado novo não muda isso |
| Caso Flávio | carta de 25 deputados, prazo 13/11; é pedido, sem força de intimação | maioria na Câmara dá poder de intimar; o desacato depende do Departamento de Justiça |

## 5. O que veio depois das outras vezes

- **Vetos desde 1981:** média de 12,7 por Congresso com governo dividido contra 0,7 com unificado; 8,7% derrubados. Trump: 0 no 115º, 10 no 116º (1 derrubado), 2 até agora no 119º. Em 23/10 ele disse *"I veto everything"* (IBTimes).
- **Impeachment:** desde 1994 a Câmara trocou 5 vezes; inquérito em 3 (1994, 2018, 2022); presidente impedido em 2, nenhum condenado.
- **Uso da força**, lista do CRS, 2 anos antes contra 2 depois de trocar a Câmara: subiu em 2, caiu em 3, igual em 1. Série fraca: mudou de critério e conta entradas de relatório. Howell e Pevehouse medem efeito do Congresso só nos grandes usos da força.
- **Tarifa média efetiva:** 1,8% em 2018, 2,6% em 2019, 2,8% em 2020, com a Câmara democrata. Hoje, 7,2% (maio).
- **O caso-espelho, 2019 e 2020:** a tarifa da China subiu de 10% para 25% em 10/05/2019, a saída da Síria veio sem o Congresso, o USMCA passou com 385 a 41, os limites de guerra foram aprovados e vetados, e o impeachment acabou em absolvição. Nada disso prova que perder a Câmara causou a alta.

## 6. O Trump

Falas e datas: `dados/e6_falas_trump.csv` e `docs/PESQUISA_TRUMP.md`. O essencial: aceita o resultado *"if they're honest elections"*; *"I veto everything"*; *"you end up working on deals"*; *"the sitting president doesn't win the midterms"*; o Alasca como *"fraudulent election"*. Na prática: mais de 1.000 monitores do Departamento de Justiça, investigação no Alasca, Suprema Corte mantendo bloqueada a regra dos Correios e sem planos de tropas nas zonas, segundo o chefe do Estado-Maior. Nenhuma fonte lida traz prova de fraude nacional até aqui.

## 7. As previsões, nos 3 mundos

Mediana de 4 modelos (fable, opus, sonnet, haiku), com a pesquisa lida, gravada em commit antes da votação. DD: democratas nas 2 casas. DR: democratas só na Câmara. RR: republicanos nas 2.

### Brasil
| Pergunta | Prazo | DD | DR | RR | Sem a história (DD, DR, RR) |
|---|---|---:|---:|---:|---|
| Os EUA reduzem a tarifa de 25% da Seção 301 contra o Brasil ou ampliam isenção relevante por acordo | 2027-06-30 | 45% | 45% | 41% | 26, 24, 21,5 |
| Trump e Lula se encontram pessoalmente | 2027-06-30 | 47,5% | 47,5% | 45% | 28,5, 27,5, 27,5 |
| Daniel Perez assume como embaixador dos EUA em Brasília | 2027-12-31 | 56,5% | 55,5% | 55,5% | 25, 34, 35,5 |
| Uma comissão da Câmara dos EUA faz audiência pública com o caso Flávio Bolsonaro entre os temas | 2027-12-31 | 30% | 30% | 11,5% | 36, 32,5, 23 |
| Uma comissão do Congresso dos EUA emite intimação (subpoena) sobre a entrada de Flávio Bolsonaro nos EUA | 2028-12-31 | 13,5% | 11% | 1% | 11,5, 10,5, 1 |
| A Câmara dos EUA aprova em plenário medida para encerrar ou limitar tarifas sobre o Brasil | 2028-12-31 | 27,5% | 26,5% | 3,5% | 28,5, 27,5, 3 |
| Os EUA aplicam sanção nominal nova a autoridade brasileira | 2027-06-30 | 12% | 12% | 13,5% | 12,5, 14, 15,5 |
| Os EUA encerram ou deixam de renovar a autorização de permanência de Flávio Bolsonaro | 2027-12-31 | 11,5% | 11,5% | 10,5% | 13,5, 12,5, 12 |
| Os EUA fazem ataque militar em solo ou águas territoriais brasileiras contra facção sem aval do Brasil | 2029-01-20 | 2% | 3% | 4% | 2,5, 3,5, 4,5 |
| As exportações do Brasil para os EUA em 2027 superam as de 2026 | 2028-02-29 | 57% | 57% | 55% | 47, 45,5, 44 |
| A PTAX de venda de 30/06/2027 fica abaixo da PTAX de 30/10/2026 | 2027-06-30 | 55% | 54,5% | 52% | 46, 46,5, 44,5 |
| O Brasil concede o agrément a Daniel Perez | 2027-06-30 | 50% | 49% | 48% | nova |

### Mundo
| Pergunta | Prazo | DD | DR | RR | Sem a história (DD, DR, RR) |
|---|---|---:|---:|---:|---|
| O Congresso aprova nova ajuda à Ucrânia de pelo menos US$ 10 bilhões | 2028-12-31 | 15% | 10,5% | 4% | 16, 10, 4,5 |
| O Congresso aprova lei nova de sanções contra a Rússia, além da Lei Graham de 18/09/2026 | 2028-12-31 | 15% | 11% | 6,5% | 23, 19, 17 |
| Uma resolução conjunta de poderes de guerra (a que vai ao presidente) passa nas 2 casas depois de 03/01/2027 | 2028-12-31 | 61% | 35% | 11% | 47,5, 18, 7 |
| O Congresso derruba um veto de Trump sobre tarifa ou uso da força | 2029-01-03 | 3,5% | 2% | 1% | 4, 2, 1 |
| A tarifa média efetiva dos EUA em 31/12/2027 fica pelo menos 3 pontos abaixo da de 31/10/2026 | 2027-12-31 | 14,5% | 13,5% | 10,5% | 25, 21, 16 |
| Os EUA fazem nova operação militar em país da América Latina sem aval do governo local | 2027-12-31 | 27,5% | 28,5% | 32,5% | 27,5, 30, 35 |
| EUA e China assinam acordo comercial formal | 2027-12-31 | 23,5% | 24,5% | 25,5% | 24,5, 25, 25 |
| Os EUA retomam ataques ao território do Irã | 2027-12-31 | 35,5% | 38% | 41,5% | 40, 42,5, 47,5 |
| Os EUA passam a cobrar a tarifa da Lei Graham de pelo menos 25% de algum país comprador de energia russa | 2027-12-31 | 9% | 7,5% | 7% | nova |

### Trump e Congresso
| Pergunta | Prazo | DD | DR | RR | Sem a história (DD, DR, RR) |
|---|---|---:|---:|---:|---|
| Trump afirma publicamente que o resultado nacional de 2026 foi fraudado | 2027-01-03 | 52,5% | 36% | 7% | 60, 47,5, 9 |
| Uma maioria eleita deixa de tomar posse no início do novo Congresso em 03/01/2027 | 2027-01-05 | 3% | 3% | 5% | 3,5, 3,5, 2 |
| A Câmara aprova artigos de impeachment contra Trump | 2029-01-03 | 30,5% | 26,5% | 1% | 36,5, 34, 1 |
| A Câmara aprova artigos de impeachment contra um secretário do governo Trump | 2029-01-03 | 30% | 30% | 1% | 37,5, 35,5, 1 |
| O governo federal fica paralisado por pelo menos 7 dias | 2027-12-31 | 42% | 42% | 33% | 36,5, 35,5, 20 |
| Trump dá pelo menos 10 vetos | 2028-12-31 | 58,5% | 39% | 4% | 45, 22,5, 4,5 |

**O que ler a história mudou:** em média, 6,6 pontos. As perguntas W02 e W03 foram corrigidas depois da condição A, então a comparação nelas é só aproximada.

## 8. O Brasil em números

- Exportações para os EUA, janeiro a setembro: US$ 29,4 bi em 2025, US$ 27,5 bi em 2026 (-6,5%). Para a China: US$ 75,6 bi e US$ 84,7 bi (+12%). Isso não mede só a tarifa.
- Depois da midterm de 2018, as exportações para os EUA foram de US$ 20,6 bi para US$ 22,1 bi; depois da de 2022, de US$ 27,9 bi para US$ 26,7 bi.
- Dólar: mediana de +0,8% em 30 dias depois das midterms de 1998 a 2022, com 6 altas e 1 queda, sem padrão útil: toda midterm cai em ano de eleição no Brasil, então não dá para separar. PTAX de 30/10/2026: R$ 5,4212.

## 9. O mundo

Por região, com divergências: `docs/PESQUISA_MUNDO.md` e `dados/e5_mundo.csv`. As fontes discordam sobre a Ucrânia (Reuters vê 2/3 possíveis para ajuda nova; autoridades europeias duvidam) e sobre a Europa (AFP: *"expectations are low"*; Smith: *"tremendous expectation"*).

## 10. O que acompanhar

03/nov, a votação; 13/nov, o prazo da carta dos 25; a proposta americana do grupo de trabalho sobre tarifas; a reunião de Vieira e Rubio; 14 e 15/dez, o G20 em Miami; 03/jan/2027, o novo Congresso; 05/jan, a posse do Lula; 07/abr/2027, o fim da licença do diesel russo.
