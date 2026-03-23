# 🚀 GUIA RÁPIDO: DEPLOY NO STREAMLIT CLOUD (5 MINUTOS)

## O que você precisa:
- ✅ Conta GitHub (grátis em github.com)
- ✅ Conta Streamlit (conecta com GitHub)
- ✅ Este projeto em um repositório público

---

## PASSO 1: Preparar o Projeto (2 min)

### 1a) Abra PowerShell na pasta do projeto
```powershell
cd c:\Users\egmig\OneDrive\Desktop\Tech-ajuda
```

### 1b) Inicialize Git e faça commit
```powershell
git config --global user.email "seu-email@gmail.com"
git config --global user.name "Seu Nome"

git init
git add .
git commit -m "Initial commit: ESCUTA+ app"
```

**Se der erro "git not found":** Baixe em https://git-scm.com

---

## PASSO 2: Suba para GitHub (2 min)

### 2a) Crie um repositório vazio no GitHub
1. Acesse https://github.com/new
2. Digite `tech-ajuda` como nome
3. Deixe **público** (IMPORTANTE!)
4. Clique em "Create repository"

### 2b) Conecte seu Git local com GitHub
```powershell
git remote add origin https://github.com/SEU_USUARIO/tech-ajuda.git
git branch -M main
git push -u origin main
```

**Se pedir senha:** Use seu token de acesso do GitHub (não a senha da conta)
- Gere em: https://github.com/settings/tokens

---

## PASSO 3: Deploy no Streamlit Cloud (1 min)

### 3a) Acesse Streamlit
1. Vá para https://share.streamlit.io
2. Clique em **"Sign in with GitHub"**
3. Autorize a aplicação

### 3b) Crie novo app
1. Clique em **"New app"**
2. Preencha:
   - **Repository:** `SEU_USUARIO/tech-ajuda`
   - **Branch:** `main`
   - **Main file path:** `app.py`
3. Clique em **"Deploy"**

**Seu link será:** `https://tech-ajuda-<código>.streamlit.app`

---

## ✅ Pronto!

Seu app está ao vivo! Você pode:
- ✅ Compartilhar o link com a banca
- ✅ Apresentar ao vivo durante o hackathon
- ✅ Os dados são salvos na nuvem automaticamente

---

## 🔄 Atualizar o App

Se precisar fazer mudanças:

```powershell
# Faça as edições em app.py
# Depois:

git add .
git commit -m "Descrição da mudança"
git push origin main

# O Streamlit detecta e redeploy automaticamente em 30 segundos
```

---

## 💡 Dicas Importantes

1. **Link para a banca:** Copie de `https://share.streamlit.io/deployments`
2. **Mudar número WhatsApp:** Edite em `app.py` linha ~25
3. **Ver denúncias salvas:** Baixe `denuncias.csv` do repositório
4. **Problema de permissões Git:** Use SSH key ou token em vez de senha

---

## 🆘 Troubleshooting Rápido

| Erro | Solução |
|------|---------|
| "Repository not found" | Verifique se é público (GitHub > Repo > Settings > Visibility: Public) |
| "Main file path not found" | Certifique-se que `app.py` está na raiz do repositório |
| "Erro na linha X do app.py" | Verifique se all imports estão em `requirements.txt` |
| "App branco/em branco" | Clique em "Logs" no Streamlit Cloud para ver erro |

---

**Você está pronto para apresentar! 🎉**
