# VIDEO_024 · Plano do projeto e do roteiro

**02/nov/2026, na véspera da votação americana. Estado: em execução, com a autorização dele para ir do plano ao roteiro v1 sem parar** (*"seguindo o mesmo passo a passo [...] e afinal fazer commit push"*, no molde do pedido do vídeo 23). Fatos: [`PESQUISA.md`](PESQUISA.md). Projeto: `Downloads/repositorios/eleicoes-eua-2026`.

## 1. Objetivo final

> **Colocar a IA para analisar, com geopolítica e com o histórico dos Estados Unidos, o que muda de verdade no Brasil e no mundo em cada resultado das eleições de meio de mandato: se os democratas vencem, se os republicanos seguram, e o que o Trump tem dito e deve fazer em cada caso.**

Palavras dele: *"utilizar a IA para analisar de forma geopolítica, a partir de dados históricos dos Estados Unidos, e a partir disso tentar analisar o que é que a gente se espera de impactos aqui no Brasil, no caso da vitória de um lado, no caso da vitória de outro, o que é que o mundo se espera, o que é que o Donald Trump tem falado, quais são as informações mais recentes"*.

**Por que é diferente dos anteriores:** o 17 tratou da reação do mundo ao resultado brasileiro; o 21, do quadro de guerra até 2029; o 22, do próximo passo do caso Flávio. A forma daqui é outra: **um mapa condicional, "se A, então isso; se B, então aquilo"**, com a mesma pergunta respondida em cada mundo, e a resposta medindo **o quanto o resultado muda a resposta**. ⛔ Sem as 2 visões, sem critérios com peso por candidato. Não é eleição brasileira: a Res. TSE 23.755 não se aplica, mas as travas do assunto continuam (⛔ recomendação, julgar intenção, "fraude" como conclusão).

**O que o vídeo responde:** (1) quem deve ganhar e o que a história diz disso; (2) o que uma Câmara e um Senado de oposição conseguem e não conseguem fazer; (3) o que aconteceu de fato nas outras vezes em que o presidente perdeu a Câmara, com o caso-espelho de 2018 a 2020; (4) o que o Trump tem dito, inclusive sobre fraude, e o que tende a fazer em cada resultado; (5) o Brasil em cada mundo: tarifa, sanção, caso Flávio, embaixador, dólar; (6) o mundo em cada mundo: Ucrânia, China, Irã, América Latina; (7) a frase final: o que muda e o que não muda, com previsões gravadas.

**A conclusão esperada, a provar ou derrubar:** o resultado muda muito dentro dos EUA (fiscalização, intimação, orçamento, impeachment) e muda pouco e devagar na tarifa e na força, porque tarifa e força moram na mão do presidente, e derrubar veto exige 2/3. Para o Brasil, a mudança concreta é o custo político, as perguntas sobre o Flávio virando intimação e o Senado no embaixador. O caminho da resolução de 2025 contra as tarifas pode nem existir mais, porque a tarifa trocou de base legal.

**O que não consegue responder:** o resultado de amanhã, a intenção de ninguém, e o que o Trump decide num dia qualquer. Número abaixo de 5% é piso de modelo, medida não.

## 2. O método, da área

| Método | Fonte | Como a IA aplica |
|---|---|---|
| Classe de referência (*outside view*) | Kahneman e Lovallo; Tetlock | 20 midterms de 1946 a 2022, e cada vez que a oposição assumiu uma casa |
| Modelo de cadeiras por aprovação e voto nacional | Tufte 1975; Abramowitz; Bafumi, Erikson e Wlezien | regressão pequena com teste do passado, deixando uma eleição de fora por vez |
| Previsão condicional e estruturada | Tetlock, *Superforecasting*; nota de Brier | a mesma pergunta nos 3 mundos, com regra de resolução e prazo, gravada antes de a votação abrir |
| Análise de hipóteses concorrentes | Heuer, *Psychology of Intelligence Analysis* | *"o Congresso freia"* contra *"o presidente segue igual"* contra *"o presidente endurece"* |
| Limites do presidente em política externa | Howell e Pevehouse; Kriner; Milner e Tingley; Mayhew | o que já foi medido sobre governo dividido e uso da força |
| Escala de probabilidade | ICD 203 | faixas em palavras na fala |
| Teste de efeito no Brasil | jornalismo de dados | ComexStat e PTAX do BCB em torno das midterms, com o limite dito: todo ano de midterm é ano de eleição no Brasil |

## 3. A conexão com IA

| Papel | No vídeo |
|---|---|
| **Analista** | é a IA que monta as bases, roda o modelo e responde as perguntas nos 3 mundos |
| **Previsor** | 4 modelos separados, da mesma empresa, antes e depois de ler a história; o efeito de ler a história é publicado |
| **O limite** | concordância entre modelos da mesma empresa não confirma nada; a previsão gravada é o que permite cobrar |

## 4. Os caminhos comparados

