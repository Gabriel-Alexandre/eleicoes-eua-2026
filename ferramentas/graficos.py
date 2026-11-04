"""Gráficos 1920x1080 a partir de resultados/RESUMO.json e dos dados.

Uso: python ferramentas/graficos.py  (grava em resultados/figuras/)
"""
import json
import textwrap
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
RES = RAIZ / "resultados"
FIG = RES / "figuras"
D = RAIZ / "dados"
R = json.loads((RES / "RESUMO.json").read_text(encoding="utf-8"))
AZUL, VERM, CINZA, VERDE, OURO = "#2D6A8A", "#C8553D", "#6B6B6B", "#2E8B57", "#C9902B"
CLARO = "#D9D9D9"
RODAPE = "github.com/Gabriel-Alexandre/eleicoes-eua-2026 · análise feita pelo Claude"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 22, "axes.spines.top": False, "axes.spines.right": False})


def nova(titulo, subtitulo):
    fig, ax = plt.subplots(figsize=(16, 9), dpi=120)
    fig.subplots_adjust(left=0.08, right=0.95, top=0.76, bottom=0.21)
    fig.suptitle(titulo, x=0.05, y=0.965, ha="left", fontsize=36, fontweight="bold")
    fig.text(0.05, 0.895, textwrap.fill(subtitulo, 95), ha="left", va="top", fontsize=21, color="#444444")
    return fig, ax


def salvar(fig, nome, fonte):
    fig.text(0.05, 0.05, f"Fonte: {fonte}", fontsize=15, color="#555555")
    fig.text(0.05, 0.018, RODAPE, fontsize=15, color="#555555")
    FIG.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIG / f"{nome}.png")
    plt.close(fig)


def g01_cadeiras():
    e = pd.read_csv(D / "e1_midterms.csv")
    h = R["historia"]
    fig, ax = nova(f"O partido do presidente perdeu em {h['camara_perdeu_cadeiras']} de {h['n']} eleições", "Variação de cadeiras na Câmara do partido do presidente, por eleição de meio de mandato")
    trocou = e.camara_maioria_antes != e.camara_maioria_depois
    cores = [VERM if t else CLARO for t in trocou]
    x = range(len(e))
    ax.bar(x, e.camara_variacao_partido_presidente, color=cores)
    ax.set_xticks(list(x))
    ax.set_xticklabels(e.ano, rotation=60, fontsize=17)
    ax.axhline(0, color="#222222", lw=1.5)
    ax.axhline(h["camara_media"], color=CINZA, ls="--", lw=2)
    ax.text(4.5, h["camara_media"] - 6, f"média {h['camara_media']:.1f}".replace(".", ","), ha="center", fontsize=20, color=CINZA, backgroundcolor="white")
    ax.bar([0], [0], color=VERM, label="a Câmara trocou de mãos")
    ax.legend(frameon=False, loc="lower left", fontsize=20)
    ax.set_ylabel("cadeiras")
    salvar(fig, "g01_cadeiras", "American Presidency Project (UCSB), Câmara dos EUA")


def g02_aprovacao():
    e = pd.read_csv(D / "e1_midterms.csv")
    h = R["historia"]
    b = h["modelos"]["aprovacao"]["coef"]
    fig, ax = nova("Quanto menor a aprovação, maior a perda", "Cada ponto é uma eleição de meio de mandato. A linha vertical é a aprovação do Trump hoje, média de pesquisas")
    ax.scatter(e.aprovacao_gallup, e.camara_variacao_partido_presidente, s=170, color=AZUL, zorder=3)
    for _, r in e.iterrows():
        if r.ano in (1946, 1998, 2002, 2006, 2010, 2018, 2022, 1962):
            ax.annotate(str(r.ano), (r.aprovacao_gallup, r.camara_variacao_partido_presidente), xytext=(10, 6), textcoords="offset points", fontsize=18)
    xs = [25, 70]
    ax.plot(xs, [b[0] + b[1] * v for v in xs], color=CINZA, lw=2)
    ax.axvline(h["aprovacao_2026"], color=VERM, lw=3)
    ax.text(h["aprovacao_2026"] + 0.6, 12, "2026: 37,9%", color=VERM, fontsize=24, fontweight="bold")
    ax.set_xlabel("aprovação do presidente (%)")
    ax.set_ylabel("cadeiras na Câmara")
    salvar(fig, "g02_aprovacao", "American Presidency Project (Gallup), PollCheck (2026, outra fonte de pesquisa)")


