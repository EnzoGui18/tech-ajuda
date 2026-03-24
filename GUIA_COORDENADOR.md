# 🔐 PAINEL DO COORDENADOR - GUIA DE USO

## O que mudou?

O ESCUTA+ agora possui um **painel exclusivo para coordenadores** que mostra **TODAS as denúncias em tempo real**, sem depender de WhatsApp!

---

## 🚀 Como Usar na Escola

### 1️⃣ **Tela Inicial - Escolher Acesso**

```
[💙 Bem-vindo ao ESCUTA+]

[➡️ Entrar no Aplicativo] [🔐 Sou Coordenador]
```

### 2️⃣ **Se clicar "Sou Coordenador"**

```
[🔐 Acesso Coordenador]
Senha: [_____________]
[🔓 Entrar]
```

**Senha padrão:** `escuta123`  
*(Mudar em `app.py` linha ~30)*

### 3️⃣ **Dashboard em Tempo Real**

Após login, coordenador vê:

```
📊 PAINEL DO COORDENADOR - ESCUTA+
🔄 Atualiza automaticamente a cada 5 segundos

📈 Estatísticas
┌──────────────┬──────────────┬──────────────┬──────────────┐
│ Total        │ 🚨 Bullying  │ 🎓 Racismo   │ 💙 Sofrimento│
│    5         │      2       │      1       │      2       │
└──────────────┴──────────────┴──────────────┴──────────────┘

🔔 DENÚNCIAS RECENTES

[#20260323140000 - Bullying - 2026-03-23 14:00:00] ▼
   Aluno: Lucas (Matrícula: 2024003)
   Tipo: Bullying
   Local: Quadra de Esportes
   Anônimo? ❌ Não
   ⏰ 2026-03-23 14:00:00
   
   Descrição:
   Excluem-me do time nas aulas de educação física. Ficam rindo de mim
   
   [✅ Marcar como Acompanhado]

[📥 Exportar Relatório] [🔄 Atualizar]
```

---

## ✨ Funcionalidades

### 🔄 **Atualização Automática**
- Dashboard RECARREGA a cada 5 segundos
- Novos denúncias aparecem na hora
- Não precisa sair e entrar de novo

### 📊 **Estatísticas Visuais**
- Total de denúncias
- Contagem por tipo (Bullying, Racismo, Assédio, Sofrimento)
- Últimas 10 denúncias em destaque

### 📋 **Informações Completas**
Cada denúncia mostra:
- ✅ ID único e timestamp
- ✅ Nome do aluno (ou "Anônimo")
- ✅ Tipo de situação (categorizado automaticamente)
- ✅ Onde aconteceu
- ✅ Se é anônimo ou não
- ✅ Descrição completa

### ✅ **Marcar como Acompanhado**
Coordenador pode confirmar que viu e está tratando

### 📥 **Exportar Relatório**
Download em JSON com todos os dados para análise posterior

---

## 🎯 Fluxo Completo (Do Zero)

```
┌─────────────────────────────────────────────────────────┐
│  ALUNO                          COORDENADOR              │
│                                                          │
│  [Abre app]                                             │
│  ├─ [Clica "Pedir Ajuda"]                              │
│  ├─ [Preenche formulário]                              │
│  └─ [Envia...]                                          │
│        ↓                                                 │
│        ├─ Salva em denuncias.json                       │
│        ├─ CSV também atualizado                         │
│        └─ Mostra confirmação                            │
│                                                          │
│                              ← Dashboard recarrega →    │
│                              ← Vê nova denúncia aqui →  │
│                              ← Clica "Acompanhado" →    │
│                                                          │
│                          [RESOLUÇÃO LOCAL]              │
│                          Coordenador fala com aluno,   │
│                          registra ação, segue adiante  │
└─────────────────────────────────────────────────────────┘
```

---

## 🔧 Configurações Importantes

### **Alterar Senha**

Abra `app.py` e procure por:

```python
SENHA_COORDENADOR = "escuta123"  # ← Mudar para sua senha
```

Exemplo: `SENHA_COORDENADOR = "escola2024"`

---

### **Dados Persistentes**

Os dados são salvos em:
- `denuncias.json` - Formato JSON (usado pelo dashboard)
- `denuncias.csv` - Formato CSV (compatibilidade)

Ambos são atualizados automaticamente.

---

## 📱 Para Usar nos Computadores da Escola

### **Opção 1: Computadores na Biblioteca/Lab**

```
1. Abrir Chrome/Firefox → http://localhost:8501
2. App Streamlit abre automaticamente
3. Alunos usam normalmente
4. Coordenador tem acesso 24/7 no mesmo lab
```

### **Opção 2: Máquina Online (Melhor)**

```
1. Deploy no Streamlit Cloud (https://share.streamlit.io)
2. Link fica: https://tech-ajuda-xyz.streamlit.app
3. Alunos acessam de qualquer navegador na escola
4. Coordenador acessa em qualquer computador com internet
5. Dashboard sempre atualizado
```

---

## 🎓 Dados de Teste

Já incluímos 5 denúncias de exemplo em `denuncias.json`.

Para **LIMPAR tudo e começar do zero**:

```powershell
# Apague os arquivos:
# - denuncias.json
# - denuncias.csv

# Reinicie o app
streamlit run app.py
```

---

## 🆘 Troubleshooting

| Problema | Solução |
|----------|---------|
| "Senha incorreta" | Verifique se a senha em `app.py` está correta |
| Dashboard não atualiza | Recarregue a página (F5) ou aguarde 5s |
| Denúncias desaparecem | Nunca delete `denuncias.json` ou `denuncias.csv` |
| Total errado | Verifique `denuncias.json` - pode ter duplicatas |

---

## 🔐 Segurança

⚠️ **IMPORTANTE PARA PRODUÇÃO:**

```python
# MUDAR A SENHA PADRÃO!
SENHA_COORDENADOR = "escuta123"  ← Não use isso na sua escola!

# Use algo mais seguro:
SENHA_COORDENADOR = "Edu@Solidaria2026#Escola123"
```

---

## 📞 Suporte

Se tiver dúvidas sobre como usar o painel:

1. Verifique se o arquivo `denuncias.json` existe
2. Confirme a senha em `app.py`
3. Reinicie o app com `streamlit run app.py`
4. Recarregue o navegador

---

**Sistema desenvolvido com ❤️ para proteção dos alunos** 💙
