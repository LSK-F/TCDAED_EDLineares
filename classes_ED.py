from abc import ABC, abstractmethod

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