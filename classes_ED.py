from abc import ABC, abstractmethod
from collections.abc import Iterable
from typing import Optional

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
    
class Array(EstruturaLinear):
    def __init__(self, iterable=None):
        self._dados = []
        if iterable is not None:
            if not isinstance(iterable, Iterable):
                raise TypeError("O argumento deve ser iterável")
            self._dados = list(iterable)
    
    def __len__(self):
        return len(self._dados)
    
    def estrutura_vazia(self):
        return len(self) == 0
    
    def __getitem__(self, index):
        if index < 0 or index >= len(self):
            raise IndexError("Índice fora dos limites")
        return self._dados[index]
    
    def __setitem__(self, index, value):
        if index < 0 or index >= len(self):
            raise IndexError("Índice fora dos limites")
        self._dados[index] = value
    
    # Implementações dos métodos abstratos
    def inserir_topo(self, item):
        self._dados.insert(0, item)
    
    def inserir_ultimo(self, item):
        self._dados.append(item)
    
    def inserir_index(self, index, item):
        if index < 0 or index > len(self):
            raise IndexError("Índice fora dos limites")
        self._dados.insert(index, item)
    
    def remover_topo(self):
        if self.estrutura_vazia():
            raise IndexError("Underflow")
        return self._dados.pop(0)
    
    def remover_ultimo(self):
        if self.estrutura_vazia():
            raise IndexError("Underflow")
        return self._dados.pop()
    
    def remover_index(self, index):
        if index < 0 or index >= len(self):
            raise IndexError("Índice fora dos limites")
        return self._dados.pop(index)
    
    def obter_topo(self):
        if self.estrutura_vazia():
            raise IndexError("Underflow")
        return self._dados[0]
    
    def obter_ultimo(self):
        if self.estrutura_vazia():
            raise IndexError("Underflow")
        return self._dados[-1]
    
    def obter_index(self, index):
        return self[index]
    
    def atualizar_index(self, index, new_item):
        self[index] = new_item
    
    def trocar(self, i, j):
        if i < 0 or i >= len(self) or j < 0 or j >= len(self):
            raise IndexError("Índice fora dos limites")
        self._dados[i], self._dados[j] = self._dados[j], self._dados[i]
    
    def bubble_sort(self):
        n = len(self)
        for i in range(n):
            for j in range(0, n-i-1):
                if self._dados[j] > self._dados[j+1]:
                    self.trocar(j, j+1)


class NoSimples():
    __slots__ = ('dado', 'proximo')
    def __init__(self, dado):
        self.dado = dado
        self.proximo: Optional[NoSimples] = None

class ListaEncadeadaSimples(EstruturaLinear):
    def __init__(self, iterable=None):
        self.cabeca: Optional[NoSimples] = None
        self.tail: Optional[NoSimples] = None
        self._size = 0
        
        if iterable is not None:
            try:
                iterator = iter(iterable)
                for item in iterator:
                    self.inserir_ultimo(item)
            except TypeError:
                raise TypeError("O argumento deve ser iterável")
    
    def __len__(self):
        return self._size
    
    def estrutura_vazia(self):
        return self._size == 0
    
    def inserir_topo(self, item):
        novo_no = NoSimples(item)
        novo_no.proximo = self.cabeca
        self.cabeca = novo_no
        if self.tail is None:
            self.tail = novo_no
        self._size += 1
    
    def inserir_ultimo(self, item):
        novo_no = NoSimples(item)
        if self.tail is None:
            self.cabeca = self.tail = novo_no
        else:
            self.tail.proximo = novo_no
            self.tail = novo_no
        self._size += 1
    
    def inserir_index(self, index, item):
        if index < 0 or index > self._size:
            raise IndexError("Índice fora dos limites")
        
        if index == 0:
            self.inserir_topo(item)
            return
        elif index == self._size:
            self.inserir_ultimo(item)
            return
        
        current = self.cabeca
        for i in range(index - 1):
            if current is None:
                break
            current = current.proximo
            
        if current is None:
            raise IndexError("Posição inválida durante inserção")
            
        novo_no = NoSimples(item)
        novo_no.proximo = current.proximo
        current.proximo = novo_no
        self._size += 1
    
    def remover_topo(self):
        if self.estrutura_vazia():
            raise IndexError("Underflow")
        if self.cabeca is None:
            raise RuntimeError("Estado inválido")
            
        dado = self.cabeca.dado
        self.cabeca = self.cabeca.proximo
        if self.cabeca is None:
            self.tail = None
        self._size -= 1
        return dado
    
    def remover_ultimo(self):
        if self.estrutura_vazia():
            raise IndexError("Underflow")
            
        if self._size == 1:
            return self.remover_topo()
        
        current = self.cabeca
        while current and current.proximo != self.tail:
            current = current.proximo
            
        if current is None or self.tail is None:
            raise RuntimeError("Estado inválido")
        
        dado = self.tail.dado
        self.tail = current
        self.tail.proximo = None
        self._size -= 1
        return dado
    
    def remover_index(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Índice fora dos limites")
        
        if index == 0:
            return self.remover_topo()
        elif index == self._size - 1:
            return self.remover_ultimo()
        
        current = self.cabeca
        for i in range(index - 1):
            if current is None:
                break
            current = current.proximo
            
        if current is None or current.proximo is None:
            raise RuntimeError("Estado inválido")
            
        dado = current.proximo.dado
        current.proximo = current.proximo.proximo
        self._size -= 1
        return dado
    
    def obter_topo(self):
        if self.estrutura_vazia():
            raise IndexError("Underflow")
        if self.cabeca is None:
            raise RuntimeError("Estado inválido")
        return self.cabeca.dado
    
    def obter_ultimo(self):
        if self.estrutura_vazia():
            raise IndexError("Underflow")
        if self.tail is None:
            raise RuntimeError("Estado inválido")
        return self.tail.dado
    
    def obter_index(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Índice fora dos limites")
        
        current = self.cabeca
        for i in range(index):
            if current is None:
                break
            current = current.proximo
            
        if current is None:
            raise RuntimeError("Estado inválido")
            
        return current.dado
    
    def atualizar_index(self, index, new_item):
        if index < 0 or index >= self._size:
            raise IndexError("Índice fora dos limites")
        
        current = self.cabeca
        for i in range(index):
            if current is None:
                break
            current = current.proximo
            
        if current is None:
            raise RuntimeError("Estado inválido")
            
        current.dado = new_item
    
    def __iter__(self):
        current = self.cabeca
        while current:
            yield current.dado
            current = current.proximo
