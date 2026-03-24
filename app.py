import streamlit as st
import urllib.parse
import csv
import os
import base64
from datetime import datetime

# 1. CONFIGURAÇÃO BÁSICA DA PÁGINA
st.set_page_config(
    page_title="ESCUTA+ | Acolhimento Escolar",
    page_icon="💙",
    layout="centered" 
)

# 2. CONFIGURAÇÃO DE BANCO DE DADOS (CSV local)
ARQUIVO_DENUNCIAS = "denuncias.csv"
ARQUIVO_BACKGROUND = "background.avif"

def salvar_denuncia(usuario, anonimato, tipo, local, descricao):
    """Salva a denúncia em CSV para análise posterior."""
    try:
        dados = {
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'usuario': usuario,
            'anonimato': anonimato,
            'tipo': tipo,
            'local': local,
            'descricao': descricao
        }
        
        arquivo_existe = os.path.exists(ARQUIVO_DENUNCIAS)
        
        with open(ARQUIVO_DENUNCIAS, 'a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=dados.keys())
            if not arquivo_existe:
                writer.writeheader()
            writer.writerow(dados)
        return True
    except Exception as e:
        st.error(f"Erro ao salvar: {e}")
        return False

def get_base64_image(image_path):
    """Converte imagem para base64."""
    try:
        with open(image_path, "rb") as image_file:
            encoded = base64.b64encode(image_file.read()).decode()
            return f"data:image/avif;base64,{encoded}"
    except FileNotFoundError:
        return ""

def detectar_categoria(descricao):
    """Detecta automaticamente a categoria baseado em palavras-chave."""
    if not descricao:
        return None
    
    descricao_lower = descricao.lower()
    
    # Keywords para cada categoria
    bullying_keys = ["brinca", "apelido", "zoação", "excluem", "isolam", "chacota", "gozação", "implicam", "tiram sarro"]
    racismo_keys = ["preto", "negro", "branco", "raça", "etnia", "cor", "origem", "descendente", "etnias"]
    assdio_keys = ["toca", "beija", "abraça", "sem permissão", "constrangedor", "constrangida", "assédio", "impróprio"]
    sofrimento_keys = ["triste", "depressão", "ansiedade", "medo", "isolamento", "sozinho", "chorando", "suicida", "morte"]
    
    # Verificar cada categoria
    for key in bullying_keys:
        if key in descricao_lower:
            return "Bullying"
    
    for key in racismo_keys:
        if key in descricao_lower:
            return "Racismo"
    
    for key in assdio_keys:
        if key in descricao_lower:
            return "Assédio"
    
    for key in sofrimento_keys:
        if key in descricao_lower:
            return "Sofrimento Emocional"
    
    return None

# 3. INJEÇÃO DE CSS DE ALTA ACESSIBILIDADE E DESIGN
base64_bg = get_base64_image(ARQUIVO_BACKGROUND)

if base64_bg:
    css_background = f"""
    .stApp {{
        background-image: url("{base64_bg}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    """
else:
    css_background = ".stApp {background-color: #F0F4F8;}"

st.markdown(f"""
    <style>
    /* --- FUNDO E CAIXA DE CONTEÚDO --- */
    {css_background}
    
    /* Overlay semi-transparente para melhor legibilidade */
    .stApp::before {{
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(0, 0, 0, 0.25);
        z-index: -1;
    }}
    
    /* Uma única caixa branca que envolve toda a tela - ACESSÍVEL */
    .block-container {{
        background-color: rgba(255, 255, 255, 0.98) !important; 
        padding: 2rem 3rem !important; 
        border-radius: 24px !important; 
        box-shadow: 0px 10px 40px rgba(0,0,0,0.3) !important; 
        margin-top: 2rem !important;
        margin-bottom: 2rem !important;
        border: 3px solid #0056B3 !important;
    }}
    
    /* --- ACESSIBILIDADE DE TEXTO --- */
    h1, h2, h3, p, label, .stRadio > div {{
        color: #121212 !important; 
        font-family: 'Arial', sans-serif !important; 
    }}
    p, li, label, div[data-baseweb="radio"] {{
        font-size: 22px !important; 
        line-height: 1.6 !important; 
    }}
    h1 {{
        font-size: 40px !important;
        color: #0056B3 !important; 
        font-weight: 900 !important;
    }}
    
    /* --- ACESSIBILIDADE MOTORA --- */
    .stButton > button, .stLinkButton > a {{
        height: auto !important;
        padding: 24px !important;
        font-size: 26px !important;
        font-weight: 900 !important;
        border-radius: 16px !important;
        width: 100% !important;
        text-align: center !important;
        display: block !important;
        text-decoration: none !important;
        transition: 0.2s;
    }}
    
    .stButton > button:focus, .stLinkButton > a:focus, input:focus, textarea:focus {{
        outline: 6px solid #FFC107 !important; 
        outline-offset: 4px !important;
    }}
    
    button[kind="primary"], .stLinkButton > a {{
        background-color: #D32F2F !important; 
        color: #FFFFFF !important;
        border: 4px solid transparent !important;
    }}
    
    button[kind="primary"]:hover, .stLinkButton > a:hover {{
        background-color: #9A0007 !important;
        border: 4px solid #121212 !important; 
    }}
    
    button[kind="secondary"] {{
        background-color: #FFFFFF !important;
        color: #0056B3 !important;
        border: 4px solid #0056B3 !important;
    }}
    
    input, textarea, div[data-baseweb="select"] {{
        font-size: 20px !important;
        border: 3px solid #555 !important; 
        border-radius: 8px !important;
    }}
    
    [data-testid="stImage"] {{
        display: flex;
        justify-content: center;
    }}
    </style>
""", unsafe_allow_html=True)

# 3. GERENCIAMENTO DE ESTADO
if 'tela' not in st.session_state:
    st.session_state.tela = 1
if 'usuario' not in st.session_state:
    st.session_state.usuario = "Anônimo"
if 'historico_denuncias' not in st.session_state:
    st.session_state.historico_denuncias = 0
if 'ultima_denuncia' not in st.session_state:
    st.session_state.ultima_denuncia = None

def mudar_tela(nova_tela):
    st.session_state.tela = nova_tela

# --- TELA 1: LOGIN ACESSÍVEL ---
if st.session_state.tela == 1:
    st.title("💙 Bem-vindo ao ESCUTA+")
    st.write("Identifique-se para entrar ou continue anonimamente.")
    
    st.write("### Suas Informações")
    nome = st.text_input("1. Qual seu Nome?")
    matricula = st.text_input("2. Qual sua Matrícula?")
    
    st.write("")
    if st.button("➡️ Entrar no Aplicativo", type="secondary"):
        if nome and matricula:
            st.session_state.usuario = f"{nome} (Matrícula: {matricula})"
        elif nome:
            st.session_state.usuario = nome
        elif matricula:
            st.session_state.usuario = f"Aluno da Matrícula {matricula}"
        else:
            st.session_state.usuario = "Anônimo"
            
        mudar_tela(2)
        st.rerun()

# --- TELA 2: BOTÃO DO PÂNICO (Home) ---
elif st.session_state.tela == 2:
    st.title("ESCUTA+")
    st.write(f"Olá, **{st.session_state.usuario}**. Você está em um ambiente seguro.")
    st.write("---")
    
    # Mostrar histórico do aluno
    if st.session_state.historico_denuncias > 0:
        st.info(f"📊 **Seu histórico:** Você já fez {st.session_state.historico_denuncias} pedido(s) de ajuda. Estamos sempre ouvindo!")
        if st.session_state.ultima_denuncia:
            st.write(f"_Último pedido: {st.session_state.ultima_denuncia}_")
    
    st.write("")
    st.write("### O que você precisa agora?")
    
    if st.button("🚨 PEDIR AJUDA AGORA", type="primary"):
        mudar_tela(4)
        st.rerun()
        
    st.write("")
    st.write("")
    
    if st.button("ℹ️ Entenda o que está passando (Acolhimento)", type="secondary"):
        mudar_tela(3)
        st.rerun()

# --- TELA 3: ACOLHIMENTO ---
elif st.session_state.tela == 3:
    st.title("🤝 Acolhimento")
    st.write("Leia com calma. Entender o problema é o primeiro passo para a solução.")
    
    st.markdown("### O que são essas situações?")
    st.error("**Bullying:** Atos violentos, intencionais e repetidos contra alguém indefeso.")
    st.warning("**Racismo:** Discriminação baseada na cor da pele ou etnia.")
    st.info("**Sofrimento Emocional:** Tristeza intensa, medo ou isolamento. É normal pedir ajuda!")
        
    st.write("---")
    if st.button("⬅️ Voltar para o Início", type="secondary"):
        mudar_tela(2)
        st.rerun()

# --- TELA 4: FORMULÁRIO DE DENÚNCIA ---
elif st.session_state.tela == 4:
    st.title("📝 Pedido de Ajuda")
    st.write("Preencha apenas o que conseguir. Nós vamos te ajudar.")
    
    anonimato = st.radio("1. Como deseja falar com a gente?", ["Quero ser Anônimo", "Pode usar meu login"])
    tipo = st.selectbox("2. O que aconteceu com você?", ["Toque aqui para escolher...", "Bullying", "Racismo", "Assédio", "Sofrimento Emocional", "Outros"])
    local = st.text_input("3. Onde isso aconteceu? (Ex: Sala de Aula, Corredor, Refeitório...)")
    descricao = st.text_area("4. Quer contar mais detalhes? ")
    
    # 🤖 DETECÇÃO AUTOMÁTICA DE CATEGORIA
    categoria_detectada = detectar_categoria(descricao)
    if categoria_detectada and tipo == "Toque aqui para escolher...":
        st.success(f"✅ Detectamos **{categoria_detectada}** no seu relato. Atualizamos para você!")
        tipo = categoria_detectada
    
    st.write("---")
    
    # 📚 SUGESTÕES DE RECURSOS
    recursos_por_tipo = {
        "Bullying": "📞 **Telefone da Doméstica:** 100 | 🌐 **Disque Denúncia:** 181 | 💬 **Chat com Psicólogo:** [clique aqui](https://www.psicologiaviva.com.br)",
        "Racismo": "🎓 **Material Educativo:** [Combate ao Racismo](https://www.gov.br/cidadania) | 📞 **Ouvidoria de Igualdade:** 136",
        "Assédio": "⚖️ **Delegacia Eletrônica:** [Aqui](https://www.delegaciaeletronica.pc.sp.gov.br) | 📞 **Disque Mulher:** 180",
        "Sofrimento Emocional": "💙 **CVV (Prevenção ao Suicídio):** 188 | 🏥 **Buscar Psicólogo:** [CAMINHO](https://www.caminhodaluz.org.br) | 📱 **App Meu Acolher:** Download grátis",
        "Outros": "📞 **Coordenação Escolar:** Procure um professor de confiança | 🤝 **Orientador:** Sempre disponível"
    }
    
    if tipo != "Toque aqui para escolher...":
        with st.expander("💡 Recursos e Ajuda para " + tipo, expanded=False):
            st.markdown(recursos_por_tipo.get(tipo, "Estamos aqui para ouvir você."))
        
        numero_destino = "558694231846" 
        
        nome_aluno_envio = "Anônimo" if anonimato == "Quero ser Anônimo" else st.session_state.usuario
        relato_envio = descricao if descricao else "O aluno preferiu não detalhar agora."
            
        mensagem = f"""🚨 *ALERTA DE EMERGÊNCIA - ESCUTA+* 🚨\n\nOlá, Coordenação. Um novo pedido de ajuda foi registrado pelo aplicativo.\n\n*Aluno:* {nome_aluno_envio}\n*Situação:* {tipo}\n*Local:* {local}\n*Relato:* {relato_envio}\n\n⚠️ _Por favor, verifique a situação e inicie o protocolo de acolhimento._"""
        
        msg_codificada = urllib.parse.quote(mensagem)
        link_whatsapp = f"https://wa.me/{numero_destino}?text={msg_codificada}"
        
        if st.button("📲 Confirmar e Enviar Pedido de Ajuda", type="primary"):
            # Salva os dados antes de abrir WhatsApp
            salvar_denuncia(
                usuario=st.session_state.usuario,
                anonimato=anonimato,
                tipo=tipo,
                local=local,
                descricao=descricao
            )
            
            # Atualizar histórico
            st.session_state.historico_denuncias += 1
            st.session_state.ultima_denuncia = datetime.now().strftime("%d/%m às %H:%M")
            
            st.success("✅ Seu pedido foi registrado com segurança!")
            st.info(f"📊 Total de pedidos: {st.session_state.historico_denuncias}")
            st.info("📱 Clique no link abaixo para enviar pelo WhatsApp:")
            st.markdown(f"[📲 Enviar para Coordenação]({link_whatsapp})")
            st.balloons()
        
    else:
        st.button("📲 Confirmar e Enviar Pedido de Ajuda", disabled=True)
        st.warning("⚠️ Escolha uma opção na pergunta número 2 para liberar o botão de envio.")
        
    st.write("")
    if st.button("⬅️ Cancelar e Voltar", type="secondary"):
        mudar_tela(2)
        st.rerun()