from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

st.set_page_config(
    page_title="Equação do 1º Grau", page_icon="📈", layout="centered")

st.markdown("""
<style>
    /* Fundo principal */
    .stApp {
        background: linear-gradient(
            135deg,
            #f3e8ff 0%,
            #e9d5ff 50%,
            #ddd6fe 100%
        );
    }

    /* Área central do conteúdo */
    .main .block-container {
        background-color: rgba(255, 255, 255, 0.75);
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 8px 30px rgba(91, 33, 182, 0.15);
    }

    /* Título */
    h1 {
        color: #6b21a8 !important;
        text-align: center;
    }

    /* Subtítulos */
    h2, h3 {
        color: #7e22ce !important;
    }

    /* Textos */
    p, label {
        color: #4c1d95 !important;
    }

    /* Campos de entrada */
    div[data-baseweb="input"] {
        border: 2px solid #c084fc;
        border-radius: 10px;
        background-color: #faf5ff;
    }

    div[data-baseweb="input"]:focus-within {
        border-color: #9333ea;
        box-shadow: 0 0 0 2px rgba(147, 51, 234, 0.15);
    }

    /* Botão */
    .stButton > button {
        background: linear-gradient(
            90deg,
            #9333ea,
            #7e22ce
        );
        color: white;
        border: none;
        border-radius: 12px;
        font-weight: bold;
        padding: 0.6rem 1rem;
        transition: 0.3s;
    }

    .stButton > button:hover {
        background: linear-gradient(
            90deg,
            #7e22ce,
            #6b21a8
        );
        transform: scale(1.02);
    }

    /* Resultado */
    div[data-testid="stAlert"] {
        border-radius: 12px;
    }

    /* Linha divisória */
    hr {
        border-color: #c084fc;
    }

    /* Rodapé */
    .stCaption {
        color: #6b21a8 !important;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

if "calculado" not in st.session_state:
  st.session_state.calculado = False

PASTA_APP = Path(__file__).parent
CAMINHO_LOGO = PASTA_APP / "flavia.png"

if CAMINHO_LOGO.exists():
  col1, col2, col3 = st.columns([1, 2, 1])
  with col2:
    st.image(str(CAMINHO_LOGO), use_container_width=True)
else:
  st.warning("A imagem não foi encontrada.")

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

    st.subheader("📊 Gráfico da função")

    x = np.linspace(x_raiz - 10, x_raiz + 10, 500)

y = a * x + b

fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(x, y, linewidth=2, label=f"y = {a}x + {b}")

ax.axhline(y=0, color='black', linewidth=1)
ax.axvline(x=0, color='black', linewidth=1)

ax.scatter([x_raiz], [0], color='red', s=100, zorder=5, label=f"Raiz x = {x_raiz:.2f}")

ax.set_xlabel("Eixo X")  
ax.set_ylabel("Eixo Y") 
ax.set_title("Gráfico da Função do 1º Grau")
ax.grid(True)
ax.legend()

st.pyplot(fig)
plt.close(fig)

st.divider()
st.caption("📚 Calculadora de Equação do 1º Grau")
