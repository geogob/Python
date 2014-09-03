#Funções


x = int(raw_input('Informe um valor'))


def soma(x,y):
    x = x+y
    return x

def somatorio (*argumentos):
    result = 0
    for i in argumentos:
        result+=i
    return result



print 'valor + 5 = '+ str(soma(x,5))

print 'somatorio = '+ str(somatorio(5,12,22))

