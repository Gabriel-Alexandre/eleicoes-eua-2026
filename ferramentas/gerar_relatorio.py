"""Escreve RELATORIO.md, RESUMO_SIMPLES.md e docs/LEITURA_DA_IA.md a partir de resultados/RESUMO.json.

Uso: python ferramentas/gerar_relatorio.py
"""
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
R = json.loads((RAIZ / "resultados" / "RESUMO.json").read_text(encoding="utf-8"))
RES = json.loads((RAIZ / "resultados" / "RESULTADO.json").read_text(encoding="utf-8"))
VOT = json.loads((RAIZ / "dados" / "resultado_03nov.json").read_text(encoding="utf-8"))
h, pv, b, v, c = R["historia"], R["previsoes"], R["brasil"], R["vetos"], R["chances"]
Q = {p["id"]: p for p in pv["perguntas"]}


def br(x, casas=1):
    return f"{x:.{casas}f}".replace(".", ",")


def n(x):
    return br(x, 1).replace(",0", "")


def tabela(grupo):
    l = ["| Pergunta | Prazo | DD | DR | RR | Sem a história (DD, DR, RR) |", "|---|---|---:|---:|---:|---|"]
    for p in pv["perguntas"]:
        if p["grupo"] == grupo:
            a = "nova" if p["A_DD"] is None else f"{n(p['A_DD'])}, {n(p['A_DR'])}, {n(p['A_RR'])}"
            l.append(f"| {p['pergunta']} | {p['prazo']} | {n(p['DD'])}% | {n(p['DR'])}% | {n(p['RR'])}% | {a} |")
    return "\n".join(l)


m = h["modelos"]
f = R["forca"]
pm = pv["pesos_mundos"]
ef = pv["efeito_por_grupo"]
pa = pv["p_mundos_a"]
dd_a = [x["DD"] for x in pa.values()]
altas = sum(1 for d in b["dolar"] if d["d30"] > 0)
quedas = sum(1 for d in b["dolar"] if d["d30"] < 0)

