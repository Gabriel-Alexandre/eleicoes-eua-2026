# Revisão adversarial: viés contra Trump e os republicanos, ou alarmismo

**Papel:** o leitor que acha que a análise pende contra os republicanos. **Revisão de 02/nov/2026, antes da votação**, sobre o commit `15ecaa9`.

**Como ler a evidência.** `slug` é arquivo em `documentacao/referencias-conteudo/roteiros/videos-longos/VIDEO_024_ELEICOES_EUA_2026/referencias/textos/`. URL é página aberta nesta revisão. O que veio só de resumo de buscador está marcado e não sustenta objeção. As contas são minhas, feitas com os arquivos do projeto.

**Veredito.** Nas probabilidades condicionais, o viés é pequeno, e o relatório acerta em separar fala de ato. O problema está na parte de quem ganha: a fonte mais desfavorável aos democratas foi deixada de fora mesmo estando capturada, e erro de pesquisa e redesenho não aparecem em nenhum texto público. Corrigir isso move o mundo RR de 6,3% para perto de 8%, com teto de 15%. O risco republicano fica maior e mais visível, sem mudar quem é favorito.

---

## A. Gravidade alta

### A1. O Decision Desk HQ foi cortado da tabela de chances, e é a fonte menos favorável aos democratas

**Evidência.** `previsoes/ddhq-forecast` traz, na mesma página de onde saiu o 84% da Câmara:

| Decision Desk HQ, 02/nov | % |
|---|---|
| Democratas nas 2 casas | 63 |
| Republicanos no Senado, democratas na Câmara | 21 |
| Republicanos nas 2 casas | 15 |
| Democratas no Senado, republicanos na Câmara | 2 |
| Senado democrata | 65 |

`dados/e2_chances.csv` guarda do DDHQ só `camara_d = 84` e 241 cadeiras, com Senado e combinações em branco. Como `analise.py` faz `dropna(subset=["DD"])`, ele fica fora da mediana.

O mesmo corte aparece em outras fontes capturadas:
- `previsoes/pollcheck`: Senado democrata 68%, republicano 30%, nenhum 3%, e Câmara 230 a 205. A PollCheck é a fonte da aprovação usada no relatório, mas não entra nas chances.
- `mundo/cnbc-wall-street`: a Wolfe Research dá 49% ao Senado democrata (27/out). Os investidores que ela ouviu dão 58%.
- `previsoes/wion-mercados`: mercados com 71% e 72% no Senado.

O relatório escreve *"Senado democrata de 76% a 80,1% nos modelos"* e *"cadeiras democratas na Câmara de 236 a 241"*. A faixa real capturada é **65% a 80,1% nos modelos, 49% numa casa de análise**, e **230 a 241** cadeiras. O dossiê entregue aos modelos também dizia *"DD de 74 a 75%"* e *"RR de 4,5 a 8%"*, sem o 63 e o 15.

**O que muda.** Os números abaixo são os meus, com DDHQ na mediana.

| Mundo | Relatório | Com DDHQ | Só DDHQ |
|---|---|---:|---:|
| DD | 75,1 | 72,8 | 63,6 |
| DR | 18,6 | 19,4 | 21,2 |
| RR | 6,3 | 7,8 | 15,2 |

- Refazer `e2_chances.csv` com todas as fontes e publicar a faixa, sem casa decimal no resumo.
- Nas perguntas, as médias ponderadas mudam até 1 ponto com a mediana nova e até 5,3 só com DDHQ (T06 de 51,4 para 46,1; W03 de 53,0 para 47,9; T01 de 46,6 para 42,1). As condicionais não mudam.
- Registrar em `docs/RODADAS.md` que o dossiê da condição B saiu com a faixa estreita. As previsões gravadas ficam como estão, como manda a regra do projeto.

### A2. O erro de pesquisa contra republicanos não aparece, e o projeto tinha o material

