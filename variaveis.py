# Declaração de variáveis
aluno = [] # Lista que recebe os Alunos que seram cadastrados
disciplina = ['Algoritmos', 'Lógica', 'Cálculo', 'Filosofia', 'Administração'] # Lista com as disciplinas
# Lista de notas com 3 camadas, 1ª para alunos, 2ª para a disciplina e 3ª para as notas
notas = [] 
for i in range(2):
    notas.append([])
    for n in range(5):
        notas[i].append([0.0]*3)

# Criando variável que recebera o comando de limpa tela de terminais com condição para compatibilidade com OS
limpar = 'cls'