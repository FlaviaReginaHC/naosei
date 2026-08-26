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
    /* Fundo principal */
    .stApp {
        background-color: #D8B4E2;
    }
    /* Área principal */
    .main {
        background-color: #D8B4E2;
    }
    /* Título */
    h1 {
        color: #FFFFFF;
        text-align: center;
    }
    /* Subtítulos */
    h2, h3 {
        color: #FFFFFF;
    }
    /* Texto */
    p, label {
        color: #FFFFFF;
    }
    /* Botão */
    .stButton > button {
        background-color: #8E44AD;
        color: white;
        border: none;
        border-radius: 10px;
    }
    .stButton > button:hover {
        background-color: #6C3483;
        color: white;
    }
    <style>
""", unsafe_allow_html=True)


# Controla se o cálculo foi realizado
if "calculado" not in st.session_state:
    st.session_state.calculado = False


# Caminho da imagem
PASTA_APP = Path(__file__).parent
CAMINHO_LOGO = PASTA_APP / "mat.jpg"


# Logo
if CAMINHO_LOGO.exists():
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.image(
            str(CAMINHO_LOGO),
            use_container_width=True
        )
else:
    st.warning("A imagem mat.jpg não foi encontrada.")


# Título
st.title("Áexis")

st.write("Equação do segundo grau no formato:")

st.latex(r"ax^2 + bx + c = 0")


# Coeficientes
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

c = st.number_input(
    "Digite o valor de c",
    value=0,
    step=1
)


# Botão
if st.button("Calcular", use_container_width=True):
    st.session_state.calculado = True


# =========================
# CÁLCULO
# =========================

if st.session_state.calculado:

    # Verifica se é realmente segundo grau
    if a == 0:

        st.error(
            "O valor de 'a' não pode ser 0 em uma equação do segundo grau."
        )

    else:

        # Calcula o Delta
        delta = b**2 - 4*a*c

        st.subheader("📐 Delta")

        st.latex(r"\Delta = b^2 - 4ac")

        st.latex(
            rf"\Delta = ({b})^2 - 4({a})({c}) = {delta}"
        )


        # =========================
        # EQUAÇÃO
        # =========================

        st.subheader("📝 Equação")

        if b >= 0 and c >= 0:

            st.latex(
                rf"{a}x^2 + {b}x + {c} = 0"
            )

        elif b >= 0 and c < 0:

            st.latex(
                rf"{a}x^2 + {b}x - {abs(c)} = 0"
            )

        elif b < 0 and c >= 0:

            st.latex(
                rf"{a}x^2 - {abs(b)}x + {c} = 0"
            )

        else:

            st.latex(
                rf"{a}x^2 - {abs(b)}x - {abs(c)} = 0"
            )


        # =========================
        # DELTA NEGATIVO
        # =========================

        if delta < 0:

            st.warning(
                "A equação não possui raízes reais, pois Δ < 0."
            )

            st.write(f"Δ = {delta}")


        # =========================
        # DELTA IGUAL A ZERO
        # =========================

        elif delta == 0:

            x1 = -b / (2 * a)

            st.success(
                "A equação possui uma única raiz real."
            )

            st.subheader("🎯 Resultado")

            st.success(
                f"x = {x1:.2f}"
            )

            st.subheader("📚 Resolução")

            st.latex(
                r"x = \frac{-b \pm \sqrt{\Delta}}{2a}"
            )

            st.latex(
                rf"x = \frac{{-({b})}}{{2({a})}}"
            )

            st.latex(
                rf"x = {x1:.2f}"
            )


        # =========================
        # DELTA POSITIVO
        # =========================

        else:

            x1 = (-b + np.sqrt(delta)) / (2 * a)

            x2 = (-b - np.sqrt(delta)) / (2 * a)

            st.success(
                "A equação possui duas raízes reais."
            )

            st.subheader("🎯 Resultado")

            col1, col2 = st.columns(2)

            with col1:

                st.write("Primeira raiz:")

                st.success(
                    f"x₁ = {x1:.2f}"
                )

            with col2:

                st.write("Segunda raiz:")

                st.success(
                    f"x₂ = {x2:.2f}"
                )


            st.subheader("📚 Resolução")

            st.latex(
                r"x = \frac{-b \pm \sqrt{\Delta}}{2a}"
            )

            st.latex(
                rf"x_1 = \frac{{-({b}) + \sqrt{{{delta}}}}}{{2({a})}}"
            )

            st.latex(
                rf"x_1 = {x1:.2f}"
            )

            st.latex(
                rf"x_2 = \frac{{-({b}) - \sqrt{{{delta}}}}}{{2({a})}}"
            )

            st.latex(
                rf"x_2 = {x2:.2f}"
            )


        # =========================
        # GRÁFICO
        # =========================

        st.subheader("📊 Gráfico da função")


        # Vértice
        xv = -b / (2 * a)

        yv = a * xv**2 + b * xv + c


        # Define o intervalo do gráfico
        if delta > 0:

            menor_x = min(x1, x2)

            maior_x = max(x1, x2)

            margem = max(
                5,
                abs(maior_x - menor_x)
            )

            inicio = menor_x - margem

            fim = maior_x + margem

        else:

            # Quando não existem duas raízes,
            # usamos o vértice como centro
            inicio = xv - 10

            fim = xv + 10


        # Valores de X
        x = np.linspace(
            inicio,
            fim,
            500
        )


        # Função quadrática
        y = a * x**2 + b * x + c


        # Cria o gráfico
        fig, ax = plt.subplots(
            figsize=(8, 5)
        )


        # Parábola
        ax.plot(
            x,
            y,
            color="#e91e63",
            linewidth=2.5,
            label=f"y = {a}x² + {b}x + {c}"
        )


        # Eixo X
        ax.axhline(
            y=0,
            color="black",
            linewidth=1
        )


        # Eixo Y
        ax.axvline(
            x=0,
            color="black",
            linewidth=1
        )


        # =========================
        # MARCA AS RAÍZES
        # =========================

        if delta > 0:

            ax.scatter(
                [x1, x2],
                [0, 0],
                color="red",
                s=100,
                zorder=5,
                label="Raízes"
            )

        elif delta == 0:

            ax.scatter(
                [x1],
                [0],
                color="red",
                s=100,
                zorder=5,
                label="Raiz"
            )


        # =========================
        # MARCA O VÉRTICE
        # =========================

        ax.scatter(
            [xv],
            [yv],
            color="blue",
            s=80,
            zorder=5,
            label=f"Vértice ({xv:.2f}, {yv:.2f})"
        )


        # Configurações
        ax.set_xlabel("Eixo X")

        ax.set_ylabel("Eixo Y")

        ax.set_title(
            "Gráfico da Função do 2º Grau"
        )

        ax.grid(True)

        ax.legend()


        # Mostra gráfico no Streamlit
        st.pyplot(fig)

        plt.close(fig)


st.divider()

st.caption(
    "📚 Calculadora de Equação do 2º Grau"
)

