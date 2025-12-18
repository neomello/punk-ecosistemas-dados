# ◈ Setup do Ambiente

> Este setup destina-se a operadores do ecossistema.  
> Não representa produto final nem interface pública.

---

## ◇ Pré-requisitos

| Stack | Versão Mínima | Comando |
|-------|---------------|---------|
| **JVM** | Java 17+ | `java -version` |
| **PY** | Python 3.10+ | `python --version` |
| **TS** | Node.js 18+ | `node --version` |

```bash
# Verificação rápida
java -version
python --version
node --version
```

---

## ◎ Setup Rápido

```bash
# Clone o repositório
git clone https://github.com/neomello/punk-ecosistemas-dados
cd punk-ecosistemas-dados

# Instale dependências por stack
./scripts/setup.sh

# Rode testes
./scripts/test.sh
```

---

## ⧉ Setup por Stack

### JVM (Java)

```bash
cd core
./gradlew build
```

### PY (Python)

```bash
cd research
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### TS (Node/TypeScript)

```bash
cd api
npm install
```

---

## ⬡ Variáveis de Ambiente

Copie o arquivo de exemplo:

```bash
cp .env.example .env
```

Variáveis obrigatórias:

| Variável | Descrição |
|----------|-----------|
| `THIRDWEB_CLIENT_ID` | Client ID do Thirdweb |
| `THIRDWEB_SECRET_KEY` | Secret key do Thirdweb |
| `MAILCHAIN_SECRET_KEY` | Secret key do Mailchain |

---

<sub>Ø((Ø))</sub>
