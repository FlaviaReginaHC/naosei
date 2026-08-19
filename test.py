from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

st.set_page_config(
    page_title="Equação do 1º Grau",
    page_icon="📈",
    layout="centered"
)

st.markdown("""
<style>

    /* ============================= */
    /* FUNDO PRINCIPAL */
    /* ============================= */

    .stApp {
        background-color: #D8B4E2;
    }

    .main {
        background-color: #D8B4E2;
    }

    /* ============================= */
    /* TÍTULOS */
    /* ============================= */

    h1, h2, h3, h4, h5, h6 {
        color: #FFFFFF !important;
    }

    /* ============================= */
    /* TEXTOS */
    /* ============================= */

    p, label, span {
        color: #FFFFFF;
    }

    /* Texto dos captions */
    .stCaption {
        color: #FFFFFF !important;
    }

    /* ============================= */
    /* INPUTS */
    /* ============================= */

    .stNumberInput label {
        color: #FFFFFF !important;
        font-weight: bold;
    }

    .stNumberInput input {
        color: #FFFFFF !important;
        background-color: #B57AC4 !important;
        border: 2px solid #FFFFFF !important;
        border-radius: 8px;
    }

    /* Placeholder */
    .stNumberInput input::placeholder {
        color: #F5EAF7 !important;
    }

    /* Botões de aumentar/diminuir */
    .stNumberInput button {
        background-color: #8E44AD !important;
        color: #FFFFFF !important;
        border: none !important;
    }

    .stNumberInput button:hover {
        background-color: #6C3483 !important;
    }

    /* ============================= */
    /* BOTÃO CALCULAR */
    /* ============================= */

    .stButton > button {
        background-color: #8E44AD !important;
        color: #FFFFFF !important;
        border: 2px solid #FFFFFF !important;
        border-radius: 10px;
        font-size: 18px;
        font-weight: bold;
    }

    .stButton > button p {
        color: #FFFFFF !important;
    }

    .stButton > button:hover {
        background-color: #6C3483 !important;
        color: #FFFFFF !important;
        border-color: #FFFFFF !important;
    }

    /* ============================= */
    /* ALERTAS / RESULTADOS */
    /* ============================= */

    .stAlert {
        border-radius: 10px;
    }

    .stAlert p,
    .stAlert span,
    .stAlert div {
        color: #FFFFFF !important;
    }

    /* ============================= */
    /* DIVISOR */
    /* ============================= */

    hr {
        border-color: #FFFFFF !important;
    }

    /* ============================= */
    /* LATEX */
    /* ============================= */

    .stLatex {
        color: #FFFFFF !important;
    }

</style>
""", unsafe_allow_html=True)


if "calculado" not in st.session_state:
    st.session_state.calculado = False


PASTA_APP = Path(__file__).parent
CAMINHO_LOGO = PASTA_APP / "image.png"


if CAMINHO_LOGO.exists():

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.image(
            str(CAMINHO_LOGO),
            use_container_width=True
        )

else:
    st.warning(
        "A imagem image.png não foi encontrada."
    )


st.title("Equação do 1º Grau")

st.write("Equação no formato:")

st.latex(r"ax + b = 0")


a = st.number_input(
    "Digite o valor de a",
    value=1,
    step=1
)


b = st.number_input(
    "Digite o valor de b",
    value=0,
    step=1
)


if st.button(
    "Calcular",
    use_container_width=True
):
    st.session_state.calculado = True


if st.session_state.calculado:

    if a == 0:

        if b == 0:

            st.warning(
                "A equação possui infinitas soluções."
            )

        else:

            st.error(
                "A equação não possui solução."
            )

    else:

        x_raiz = -b / a

        st.subheader("Resultado")

        st.write(
            "A raiz da equação é:"
        )

        st.success(
            f"x = {x_raiz:.2f}"
        )

        st.subheader("Equação")

        if b >= 0:

            st.latex(
                f"{a}x + {b} = 0"
            )

        else:

            st.latex(
                f"{a}x - {abs(b)} = 0"
            )

        st.subheader("Resolução")

        if b >= 0:

            st.latex(
                f"{a}x + {b} = 0"
            )

            st.latex(
                f"{a}x = {-b}"
            )

            st.latex(
                f"x = \\frac{{{-b}}}{{{a}}}"
            )

            st.latex(
                f"x = {x_raiz:.2f}"
            )

        else:

            st.latex(
                f"{a}x - {abs(b)} = 0"
            )

            st.latex(
                f"{a}x = {-b}"
            )

            st.latex(
                f"x = \\frac{{{-b}}}{{{a}}}"
            )

            st.latex(
                f"x = {x_raiz:.2f}"
            )

        st.subheader("Gráfico da função")

        x = np.linspace(
            x_raiz - 10,
            x_raiz + 10,
            500
        )

        y = a * x + b

        fig, ax = plt.subplots(
            figsize=(8, 5)
        )

        # Fundo do gráfico
        fig.patch.set_facecolor("#D8B4E2")
        ax.set_facecolor("#E8D5EC")

        # Linha da função
        ax.plot(
            x,
            y,
            color="#6C3483",
            linewidth=3,
            label=f"y = {a}x + {b}"
        )

        # Eixos
        ax.axhline(
            y=0,
            color="#FFFFFF",
            linewidth=1.5
        )

        ax.axvline(
            x=0,
            color="#FFFFFF",
            linewidth=1.5
        )

        # Raiz
        ax.scatter(
            [x_raiz],
            [0],
            color="#FFFFFF",
            edgecolors="#6C3483",
            linewidths=2,
            s=100,
            zorder=5,
            label=f"Raiz x = {x_raiz:.2f}"
        )

        # Textos do gráfico
        ax.set_xlabel(
            "Eixo X",
            color="#FFFFFF"
        )

        ax.set_ylabel(
            "Eixo Y",
            color="#FFFFFF"
        )

        ax.set_title(
            "Gráfico da Função do 1º Grau",
            color="#FFFFFF"
        )

        # Números dos eixos
        ax.tick_params(
            colors="#FFFFFF"
        )

        # Bordas
        for spine in ax.spines.values():
            spine.set_color("#FFFFFF")

        # Grade
        ax.grid(
            True,
            color="#FFFFFF",
            alpha=0.25
        )

        # Legenda
        legend = ax.legend()

        legend.get_frame().set_facecolor(
            "#8E44AD"
        )

        legend.get_frame().set_edgecolor(
            "#FFFFFF"
        )

        for text in legend.get_texts():
            text.set_color("#FFFFFF")

        st.pyplot(fig)

        plt.close(fig)


st.divider()

st.caption(
    "Calculadora de Equação do 1º Grau"
)
