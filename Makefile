# ══════════════════════════════════════════════════════════════════════════════
# PUNK ECOSISTEMAS - MAKEFILE
# ══════════════════════════════════════════════════════════════════════════════
# Comandos de conveniência para desenvolvimento
# Uso: make <comando>
# ══════════════════════════════════════════════════════════════════════════════

.PHONY: help setup start stop clean logs db-shell redis-shell ai

# Cores
CYAN := \033[36m
GREEN := \033[32m
YELLOW := \033[33m
RESET := \033[0m

help: ## Mostra esta ajuda
	@echo "$(CYAN)╔══════════════════════════════════════════════════════════════╗$(RESET)"
	@echo "$(CYAN)║           PUNK ECOSISTEMAS - COMANDOS                        ║$(RESET)"
	@echo "$(CYAN)╚══════════════════════════════════════════════════════════════╝$(RESET)"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "$(GREEN)%-15s$(RESET) %s\n", $$1, $$2}'

# ─────────────────────────────────────────────────────────────────────────────
# SETUP
# ─────────────────────────────────────────────────────────────────────────────

setup: ## Configura ambiente inicial
	@echo "$(YELLOW)Criando .env a partir do template...$(RESET)"
	@cp -n .env.example .env 2>/dev/null || echo ".env já existe"
	@echo "$(GREEN)Setup completo!$(RESET)"

# ─────────────────────────────────────────────────────────────────────────────
# DOCKER
# ─────────────────────────────────────────────────────────────────────────────

start: ## Inicia containers (postgres + redis)
	@echo "$(YELLOW)Iniciando serviços...$(RESET)"
	docker-compose up -d postgres redis
	@echo "$(GREEN)Serviços rodando!$(RESET)"

start-all: ## Inicia todos os containers (incluindo tools)
	docker-compose --profile tools up -d

start-ai: ## Inicia containers com Ollama
	docker-compose --profile ai up -d

stop: ## Para todos os containers
	docker-compose down

clean: ## Remove containers e volumes
	docker-compose down -v
	@echo "$(GREEN)Containers e volumes removidos$(RESET)"

logs: ## Mostra logs dos containers
	docker-compose logs -f

# ─────────────────────────────────────────────────────────────────────────────
# SHELLS
# ─────────────────────────────────────────────────────────────────────────────

db-shell: ## Acessa shell do PostgreSQL
	docker exec -it punk-postgres psql -U punk -d punk_ecosistemas

redis-shell: ## Acessa shell do Redis
	docker exec -it punk-redis redis-cli

# ─────────────────────────────────────────────────────────────────────────────
# STATUS
# ─────────────────────────────────────────────────────────────────────────────

status: ## Mostra status dos containers
	docker-compose ps

health: ## Verifica saúde dos serviços
	@echo "$(CYAN)PostgreSQL:$(RESET)"
	@docker exec punk-postgres pg_isready -U punk -d punk_ecosistemas 2>/dev/null && echo "$(GREEN)OK$(RESET)" || echo "$(YELLOW)Offline$(RESET)"
	@echo "$(CYAN)Redis:$(RESET)"
	@docker exec punk-redis redis-cli ping 2>/dev/null && echo "$(GREEN)OK$(RESET)" || echo "$(YELLOW)Offline$(RESET)"