RELATORIO = f"""# Relatório: eleições dos EUA de 2026, o que muda em cada resultado

**Rodada 1, 02/nov/2026, antes da votação de 03/nov.** Análise feita pelo Claude, com fontes capturadas e número saído de script (`resultados/RESUMO.json`). Comece pelo `RESUMO_SIMPLES.md`.

## O que este projeto não consegue dizer

- **O resultado.** Este relatório foi escrito antes da votação. As chances dos 3 mundos são de terceiros, não uma previsão própria.
- **Causa.** As comparações de antes e depois têm poucos casos, cada um com a sua história. Mostram o que veio depois, sem provar que veio por causa.
- **Intenção.** O que o Trump pretende não dá para ler de fora. O relatório separa o que ele disse do que fez.
- **As probabilidades de IA** são de 4 modelos da mesma empresa, com o mesmo texto: concordar entre eles não confirma nada, e modelos ainda perdem de previsores humanos treinados. Abaixo de 5%, o número é mais piso do que medida. A discordância média entre eles foi de {n(pv['discordancia_media_DD'])} pontos no mundo DD.
- **Acesso:** `senate.gov` recusou este computador; o voto a voto do Senado vem de imprensa. Não há Gallup de 2026, porque a Gallup encerrou a medição em fevereiro.
- **Lei:** a conclusão de que não há rito rápido contra a tarifa da Seção 301 é leitura do texto da lei feita pela IA, sem parecer de advogado lido; as seções 2413 e 2418 a 2420 não foram lidas.

## 0. O resultado de 03/nov (atualização de 04/nov, manhã)

⚠️ Apuração em andamento: são projeções da imprensa, não resultado oficial. Fontes e falas em `dados/resultado_03nov.json` e `docs/PESQUISA_RESULTADO.md`.

- **Aconteceu o mundo DD: democratas nas 2 casas.** Câmara: {VOT['camara']['d_projetadas']} democratas e {VOT['camara']['r_projetadas']} republicanos projetados, {VOT['camara']['sem_projecao']} sem projeção, {VOT['camara']['virou_liquido_ate_agora']} cadeiras viradas até aqui; a NBC estima {VOT['camara']['estimativa_nbc_d']} a {VOT['camara']['estimativa_nbc_r']} no fim. Senado: {VOT['senado']['d']} a {VOT['senado']['r']}, com {' e '.join(VOT['senado']['sem_projecao'])} sem projeção ({VOT['senado']['mississippi_diferenca_votos']} votos de diferença no Mississippi); viradas em {', '.join(VOT['senado']['viradas'])}.
- **O modelo de história acertou melhor que os modelos por distrito, por enquanto.** Pela estimativa da NBC, os republicanos perdem {n(abs(RES['perda_republicana_estimada']))} cadeiras. O modelo com aprovação e voto genérico tinha dito {n(abs(RES['previsao_dos_modelos_de_historia']['os_dois']))}, o de aprovação {n(abs(RES['previsao_dos_modelos_de_historia']['aprovacao']))}; os modelos por distrito davam de {n(min(x['cadeiras_camara_d'] for x in RES['previsoes_por_distrito_cadeiras_d']))} a {n(max(x['cadeiras_camara_d'] for x in RES['previsoes_por_distrito_cadeiras_d']))} democratas. A objeção da revisão de que o modelo de história exagerava por não ver o redesenho (`docs/revisao/vies_contra_republicanos.md` A3) não se confirmou nesta eleição. Uma eleição só não valida modelo.
- **Nota de Brier dos 3 mundos** (0 é perfeito; 0,667 é chutar um terço para cada): mercados e modelos {br(RES['brier_3_mundos']['mercados_e_modelos'], 3)}; as 4 IAs sem a história de {br(min(v for k, v in RES['brier_3_mundos'].items() if k.startswith('ia_a')), 3)} a {br(max(v for k, v in RES['brier_3_mundos'].items() if k.startswith('ia_a')), 3)}; com o dossiê, de {br(min(v for k, v in RES['brier_3_mundos'].items() if k.startswith('ia_b')), 3)} a {br(max(v for k, v in RES['brier_3_mundos'].items() if k.startswith('ia_b')), 3)}. O dossiê trazia as chances dos mercados, então a condição B não é previsão independente sobre quem ganha.
- **O Trump aceitou o resultado e manteve o veto.** Ao New York Times: *"I am absolutely willing to accept those results"*. Na Truth Social, culpou não estar na cédula. À Fox: *"They'll send over things that are insane, and I'll veto them"*, e depois *"we'll work together"*; postou o boné com a palavra VETO. A pergunta T01 (dizer que o resultado nacional foi fraudado, prazo 03/01/2027) segue aberta, com a leitura de agora contra ela.
- **Veto:** com {VOT['camara']['estimativa_nbc_d']} democratas na Câmara e {VOT['senado']['d']} no Senado, derrubar veto pede {RES['veto']['camara_republicanos_para_2_tercos']} republicanos na Câmara e {RES['veto']['senado_republicanos_para_2_tercos']} no Senado.
- **Intimação:** o principal democrata da comissão de Fiscalização postou *"LAWYER UP"*; o poder de intimar começa com o novo Congresso, e o Departamento de Justiça atual dificilmente executa intimação do Congresso (CNN).
- **Mercado e Brasil:** bolsas americanas para cima, juros e dólar para baixo na manhã de 04/11 (CNN). Até a captura, sem nota oficial do Planalto ou do Itamaraty; a PTAX de 04/11 ainda não tinha saído.

## 1. A resposta

**O resultado muda muito dentro dos Estados Unidos e pouco no que o Trump faz sozinho.** Entre democratas nas 2 casas e republicanos nas 2, a chance muda em média {n(ef['trump'])} pontos nas perguntas sobre Trump e Congresso, {n(ef['mundo'])} nas do mundo e {n(ef['brasil'])} nas do Brasil. Dentro do Brasil, {n(pv['efeito_brasil_depende_do_congresso'])} pontos no que depende de voto do Congresso (audiência, intimação, votação contra a tarifa) e {n(pv['efeito_brasil_nao_depende'])} no resto (tarifa de fato, sanção, embaixador, encontro, ataque, exportação, dólar).

## 2. A história

- Nas {h['n']} midterms de 1946 a 2022, o partido do presidente perdeu cadeiras na Câmara em {h['camara_perdeu_cadeiras']}, em média {n(abs(h['camara_media']))} (contando as 2 em que ganhou). Com aprovação abaixo de 50% ({h['n_abaixo_50']} casos), {n(abs(h['camara_media_abaixo_50']))}; com 50% ou mais, {n(abs(h['camara_media_50_ou_mais']))}.
- No Senado perdeu em {h['senado_perdeu_cadeiras']} de {h['n']}, em média {n(abs(h['senado_media']))}, e ganhou cadeiras com aprovação até 45% em {', '.join(map(str, h['senado_ganhou_com_aprovacao_ate_45']))}: o Senado depende de quais cadeiras estão em jogo.
- A Câmara trocou de mãos em {len(h['camara_trocou'])} eleições ({', '.join(map(str, h['camara_trocou']))}) e o Senado em {len(h['senado_trocou'])} ({', '.join(map(str, h['senado_trocou']))}).
- **Modelo simples:** com aprovação de {br(h['aprovacao_2026'])}% e voto genérico de D+{br(h['generic_2026'])}, a perda republicana seria de {n(abs(m['generic']['previsao_2026']))} cadeiras pelo voto genérico, {n(abs(m['aprovacao']['previsao_2026']))} pela aprovação e {n(abs(m['os_dois']['previsao_2026']))} pelos dois.
- **Teste do passado**, deixando uma eleição de fora por vez ({m['os_dois']['n']} eleições): erro médio de {n(m['aprovacao']['erro_medio_absoluto_fora_da_amostra'])} cadeiras pela aprovação, {n(m['generic']['erro_medio_absoluto_fora_da_amostra'])} pelo voto genérico, {n(m['os_dois']['erro_medio_absoluto_fora_da_amostra'])} pelos dois, contra {n(m['media_simples']['erro_medio_absoluto_fora_da_amostra'])} de só repetir a média. O modelo ajuda pouco e erra por muito. Maior erro do modelo dos dois: {m['os_dois']['maior_erro']['ano']}, {n(abs(m['os_dois']['maior_erro']['cadeiras']))} cadeiras. Serve de ordem de grandeza.
- ⚠️ A aprovação de 2026 vem de outra fonte (média PollCheck), porque a Gallup parou. Ela varia de 31% a 40% conforme o instituto.

## 3. As chances, em 02/nov

Democratas nas 2 casas {n(pm['DD'])}%, democratas só na Câmara {n(pm['DR'])}%, republicanos nas 2 {n(pm['RR'])}% (mediana de Midterm Forecast, Polymarket e Kalshi, reescalada). Senado democrata de {n(c['senado_d_faixa'][0])}% a {n(c['senado_d_faixa'][1])}% nos modelos; cadeiras democratas na Câmara de {n(c['camara_d_cadeiras_faixa'][0])} a {n(c['camara_d_cadeiras_faixa'][1])}. Tabela: `dados/e2_chances.csv`. **O que a IA errou sem ler nada:** sem a pesquisa, os 4 modelos deram de {min(dd_a)}% a {max(dd_a)}% ao mundo DD, contra perto de 75% dos modelos eleitorais e mercados.

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

- **Vetos desde 1981:** média de {n(v['desde_1981']['media_dividido'])} por Congresso com governo dividido contra {n(v['desde_1981']['media_unificado'])} com unificado; {n(v['desde_1981']['pct_derrubados'])}% derrubados. Trump: 0 no 115º, 10 no 116º (1 derrubado), 2 até agora no 119º. Em 23/10 ele disse *"I veto everything"* (IBTimes).
- **Impeachment:** desde 1994 a Câmara trocou {R['impeachment']['casos']} vezes; inquérito em {R['impeachment']['inquerito_aberto']} ({', '.join(map(str, R['impeachment']['anos']))}); presidente impedido em 2, nenhum condenado.
- **Uso da força**, lista do CRS, 2 anos antes contra 2 depois de trocar a Câmara: subiu em {f['subiu']}, caiu em {f['caiu']}, igual em {f['igual']}. Série fraca: mudou de critério e conta entradas de relatório. Howell e Pevehouse medem efeito do Congresso só nos grandes usos da força.
- **Tarifa média efetiva:** {n(R['tarifa']['2018'])}% em 2018, {n(R['tarifa']['2019'])}% em 2019, {n(R['tarifa']['2020'])}% em 2020, com a Câmara democrata. Hoje, {n(R['tarifa']['2026'])}% (maio).
- **O caso-espelho, 2019 e 2020:** a tarifa da China subiu de 10% para 25% em 10/05/2019, a saída da Síria veio sem o Congresso, o USMCA passou com 385 a 41, os limites de guerra foram aprovados e vetados, e o impeachment acabou em absolvição. Nada disso prova que perder a Câmara causou a alta.

## 6. O Trump

Falas e datas: `dados/e6_falas_trump.csv` e `docs/PESQUISA_TRUMP.md`. O essencial: aceita o resultado *"if they're honest elections"*; *"I veto everything"*; *"you end up working on deals"*; *"the sitting president doesn't win the midterms"*; o Alasca como *"fraudulent election"*. Na prática: mais de 1.000 monitores do Departamento de Justiça, investigação no Alasca, Suprema Corte mantendo bloqueada a regra dos Correios e sem planos de tropas nas zonas, segundo o chefe do Estado-Maior. Nenhuma fonte lida traz prova de fraude nacional até aqui.

## 7. As previsões, nos 3 mundos

Mediana de 4 modelos (fable, opus, sonnet, haiku), com a pesquisa lida, gravada em commit antes da votação. DD: democratas nas 2 casas. DR: democratas só na Câmara. RR: republicanos nas 2.

### Brasil
{tabela('brasil')}

### Mundo
{tabela('mundo')}

### Trump e Congresso
{tabela('trump')}

**O que ler a história mudou:** em média, {n(pv['efeito_medio_de_ler_a_historia'])} pontos. As perguntas W02 e W03 foram corrigidas depois da condição A, então a comparação nelas é só aproximada.

## 8. O Brasil em números

- Exportações para os EUA, janeiro a setembro: US$ {n(b['jan_set_eua'][0])} bi em 2025, US$ {n(b['jan_set_eua'][1])} bi em 2026 ({n(b['jan_set_eua'][2])}%). Para a China: US$ {n(b['jan_set_china'][0])} bi e US$ {n(b['jan_set_china'][1])} bi (+{n(b['jan_set_china'][2])}%). Isso não mede só a tarifa.
- Depois da midterm de 2018, as exportações para os EUA foram de US$ {n(b['export_2018_2019'][0])} bi para US$ {n(b['export_2018_2019'][1])} bi; depois da de 2022, de US$ {n(b['export_2022_2023'][0])} bi para US$ {n(b['export_2022_2023'][1])} bi.
- Dólar: mediana de +{n(b['dolar_mediana_d30'])}% em 30 dias depois das midterms de 1998 a 2022, com {altas} altas e {quedas} queda, sem padrão útil: toda midterm cai em ano de eleição no Brasil, então não dá para separar. PTAX de 30/10/2026: R$ {br(b['dolar_30_10_2026'], 4)}.

## 9. O mundo

Por região, com divergências: `docs/PESQUISA_MUNDO.md` e `dados/e5_mundo.csv`. As fontes discordam sobre a Ucrânia (Reuters vê 2/3 possíveis para ajuda nova; autoridades europeias duvidam) e sobre a Europa (AFP: *"expectations are low"*; Smith: *"tremendous expectation"*).

## 10. O que acompanhar

03/nov, a votação; 13/nov, o prazo da carta dos 25; a proposta americana do grupo de trabalho sobre tarifas; a reunião de Vieira e Rubio; 14 e 15/dez, o G20 em Miami; 03/jan/2027, o novo Congresso; 05/jan, a posse do Lula; 07/abr/2027, o fim da licença do diesel russo.
"""