def g03_mundos():
    p = R["previsoes"]["pesos_mundos"]
    fig, ax = nova("Os 3 mundos, na véspera", "Mediana de modelos e mercados em 02/nov/2026, reescalada para somar 100. É estimativa, não resultado")
    nomes = ["Democratas\nnas 2 casas", "Democratas na Câmara,\nrepublicanos no Senado", "Republicanos\nnas 2 casas"]
    vals = [p["DD"], p["DR"], p["RR"]]
    bars = ax.bar(nomes, vals, color=[AZUL, OURO, VERM], width=0.6)
    for b_, v in zip(bars, vals):
        ax.text(b_.get_x() + b_.get_width() / 2, v + 1.5, f"{v:.0f}%", ha="center", fontsize=44, fontweight="bold")
    ax.set_ylim(0, 95)
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    salvar(fig, "g03_mundos", "Midterm Forecast, Polymarket, Kalshi (dados/e2_chances.csv)")


def g04_veto():
    # Câmara com a mediana de um modelo (236 democratas), Senado com 53, Midterm Forecast.
    fig, axs = plt.subplots(1, 2, figsize=(16, 9), dpi=120)
    fig.subplots_adjust(left=0.08, right=0.95, top=0.72, bottom=0.2, wspace=0.3)
    fig.suptitle("Para derrubar um veto, faltaria muita gente", x=0.05, y=0.965, ha="left", fontsize=36, fontweight="bold")
    fig.text(0.05, 0.895, textwrap.fill("Republicanos que teriam de cruzar, no cenário de 236 democratas na Câmara e 53 no Senado, contra o recorde de 2025 e 2026", 95), ha="left", va="top", fontsize=21, color="#444444")
    for ax, casa, precisa, rec_t, rec_g in [(axs[0], "Câmara", 290 - 236, 6, 7), (axs[1], "Senado", 67 - 53, 5, 4)]:
        bars = ax.bar(["teriam de\ncruzar", "recorde\nem tarifa", "recorde\nem guerra"], [precisa, rec_t, rec_g], color=[VERM, CLARO, CLARO], width=0.65)
        for b_ in bars:
            ax.text(b_.get_x() + b_.get_width() / 2, b_.get_height() + precisa * 0.02, f"{int(b_.get_height())}", ha="center", fontsize=38, fontweight="bold")
        ax.set_title(casa, fontsize=28, fontweight="bold", loc="left")
        ax.set_yticks([])
        ax.spines["left"].set_visible(False)
        ax.set_ylim(0, precisa * 1.2)
    salvar(fig, "g04_veto", "Clerk da Câmara, congress.gov, Midterm Forecast (dados/e4_votos_congresso.csv)")


def g05_graham():
    fig, ax = nova("86 a 11 no Senado, e dispensada em 28 dias", "A Lei Graham de sanções contra a Rússia")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")
    ax.plot([0.6, 9.4], [3, 3], color="#222222", lw=4)
    ev = [(1.0, "07/ago", "Senado\n86 a 11", AZUL), (3.6, "16/set", "Câmara\n262 a 159", AZUL), (5.6, "18/set", "Trump\nsanciona", CINZA), (8.9, "16/out", "Trump dispensa\na parte da Rússia", VERM)]
    for x, d_, t, c in ev:
        ax.scatter(x, 3, s=500, color=c, zorder=3)
        ax.text(x, 3.6, d_, ha="center", fontsize=26, fontweight="bold")
        ax.text(x, 2.4, t, ha="center", va="top", fontsize=26, color=c)
    salvar(fig, "g05_graham", "ABC News, Morgan Lewis, Holland & Knight, KAS (referencias/textos/congresso)")


