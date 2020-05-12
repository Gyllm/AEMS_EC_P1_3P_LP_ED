from atleta import Atleta

class futebolista(Atleta):
    def __init__(self,nome,idade,gols_marcados):
        super().__init__(nome,idade)
        self.gols_marcados = gols_marcados

    def faz_o_que(self):
         return f'O {self.nome} é jogador de futebol e já marcou {self.gols_marcados} gols!!'