class Avaliacao:
    def __int__(self, cliente, nota):
        self._cliente = cliente # Nome do cliente que fez a avaliação
        self._nota = nota # Nota dada pelo cliente
    
    # Método para converter o objeto em um dicionário para salvar em JSON
    def __dict__(self):
        return {
            'cliente' : self._cliente,
            'nota' : self._nota
        }