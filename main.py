notas = {'Ana':7.00}
notas['Viktor'] = 7.30
notas['Larisa'] = 8.00
notas['Ana'] = 6.00
print(notas)
nota = {'Ana':7.00,'Viktor':7.00,'Larisa':8.00}
media = input("insira o nome do discente:")
media = float(input("insira a nota do discente:")
if media in nota.keys():
 nota[nome] = media
else:
 print("aluno inexistente!")
 print(nota)
nota = {'Ana':7.00,'Viktor':7.00,'Larisa':8.00}
nome = input("insira o nome do discente a ser excluido:")
if nome in nota.keys():
 nota.pop(nome)
else:
 print("aluno inexistente!")
print(nota)

print("ola, mundo")