SIMPLES = f"""# Resumo simples

**Feito antes da votação de 03/nov/2026, com o resultado acrescentado em 04/nov.** Análise feita pelo Claude.

| Pergunta | Resposta | Por quê |
|---|---|---|
| O que aconteceu? | Democratas nas 2 casas: {VOT['camara']['d_projetadas']} cadeiras projetadas na Câmara (a NBC estima {VOT['camara']['estimativa_nbc_d']}) e {VOT['senado']['d']} no Senado, com 2 disputas em aberto. O Trump disse que aceita o resultado e que vai vetar | projeções da imprensa em 04/11 de manhã, `RELATORIO.md` §0 |
| Quem devia ganhar, na véspera? | Modelos e mercados dão {n(pm['DD'])}% aos democratas nas 2 casas, {n(pm['DR'])}% só na Câmara e {n(pm['RR'])}% aos republicanos | aprovação baixa e história: o partido do presidente perdeu cadeiras em {h['camara_perdeu_cadeiras']} de {h['n']} |
| O que muda nos EUA? | Muito: vetos, investigações, votos sobre guerra, chance de impeachment | {n(ef['trump'])} pontos de diferença média entre os extremos |
| O que muda no mundo? | Pouco e devagar: {n(ef['mundo'])} pontos | tarifa e força moram na mão do presidente, e derrubar veto pede 2/3 |
| O que muda no Brasil? | {n(pv['efeito_brasil_nao_depende'])} pontos no que não depende de voto do Congresso; {n(pv['efeito_brasil_depende_do_congresso'])} no que depende | a tarifa de hoje não tem rito rápido no Congresso, e o embaixador já foi confirmado |
| A tarifa do Brasil cai? | {n(Q['B01']['DD'])}% com democratas nas 2 casas, {n(Q['B01']['RR'])}% com republicanos, até junho de 2027 | depende mais do grupo de trabalho do que da eleição |
| O Trump vai contestar? | {n(Q['T01']['DD'])}% de chance de dizer que o resultado nacional foi fraudado, se os democratas levarem as 2 casas; {n(Q['T02']['DD'])}% de a maioria eleita não tomar posse | fala é uma coisa, posse é outra |
| Impeachment? | {n(Q['T03']['DD'])}% na Câmara com democratas nas 2 casas, até 2029 | a liderança evita, a base pressiona, e condenar pede 67 |

Limites: 4 modelos da mesma empresa, poucos casos históricos, e nada aqui prova causa. Tudo gravado antes da votação para ser cobrado: `dados/previsoes/`.
"""

