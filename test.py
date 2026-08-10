from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

st.set_page_config(
    page_title="Equação do 1º Grau", page_icon="📈", layout="centered"
)

# Inicializa a variável de controle no Session State
if "calculado" not in st.session_state:
  st.session_state.calculado = False

PASTA_APP = Path(__file__).parent
CAMINHO_LOGO = PASTA_APP / "mat.jpeg"

if CAMINHO_LOGO.exists():
  col1, col2, col3 = st.columns([1, 2, 1])
  with col2:
    st.image(str(CAMINHO_LOGO), use_container_width=True)
else:
  st.warning("A imagem mat.jpeg não foi encontrada.")

st.title("Equação do 1º Grau")
st.write("Equação no formato:")
st.latex(r"ax + b = 0")

a = st.number_input("Digite o valor de a", value=1, step=1)
b = st.number_input("Digite o valor de b", value=0, step=1)

# O botão apenas ativa o estado de cálculo
if st.button("Calcular", use_container_width=True):
  st.session_state.calculado = True

# Executa o código se o botão foi clicado anteriormente
if st.session_state.calculado:
  # ========================================
  # VERIFICA O VALOR DE A
  # ========================================
  if a == 0:
    if b == 0:
      st.warning("A equação possui infinitas soluções.")
    else:
      st.error("A equação não possui solução.")
  else:
    # ====================================
    # CALCULA A RAIZ
    # ====================================
    x_raiz = -b / a

    # ====================================
    # RESULTADO
    # ====================================
    st.subheader("Resultado")
    st.write("A raiz da equação é:")
    st.success(f"x = {x_raiz:.2f}")

    # ====================================
    # MOSTRA A EQUAÇÃO
    # ====================================
    st.subheader("Equação")
    if b >= 0:
      st.latex(f"{a}x + {b} = 0")
    else:
      st.latex(f"{a}x - {abs(b)} = 0")

    # ====================================
    # MOSTRA O CÁLCULO
    # ====================================
    st.subheader("Resolução")
    if b >= 0:
      st.latex(f"{a}x + {b} = 0")
    else:
      st.latex(f"{a}x - {abs(b)} = 0")
    st.latex(f"{a}x = {-b}")
    st.latex(f"x = \\frac{{{-b}}}{{{a}}}")
    st.latex(f"x = {x_raiz:.2f}")

    # ====================================
    # GRÁFICO
    # ====================================
    st.subheader("Gráfico da função")

    # Cria intervalo dinâmico para o gráfico
    x = np.linspace(x_raiz - 10, x_raiz + 10, 500)
    y = a * x + b

    fig, ax = plt.subplots(figsize=(8, 5))

    # Desenha a reta e eixos
    ax.plot(x, y, linewidth=2, label=f"y = {a}x + {b}", color="#1f77b4")
    ax.axhline(y=0, color="black", linewidth=1, linestyle="--")
    ax.axvline(x=0, color="black", linewidth=1, linestyle="--")

    # Marca a raiz (ponto vermelho)
    ax.scatter(
        [x_raiz],
        color="red",
        s=100,
        zorder=5,
        label=f"Raiz x = {x_raiz:.2f}",
    )

    # Configuração visual do gráfico
    ax.set_xlabel("Eixo X")
    ax.set_ylabel("Eixo Y")
    ax.set_title("Gráfico da Função do 1º Grau")
    ax.grid(True, linestyle=":", alpha=0.6)
    ax.legend()

    # Mostra o gráfico no Streamlit
    st.pyplot(fig)
    plt.close(fig)

st.divider()
st.caption("Calculadora de Equação do 1º Grau")
