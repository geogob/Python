#geogobgob@gmail.com

#--------Impressão de Strings-------
print '-------------------------------------'
print 'trabalhando com strings:'
palavra = 'Hello python world !'

#Completa
print palavra
print palavra[:]

#Apenas uma posição
print palavra[2]

#Incrementando de 2 em 2
print palavra[0::2]

#Ao contráro (decrementando)
print palavra[17::-1]

#Concatenação de Strings

palavra = palavra + 'of my God'
print palavra

#Tamanho da sequencia
print len(palavra)


#--------Trabalhando com listas-------
print '-------------------------------------'
print 'trabalhando com vetores genéricos:'
vetor=[0,3,5,7,8]
print vetor
print vetor[2]
print vetor[2] + vetor[4]

#concatenando uma lista
vetor = vetor + [0,1,0,1]
print vetor
print 'Tamanho da lista igual a: ' + str(len(vetor))

# A estrututa de uma string é bem amarrada. Logo nós podemos mudar o conteúdo de uma determinad posição de uma lista, mas não de uma string

print'-------------------------'
print'Matriz'
matriz=[[1,2,3],[1,1,1],[2,2,2]]


#Dicionários
print'-------------------------'
print'Dicionários'

dicionario = {'Nome':'George','Idade':'22', 'Altura':'163'}
print dicionario















