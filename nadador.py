from atleta import Atleta

class nadador(Atleta):
    def __init__(self,nome,idade,numero_de_medalhas,numero_olimpiadas_disputadas):
        super().__init__(nome,idade)
        self.numero_de_medalhas = numero_de_medalhas
        self.numero_olimpiadas_disputadas = numero_olimpiadas_disputadas

    def faz_o_que(self):
         return f'O {self.nome} é um competidor de natação e já ganhou {self.numero_de_medalhas} medalhas em {self.numero_olimpiadas_disputadas} olimpíadas!!'