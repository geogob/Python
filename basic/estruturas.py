#Estruturas de dados em Python
#Exerc�cios da Apostila Introdu��o a PYthon: M�dulo PAG 15
#George Oliveira Barros


# Input de dados:
# Aten��o essa fun��o sempre retorna um Str
x = int(raw_input ('Informe um valor'))


#O que delimita o loop � a identa��o
while x < 10:
    
    if (x%2)==0:
        print x

    x = x+1
    
print type (x)


#For

a = [1,0,0,1,2,3,1,6,0]

for i in a:
    print i



#Numero perfeito

print 'numeros perfeitos'
n = int(raw_input('informe o n�mero'))
teste = 0
for i in range(1,n):
    if n % i == 0:
        teste = teste + i
if teste == n:
    print n, 'e um numero perfeito'
else:
    print n, 'n�o � um perfeito'
