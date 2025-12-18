# Contracts

## O Centro do Sistema

Este diretório é o **tratado de paz entre reinos**.

Aqui vivem os contratos que todas as stacks obedecem.
Linguagens mudam. Contratos permanecem.

## Estrutura

```
contracts/
├── intents/          # Definições de intenções
├── events/           # Schemas de eventos
├── permissions/      # Regras de acesso
├── schemas/          # Tipos compartilhados
└── boundaries/       # Fronteiras de domínio
```

## Regra Fundamental

> Núcleos falam por contrato, não por framework.

O que as stacks **compartilham**:
- Eventos
- Mensagens
- IDs
- Hashes
- Wallets

O que as stacks **NÃO compartilham**:
- Banco direto
- Models internos
- Lógica oculta

## Distribuição por Stack

| Stack | Função | Núcleos |
|-------|--------|---------|
| Java | Domínios estáveis, governança | core/, domains/, governance/ |
| Node/TS | APIs de borda, Thirdweb, MCP | api/, identity-access/, infrastructure/mcp/ |
| Python | Coleta, NLP, análise, agentes | ingestion/, intelligence/, agents/ |
| Rust/Go | Serviços críticos (futuro) | performance, security |

---

Author: MELLØ // POST-HUMAN

