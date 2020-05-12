from atleta import Atleta

class lutadorMMA(Atleta):
    def __init__(self,nome,idade,categoria_de_peso,cinturoes_disputados):
        super().__init__(nome,idade)
        self.categoria_de_peso = categoria_de_peso
        self.cinturoes_disputados = cinturoes_disputados

    def faz_o_que(self):
         return f'O {self.nome} é um lutador de MMA na categoria {self.categoria_de_peso} e já disputou {self.cinturoes_disputados} cinturões!!'