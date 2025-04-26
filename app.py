import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
from streamlit_autorefresh import st_autorefresh
from streamlit_custom_notification_box import custom_notification_box
import calculator
import platform
import darkdetect

# Configuração da página
st.set_page_config(
    page_title="PyCalculator IA",
    page_icon="🔢",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Detectar tema do sistema
system_theme = "dark" if darkdetect.isDark() else "light"

# CSS personalizado para a interface
st.markdown("""
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
<style>
    /* Fonte monoespaçada para o display */
    .stTextInput, .stTextArea {
        font-family: 'Courier New', Courier, monospace !important;
    }
    
    /* Animações suaves para botões */
    .stButton>button {
        transition: all 0.3s ease-in-out !important;
        font-family: 'Inter', sans-serif !important;
        font-weight: 500 !important;
    }
    
    .stButton>button:active {
        transform: scale(0.95) !important;
    }
    
    /* Estilo moderno para o display */
    .calculator-display {
        background: linear-gradient(135deg, #f5faff 60%, #e3f0ff 100%);
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        font-family: 'Courier New', Courier, monospace;
        font-size: 2em;
        text-align: right;
        box-shadow: 0 4px 12px rgba(33, 150, 243, 0.08), 0 1.5px 4px rgba(0,0,0,0.06);
        border: 1.5px solid #e3f0ff;
        color: #222;
        font-weight: bold;
    }

    /* Estilos específicos para botões de operação */
    .stButton>button[data-testid^="btn_"] {
        font-size: 1.2em !important;
    }

    /* Botões de operação com azul mais claro */
    .stButton > button[data-testid="btn_plus"],
    .stButton > button[data-testid="btn_minus"],
    .stButton > button[data-testid="btn_multiply"],
    .stButton > button[data-testid="btn_divide"] {
        background-color: #64B5F6 !important;
        color: white !important;
        border: none !important;
    }
    .stButton > button[data-testid="btn_plus"]:focus,
    .stButton > button[data-testid="btn_minus"]:focus,
    .stButton > button[data-testid="btn_multiply"]:focus,
    .stButton > button[data-testid="btn_divide"]:focus,
    .stButton > button[data-testid="btn_plus"]:active,
    .stButton > button[data-testid="btn_minus"]:active,
    .stButton > button[data-testid="btn_multiply"]:active,
    .stButton > button[data-testid="btn_divide"]:active {
        background-color: #64B5F6 !important;
        color: white !important;
        border: none !important;
    }
    /* Botões AC e resultado (=) em laranja mais forte */
    .stButton > button[data-testid="btn_clear"],
    .stButton > button[data-testid="btn_equals"] {
        background-color: #FF6F00 !important;
        color: white !important;
        border: none !important;
    }
    .stButton > button[data-testid="btn_clear"]:focus,
    .stButton > button[data-testid="btn_equals"]:focus,
    .stButton > button[data-testid="btn_clear"]:active,
    .stButton > button[data-testid="btn_equals"]:active {
        background-color: #FF6F00 !important;
        color: white !important;
        border: none !important;
    }
    /* Botões de controle com cores diferentes */
    .stButton>button[data-testid="btn_plusminus"],
    .stButton>button[data-testid="btn_percent"] {
        background-color: #FF9800 !important;
        color: white !important;
    }
    
    /* Responsividade aprimorada para grid de botões */
    .stColumns {
        display: grid !important;
        grid-template-columns: repeat(4, 1fr) !important;
        gap: 0.5rem !important;
    }
    .stColumn {
        min-width: 60px !important;
        max-width: 1fr !important;
    }
    .stButton>button {
        min-width: 48px !important;
        min-height: 48px !important;
        font-size: 1.2em !important;
    }
    @media (max-width: 500px) {
        .calculator-display {
            font-size: 1.2em;
            padding: 10px;
        }
        .stColumns {
            grid-template-columns: repeat(4, 1fr) !important;
        }
        .stButton>button {
            min-width: 40px !important;
            min-height: 40px !important;
            font-size: 1em !important;
        }
    }
    @media (max-width: 350px) {
        .stColumns {
            grid-template-columns: repeat(2, 1fr) !important;
        }
    }

    /* Estilo para o título com ícone */
    .title-with-icon {
        display: flex;
        align-items: center;
        gap: 10px;
        font-size: 2em;
        margin-bottom: 1em;
    }
    
    .title-with-icon i {
        color: #2196F3;
    }

    /* Reset de padding/margin dos pais do grid */
    section.main > div.block-container {
        padding-left: 0 !important;
        padding-right: 0 !important;
        margin-left: 0 !important;
        margin-right: 0 !important;
        max-width: 100vw !important;
    }

    /* Hover para botões de operação (azul claro) */
    .stButton > button[data-testid="btn_plus"]:hover,
    .stButton > button[data-testid="btn_minus"]:hover,
    .stButton > button[data-testid="btn_multiply"]:hover,
    .stButton > button[data-testid="btn_divide"]:hover {
        background-color: #42a5f5 !important;
        color: white !important;
        transform: scale(1.05) !important;
    }
    /* Hover para botões AC e = (laranja forte) */
    .stButton > button[data-testid="btn_clear"]:hover,
    .stButton > button[data-testid="btn_equals"]:hover {
        background-color: #FF9800 !important;
        color: white !important;
        transform: scale(1.05) !important;
    }

    /* Botão primary (AC e =) em laranja intermediário */
    button[kind="primary"] {
        background-color: #FFA726 !important;
        color: white !important;
        border: none !important;
    }
    button[kind="primary"]:hover, button[kind="primary"]:focus, button[kind="primary"]:active {
        background-color: #FFCC80 !important;
        color: white !important;
    }
    /* Botão secondary (demais) em azul claro */
    button[kind="secondary"] {
        background-color: #64B5F6 !important;
        color: white !important;
        border: none !important;
    }
    button[kind="secondary"]:hover, button[kind="secondary"]:focus, button[kind="secondary"]:active {
        background-color: #42a5f5 !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# Título com animação de carregamento e ícone Font Awesome
with st.spinner('Carregando...'):
    st.markdown('<div class="title-with-icon"><i class="fas fa-calculator"></i>PyCalculator IA</div>', unsafe_allow_html=True)

# Inicialização do estado da calculadora
if 'display' not in st.session_state:
    st.session_state.display = "0"
if 'memory' not in st.session_state:
    st.session_state.memory = None
if 'operator' not in st.session_state:
    st.session_state.operator = None
if 'waiting_for_operand' not in st.session_state:
    st.session_state.waiting_for_operand = False
if 'expression' not in st.session_state:
    st.session_state.expression = ""
if 'show_result' not in st.session_state:
    st.session_state.show_result = False

# Função utilitária para exibir operadores matemáticos tradicionais na expressão
def beautify_expression(expr):
    return expr.replace('*', '×').replace('/', '÷')

# Função para atualizar o display e a expressão
def update_display(value):
    if st.session_state.waiting_for_operand:
        st.session_state.display = value
        st.session_state.waiting_for_operand = False
    else:
        st.session_state.display = st.session_state.display + value if st.session_state.display != "0" else value
    # Atualiza a expressão
    if st.session_state.show_result:
        st.session_state.expression = value
        st.session_state.show_result = False
    else:
        if st.session_state.expression and st.session_state.expression[-1] == '=':
            st.session_state.expression = value
        else:
            st.session_state.expression += value
    st.rerun()

# Função para formatar o número mantendo a consistência entre inteiros e decimais
def format_number(number):
    # Converte para float primeiro para garantir
    float_num = float(number)
    # Se o número é inteiro, retorna sem casas decimais
    if float_num.is_integer():
        return str(int(float_num))
    # Se é decimal, retorna como está
    return str(float_num)

# Função para operações
def perform_operation(op):
    try:
        # Se não houver valor na memória, apenas armazena o valor atual e define a operação
        if st.session_state.memory is None:
            st.session_state.memory = float(st.session_state.display)
            st.session_state.operator = None if op == "=" else op
            if op != "=":
                st.session_state.expression += op
            st.session_state.waiting_for_operand = True
            st.session_state.show_result = False
            st.rerun()
            return

        # Se estamos esperando um novo operando e não é o sinal de igual,
        # apenas atualiza o operador
        if st.session_state.waiting_for_operand and op != "=":
            # Atualiza o último operador na expressão
            if st.session_state.expression and st.session_state.expression[-1] in "+-*/":
                st.session_state.expression = st.session_state.expression[:-1] + op
            else:
                st.session_state.expression += op
            st.session_state.operator = op
            st.rerun()
            return

        current_value = float(st.session_state.display)
        # Realiza a operação apropriada
        if st.session_state.operator is None:
            result = current_value
        elif st.session_state.operator == "+":
            result = st.session_state.memory + current_value
        elif st.session_state.operator == "-":
            result = st.session_state.memory - current_value
        elif st.session_state.operator == "*":
            result = st.session_state.memory * current_value
        elif st.session_state.operator == "/":
            if current_value == 0:
                raise ValueError("Divisão por zero não é permitida")
            result = st.session_state.memory / current_value

        # Atualiza o display e a memória mantendo o formato apropriado
        st.session_state.display = format_number(result)
        st.session_state.memory = result

        # Atualiza a expressão
        if op == "=":
            st.session_state.expression += f"={format_number(result)}"
            st.session_state.show_result = True
        else:
            st.session_state.expression += op
            st.session_state.show_result = False

        # Configura o próximo operador
        st.session_state.operator = None if op == "=" else op
        st.session_state.waiting_for_operand = True
        st.rerun()
    except Exception as e:
        st.error(f"Erro: {str(e)}")

# Display da calculadora
if st.session_state.show_result:
    display_content = st.session_state.display
else:
    # Mostra a expressão se houver, senão o display
    display_content = beautify_expression(st.session_state.expression) if st.session_state.expression else st.session_state.display

st.markdown(f"""
    <div class="calculator-display">
        {display_content}
    </div>
""", unsafe_allow_html=True)

# Layout dos botões em colunas usando st.columns e st.button, sem tooltips
col1, col2, col3, col4 = st.columns(4)

# Primeira linha
with col1:
    if st.button("AC", use_container_width=True, key="btn_clear", type="primary"):
        st.session_state.display = "0"
        st.session_state.memory = None
        st.session_state.operator = None
        st.session_state.waiting_for_operand = False
        st.session_state.expression = ""
        st.session_state.show_result = False
        st.rerun()
with col2:
    if st.button("⁺∕₋", use_container_width=True, key="btn_plusminus"):
        if st.session_state.display != "0":
            if st.session_state.display.startswith("-"):
                st.session_state.display = st.session_state.display[1:]
            else:
                st.session_state.display = "-" + st.session_state.display
            st.rerun()
with col3:
    if st.button("％", use_container_width=True, key="btn_percent"):
        current = float(st.session_state.display)
        st.session_state.display = str(current / 100)
        st.rerun()
with col4:
    if st.button("÷", use_container_width=True, key="btn_divide"):
        perform_operation("/")

# Segunda linha
with col1:
    if st.button("7", use_container_width=True, key="btn_7"):
        update_display("7")
with col2:
    if st.button("8", use_container_width=True, key="btn_8"):
        update_display("8")
with col3:
    if st.button("9", use_container_width=True, key="btn_9"):
        update_display("9")
with col4:
    if st.button("×", use_container_width=True, key="btn_multiply"):
        perform_operation("*")

# Terceira linha
with col1:
    if st.button("4", use_container_width=True, key="btn_4"):
        update_display("4")
with col2:
    if st.button("5", use_container_width=True, key="btn_5"):
        update_display("5")
with col3:
    if st.button("6", use_container_width=True, key="btn_6"):
        update_display("6")
with col4:
    if st.button("−", use_container_width=True, key="btn_minus"):
        perform_operation("-")

# Quarta linha
with col1:
    if st.button("1", use_container_width=True, key="btn_1"):
        update_display("1")
with col2:
    if st.button("2", use_container_width=True, key="btn_2"):
        update_display("2")
with col3:
    if st.button("3", use_container_width=True, key="btn_3"):
        update_display("3")
with col4:
    if st.button("＋", use_container_width=True, key="btn_plus"):
        perform_operation("+")

# Quinta linha
with col1:
    if st.button("0", use_container_width=True, key="btn_0"):
        update_display("0")
with col2:
    if st.button(".", use_container_width=True, key="btn_dot"):
        if "." not in st.session_state.display:
            st.session_state.display += "."
            st.rerun()
with col3:
    if st.button("⌫", use_container_width=True, key="btn_backspace"):
        st.session_state.display = st.session_state.display[:-1] if len(st.session_state.display) > 1 else "0"
        st.rerun()
with col4:
    if st.button("＝", use_container_width=True, key="btn_equals", type="primary"):
        perform_operation("=")

# Rodapé com informações
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>Pressione as teclas numéricas ou operadores para usar o teclado</p>
    <p>Tema atual: {}</p>
</div>
""".format("Escuro" if system_theme == "dark" else "Claro"), unsafe_allow_html=True) 