def g06_tarifa():
    t = R["tarifa"]
    fig, ax = nova("A tarifa subiu depois de o Trump perder a Câmara", "Tarifa média efetiva dos EUA, % do valor importado. 2026 é a taxa de maio")
    anos = list(t)
    v = [t[a] for a in anos]
    cores = [VERM if a in ("2019", "2020") else (AZUL if a in ("2025", "2026") else CLARO) for a in anos]
    bars = ax.bar(anos, v, color=cores)
    for b_, x in zip(bars, v):
        ax.text(b_.get_x() + b_.get_width() / 2, x + 0.12, f"{x:.1f}%".replace(".", ","), ha="center", fontsize=23, fontweight="bold")
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    ax.text(2.5, 4.4, "Câmara democrata\n2019 e 2020", ha="center", fontsize=23, color=VERM)
    salvar(fig, "g06_tarifa", "USITC, Penn Wharton Budget Model (dados/e3_tarifa_media.csv)")


def g07_vetos():
    v = R["vetos"]["desde_1981"]
    fig, ax = nova("Governo dividido é governo de veto", "Vetos por Congresso desde 1981")
    bars = ax.bar(["Congresso unificado", "Congresso dividido"], [v["media_unificado"], v["media_dividido"]], color=[CLARO, VERM], width=0.5)
    for b_ in bars:
        ax.text(b_.get_x() + b_.get_width() / 2, b_.get_height() + 0.3, f"{b_.get_height():.1f}".replace(".", ","), ha="center", fontsize=46, fontweight="bold")
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    ax.set_ylim(0, 16)
    ax.text(1.5, 13.5, f"{v['pct_derrubados']:.1f}% dos vetos\nforam derrubados".replace(".", ","), ha="right", fontsize=24, color=CINZA)
    salvar(fig, "g07_vetos", "American Presidency Project, Câmara e Senado dos EUA (dados/e3_vetos_por_congresso.csv)")


ROTULOS = {
    "B01": "Tarifa do Brasil reduzida (até jun/2027)",
    "B12": "Brasil aceita o embaixador Perez (até jun/2027)",
    "B02": "Trump e Lula se encontram (até jun/2027)",
    "B07": "Nova sanção a autoridade brasileira (até jun/2027)",
    "B09": "Ataque em território brasileiro (até jan/2029)",
    "B04": "Audiência na Câmara sobre o Flávio (até 2027)",
    "B05": "Intimação sobre a entrada do Flávio (até 2028)",
    "B06": "Câmara vota contra a tarifa do Brasil (até 2028)",
    "W03": "Limite de guerra com força de lei passa nas 2 casas",
    "W04": "Veto derrubado em tarifa ou força (até 2029)",
    "W05": "Tarifa média cai 3 pontos (até 2027)",
    "W01": "Nova ajuda à Ucrânia, US$ 10 bi (até 2028)",
    "W06": "Operação na América Latina sem aval (até 2027)",
    "W08": "Novos ataques ao Irã (até 2027)",
    "W07": "Acordo comercial formal com a China (até 2027)",
    "T01": "Trump diz que o resultado nacional foi fraudado",
    "T03": "Câmara aprova impeachment do Trump (até 2029)",
    "T04": "Câmara aprova impeachment de secretário (até 2029)",
    "T06": "Trump dá 10 vetos ou mais (até 2028)",
    "T05": "Paralisação de 7 dias ou mais (até 2027)",
}


def painel(nome, titulo, ids):
    q = {p["id"]: p for p in R["previsoes"]["perguntas"]}
    fig, ax = plt.subplots(figsize=(16, 9), dpi=120)
    fig.subplots_adjust(left=0.5, right=0.97, top=0.72, bottom=0.12)
    fig.suptitle(titulo, x=0.05, y=0.965, ha="left", fontsize=34, fontweight="bold")
    fig.text(0.05, 0.895, "Chance em %, em cada mundo. Mediana de 4 modelos de IA da mesma empresa, gravada antes da votação", ha="left", va="top", fontsize=20, color="#444444")
    for y, i in enumerate(reversed(ids)):
        ax.text(-0.04, y, ROTULOS[i], ha="right", va="center", fontsize=18, transform=ax.get_yaxis_transform())
        for x, w, c in [(0, "DD", AZUL), (1, "DR", OURO), (2, "RR", VERM)]:
            v = q[i][w]
            ax.scatter(x, y, s=1000 + v * 22, color=c)
            ax.text(x, y, f"{v:.0f}", ha="center", va="center", fontsize=23, fontweight="bold", color="white")
    ax.set_xlim(-0.5, 2.5)
    ax.set_ylim(-0.7, len(ids) - 0.3)
    ax.set_xticks([0, 1, 2])
    ax.set_xticklabels(["democratas\nnas 2 casas", "só na\nCâmara", "republicanos\nnas 2 casas"], fontsize=19)
    ax.xaxis.tick_top()
    ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)
    ax.tick_params(length=0)
    salvar(fig, nome, "dados/previsoes/rodada_b, commit e90451a, antes da votação de 03/11/2026")