**Evidência.** Os termos `2016`, `2024`, *polling* e *erro de pesquisa* não aparecem em `RELATORIO.md`, `RESUMO_SIMPLES.md`, `docs/LEITURA_DA_IA.md` nem `dossie_b.md`. A captura traz:
- Silver: *"another embarrassing systematic polling error"* (`previsoes/newsweek-silver-final`).
- Newsweek: sub-representação de republicanos *"as occurred in 2016 and 2024"* (mesmo arquivo).
- Cohn, da NYT, sobre um possível *"misfire"* e *"it's absolutely possible that Democrats will be disappointed once more"* (`previsoes/yahoo-silver-80`).
- FiveThirtyEight: voto genérico de D+7,3 em 2020 para resultado de D+3,0, erro de 4,3 pontos; erro médio de 3,0 pontos em 21 ciclos (`historico/538-best-tool-2022-arquivo`).

**A conta que falta.** Média de voto genérico do relatório, D+8,6. Limiar estimado para os democratas levarem a Câmara depois do redesenho, cerca de D+4 ([Morris, 10/mai/2026](https://www.gelliottmorris.com/p/2026-05-10-dem-house-pop-vote-threshold-gerrymandering)). A folga é de **4,6 pontos**, ou 3,8 usando a média do DDHQ (D+7,8, em `previsoes/midtermforecast`). Um erro do tamanho do de 2020 leva a disputa para perto do limiar. A frase da Wolfe, de que seria preciso erro *"well above"* o de 2020 (`mundo/cnbc-wall-street`), parece forte demais diante dessa conta, embora o limiar seja estimativa de maio.

**No Senado o risco é mais concreto.** Em 2020 Collins liderou em nenhuma pesquisa independente e venceu por 8,6 pontos (`previsoes/pollcheck` traz 51 a 42,4; a ausência de liderança vem de resumo de buscador, e falta abrir a página). Hoje a pesquisa dá Jackson +2,7 no Maine, e o mercado dá 73% (`previsoes/pollcheck`, `previsoes/cryptonews-kalshi-polymarket`). O mundo DD depende de estados vermelhos, justamente onde Cohn alerta.

**Onde a objeção perde força, e o relatório deve dizer também.**
- A coluna do próprio `e1_midterms.csv`, comparando genérico final com voto nacional, nunca foi usada. Em 18 midterms o erro médio é de -0,55 ponto: as pesquisas tendem a subestimar um pouco a oposição.
- Só 2006 passou de 4,6 pontos no sentido de superestimar a oposição (5,6). E 2006 foi uma onda contra presidente republicano impopular, o caso mais parecido com este.
- 2018 (-1,7) e 2022 (-0,1) foram bons. Os grandes erros de 2016, 2020 e 2024 são de anos presidenciais com Trump na cédula. [Barker, da Brookings](https://www.brookings.edu/articles/democrats-on-track-to-outperform-2026-house-forecasts/), rejeita o risco para 2026 porque *"2018 and 2022 were both relatively accurate polling years"*.
- O erro de 2024 no voto genérico não foi conferido nesta revisão.

**O que muda.** Uma seção curta em §3 com o histórico de erro, o limiar e a folga, e a pergunta *"o que acontece com um erro como o de 2020"*. Uma linha no resumo simples. Rascunho de tamanho do risco, com a folga de 4,6 e erro normal: 3,8% com o desvio de 2,6 usado pelo Midterm Forecast, 9,1% com 3,45 (midterms desde 2006, `e1`), 11,1% com 3,76 (equivalente ao erro médio de 3,0 da FiveThirtyEight).

### A3. O redesenho de distritos sumiu dos textos, e o modelo simples aponta acima de todas as previsões

**Evidência.** *Redesenho*, *redistritamento* e *gerrymander* têm **zero ocorrências** em `RELATORIO.md`, `RESUMO_SIMPLES.md`, `LEITURA_DA_IA.md` e `dossie_b.md`. O dado está só em `docs/PESQUISA_CONGRESSO.md` B6: **+9 republicanos líquidos** em potencial.

O relatório diz que a perda republicana *"seria de 31,8 cadeiras pelo voto genérico, 37,6 pela aprovação e 41,4 pelos dois"*. Partindo de 218, isso dá de 176 a 186 republicanos, ou de **249 a 259 democratas**. As previsões capturadas ficam abaixo: 230 (PollCheck), 236 (Midterm Forecast, *"a gain of 23"*), 237 em noite boa (`previsoes/fox-power-rankings`, 13/out), 241 (DDHQ). O relatório põe os dois números um depois do outro, sem dizer que discordam em 8 a 29 cadeiras.

A regressão ignora 2 coisas que explicam parte da diferença:
- **O mapa novo.** A mediana dos distritos ficou cerca de 2 pontos mais republicana, e o colchão é de 7 ou 8 cadeiras (Barker, Brookings).
- **A exposição.** Quem tem 218 cadeiras tem menos a perder que quem tinha 241 em 2018 ou 256 em 2010.

**Onde a objeção perde força.** Os modelos de corrida usam o mapa novo (a metodologia do [Midterm Forecast](https://midtermforecast.com/methodology/) diz que sim), e a Fox escreve que o redesenho *"could fall short of expectations"*. Portanto o erro está no modelo simples e no silêncio, e os 75% não dependem dele.

**O que muda.**
- Dizer no §2 que o modelo não conhece mapa nem exposição, e que fica acima das previsões por corrida.
- Testar uma variável de cadeiras em risco, ou descontar o mapa. Sem isso, tirar o 41,4 do texto, porque a fala do vídeo tende a citar o número mais alto.
- Citar +9 potencial e o limiar de cerca de D+4 no §3.
- Fechar Virgínia em B6, deixada em aberto: a própria captura cita a queda do mapa em 08/mai (AP) e a recusa da Suprema Corte em 15/mai (`congresso/redis-ballotpedia`).

### A4. Mercados e modelos foram aceitos sem medir o histórico, e a IA foi chamada de errada antes da votação

**Evidência.** O projeto fez teste do passado para a própria regressão e nada para as fontes que dão os 75%. O relatório escreve *"O que a IA errou sem ler nada"*, porque os modelos deram de 18% a 30% ao DD contra perto de 75%. **Isso foi escrito antes da votação.** Ninguém errou ainda. E a condição B só repete o dossiê: DD de 72 a 74, RR de 6 a 7 (`dados/previsoes/rodada_b/*.json`), então ela não confirma nada.

O que existe sobre o histórico:

| Fato | Fonte |
|---|---|
| Em 2022, mercados deram 73% a um Senado republicano; a FiveThirtyEight tratou como moeda ao ar; os democratas mantiveram | [Morris, 26/mar/2026](https://www.gelliottmorris.com/p/why-we-trust-real-polls-over-prediction), que aqui tem lado: defende pesquisa contra mercado |
| Polymarket e PredictIt pontuaram abaixo da FiveThirtyEight em 2022, e o autor chama isso de *"basically just one data point"* | [First Sigma](https://firstsigma.substack.com/p/midterm-elections-forecast-comparison-analysis) |
| Em 2024 os mercados bateram os modelos na presidencial, e os modelos ganharam nas disputas menores | Morris |
| Mercados deram a liderança a Flávio Bolsonaro antes do 2º turno que Lula venceu | `previsoes/cryptonews-kalshi-polymarket` |
| Estudo de 72 milhões de operações da Kalshi: *"prices tracked outcomes closely"*. Outro: US$ 3.500 movem 97% dos mercados ligados às midterms em 5 centavos ou mais | [Decrypt, 20/out/2026](https://decrypt.co/380966/the-midterms-are-the-first-real-test-of-whether-markets-beat-pollsters). O número vale para mercados finos de corrida, menos para este de US$ 59 milhões |

Um detalhe conta a favor do projeto: o erro de 2022 foi **a favor** dos republicanos. Mercado não é viés antirrepublicano, é fonte com erro nas 2 direções.

**O que muda.** Trocar *"O que a IA errou"* por *"o que a IA achava antes de ler"*, com a cobrança depois de 03/nov. Acrescentar a tabela acima em §3 e uma coluna de qualidade em `e2_chances.csv`.

### A5. O *"muda muito"* de 28,2 pontos nasce da escolha das perguntas

**Evidência.** As 6 perguntas de Trump e Congresso são todas de conflito: dizer que houve fraude, maioria sem posse, 2 impeachments, paralisação, vetos. Em 28 perguntas, **nenhuma mede o que Trump consegue**: lei bipartidária sancionada, acordo orçamentário, juiz ou indicado confirmado, recuperação de aprovação. O próprio Trump diz *"you end up working on deals"* (`trump/voz-aceita-se-justa`), e nenhuma pergunta testa isso.

Parte do efeito é definição. Câmara republicana não aprova impeachment de Trump, então T03 e T04 dão 1% em RR por construção. T01 mede uma fala, e sozinha carrega 45,5 pontos: sem ela a média cai para 24,8. O número é a mediana de 4 modelos da mesma empresa, e o resumo o apresenta como *"Muito"*. O plano ainda declarava antes a conclusão esperada, *"muda muito dentro dos EUA"*, e as perguntas foram escritas sob ela.

**O que muda.** Não publicar 28,2 como medida de quanto os EUA mudam. Escrever *"nestas 6 perguntas, escolhidas sobre conflito"*. Numa rodada nova, em pasta nova, incluir perguntas do lado do que Trump consegue, como lei relevante sancionada com voto democrata, juiz da Suprema Corte confirmado e orçamento anual aprovado sem paralisação.

---

## B. Gravidade média

### B1. Impeachment: a base está inflada, e o número ficou abaixo do mercado sem explicação

**Base.** O relatório diz que desde 1994 a Câmara trocou 5 vezes, com *"presidente impedido em 2"*. Clinton foi impedido em dezembro de 1998, no 105º Congresso, 4 anos depois da troca (`dados/e3_impeachment_e_oversight.csv`). T03 cobre só o Congresso seguinte à eleição. Na mesma janela, o caso é **1 de 5** (Trump, 2019), e aconteceu por um episódio específico. A liderança votou *presente* nos arquivamentos (`docs/PESQUISA_CONGRESSO.md` B7).

**Mas a objeção de peso excessivo não passa.** Com democratas nas 2 casas, T03 dá 30,5% até 2029. A Kalshi dava 53% para impeachment antes de agosto de 2027, em qualquer mundo ([Action Network, 27/out/2026](https://www.actionnetwork.com/politics/trump-impeachment-odds-are-tied-directly-to-next-weeks-midterms)). E os 2 últimos arquivamentos tiveram 140 e 147 votos contrários (`docs/PESQUISA_CONGRESSO.md` B7). O projeto confia no mercado para os 75% e diverge dele por 2 vezes aqui, sem dizer.

**O que muda.** Corrigir para *"1 de 5 no Congresso seguinte à troca, 2 de 5 no prazo maior"*. Citar o preço de mercado ao lado de T03, com a divergência dita. Isso também mostra que mercado não é oráculo.

### B2. A mediana mistura fontes de qualidade muito diferente, sem avisar

Resposta à pergunta extra.
- **Midterm Forecast:** projeto independente de um desenvolvedor de software, Craig Vander Galien. Tem teste do passado só no Senado (138 corridas, de 91% a 100% de acerto na véspera) e diz literalmente *"House districts have few polls and are not backtested"*. Usa erro nacional de 2,6 pontos, abaixo do erro médio de 3,0 da FiveThirtyEight. Lista a Kalshi entre as fontes, e não verifiquei se ela entra no cálculo ([metodologia](https://midtermforecast.com/methodology/)). Tem método público, então *"duvidoso"* é exagero. Mas a previsão de Câmara dele não tem histórico testado, e ele pesa 1 em 3 na mediana, enquanto o DDHQ, de casa estabelecida, ficou fora.
- **Poliwave:** **não está na tabela.** Zero ocorrências no repositório e nas capturas. Aparece só como base de pesquisas usada pelo Midterm Forecast. A objeção, neste ponto, não procede.
- **Polymarket:** lido por um agregador de terceiros, `polyinsider.io`. No mesmo dia o mesmo mercado aparece com DD de 71% (`previsoes/wion-mercados`), 74,5% (`previsoes/polyinsider-balance`) e 78% (`previsoes/cryptonews-kalshi-polymarket`). Um único comprador pôs US$ 225.089 em DD, numa linha de US$ 14,6 milhões. *"75,1%"* tem precisão que a fonte não tem.
- **Kalshi:** lida num site de cripto. **O DR = 22 está mal lido:** o texto diz *"only gives Republicans a 22% chance of retaining Senate control"*, que é a chance do Senado republicano inteira, incluindo o RR. O DR é menor que 22.
- **Silver Bulletin e RacetotheWH:** só o Senado, via Newsweek, sem combinações. A página da RacetotheWH capturada não traz o número (`previsoes/rtwh-senado`).
- **Peso:** a mediana usa 3 fontes, 2 de mercado, que podem se influenciar com os modelos. Não são 3 sinais independentes. O plano citava Cook e Fox, que não entraram.

**O mundo RR está subestimado?** De leve, sem exagero. RR é quase igual à chance de Câmara republicana, porque Câmara republicana com Senado democrata fica entre 0,55% e 2%. Essa chance vai de 5 a 7 nos mercados (`previsoes/wion-mercados`), 9 no Midterm Forecast e 17 no DDHQ. Minha leitura: **central perto de 8, faixa de 5 a 15**. Os 6,3 ficam dentro, na metade de baixo. Também pesa contra a objeção que mercados costumam cobrar caro por azarões, então 4,5 pode até estar alto. O problema maior é a faixa escondida, mais do que o ponto.

**O que muda.** Publicar 3 linhas separadas (mercados, modelos com combinação, modelos só de Senado), corrigir o DR da Kalshi, indicar como cada um foi lido e dar a faixa no lugar de um número único.

### B3. O caso-espelho conta os freios e deixa de fora o que Trump conseguiu com a Câmara democrata

**Evidência.** O §5 do relatório cita USMCA como único resultado positivo. Foram sancionadas no 116º Congresso também: NDAA de 2020 (20/dez/2019), CARES (27/mar/2020), Great American Outdoors Act (04/ago/2020) e Consolidated Appropriations Act de 2021 (27/dez/2020) ([Wikipédia, 116º Congresso](https://en.wikipedia.org/wiki/116th_United_States_Congress); a pandemia explica parte). A Fase Um com a China está em `docs/PESQUISA_MUNDO.md` e no dossiê, e não no relatório. Nomeações foram adiante com o Senado republicano, o que pesa na diferença entre DR e DD e não tem pergunta nenhuma.

**Limite da objeção.** A tese central do relatório, de que o presidente faz muito sozinho, já é favorável a essa leitura.

**O que muda.** Acrescentar 1 linha ao §5 com essas leis e a Fase Um, e 1 frase separando DR de DD em nomeações.

### B4. *"I veto everything"* foi cortado, e a fala não está na base conferida

**Evidência.** `trump/ibtimes-veto` traz: *"But if there was, you call it gridlock, what happens is I veto everything [...] And then the Democrats come and they want to make a deal. So we'll work it out."* Isto é barganha condicional. O §5 do relatório põe só as 3 palavras depois da estatística de vetos, em tom de intenção. A fala não está em `dados/e6_falas_trump.csv` nem em `docs/PESQUISA_TRUMP.md`, embora o §6 aponte para esses arquivos. O mesmo vale para *"you end up working on deals"*, que vem da Voz, veículo marcado com lado. A IBTimes é fonte fraca, e ainda não há segunda fonte.

**O que muda.** Citar a frase inteira, entrar com as 2 falas no CSV com o conferidor e buscar a transcrição de 23/out. O §6 já junta os 2 lados, e isso pode ficar.

### B5. *"O Trump vai contestar?"* responde a outra pergunta

**Evidência.** `RESUMO_SIMPLES.md` pergunta se ele vai contestar e responde com T01, que mede *"afirmar publicamente que o resultado nacional foi fraudado"*. Falar não é contestar, e isso nem sequer é a regra escrita. *"Fala ou post com a afirmação sobre o resultado nacional"* deixa aberto o que conta: *"rigged"* solto? Fraude em um estado? Ele já disse *"our elections are totally rigged"* em junho (`dados/e6_falas_trump.csv`). Em 02/nov, ele deu a linha oposta: *"the sitting president doesn't win the midterms, but we gave this a very strong shot"*, e Vance disse *"of course we're gonna support the results"*. A única previsão direta de que contestará é inferência de analista da CNN.

**O que muda.** Reescrever a linha como *"Vai dizer que foi fraude?"*. Fixar agora, em nota datada, como a regra será aplicada, sem mudar a pergunta gravada. Pôr no resumo também a chance de ato concreto, que é o que T02 tenta medir. E separar no fecho o que ele diz do que o governo faz, como o §6 já faz.

### B6. T02 pode dar SIM por causa de briga de presidência da Câmara, sem nada de Trump

**Evidência.** O título é *"uma maioria eleita deixa de tomar posse"*, e a regra é *"a Câmara ou o Senado não organizados com a maioria eleita até 05/01/2027"*. Em janeiro de 2023 a presidência da Câmara só saiu em 07/jan (conhecimento geral, não aberto nesta revisão). Com maioria estreita, como os 216 republicanos do cenário da Fox, uma repetição resolveria SIM e viraria manchete alarmista no vídeo. Outro caso que a regra não resolve: o governador do Alasca disse que pode não certificar (`trump/cnn-contestar-eleicao`), e a regra não diz como contar uma cadeira parada que decida a maioria. E T02 em RR (5%) maior que em DD (3%) só pode vir de brigas internas, o que confirma a mistura.

**O que muda.** Nota datada em `docs/RODADAS.md` explicando como T02 será lida. Na fala, não descrever como *"Trump impedir a posse"*.

### B7. O relatório traz a agenda dos democratas e nenhum argumento republicano

**Evidência.** `docs/PESQUISA_TRUMP.md` tem a seção *"O que dizem os democratas"* e não tem a equivalente. A vantagem republicana de gasto, citada em `previsoes/fox-power-rankings` (*"$400M GOP spending advantage"*, só título) e por Barreto (`previsoes/newsweek-silver-final`), não aparece. A matéria da Fox *"Six forces could help them defy history"* aparece só como título e não foi capturada. Em Congresso, as falas republicanas sobre o Brasil param em 2025, e isso está declarado (`docs/PESQUISA_CONGRESSO.md` A6).

**Crédito ao projeto.** Fonte com lado está marcada, inclusive à esquerda (Mediaite, Rawstory, Truthout). A Fox dá a Câmara como *"likely out of reach for the GOP"*, e Ginsberg, advogado republicano, é voz contra a tese da fraude. A amostra não é só de um lado. O vazio é o caso eleitoral republicano.

**O que muda.** Capturar a matéria das 6 forças e a do gasto, e escrever a seção *"o que dizem os republicanos"*, com o argumento na versão mais forte, no mesmo formato.

### B8. O Alasca e os monitores aparecem sem o contexto que importa

**Alasca.** O §6 cita *"o Alasca como fraudulent election"* e *"investigação no Alasca"* sem dizer que há base factual: a NYT noticiou que a campanha de Peltola e outros democratas recrutaram um segundo Dan Sullivan, o que ela nega (`trump/nbc-sets-stage-losses`). Ginsberg chama de *"remarkably politically clumsy and embarrassing"*, e também diz que *"there's not an illegality here"* (`trump/cnn-contestar-eleicao`). Sem isso, parece invenção. A pesquisa cita a negativa e Ginsberg, e omite a parte do constrangimento.

**Monitores.** O §6 lista *"mais de 1.000 monitores"* sem base de comparação. A CNN diz que a prática *"is nothing new"* e *"more than doubling"* em relação à última midterm. Foram 289 em 2022 e 714 em 2024, e os 1.000 são plano sob dúvida de capacidade, porque a divisão perdeu mais de 70% da equipe de carreira ([CBS, 18/ago/2026](https://cbsnews.com/news/justice-department-election-monitors-midterms)).

**O que muda.** 1 frase em cada, com os 2 lados.

---

## C. Gravidade baixa

| # | Objeção | Evidência | O que muda |
|---|---|---|---|
| C1 | *"Nenhuma fonte lida traz prova de fraude nacional até aqui"* soa estranho antes de haver votação | `RELATORIO.md` §6 | *"Até 02/nov, nenhuma fonte lida traz prova das alegações feitas sobre esta eleição"* |
| C2 | A aprovação de 37,9% em média inclui pesquisas de adultos, e a série histórica é Gallup. NBC, eleitores registrados, dá 40 | `docs/PESQUISA_TRUMP.md`. O relatório já avisa. Com 40, o modelo muda perto de 1,7 cadeira | Nada além do aviso já dado |
| C3 | Trump dizendo *"no"* a novo ataque ao Irã (NBC) não aparece em §6, onde a guerra é tema | `trump/nbc-liveblog-02nov` | 1 linha. Está no dossiê |
| C4 | *"Quem deve ganhar"* no resumo explica com aprovação e história, enquanto as chances vêm de pesquisa e mapa | `RESUMO_SIMPLES.md` | Trocar o porquê por *"pesquisas à frente, aprovação baixa e história; pode falhar se as pesquisas errarem como em 2020"* |

---

## D. O que testei e não se sustenta

- **Tratar fala como intenção.** O relatório declara o limite, separa fala de ato no §6 e lembra Suprema Corte e chefe do Estado-Maior. B4 e B5 são exceções pontuais.
- **Peso em fraude como conclusão.** T02 em 3%, *"fala é uma coisa, posse é outra"*, e o plano veta *"fraude"* como conclusão.
- **Modelos ignoram erro correlacionado.** O Midterm Forecast simula erro na mesma direção entre corridas (`previsoes/midtermforecast`), e Silver avisa sobre isso.
- **Só a imprensa de esquerda vê onda azul.** A Fox vê a Câmara fora de alcance para o partido, e a Wolfe chama Câmara democrata de *"obvious consensus base case"*.
- **Poliwave na tabela.** Não está.
- **Mais impeachment do que o razoável.** O número está abaixo do mercado. Ver B1.
- **`docs/LEITURA_DA_IA.md`.** O item 5 já admite que a simetria dos efeitos pode ser só o que os modelos não sabem.

---

## E. Limites desta revisão

- Fiz 8 buscas na web e abri as páginas citadas com URL. O leitor de páginas devolve trechos, não a página inteira, e a [Axios](https://www.axios.com/2026/06/07/redistricting-gerrymander-house-republicans-democrats) recusou o acesso.
- O limiar de D+4 é de maio, tem trecho sob assinatura e vem de um autor com posição própria. A faixa de 3 a 4,9 que vi em outras fontes veio só de buscador. Conferir antes de citar.
- A conta de 3,8% a 11,1% é rascunho, com a hipótese de erro normal, e não inclui o erro por distrito.
- Sou da mesma empresa dos modelos que produziram as previsões, e isso vale como limite também para esta revisão.
