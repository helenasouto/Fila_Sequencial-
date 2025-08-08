# Define o interpretador Python a ser usado. Use python3 ou python, conforme sua necessidade.
PYTHON = python3

# O alvo padrão que será executado se você digitar apenas "make"
.DEFAULT_GOAL := help

# Phony targets são alvos que não representam arquivos.
.PHONY: all run clean test help

# Alvo "all", que por padrão executa o programa.
all: run

# Alvo para executar o programa principal.
# Corresponde a "criar um arquivo main para poder testar as seguintes operações" [cite: 6]
run:
	@echo "Executando o programa principal..."
	@$(PYTHON) main.py

# Alvo para limpar arquivos temporários do Python.
clean:
	@echo "Limpando arquivos temporários (.pyc, __pycache__)..."
	@find . -type f -name "*.pyc" -delete
	@find . -type d -name "__pycache__" -exec rm -r {} +
	@echo "Limpeza concluída."

# Alvo para rodar os testes.
# Neste caso, "testar" é executar o programa interativo, conforme a necessidade de "casos de teste" [cite: 16]
test:
	@echo "Iniciando modo de teste interativo..."
	@$(PYTHON) main.py

# Alvo "help" para exibir uma lista de todos os comandos disponíveis.
help:
	@echo "Comandos disponíveis no Makefile:"
	@echo "  make run    -> Executa o programa principal (main.py)"
	@echo "  make test   -> Inicia o programa em modo de teste interativo"
	@echo "  make clean  -> Remove arquivos temporários do Python"
	@echo "  make help   -> Mostra esta mensagem de ajuda"