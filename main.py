# main.py
from fila import FilaCircular

def exibir_menu():
   
    print("\n---------- MENU - Fila Circular ----------")
    print("1. Inserir no fim da fila")
    print("2. Remover do início da fila")
    print("3. Consultar o início da fila")
    print("4. Verificar se a fila está vazia")
    print("5. Verificar se a fila está cheia")
    print("0. Sair do programa")
    print("----------------------------------------")

def main():
    """Função principal que executa o programa interativo."""
    
    # Pergunta ao usuário a capacidade da fila
    while True:
        try:
            capacidade = int(input("Primeiro, defina a capacidade da fila: "))
            if capacidade > 0:
                break
            else:
                print("Erro: A capacidade deve ser um número positivo.")
        except ValueError:
            print("Erro: Por favor, digite um número inteiro válido.")

    # Cria a instância da Fila Circular
    fila = FilaCircular(capacidade)
    
    # Loop principal do menu
    while True:
        # Mostra o estado atual da fila e o menu de opções
        print(f"\nEstado atual -> {fila}")
        exibir_menu()
        
        escolha = input("Escolha uma opção: ")

        if escolha == '1': # Inserir no fim da fila [cite: 7]
            try:
                valor = int(input("Digite o número inteiro para inserir: "))
                fila.enfileirar(valor)
            except ValueError:
                print("Erro: Entrada inválida. Por favor, digite um número.")

        elif escolha == '2': # Remover do início da fila [cite: 8]
            fila.desenfileirar()

        elif escolha == '3': # Consultar o início da fila [cite: 9]
            item = fila.consultar_inicio()
            if item is not None:
                print(f"Resultado da consulta: O item no início é {item}.")

        elif escolha == '4': # Indicar se a fila está vazia [cite: 10]
            if fila.esta_vazia():
                print("Resultado: Sim, a fila está vazia.")
            else:
                print("Resultado: Não, a fila contém elementos.")

        elif escolha == '5': # Indicar se a fila está cheia [cite: 11]
            if fila.esta_cheia():
                print("Resultado: Sim, a fila está cheia.")
            else:
                print("Resultado: Não, a fila não atingiu a capacidade máxima.")
        
        elif escolha == '0':
            print("Encerrando o programa. Até logo!")
            break
        
        else:
            print("Opção inválida! Por favor, escolha um número do menu.")

# Ponto de entrada do programa
if __name__ == "__main__":

    main()
