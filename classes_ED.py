from abc import ABC, abstractmethod
from collections.abc import Iterable

class EstruturaLinear(ABC):
    @abstractmethod
    def __len__(self):
        """Retorna o número de itens"""
        pass

    @abstractmethod
    def estrutura_vazia(self):
        """Verifica se a estrutura está vazia"""
        pass

    def estrutura_cheia(self):
        """Verifica se a estrutura está cheia"""
        return False

    @abstractmethod
    def inserir_topo(self, item):
        """Insere item no início da estrutura"""
        pass

    @abstractmethod
    def inserir_ultimo(self, item):
        """Insere item no final da estrutura"""
        pass

    def inserir_index(self, index, item):
        """Insere item na posição index"""
        pass

    def inserir_antes(self, key, item):
        """Insere antes do item com chave key"""
        pass

    def inserir_depois(self, key, item):
        """Insere depois do item com chave key"""
        pass

    def atualizar(self, key, new_item):
        """Atualiza item com chave key"""
        pass

    def atualizar_index(self, index, new_item):
        """Atualiza item na posição index"""
        pass
    def remover_topo(self):
        """Remove item do início da estrutura"""
        pass

    def remover_ultimo(self):
        """Remove item do final da estrutura"""
        pass

    def remover_index(self, index):
        """Remove item da posição index"""
        pass

    def remover_chave(self, key):
        """Remove item com chave key"""
        pass

    def obter_topo(self):
        """Retorna primeiro item sem remover"""
        pass

    def obter_ultimo(self):
        """Retorna último item sem remover"""
        pass

    def obter_index(self, index):
        """Retorna item na posição index"""
        pass

    def obter_chave(self, key):
        """Busca item por chave"""
        pass

    def obter_proximo_chave(self, key):
        """Busca próximo item após chave"""
        pass
    
    def trocar(self, i, j):
        """Troca itens nas posições i e j"""
        pass
    
    def bubble_sort(self):
        """Ordena estrutura com bubble sort"""
        pass


class Pilha(EstruturaLinear):
    def __init__(self, iterable=None):
        self._dados = []
        if iterable is not None:
            if not isinstance(iterable, Iterable):
                raise TypeError("O argumento deve ser iterável")
            for item in iterable:
                self.push(item)
    
    def __len__(self):
        return len(self._dados)
    
    def estrutura_vazia(self):
        return len(self) == 0
    
    def push(self, item):
        """Insere um item no topo da pilha"""
        self._dados.append(item)
    
    def pop(self):
        """Remove e retorna o item do topo da pilha"""
        if self.estrutura_vazia():
            raise IndexError("Stack underflow")
        return self._dados.pop()
    
    def top(self):
        """Retorna o item do topo sem remover"""
        if self.estrutura_vazia():
            raise IndexError("Stack underflow")
        return self._dados[-1]
    
    # Implementações dos métodos abstratos
    def inserir_topo(self, item):
        raise NotImplementedError("Inserção no início não é suportada em Pilhas")
    
    def inserir_ultimo(self, item):
        self.push(item)
    
    def remover_ultimo(self):
        return self.pop()
    
    def obter_ultimo(self):
        return self.top()
    
class Fila(EstruturaLinear):
    def __init__(self, iterable=None):
        self._dados = []
        if iterable is not None:
            if not isinstance(iterable, Iterable):
                raise TypeError("O argumento deve ser iterável")
            for item in iterable:
                self.enqueue(item)
    
    def __len__(self):
        return len(self._dados)
    
    def estrutura_vazia(self):
        return len(self) == 0
    
    def enqueue(self, item):
        """Insere um item no final da fila"""
        self._dados.append(item)
    
    def dequeue(self):
        """Remove e retorna o item do início da fila"""
        if self.estrutura_vazia():
            raise IndexError("Queue underflow")
        return self._dados.pop(0)
    
    def front(self):
        """Retorna o item do início sem remover"""
        if self.estrutura_vazia():
            raise IndexError("Queue underflow")
        return self._dados[0]
    
    # Implementações dos métodos abstratos
    
    def inserir_ultimo(self, item):
        self.enqueue(item)
    
    def remover_topo(self):
        return self.dequeue()
    
    def obter_topo(self):
        return self.front()
    
    def obter_ultimo(self):
        if self.estrutura_vazia():
            raise IndexError("Queue underflow")
        return self._dados[-1]