from atleta import Atleta
from futebolista import futebolista
from nadador import nadador
from lutadorMMA import lutadorMMA
import os

def cls():
  os.system('cls' if os.name=='nt' else 'clear')


cls()
opção=1
j=0
n=0
l=0
menu = ('''MENU - QUESTÃO 02 - P1 REMOTA
[1] - Cadastrar Atleta
[2] - Mostrar informações de atleta
[0] - Sair do programa ''')
while opção != 0:
    cls()
    print(40 * '#')
    print(menu)
    print(40 * '#')
    opção = int(input())
    if opção==0:
        print(40 * '#')
        print('Sair do programa')
        print(40 * '#')
        cls()
        break
    elif opção==1:
        # Submenu da opção 1
        jog = futebolista('','','')
        nad = nadador('','','','')
        lut = lutadorMMA('','','','')    
        m1=1
        subm1 = ('''    [1] - Cadastrar Futebolista
    [2] - Cadastrar Nadador
    [3] - Cadastrar Lutador de MMA
    [0] - Retornar ao menu anterior ''')
        while m1 != 0:
            print(40 * '#')
            print(subm1)
            print(40 * '#')
            m1 = int(input())
            if m1==1:
                #Cadastrar Futebolista
                a=[]
                if j == 0:
                    a.append((input('Digite o nome do futebolista ')))
                    a.append((input('Digite a idade do futebolista ')))
                    a.append((input('Digite a quantidade de gols marcados ')))
                    jog = futebolista(a[0],a[1],a[2])
                    print('Futebolista cadastrado com sucesso!! \n')
                    j=1
                else:
                    print(40 * '#')
                    print('Já existe um futebolista cadastrado')
                    print(40 * '#')
            elif m1==2:
                #Cadastrar Nadador
                b=[]
                if n == 0:
                    b.append((input('Digite o nome do nadador ')))
                    b.append((input('Digite a idade do nadador ')))
                    b.append((input('Digite o numero de medalhas do nadador ')))
                    b.append((input('Digite o numero de olimpíadas disputadas ')))
                    nad = nadador(b[0],b[1],b[2],b[3])
                    print('Nadador cadastrado com sucesso!! \n')
                    n=1
                else:
                    print(40 * '#')
                    print('Já existe um nadador cadastrado')
                    print(40 * '#')
            elif m1==3:
                #Cadastrar Lutador de MMA
                c=[]
                if l == 0:
                    c.append((input('Digite o nome do lutador ')))
                    c.append((input('Digite a idade do lutador ')))
                    c.append((input('Digite a categoria de peso ')))
                    c.append((input('Digite o numero de cinturões disputados ')))
                    lut = lutadorMMA(c[0],c[1],c[2],c[3])
                    print('Lutador cadastrado com sucesso!! \n')
                    l=1
                else:
                    print(40 * '#')
                    print('Já existe um lutador cadastrado')
                    print(40 * '#')
            else:
                #Opção inválida
                print(40 * '#')
                print('Você escolheu uma opção inválida')
                print(40 * '#')
    elif opção==2:
        # Submenu da opção 2
        m2=1
        subm2 = ('''    [1] - Mostrar Futebolista
    [2] - Mostrar Nadador
    [3] - Mostrar Lutador de MMA
    [0] - Retornar ao menu anterior ''')
        while m2 != 0:
            print(40 * '#')
            print(subm2)
            print(40 * '#')
            m2 = int(input())
            if m2==1:
                #Mostrar Futebolista
                if j == 0:
                    print('Ainda não foi cadastrado nenhum futebolista, cadastre um para continuar!! \n')
                else:
                    print(40 * '#')
                    print(futebolista.faz_o_que(jog))
                    print(40 * '#')
            elif m2==2:
                #Mostrar Nadador
                if n == 0:
                    print('Ainda não foi cadastrado nenhum nadador, cadastre um para continuar!! \n')
                else:
                    print(40 * '#')
                    print(nadador.faz_o_que(nad))
                    print(40 * '#')
            elif m2==3:
                #Mostrar Lutador de MMA
                if l == 0:
                    print('Ainda não foi cadastrado nenhum lutador, cadastre um para continuar!! \n')
                else:
                    print(40 * '#')
                    print(lutadorMMA.faz_o_que(lut))
                    print(40 * '#')
            else:
                #Opção inválida
                print(40 * '#')
                print('Você escolheu uma opção inválida')
                print(40 * '#')