| Caminho | Força | Problema | Decisão |
|---|---|---|---|
| Só "quem vai ganhar" | clique | todo mundo fez; envelhece amanhã | vira 1 beat |
| Só opinião de analista sobre o Brasil | fácil | não mede nada | fica como fonte |
| **Mapa condicional, com a história medida** | envelhece bem, porque o vídeo pode sair depois da votação; ninguém fez em português | mais trabalho | ✅ escolhido |

🔴 **A consequência aritmética:** como a votação é amanhã e a gravação é depois, as previsões entram em commit **antes** de a votação abrir, e o roteiro tem uma frase a preencher com o resultado. O mapa continua valendo em qualquer resultado, porque responde os 3 mundos.

## 5. O projeto

**Repositório novo e público:** `Downloads/repositorios/eleicoes-eua-2026` (skill `projeto-de-dados-publico`), relatório por rodadas. 🔴 Como é previsão de algo que não aconteceu, as previsões ficam em commit antes da votação.

| Etapa | O que faz | Dados | Sai |
|---|---|---|---|
| **E1 · A história das midterms** | quantas cadeiras o partido do presidente perde, por aprovação e voto nacional | UCSB, Gallup, Câmara, Senado | tabela, modelo e teste do passado |
| **E2 · As chances de amanhã** | quem cada modelo e mercado dá como favorito | Silver Bulletin, DDHQ, Polymarket, Kalshi, Cook, Fox | a probabilidade de cada mundo |
| **E3 · O que mudou nas outras vezes** | depois de perder a Câmara: vetos, força no exterior, tarifa, impeachment, paralisação | Senado, CRS, Budget Lab | antes × depois |
| **E4 · O que o Congresso consegue** | mecanismo por mecanismo, com os votos reais de 2025 e 2026 | congress.gov, roll calls, 19 USC 2411 | a tabela consegue × não consegue |
| **E5 · O mundo** | o que governos e analistas esperam, região por região | IFS, Reuters, centros de pesquisa | tabela dos 3 mundos |
| **E6 · O Trump** | as falas em ordem, com o original conferido | transcrições, vídeos | linha do tempo |
| **E7 · O Brasil** | exportações, dólar, tarifa, Flávio, embaixador | ComexStat, BCB, USTR | o Brasil nos 3 mundos |
| **E8 · As previsões** | perguntas condicionais, 4 modelos, com e sem a história | E1 a E7 | arquivo gravado, para medir depois |

**Validação:** dois caminhos nos números centrais; revisão por 3 leitores (quem acha que subestima o Trump, quem acha que subestima o Congresso, e o auditor de método e linguagem); teste do passado no modelo de cadeiras.

## 6. O calo do tema

| Gatilho | Fato real | Beat que responde |
|---|---|---|
| **Medo:** *"o Trump não vai aceitar"* | ordem executiva sobre o correio, Suprema Corte, temor da Guarda Nacional, falas dele | 2 e 4 |
| **Contradição:** | Trump questionou a eleição do Brasil e compara o Brasil aos democratas; em casa, diz que os democratas trapaceiam | 2 |
| **Contradição:** | o Senado americano já votou contra a tarifa do Brasil, e a tarifa continua | 3 |
| **Curiosidade:** | o Planalto espera este resultado para calibrar a relação com Washington | 5 |
| **Curiosidade:** | o que aconteceu com a tarifa da China depois que o Trump perdeu a Câmara em 2018 | 3 |
| **Teoria que circula:** | *"cancelar a eleição"*, *"guerra civil"*, *"os democratas vão salvar o Brasil"* | 4 e 5, mostrando quem diz |

⛔ O trailer mostra o que estão dizendo como o que estão dizendo.

## 7. O roteiro (≈ 13 a 15 min)

Padrão dos últimos: trailer com trechos reais (`trailer-de-tensao`, molde do vídeo 17), fundo de tensão, resultado na fala, sem bastidor técnico. Forma própria: **a mesma pergunta em 3 mundos.** Peça visual fixa: **o painel dos 3 mundos**, que começa vazio no trailer e enche pergunta por pergunta.

| Ato | Beat | Fala em uma linha |
|---|---|---|
| **0** | 0.0 a 0.2 | trechos reais; o Planalto esperando; as curiosidades |
| **1 · Quem ganha** | método e inscrição; a história das cadeiras; as chances; a frase do resultado | o partido do presidente quase sempre perde, e a Câmara é mais certa que o Senado |
| **2 · O Trump** | as falas em ordem; o que ele fez de verdade | fala × ato |
| **3 · O que o Congresso consegue** | a tabela; a tarifa do Brasil que trocou de base legal; a força; o veto; 2018 a 2020 | muda a fiscalização, a força e a tarifa quase não |
| **Bloco H** | VEYLOQ, no meio | versão *"feita com IA"* |
| **4 · O mundo** | Ucrânia, China, Irã, América Latina | o painel dos 3 mundos |
| **5 · O Brasil** | tarifa, sanção, Flávio, embaixador, dólar | o painel dos 3 mundos |
| **6 · O que esperar** | previsões, calendário, limite, conclusão, chamadas | o que muda e o que não muda |

## 8. O que é dele

Gravar antes ou depois de sair o resultado; título e thumb; a frase de opinião no fecho; o Bloco G.
