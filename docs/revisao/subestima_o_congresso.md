# Revisão adversarial: o leitor que acha que a análise subestima o Congresso

02/nov/2026, antes da votação. Papel assumido: procurar de propósito o que contraria *"muda muito lá e pouco aqui"*. Leitura do `RELATORIO.md`, `RESUMO_SIMPLES.md`, `docs/LEITURA_DA_IA.md`, `docs/PESQUISA_*.md`, `dados/previsoes/`, `resultados/previsoes.csv` e dos textos capturados. 8 buscas na web; só conta como fato o que está em página aberta (lista no fim).

**Slugs** são arquivos de `documentacao/referencias-conteudo/roteiros/videos-longos/VIDEO_024_ELEICOES_EUA_2026/referencias/textos/`.

**Veredito curto.** O miolo jurídico aguenta: sem rito rápido contra a 301, veto, resolução ignorada, Graham dispensada. O que não aguenta é passar daí para *"pouco"* com um número. O 2,1 não mede efeito pequeno: mede o que 4 modelos da mesma empresa dizem sobre um conjunto de perguntas que não tem como captar o canal do custo político, depois de ler um dossiê que deixou esse canal de fora. E o dossiê tem um erro de data que mexe na resposta mais citada do Brasil.

## Altas

### A1. O "acordo provisório até dezembro" é de novembro de 2025
- **Evidência.** `dados/previsoes/dossie_b.md` diz, na linha da tarifa de hoje: *"Rubio teria falado em acordo provisório até o fim de novembro ou início de dezembro (Tribune, uma fonte)"*. O texto `brasil/tribune-vieira-rubio` tem `DATA DA PÁGINA: 2025-11-14`, assinatura *"November 14 (ANI)"* e fala da **tarifa de 50%**, a de 2025. Não é a 301 de 2026.
- **Efeito.** 3 dos 4 modelos citam isso no `porque` de B01 (fable, opus, sonnet: *"Rubio falando em acordo provisório até dezembro"*). B01 foi de 26 para 45 no mundo DD entre as condições A e B. Não dá para saber quanto vem daí, mas é, com o grupo de trabalho, o fato do dossiê que mais aponta para acordo, e o único com prazo.
- **Deve mudar.** Corrigir o dossiê, refazer B01 (e B02, B12) em nova rodada gravada antes de a votação abrir, e registrar a errata em `docs/RODADAS.md`. O *"A tarifa do Brasil cai? 45%"* do `RESUMO_SIMPLES.md` e o *"depende mais do grupo de trabalho"* ficam suspensos até lá. O número sobe e desce junto nos 3 mundos, o que também comprime o efeito.

