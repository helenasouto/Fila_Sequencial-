# fila.py

class FilaCircular:
    """
    Implementa a estrutura de Fila sobre um vetor (lista) utilizando
    a técnica de incremento circular.
    """
    def __init__(self, capacidade: int):
        self.capacidade = capacidade
        self.fila = [None] * capacidade
        self.inicio = -1
        self.fim = -1
        self.tamanho_atual = 0

    def esta_vazia(self) -> bool:
        return self.tamanho_atual == 0

    def esta_cheia(self) -> bool:
        return self.tamanho_atual == self.capacidade

    def enfileirar(self, valor: int):
        if self.esta_cheia():
            print("Erro: A fila está cheia!")
            return
        self.fim = (self.fim + 1) % self.capacidade
        self.fila[self.fim] = valor
        self.tamanho_atual += 1
        if self.inicio == -1:
            self.inicio = self.fim
        print(f"-> Item '{valor}' inserido na fila.")

    def desenfileirar(self) -> int | None:
        if self.esta_vazia():
            print("Erro: A fila está vazia!")
            return None
        item_removido = self.fila[self.inicio]
        self.tamanho_atual -= 1
        if self.esta_vazia():
            self.inicio = -1
            self.fim = -1
        else:
            self.inicio = (self.inicio + 1) % self.capacidade
        print(f"<- Item '{item_removido}' removido da fila.")
        return item_removido

    def consultar_inicio(self) -> int | None:
        if self.esta_vazia():
            print("A fila está vazia, não há o que consultar.")
            return None
        return self.fila[self.inicio]
    
    def __str__(self) -> str:
        if self.esta_vazia():
            return "Fila: [] (vazia)"
        elementos = []
        i = self.inicio
        for _ in range(self.tamanho_atual):
            elementos.append(str(self.fila[i]))
            i = (i + 1) % self.capacidade
        return f"Fila: [{' <- '.join(elementos)}]"