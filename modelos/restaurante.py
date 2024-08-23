from modelos.avaliacao import Avaliacao

class Restaurante:
    # Lista que armazena todos os restaurantes cadastrados
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title() # Nome do restaurante, formatado com a primeira letra maiúscula
        self._categoria = categoria.upper() # Categoria do restaurante, formatada em letras maiúsculas
        self._ativo = False # Estado inicial do restaurante, definido como inativo
        self._avaliacao = [] # Lista que armazena  as avaliações do restaurante 
        Restaurante.restaurante.append(self) # Adiciona o restaurante à lista global de restaurantes

    def __str__(self):
        # Retorna uma representaçãp textual do restaurante, mostrado o nome e categoria
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        # Exibe a lista de todos os restaurantes cadastrados
        print(" ")
        print(f"{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}")
        for restaurante in cls.restaurantes:
            print(f"{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}")
    
    @property
    def ativo(self):
        # Retorna m símbolo visual representando se o restaurante está ativo ou inativo
        return '⌧' if self._ativo else '☐'
    
    def alternar_estado(self):
       # Alterna o estado do restaurante de ativo e inativo
       self._ativo = not self._ativo
    
    def receber_avaliacao(self, cliente, nota):
        # Adiciona uma nova atualização ao restaurante, desde que a nota esteja entre 0 e 10
        if 0 <= nota <= 10:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
        else:
            print("A nota deve estar entro 0 e 10.")

    @property
    def media_avaliacoes(self):
        # Calcula e retorna a média das avaliações do restaurante
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao) 
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media