LEITURA = """# Leitura da IA

Isto é leitura, inferida pela IA. O dado está no `RELATORIO.md`.

1. **O que a história sustenta:** uma Câmara de oposição é o resultado mais comum quando o presidente está mal. O Senado é mais incerto, porque depende das cadeiras em jogo.
2. **A tese do projeto, testada:** *"o Congresso fiscaliza e não governa a política externa"*. Sustentada em tarifa e força pelo caso de 2019 e 2020 e pelos votos de 2025 e 2026 (resolução ignorada, lei dispensada, veto com folga). Derrubada em parte: o plano dizia que o Senado pesava no embaixador, e Perez já foi confirmado; quem segura agora é o Brasil.
3. **O ponto menos óbvio para o Brasil:** a resolução de 2025 contra a tarifa, que virou o símbolo do apoio no Senado, não serve contra a tarifa de hoje, porque a base mudou de emergência para a Seção 301. O que pode reduzir a tarifa é o grupo de trabalho, ato do governo Trump.
4. **Onde o resultado pesa para o Brasil:** nos custos e no ruído. O caso Flávio ganha quem pergunte com poder de intimar, e o Planalto, segundo a imprensa, espera o resultado para calibrar. Nada disso derruba tarifa.
5. **Onde a análise pode estar errada:** Trump pode negociar mais para mostrar vitória depois de perder, ou endurecer lá fora para mudar de assunto. Os modelos dão efeito quase nulo aos 2 lados, e essa simetria pode ser só o que eles não sabem.
"""

(RAIZ / "RELATORIO.md").write_text(RELATORIO, encoding="utf-8")
(RAIZ / "RESUMO_SIMPLES.md").write_text(SIMPLES, encoding="utf-8")
(RAIZ / "docs" / "LEITURA_DA_IA.md").write_text(LEITURA, encoding="utf-8")
print("ok")
