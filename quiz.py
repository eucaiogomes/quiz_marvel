#Quiz da Marvel!
print(20*'-')
print("Seja bem-vindo ao Quiz!")
print(20*'-')

resposta_usuario = input ("Deseja começar? (S/N)")
print(resposta_usuario)

if resposta_usuario != 'S':
    quit()

print("Começando...")
print("Quando o primeiro filme da Marvel foi ao ar? \n(A) Capitão America \n(B) Homem de Ferro \n(C) Vingadores \n(D) Viuva Negra ")

resposta_1 = input("Resposta:")
score = 0 #pontuação 

if resposta_1 == 'B' or "b":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")
print(20*"-")

#Pergunta 2 
print("Quem escreveu a Marvel Comics? \n(A) Stan lee \n(B) Tom cruise \n(C) Dwayne Jhonson \n(D) Viuva Negra ")

resposta_1 = input("Resposta:")
score = 0
#Condição
if resposta_1 == 'A' or "a":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")
print(20*'-')
#Quiz finalizado
print(f'Quiz finalizado... sua pontuação foi {score}/2')





