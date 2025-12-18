# ◈ Checklist de Configuração

> Marque com `[x]` conforme preencher no `.env`

---

## ◇ Thirdweb (Identity-Access)

| Variável | Status | Onde Obter |
|----------|--------|------------|
| `THIRDWEB_CLIENT_ID` | [ ] | [thirdweb.com/dashboard](https://thirdweb.com/dashboard) |
| `THIRDWEB_SECRET_KEY` | [ ] | [thirdweb.com/dashboard](https://thirdweb.com/dashboard) |

---

## ◈ Blockchain

| Variável | Status | Notas |
|----------|--------|-------|
| `CHAIN_ID` | [x] | Default: 1 (Ethereum Mainnet) |
| `RPC_URL` | [ ] | Alchemy, Infura ou público |
| `WALLET_PRIVATE_KEY` | [ ] | Wallet de operação (não principal!) |

---

## ⧉ Social APIs (Ingestion)

| Variável | Status | Onde Obter |
|----------|--------|------------|
| `INSTAGRAM_ACCESS_TOKEN` | [ ] | [Meta for Developers](https://developers.facebook.com/) |
| `LINKEDIN_CLIENT_ID` | [ ] | [LinkedIn Developers](https://www.linkedin.com/developers/) |
| `LINKEDIN_CLIENT_SECRET` | [ ] | [LinkedIn Developers](https://www.linkedin.com/developers/) |
| `TWITTER_API_KEY` | [ ] | [Twitter Developer Portal](https://developer.twitter.com/) |
| `TWITTER_API_SECRET` | [ ] | [Twitter Developer Portal](https://developer.twitter.com/) |

---

## ◎ Search APIs (Ingestion)

| Variável | Status | Onde Obter |
|----------|--------|------------|
| `GOOGLE_API_KEY` | [ ] | [Google Cloud Console](https://console.cloud.google.com/) |
| `GOOGLE_SEARCH_ENGINE_ID` | [ ] | [Programmable Search](https://programmablesearchengine.google.com/) |
| `SERPER_API_KEY` | [ ] | [serper.dev](https://serper.dev/) |

---

## ⬡ AI / LLM (Intelligence)

| Variável | Status | Onde Obter |
|----------|--------|------------|
| `OPENAI_API_KEY` | [ ] | [platform.openai.com](https://platform.openai.com/) |
| `ANTHROPIC_API_KEY` | [ ] | [console.anthropic.com](https://console.anthropic.com/) |
| `OLLAMA_BASE_URL` | [x] | Default: localhost:11434 |

---

## ⬢ Feature Flags

| Flag | Status | Descrição |
|------|--------|-----------|
| `FEATURE_AGENTS_ENABLED` | [x] | false (Fase 4) |
| `FEATURE_TOKENIZATION_ENABLED` | [x] | false (Fase 5) |
| `FEATURE_MCP_ENABLED` | [x] | true |

---

## ◇ Prioridade de Configuração

### Fase 1 (Pesquisa)
1. [ ] `GOOGLE_API_KEY` ou `SERPER_API_KEY`
2. [ ] `INSTAGRAM_ACCESS_TOKEN` (opcional)

### Fase 2 (Dashboards)
- Nenhuma variável adicional

### Fase 3 (Automação)
1. [ ] APIs de Social completas
2. [ ] `OPENAI_API_KEY` ou `ANTHROPIC_API_KEY`

### Fase 4+ (Agentes/Tokenização)
1. [ ] `THIRDWEB_CLIENT_ID`
2. [ ] `THIRDWEB_SECRET_KEY`
3. [ ] `RPC_URL`
4. [ ] `WALLET_PRIVATE_KEY`

---

<sub>Ø((Ø))</sub>
