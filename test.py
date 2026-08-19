from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

st.set_page_config(
    page_title="Equação do 1º Grau", page_icon="📈", layout="centered")

if "calculado" not in st.session_state:
  st.session_state.calculado = False

PASTA_APP = Path(__file__).parent
CAMINHO_LOGO = PASTA_APP / "mat.jpg"

if CAMINHO_LOGO.exists():
  col1, col2, col3 = st.columns([1, 2, 1])
  with col2:
    st.image(str(CAMINHO_LOGO), use_container_width=True)
else:
  st.warning("A imagem mat.jpg não foi encontrada.")

st.title("Equação do 1º Grau")
st.write("Equação no formato:")
st.latex(r"ax + b = 0")

a = st.number_input("Digite o valor de a", value=1, step=1)
b = st.number_input("Digite o valor de b", value=0, step=1)

if st.button("Calcular", use_container_width=True):
  st.session_state.calculado = True

if st.session_state.calculado:
  if a == 0:
    if b == 0:
      st.warning("A equação possui infinitas soluções.")
    else:
      st.error("A equação não possui solução.")
  else:
    x_raiz = -b / a

    st.subheader("Resultado")
    st.write("A raiz da equação é:")
    st.success(f"x = {x_raiz:.2f}")

    st.subheader("Equação")
    if b >= 0:
      st.latex(f"{a}x + {b} = 0")
    else:
      st.latex(f"{a}x - {abs(b)} = 0")

    st.subheader("Resolução")
    if b >= 0:
      st.latex(f"{a}x + {b} = 0")
    else:
        st.latex(f"{a}x - {abs(b)} = 0")
        st.latex(f"{a}x = {-b}")
        st.latex(f"x = \\frac{{{-b}}}{{{a}}}")
        st.latex(f"x = {x_raiz:.2f}")

        st.subheader(
            "📊 Gráfico da função")

        x = np.linspace(
            x_raiz - 10,
            x_raiz + 10,
            500)

        y = a * x + b

        fig, ax = plt.subplots(
            figsize=(8, 5))

        ax.plot(
            x,
            y,
            linewidth=2,
            label=f"y = {a}x + {b}")

        ax.axhline(
            y=0,
            linewidth=1)

        ax.axvline(
            x=0,
            linewidth=1)

        ax.scatter(
            [x_raiz],
            [0],
            s=100,
            zorder=5,
            label=f"Raiz x = {x_raiz:.2f}"
        )

        # ====================================
        # CONFIGURAÇÃO DO GRÁFICO
        # ====================================

        ax.set_xlabel("Eixo X")
        ax.set_ylabel("Eixo Y")

        ax.set_title(
            "Gráfico da Função do 1º Grau")

        ax.grid(True)

        ax.legend()

        # ====================================
        # MOSTRA GRÁFICO
        # ====================================

        st.pyplot(fig)

        plt.close(fig)

st.divider()
st.caption("Calculadora de Equação do 1º Grau")
