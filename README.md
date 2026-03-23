# 💙 ESCUTA+ | Acolhimento Escolar

Uma aplicação acessível e segura para ajudar estudantes em situações de bullying, racismo e sofrimento emocional nas escolas.

## 🎯 Objetivo

Fornecer um canal anônimo e acessível para que alunos possam pedir ajuda à coordenação escolar, com foco em:
- **Acessibilidade**: Fontes grandes, cores de alto contraste, navegação intuitiva
- **Segurança**: Opção de anonimato garantido
- **Eficiência**: Envio direto para WhatsApp da Coordenação

---

## 🚀 Como Usar Localmente

### Pré-requisitos
- Python 3.8+
- pip (gerenciador de pacotes Python)

### Instalação

```bash
# Clone ou baixe este repositório
cd Tech-ajuda

# Instale as dependências
pip install -r requirements.txt

# Execute a aplicação
streamlit run app.py
```

A aplicação abrirá em `http://localhost:8501`

---

## 📱 Como Fazer Deploy no Streamlit Cloud (RECOMENDADO PARA HACKATHON)

### Passo 1: Prepare o Repositório Git
```bash
git init
git add .
git commit -m "Inicial: App ESCUTA+"
```

### Passo 2: Suba para GitHub
1. Crie um repositório em [github.com](https://github.com/new)
2. Faça push do código:
```bash
git remote add origin https://github.com/SEU_USUARIO/tech-ajuda.git
git branch -M main
git push -u origin main
```

### Passo 3: Deploy no Streamlit Cloud
1. Acesse [share.streamlit.io](https://share.streamlit.io)
2. Clique em "New app"
3. Selecione seu repositório e branch `main`
4. Selecione `app.py` como arquivo principal
5. Clique em "Deploy"

**Seu link ficará assim:** `https://tech-ajuda-demo.streamlit.app`

---

## 📊 Dados Coletados

As denúncias são salvas automaticamente em `denuncias.csv` com:
- Timestamp (data/hora)
- Nome do usuário ou "Anônimo"
- Tipo de situação
- Local do acontecido
- Descrição detalhada

### Para Visualizar os Dados Localmente
```bash
python -c "import pandas as pd; print(pd.read_csv('denuncias.csv'))"
```

---

## ♿ Recursos de Acessibilidade

✅ **Visuais:**
- Fonts em 22px e títulos em 40px
- Contraste WCAG AA+
- Cores de alto contraste

✅ **Motoras:**
- Botões grandes (24px padding)
- Bordas focadas (outline 6px)
- Input fields espaçosos

✅ **Cognitivas:**
- Linguagem clara e simples
- Aviso de anonimato transparente
- Passo a passo visual

---

## 🔧 Configuração do WhatsApp

Para alterar o número de destino, edite em `app.py`:

```python
numero_destino = "558694231846"  # Adicione o código do país + número
```

Formato: `55` (Brasil) + DDD (86) + número (94231846) = `558694231846`

---

## 📝 Estrutura do Projeto

```
Tech-ajuda/
├── app.py                 # Aplicação principal Streamlit
├── requirements.txt       # Dependências Python
├── denuncias.csv         # Banco de dados de denúncias (gerado automaticamente)
├── README.md             # Este arquivo
└── .gitignore            # Arquivos ignorados no Git
```

---

## 🐛 Troubleshooting

### "Arquivo não encontrado" ao rodar
Certifique-se que está na pasta correta:
```bash
cd c:\Users\egmig\OneDrive\Desktop\Tech-ajuda
streamlit run app.py
```

### Erro ao salvar denúncias
Verifique se tem permissão de escrita na pasta

### Links do WhatsApp não funcionam
- Verifique se o número tem 12+ dígitos (código país + DDD + número)
- Teste em: `https://wa.me/558694231846`

---

## 🎓 For the Judges (Banca Avaliadora)

**Link de Produção:** [Será preenchido após deploy]

**Funcionalidades Implementadas:**
1. ✅ Login com identificação ou anonimato
2. ✅ Acolhimento educativo
3. ✅ Formulário acessível de denúncia
4. ✅ Envio por WhatsApp
5. ✅ Persistência de dados em CSV
6. ✅ Design acessível (WCAG)
7. ✅ Responsivo

**Como Testar:**
- Faça login (ou anônimo)
- Clique em "PEDIR AJUDA AGORA"
- Preencha o formulário
- Clique em "Confirmar e Enviar"
- Os dados são salvos localmente + link WhatsApp é gerado

---

## 📄 Licença

Este projeto foi desenvolvido para fins educacionais e de hackathon.

---

**Desenvolvido com ❤️ para o bem-estar dos alunos** 💙