def g11_exportacoes():
    e = pd.read_csv(D / "derivados" / "exportacoes_brasil.csv")
    x = e[e.periodo == "ano"].pivot(index="ano", columns="pais", values="fob_usd").loc[2010:2025] / 1e9
    b = R["brasil"]
    fig, ax = nova("O Brasil vende cada vez mais para a China", f"Exportações, US$ bilhões. De janeiro a setembro de 2026: EUA {b['jan_set_eua'][2]:.1f}%, China +{b['jan_set_china'][2]:.1f}%".replace(".", ","))
    ax.plot(x.index, x.China, color=VERM, lw=5, marker="o", ms=10, label="China")
    ax.plot(x.index, x.EUA, color=AZUL, lw=5, marker="o", ms=10, label="EUA")
    ax.text(2025.1, x.China.iloc[-1], "China", color=VERM, fontsize=26, fontweight="bold", va="center")
    ax.text(2025.1, x.EUA.iloc[-1], "EUA", color=AZUL, fontsize=26, fontweight="bold", va="center")
    ax.set_xlim(2010, 2026.6)
    salvar(fig, "g11_exportacoes", "ComexStat (dados/derivados/exportacoes_brasil.csv)")


def g12_dolar():
    t = pd.DataFrame(R["brasil"]["dolar"])
    fig, ax = nova("Depois das midterms, o dólar não tem padrão", "Variação da PTAX 30 dias depois da eleição americana. Todo ano desses também teve eleição no Brasil")
    bars = ax.bar(t.ano.astype(str), t.d30, color=[AZUL if v < 0 else VERM for v in t.d30], width=0.6)
    for b_, v in zip(bars, t.d30):
        ax.text(b_.get_x() + b_.get_width() / 2, v + 0.15 if v >= 0 else 0.15, f"{v:+.1f}%".replace(".", ","), ha="center", fontsize=25, fontweight="bold")
    ax.axhline(0, color="#222222", lw=1.5)
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    salvar(fig, "g12_dolar", "Banco Central do Brasil, série 1 do SGS (resultados/dolar_depois_das_midterms.csv)")


def g13_quanto_muda():
    g = R["previsoes"]["efeito_por_grupo"]
    fig, ax = nova("O resultado muda muito lá e pouco aqui", "Quanto a chance muda, em média, entre democratas nas 2 casas e republicanos nas 2 casas, em pontos, por grupo de pergunta")
    nomes = {"trump": "Trump e\nCongresso", "mundo": "Mundo", "brasil": "Brasil"}
    ordem = ["trump", "mundo", "brasil"]
    bars = ax.bar([nomes[k] for k in ordem], [g[k] for k in ordem], color=[VERM, OURO, AZUL], width=0.55)
    for b_ in bars:
        ax.text(b_.get_x() + b_.get_width() / 2, b_.get_height() + 0.6, f"{b_.get_height():.1f}".replace(".", ","), ha="center", fontsize=46, fontweight="bold")
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    salvar(fig, "g13_quanto_muda", "dados/previsoes/rodada_b, mediana de 4 modelos, média do valor absoluto")


def main():
    g01_cadeiras()
    g02_aprovacao()
    g03_mundos()
    g04_veto()
    g05_graham()
    g06_tarifa()
    g07_vetos()
    painel("g08_painel_brasil", "O Brasil nos 3 mundos", ["B01", "B12", "B02", "B07", "B09", "B04", "B05", "B06"])
    painel("g09_painel_mundo", "O mundo nos 3 mundos", ["W03", "W04", "W05", "W01", "W06", "W08", "W07"])
    painel("g10_painel_trump", "O Trump nos 3 mundos", ["T01", "T03", "T04", "T06", "T05"])
    g11_exportacoes()
    g12_dolar()
    g13_quanto_muda()


if __name__ == "__main__":
    main()
