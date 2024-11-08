#primeira questão

#n = nota, numero corresponde a qual seria a nota
n1 = input('Digite a primeira nota: ')
n2 = input('Digite a segunda nota: ')
n3 = input('Digite a terceira nota: ')
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)
media = (n1 + n2 + n3) / 3
print('Sua média é: ', media)


#segunda questão

#qa= quantidade de notas
qa = int(input('Digite a quantidade de aulas: '))
#qf= quantidade de faltas
qf = int(input('Quantidade de faltas: '))
frequencia = ((qa - qf) / qa) *100
print('Sua frequência é:',frequencia,'%')


#terceira questão

#ms= media semestral
ms = int(input('Digite a media semestral:'))
#obs: nf= nota final
nf = int(input('Digite a nota final:'))
#mf= media final
mf = ((ms*6) + (nf*4)) / 10
print('Sua média é:', mf)


#quarta questão

#ch= carga horária
ch = 50
#sn= segundos necessários
sn = int(input('Digite os segundos que foram necessários:'))
#spm= segundos para minutos
spgitm= sn / 60
tn= (sn / ch)
print('São necessárias:', (tn),'para realizar a prova')


#quinta questão

#aa= alunos aprovados
aa = int(input('Digite a quantidade de alunos aprovados:'))
#ar= alunos reprovados
ar = int(input('Digite a quantidade de alunos reporavdos:'))
#ta= total de alunos
ta = aa + ar
conta = ((ta - ar) / ta) *100
print('A porcentagem de alunos aprovados é: ', conta) 