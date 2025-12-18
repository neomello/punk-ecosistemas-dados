# ◈ Descoberta do Ecossistema

> Perguntas estruturais que revelam conexões.  
> Cada resposta aponta para onde o sistema age.

---

## ⟁ Identidade

### Quem é essa empresa no mundo digital?

| Dimensão | Fonte | Núcleo |
|----------|-------|--------|
| Razão Social, CNPJ, sócios | Receita Federal | `domains/identity/` |
| Presença web, domínios | DNS, WHOIS | `domains/webPresence/` |
| Perfis sociais verificados | Instagram, LinkedIn | `domains/socialPresence/` |

**Conexão**: Os dados de identidade alimentam o `research/` que normaliza via `ingestion/` e persiste em `domains/`.

---

### Onde ela existe?

| Camada | Manifestação | Rastreamento |
|--------|--------------|--------------|
| Física | Unidades, endereços | `domains/identity/` |
| Digital | Sites, apps, landing pages | `domains/webPresence/` |
| Social | Perfis, menções, hashtags | `domains/socialPresence/` |
| Reputacional | Reviews, scores, sentimento | `domains/reputation/` |

**Conexão**: Cada camada de existência é um território em `domains/` com schemas definidos em `contracts/schemas/`.

---

## ◎ Comportamento

### Como ela se comporta?

| Padrão | Sinal | Análise |
|--------|-------|---------|
| Frequência de posts | Regularidade, horários | `intelligence/patterns/` |
| Tom de comunicação | NLP, sentiment | `intelligence/correlation/` |
| Resposta a menções | Tempo, qualidade | `intelligence/alerts/` |
| Campanhas ativas | CTAs, promoções | `intelligence/opportunities/` |

**Conexão**: Comportamento é inferido pelo `intelligence/` a partir de sinais coletados pelo `ingestion/`.

---

### Que sinais emite?

| Tipo | Exemplo | Collector |
|------|---------|-----------|
| Estruturado | Posts com métricas | `ingestion/social/` |
| Semi-estruturado | Reviews, comentários | `ingestion/web/` |
| Não-estruturado | Menções indiretas | `research/` |
| Metadata | Timestamps, geolocation | `ingestion/schedulers/` |

**Conexão**: Sinais brutos passam por `contracts/events/signal-collected.yaml` antes de virar dados estruturados.

---

## ⧉ Diagnóstico

### Onde há força?

| Indicador | Métrica | Visualização |
|-----------|---------|--------------|
| Engajamento alto | Likes/Followers ratio | `visualization/` |
| Autoridade de domínio | Backlinks, DA/PA | `intelligence/patterns/` |
| Comunidade ativa | Comentários orgânicos | `intelligence/narratives/` |
| Consistência | Frequência sem gaps | `intelligence/correlation/` |

**Conexão**: Força é um insight gerado via `contracts/events/insight-generated.yaml` e surfado pelo `visualization/`.

---

### Onde há ruído?

| Sintoma | Causa Provável | Mitigação |
|---------|----------------|-----------|
| Menções negativas | Atendimento, expectativa | `intelligence/risks/` |
| Inconsistência de marca | Multi-operador | `governance/audit/` |
| Bots, spam | Perfil público | `intelligence/alerts/` |

**Conexão**: Ruído é filtrado pelo `intelligence/` e pode disparar `agents/` para ação automatizada.

---

### Onde há silêncio?

| Gap | Implicação | Oportunidade |
|-----|------------|--------------|
| Zero presença em plataforma | Mercado inexplorado | `intelligence/opportunities/` |
| Sem reviews recentes | Percepção estagnada | `agents/` → ação |
| Domínio sem conteúdo | SEO perdido | `visualization/` → relatório |

**Conexão**: Silêncio é ausência de sinal — detectado por comparação com `domains/ecosystem/` (concorrentes, mercado).

---

## ⬡ Evolução

### O que pode ser automatizado?

| Processo | Gatilho | Executor |
|----------|---------|----------|
| Coleta periódica | Schedule | `ingestion/schedulers/` |
| Alertas de anomalia | Threshold | `agents/` |
| Relatórios recorrentes | Cron | `visualization/exporters/` |
| Notificações | Event | `infrastructure/messaging/` |

**Conexão**: Automação é orquestrada pelo MCP Layer (`infrastructure/mcp/`) que roteia intents definidos em `contracts/intents/`.

---

### O que pode ser tokenizado?

| Ativo | Valor | Mecanismo |
|-------|-------|-----------|
| Acesso a dashboards | Exclusividade | `identity-access/gating/` |
| Insights premium | Informação | `governance/tokenization/` |
| Governança de agentes | Decisão | `governance/permissions/` |
| Histórico auditável | Prova | `governance/audit/` |

**Conexão**: Tokenização é camada de governança via `identity-access/` integrado com Thirdweb.

---

### O que pode ser otimizado?

| Dimensão | Métrica | Ação |
|----------|---------|------|
| Latência de coleta | ms/request | `ingestion/` tuning |
| Precisão de insights | accuracy score | `intelligence/` training |
| Custo de operação | $/signal | `agents/` scope limiting |
| Experiência do operador | time-to-insight | `visualization/` UX |

**Conexão**: Otimização é ciclo contínuo — métricas em `governance/audit/`, decisões em `agents/`.

---

## ◇ Persistência

### Como isso evolui ao longo do tempo?

| Fase | Foco | Núcleos Ativos |
|------|------|----------------|
| ◇ Pesquisa | Coleta manual, validação | `research/` `ingestion/` |
| ◈ Dashboards | Visualização, padrões | `intelligence/` `visualization/` |
| ⧉ Automação | Workflows, schedulers | `agents/` `infrastructure/` |
| ⬡ Agentes | Decisões autônomas | `agents/` `core/` |
| ◎ Tokenização | Valor programável | `identity-access/` `governance/` |
| ⬢ Governança | Soberania total | `governance/` `contracts/` |

**Conexão**: Cada fase adiciona camadas sem invalidar anteriores. Contratos em `contracts/` garantem compatibilidade.

---

### Quais padrões persistem?

| Padrão | Evidência | Confiança |
|--------|-----------|-----------|
| Engajamento sazonal | 12+ meses de dados | Alta |
| Horário de pico | Consistência cross-plataforma | Alta |
| Tom de marca | NLP estável | Média |
| Crescimento orgânico | Tendência sem ads | Variável |

**Conexão**: Padrões persistentes viram `intelligence/narratives/` — histórias que o dado conta.

---

### Quais são ruído momentâneo?

| Sinal | Duração | Tratamento |
|-------|---------|------------|
| Viral inesperado | < 72h | Observar, não reagir |
| Crise pontual | < 7d | `agents/` alerta, humano decide |
| Trend de plataforma | < 30d | Registrar, não adaptar |

**Conexão**: Ruído é filtrado pelo `intelligence/` via decay functions. Só padrões estáveis viram insight.

---

## ⦿ Mapa de Conexões

```
Pergunta → Resposta → Núcleo → Contrato → Ação
    │         │          │         │         │
    └─────────┴──────────┴─────────┴─────────┘
              Ciclo de Descoberta
```

Cada pergunta respondida revela:
1. **Onde** o dado existe (`domains/`)
2. **Como** é coletado (`ingestion/` `research/`)
3. **O que** significa (`intelligence/`)
4. **Quem** age sobre (`agents/`)
5. **Por que** é governado (`governance/` `contracts/`)

---

<sub>Ø((Ø))</sub>
