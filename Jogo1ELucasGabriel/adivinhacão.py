#Lucas Gabriel Appelt Silva N°30
import random
# biblioteca para efetivar o sorteio d numero, já pronto, apenas iremos informar posteriormente inter
import os
#biblioteca do sistema operacional, para limpar a tela, se windows cls, no lixux clear
erro = 0
sorteado=random.randrange(0, 100)
jogador=int(input("digites seu número!   "))
while(sorteado!=jogador):
    os.system('cls')
    if(sorteado>jogador):
        print ("ERRO, o número e maior")
    elif(sorteado<jogador):
        print("ERRO, número e menor")
    erro+=1
    jogador=int(input("digite seu número de erros"))
print("numero" + str(jogador) + ", voce acertou em" + str(erro+1) + "tentativas")
                