### A2. O caso de 2019 foi lido pela metade, e o próprio repositório tem a outra metade
O relatório (§5) e a `LEITURA_DA_IA.md` (item 2) usam 2019 e 2020 para dizer que a tese é *"sustentada em tarifa e força"*. A lista escolhe a alta da China e deixa de fora, no mesmo semestre:
- **Aço e alumínio de Canadá e México caíram em 17/05/2019.** Está em `dados/e3_tarifa_media.csv` (*"Canada e Mexico isentos"*), mas não no relatório. Grassley, presidente da Comissão de Finanças: *"I made no secret that these tariffs had to be lifted for USMCA to pass Congress"* ([The Hill](https://digital-release.thehill.com/?p=444287)); tinha avisado que o acordo estaria *"dead"* ([NPR](https://www.npr.org/2019/05/17/724357441/u-s-to-lift-tariffs-on-canadas-and-mexico-s-steel-and-aluminum)). Tarifa da mão do presidente, retirada com o Congresso segurando algo que ele queria.
- **A ameaça de 5% sobre o México foi suspensa em 07/06/2019**, também em `dados/e3_tarifa_media.csv`, e também fora do relatório. McConnell: *"There is not much support in my conference for tariffs"*; republicanos falavam em *"possibly a veto-proof majority in the Senate"* ([Fox Business](https://www.foxbusiness.com/markets/trump-gop-split-senators-loudly-oppose-mexico-tariff-threat)). Trump atribui o recuo ao acordo migratório, e a causa segue em disputa.
- **O USMCA não "passou com 385 a 41" apenas.** O relatório dá só o placar. Foi uma reescrita negociada: *"House Democrats have reached a tentative agreement with labor leaders and the White House over a rewrite"*, depois de *"lengthy, detailed negotiations over enforcement provisions"* ([PBS/AP](https://www.pbs.org/newshour/economy/trump-and-democrats-in-tentative-deal-on-usmca-trade-pact); `historico/thehill-usmca-camara`: *"Democrats had reached a deal with Trump"*). É exatamente a *negociação antes do veto*. O próprio Trump a descreve em 2026: *"you end up working on deals"*.
- **A alta da China é um teste ruim.** A oposição não estava contra: Schumer tuitou *"Hang tough on China [...] Don't back down"* cinco dias antes da alta ([CNBC](https://www.cnbc.com/2019/05/06/schumer-urges-trump-to-hang-tough-after-china-trade-tariff-threat.html)). Tarifa que o Congresso de oposição apoia não mede o freio dele. No Brasil de 2026 os democratas são contra.
- **A Síria "veio sem o Congresso" é incompleta.** Em 04/02/2019 o Senado republicano aprovou 70 a 26 um texto contra a retirada ([Al Jazeera](https://www.aljazeera.com/news/2019/2/5/us-senate-rebukes-trump-over-syria-afghanistan-withdrawal-plans)). Não obriga, e Trump disse que não mudaria; mas a frase passa a ideia de campo livre.
- **A retenção da ajuda à Ucrânia, 2019.** Liberada em 11/09 ([NPR](https://www.npr.org/2019/11/27/783487901/the-hold-on-ukraine-aid-a-timeline-emerges-from-impeachment-probe)), com Lowey escrevendo a proteção da verba na lei provisória e Schumer cobrando nomes ([AP](https://www.ksl.com/article/46644025/ap-explains-the-delay-in-us-aid-to-ukraine)). Política externa decidida pelo presidente, revertida sob pressão do Congresso e sem lei. Causa não provada aqui também.

**Limite honesto.** Em quase todos esses casos a alavanca existia porque ele queria algo do Congresso, e parte da pressão veio de republicanos. Isso não prova que uma Câmara democrata derruba tarifa. Prova que *"o que dependia só do presidente mudou sem o Congresso"* (`PESQUISA_MUNDO.md` §C) está errado como resumo do período.

- **Deve mudar.** Reescrever o caso-espelho com as 2 colunas: o que subiu e o que recuou, e separar tarifa apoiada por tarifa contestada. A conclusão vira: *"o Congresso não derrubou tarifa por voto; houve recuos quando o presidente precisava de voto ou o custo subiu"*. Depois perguntar: o que Trump precisa do Congresso em 2027 (orçamento, NDAA, revisão do T-MEC)?

### A3. O episódio mais direto do Brasil não está no relatório
- **Evidência.** O §4 diz da tarifa de 2025: *"quem tirou a tarifa foi a Corte"*. Antes da Corte, em 20/11/2025, 23 dias depois do 52 a 48 no Senado, **o próprio Trump tirou os 40% de carne, café, cacau e frutas do Brasil**. A Reuters registra: *"a U-turn on some tariffs that have increased the cost of food"* e *"Rising food prices are a major factor behind Trump's declining approval ratings"* ([KSL/Reuters](https://www.ksl.com/article/51408507/trump-signs-order-to-remove-tariffs-from-brazilian-beef-coffee)). A isenção atual de carne, suco e café na 301 vai na mesma linha (`s301-fr-aviso-14542`, `brasil/embaixada-factsheet-301`). Collins fala do seu trabalho *"to exempt key Canadian products"* (`mundo/ascoa-latam-midterms`).
- **Por que importa.** É o mecanismo que o leitor aponta: custo político mudando tarifa do Brasil sem nenhuma lei. Com Congresso republicano, então não prova efeito de maioria democrata, e Trump citou a negociação. Mas o resultado de 03/nov é o maior sinal de custo político que ele vai receber.
- **Agravante.** B01 resolve com *"reduzindo a taxa ou ampliando isenção para acordo com o Brasil"*. Uma isenção unilateral por preço, o caso de novembro de 2025, **não conta**. Os 12,5% da outra 301 e a 232, que o Brasil também quer tirar (`brasil/aol-reuters-grupo-trabalho`), tampouco.
- **Deve mudar.** Corrigir a linha do §4, incluir o episódio e criar pergunta nova: *"os EUA reduzem ou isentam, por qualquer via, parte da tarifa sobre o Brasil"*, em cada camada.

### A4. O 2,1 é ruído apresentado como medida
- **Evidência.** Ler a história moveu as respostas em 6,6 pontos em média (§7). A discordância entre modelos em B01, B02 e B03 é de 16 a 18 pontos. Em B01, haiku dá -4 e sonnet +6 (`dados/previsoes/rodada_b/`). Por modelo, o "resto" do Brasil vai de 2,3 a 3,2; com sinal, a média dos medianos é 1,3. Nenhum teste de repetição mede quanto o mesmo modelo oscila.
- **A leitura certa é "não detectado", não "pouco".** O `RELATORIO.md` §1 afirma *"a chance muda em média"*, sem dizer que a chance é opinião de modelo. O `RESUMO_SIMPLES.md` diz *"O que muda no Brasil? 2,1 pontos"*. A `LEITURA_DA_IA.md` item 5 admite que *"essa simetria pode ser só o que eles não sabem"*, mas isso não sobe para a resposta.
- **Ponto não é impacto.** 4 pontos numa tarifa que pesa em US$ 27,5 bi de exportação em 9 meses valem mais que 24 pontos num voto simbólico de plenário. Perguntas binárias (B10, B11) não têm tamanho: alta de 1% e de 30% respondem igual.
- **Deve mudar.** Trocar a frase de abertura por algo como: *"os modelos veem diferença grande no que é voto do Congresso e não detectam diferença no resto; a margem de erro deles é maior que 2 pontos, então isso não prova que o efeito é pequeno"*. Publicar a faixa por modelo ao lado de cada média. Rodar 3 repetições por modelo para ter o ruído.

### A5. As perguntas não têm como captar o que o leitor aponta
- **Prazos desiguais.** O tema principal tem o prazo curto: B01, B02, B07, B11, B12 acabam em **30/06/2027**, menos de 6 meses de Congresso novo. Os que dão efeito grande têm mais tempo: B05 e B06 até 2028. No mundo, W05 acaba em 2027 e W01 a W04 em 2028. Tarifa com prazo em 2028 pode dar outro efeito; ninguém perguntou.
- **O dinheiro não aparece.** A Reuters lista 4 caminhos (`mundo/reuters-4-formas-kathmandu`): cortar verba de defesa com **uma casa só**, ajuda à Ucrânia, limitar ajuda a Israel, teto militar e ajuda externa; lembra ainda que os democratas já barraram os US$ 1,5 tri no Senado. Smith: *"Congress certainly does hold the purse"*, e a NDAA de 2027 parada será afetada pelo resultado (`mundo/chicago-council-otan-smith`). Das 27 perguntas, **nenhuma** é sobre verba condicionada, Israel, ajuda externa, teto militar, NDAA ou cláusula de orçamento, nem o projeto de Meeks contra o diesel russo; T05 mede só paralisação. A tabela `dados/e4_mecanismos.csv` tem a linha do orçamento, mas ela não vira pergunta de política externa.
- **Sem efeito antecipatório.** Nenhuma pergunta mede recuo antes de voto, nem o período de 04/nov a 03/jan, nem o custo em 2028. Com Trump sem reeleição, o incentivo dos republicanos de 2028 muda; o relatório não trata disso.
- **Senado sem pergunta.** Entre DD e DR, a média no Brasil é 0,6 ponto, no mundo 4,8 e em Trump e Congresso 6,7. Não há pergunta sobre o que só o Senado faz: indicados, juízes, Suprema Corte, Fed. O relatório só diz que Perez já passou. Isto corta contra o título também: **o 28,2 é quase todo Câmara**, e DD contra RR compara com um mundo de 6,3%. A escolha real é DD contra DR, com 93,7% da chance, e o §1 não a mostra.
- **Deve mudar.** Acrescentar antes da votação perguntas de tarifa com prazo em 2028, verba com cláusula, Israel, NDAA, recuo unilateral e indicados; dar no §1 o efeito DD contra DR; e dizer que a lista original não cobria esses canais.

### A6. A literatura do custo político foi deixada de fora, e a citada foi lida ao contrário
- **Evidência.** Howell e Pevehouse dizem: *"This presumption, we demonstrate, does not hold up"*; há *"a clear connection"* entre composição do Congresso e **grandes** usos da força (`congresso/ac-howell-io-repec`). O relatório escreve *"só nos grandes usos"*, dentro de um parágrafo sobre série fraca. Grande uso da força é justamente o caso do Irã. Kriner: hearings e debate *"influence the president's strategic decisions as he weighs the political costs"* e o Congresso *"materially shapes the initiation, scope, and duration"* (`congresso/ac-kriner-chicago`). Milner e Tingley (`congresso/ac-milner-niehaus`) dizem que o poder do presidente varia por instrumento, e que interesse material e divisão ideológica no Congresso o limitam; o resumo lista o comércio entre os instrumentos.
- **O que aconteceu.** Kriner e Milner aparecem na `PESQUISA_CONGRESSO.md` como ❓ *não lido*. Saíram do `RELATORIO.md` e do `dossie_b.md`. O dossiê diz *"Howell e Pevehouse acham efeito do Congresso só nos grandes usos"* e nada mais. A própria pesquisa conclui que *"o Congresso pesa mais no começo e no custo do que no final"*, e isso não chegou aos modelos nem ao relatório. Dizer que a tese foi *"sustentada"* sem ler a corrente que a contesta é forte demais.
- **Deve mudar.** Dar a esses autores um parágrafo no §5, com o aviso de que foram lidos só em resumo, e no limite de *"o que não consegue dizer"*: *"o projeto não testa efeito antecipatório"*. Rebaixar *"sustentada"* para *"sustentada no que é voto e lei; não testada no custo político"*.

## Médias

### M1. A média por grupo é honesta? Aritmética certa, comparação não
Os números conferem (6,17; 10,11; 28,25), mas:
- É média de **valor absoluto** de **diferença de medianas**. Com sinal, o Brasil dá 5,6, e haver sinal trocado entre modelos some.
- **W03 sozinho é 55% do grupo "mundo"** (50 de 91). Sem ele, 5,1. W03 é voto no Congresso, classificado como mundo.
- **O corte do Brasil também existe no mundo:** W01 a W04 dão 18,0 e W05 a W09 dão 3,8, quase os 18,3 e 2,1. Logo, "lá, mundo, aqui" está confundido com "a pergunta é sobre voto do Congresso".
- **O grupo Trump é quase tautológico:** T01, T03, T04 e T06 somam 158,5 de 169,5. Câmara republicana não impede Trump; Trump que ganha não alega fraude. T02 e T05 dão 5,5. Nenhuma pergunta é sobre política americana real (Medicaid, Obamacare, ICE, gasto). Então *"muda muito lá"* também não está medido.
- **Deve mudar.** Trocar os 3 grupos por *"procedimento do Congresso"* e *"resultado de política"*, ou ao menos mostrar o cruzamento. Mover W03 de grupo. Não usar a média como manchete sem a faixa por modelo.

### M2. O corte B04, B05, B06 depois de ver o número
Numericamente muda pouco: a distribuição é de fato bimodal (3 perguntas de 12,5 a 24; 9 de até 4), e outro corte chegaria perto. O problema é outro:
- **Circular.** Chamar tarifa, sanção e encontro de *"o que não depende"* (`RESUMO_SIMPLES.md`) já assume a tese que se quer testar.
- **Rótulo errado.** O relatório diz *"depende de voto do Congresso (audiência, intimação, votação)"*, mas pela `PESQUISA_CONGRESSO.md` A5 o presidente da comissão intima sozinho. Só B06 é voto.
- **Aviso no lugar errado.** A confissão de que veio depois está só em `docs/RODADAS.md`. O §1 e o resumo a omitem.
- **Deve mudar.** Dizer no §1 *"corte feito depois de ver as respostas"* e renomear para *"ação do Congresso, por construção"* contra *"ato do governo ou de terceiros"*.

### M3. A conta do veto usa só o recorte que dá folga
*"Recorde de republicanos cruzando: 6 e 5 em tarifa, 7 e 4 em guerra"* é estático e tem erro:
- `dados/e4_votos_congresso.csv` traz S.J.Res. 98a com **5** republicanos em guerra no Senado, não 4 (a nota da linha diz). Em 2020, 55 a 45 no Irã (`historico/iranintl-veto-2020`) dá 8.
- O mesmo CSV tem **35 e 24 republicanos** contra o veto em janeiro de 2026, e **18** na petição da Ucrânia (`mundo/abc-peticao-ucrania`), além de 86 a 11 e 262 a 159 na Graham. São temas de pouca saliência ou sem choque direto com Trump: não transfere inteiro, mas mostra que o teto não é 7.
- Republicanos já cobram em público depois da dispensa da Graham: McConnell, Tillis, Collins e Cornyn (`congresso/abc-waiver-graham`), e 22 deputados, com Wilson e McCaul (`congresso/newsweek-diesel-bipartidario`). Tillis: *"not following the law"*.
- **Deve mudar.** Corrigir o 4 para 5. Dar a faixa por tipo de tema. Dizer que o comportamento depois da eleição, sem primária à vista e com Trump sem reeleição, não está nos dados.

### M4. A mediana esconde a discordância justo onde o Congresso pode pesar
W02 tem 45 pontos entre modelos no mundo DD; W01, 37; T03, 30; B06, 28 (55 a 10, 42 a 5, 52 a 22, 40 a 12). A Reuters diz que a ajuda à Ucrânia *"likely would pass with the two-thirds majorities"*; a tabela dá 15%. O relatório cita a divergência das fontes no §9, mas o *"10,1, pouco e devagar"* do resumo não. Há incerteza alta ali, não efeito baixo. **Deve mudar:** mostrar a faixa dessas 4 perguntas no painel do mundo.

### M5. O Planalto espera o resultado e o modelo diz que nada muda
`congresso/perez-cnnbrasil`: *"o Planalto aguarda qual será a estratégia da Casa Branca [...] após o resultado"*; `brasil/spacemoney-midterms`: o pleito *"pode redesenhar a correlação de forças"*; `brasil/bpmoney-midterms`: fontes do Itamaraty veem ganho em big techs e meio ambiente com uma casa democrata, e esses são temas da própria 301. Mas B12 dá 2 pontos, com **sinais opostos** entre modelos (fable 50/48/44; sonnet 58/60/62). O relatório conta o Brasil como quem reage, mas nenhuma pergunta mede o Brasil mudando de postura. Ressalva a favor da tese: Rubens Barbosa e a avaliação em Brasília de *"pouca margem"* (`brasil/infomoney-midterms`). **Deve mudar:** dizer que B03 e B12 estão sem consenso de direção, e não *"quase sem efeito"*.

### M6. O dólar foi medido só para trás
O canal mais direto para o Brasil é juro e dólar: `mundo/fxstreet-yields` traz as teses por mundo, e `mundo/cnbc-wall-street` traz o déficit. O relatório só traz a PTAX depois de midterms passadas, que ele mesmo diz não separar de eleição no Brasil. B11 é binária, com 3 pontos. **Deve mudar:** incluir as teses dos bancos no §8, como tese, e perguntar por faixa de PTAX.

### M7. O dossiê levou certezas que a pesquisa não tinha
*"Pelo texto da lei, não há rito privilegiado"* entrou sem o ⚠️ de `PESQUISA_CONGRESSO.md` A3 (inferência própria, 4 seções não lidas). Saíram cortar verba, a NDAA dos 76.000, o bloqueio dos US$ 1,5 tri e os recuos de 2019. O `PLANO.md` §1 já trazia a *"conclusão esperada"*, e o dossiê saiu do mesmo projeto, com a tese já escrita. Sendo justo: o efeito não cai em tudo (W03 e T06 sobem de A para B; W05 cai de 9 para 4). **Deve mudar:** registrar o viés de enquadramento no bloco de limites, e na nova rodada dar um dossiê com as 2 colunas.

## Ids e regras mal escritos (teste das previsões)

| Id | Problema | Grav. | Correção |
|---|---|---|---|
| T02 | Título fala em maioria que *"deixa de tomar posse"*, a regra é *"não organizados até 05/01"*. Uma briga pela presidência da Câmara dispara o sim sem golpe nenhum (em 2023 durou até 07/01, de memória, conferir). 03/01/2027 é **domingo**, e o Congresso pode mudar a data por lei. RR maior que DD vem disso; fable 12 e haiku 0,5 em RR estão medindo coisas diferentes. O resumo lê como *"não tomar posse"* | média | Separar: impedimento de posse ou certificação contra demora normal; prazo relativo ao início da sessão |
| B01 | *"isenção relevante"* sem definição; exige *"por acordo"*; ignora 12,5% e 232 (ver A3) | alta | Ver A3 |
| B04 | *"entre os temas"* sem critério e *"registrada no site"*: pergunta de um deputado numa audiência com Rubio conta? Opus diz que *"a regra é frouxa"* | média | Definir: tema no título ou convocação, ou pergunta no registro; prazo igual a B05 e B06 |
| B05 | Só *"sobre a entrada"*; intimação sobre a revogação do visto de Viotti ou sobre as sanções não conta | baixa | Ampliar para o Brasil |
| B06 | Lei geral de tarifas conta? Opus e fable dizem que talvez não, e a agenda de Jeffries é geral | média | Dizer que lei geral que alcance o Brasil conta |
| B07 | Exclui visto, a ferramenta que o governo de fato usou (`carta-kamlager-release-1007`) | baixa | Pergunta irmã só de visto |
| B08 | Regra truncada: *"confirmado por governo; advogado ou duas agências"* | baixa | Reescrever |
| B03, B12 | Coerentes entre si. Mas `perez-cnnbrasil` diz que o agrément corre sob sigilo, e o anúncio pode vir depois do fato; a mesma matéria mistura com cartas credenciais | baixa | Valer a data anunciada |
| W03 | No grupo errado (ver M1) | média | Mover |
| W04 | *"sobre tarifa ou uso da força"*: NDAA com limite de tropa conta? O único veto derrubado de Trump (116º, 1 no `e3_vetos_por_congresso.csv`) foi de NDAA, de memória, conferir | média | Dizer se NDAA conta; pergunta irmã para qualquer veto |
| W05 | Resolve pelo Yale, cujo texto capturado dá 11,0% *estatutária*, indo a 11,8% (`historico/yale-tariffs-2026-04-08`). Os modelos raciocinaram sobre *"7 a 8%"* (Wharton, alfândega). Cair 3 pontos é outra coisa em cada escala; o valor de 31/10 não foi gravado | média | Fixar medida e gravar a base antes da votação |
| T01 | *"Resultado nacional"*: *"our elections are totally rigged"* conta? Em RR, sobre o quê? | baixa | Exigir citação de 2026 e de abrangência nacional |
| T06 | Resolve por `senate.gov`, que recusou este computador (limites do relatório) | baixa | Usar `ucsb-vetoes` ou clerk |

**Entre mundos.** Não achei inversão grave: DD ≥ DR ≥ RR nas perguntas de Congresso, e DD = DR quando só a Câmara importa (B04, T04). T05 igual em DD e DR (42) é discutível: um Senado democrata muda a negociação do orçamento. Ordem dos ids: B12 e W09 no fim do CSV é só herança da errata.

## O que resistiu

- **301 sem rito rápido e 2/3 fora do alcance por voto direto.** Não achei texto que contradiga. Continua sem parecer de advogado, como o relatório já avisa.
- **Lei Graham dispensada em 28 dias e resolução concorrente ignorada.** São os melhores argumentos da tese.
- **Rubens Barbosa e a leitura de Brasília** (`brasil/infomoney-midterms`) sustentam *"pouca margem para reverter as tarifas no curto prazo"*. *Curto prazo* é a palavra: o relatório só perguntou o curto prazo.
- **Jefferies sobre a Índia e AFP sobre a Europa** apoiam o ceticismo.
- **Nenhum episódio acima prova causa,** do mesmo jeito que o relatório diz da alta da China.

## Pistas não abertas (não usar sem conferir)

Viram só em resumo de buscador ou de memória: o recuo da rescisão de US$ 4 bi em ago/2019; a NDAA derrubada em jan/2021, com os limites de tropa; os cerca de 400 militares mantidos na Síria em 2019; os 12 republicanos no voto da emergência da fronteira em 2019; a duração da eleição do presidente da Câmara em 2023; a ameaça de Durbin sobre a verba do Pentágono em 2019.

## Páginas abertas

[The Hill, 17/05/2019](https://digital-release.thehill.com/?p=444287) · [NPR, 17/05/2019](https://www.npr.org/2019/05/17/724357441/u-s-to-lift-tariffs-on-canadas-and-mexico-s-steel-and-aluminum) · [Fox Business, jun/2019](https://www.foxbusiness.com/markets/trump-gop-split-senators-loudly-oppose-mexico-tariff-threat) · [PBS/AP, dez/2019](https://www.pbs.org/newshour/economy/trump-and-democrats-in-tentative-deal-on-usmca-trade-pact) · [CNBC, 06/05/2019](https://www.cnbc.com/2019/05/06/schumer-urges-trump-to-hang-tough-after-china-trade-tariff-threat.html) · [Al Jazeera, 05/02/2019](https://www.aljazeera.com/news/2019/2/5/us-senate-rebukes-trump-over-syria-afghanistan-withdrawal-plans) · [NPR, 27/11/2019](https://www.npr.org/2019/11/27/783487901/the-hold-on-ukraine-aid-a-timeline-emerges-from-impeachment-probe) · [AP/KSL, 2019](https://www.ksl.com/article/46644025/ap-explains-the-delay-in-us-aid-to-ukraine) · [Reuters/KSL, 20/11/2025](https://www.ksl.com/article/51408507/trump-signs-order-to-remove-tariffs-from-brazilian-beef-coffee)
