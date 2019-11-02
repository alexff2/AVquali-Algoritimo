# Importação de bibliotecas e arquivos externos
import os # Biblioteca de função de limpeza de tela de terminal
import variaveis as var # Arquivo externo de variáveis

# Função de cadastro de Alunos
def cadAluno():
    """
    Declaração de varivel da condição de repetição da rotina de cadastro, que recebi os valores 1 - caso usuário queira
    cadastrar outro Aluno e 2 - caso não
    """
    cond = 1
    while cond != 2:
        # Condição que verifica quantidade de alunos cadastrados após ultima inserção
        if len(var.aluno) >= 3:
            print('WORNING: Você já cadastrou o máximo de 3 Alunos suportados na sala')
            print('')
            input('Aperte Enter para voltar ao menu inicial')
            cond = 2
            os.system(var.limpar) # Limpa tela de alerta de máximo de Alunos
        # Caso não tenha atingido o máximo de casdastro, continua rotina de casdastro
        else:
            print('***** Cadastro de Aluno *****')
            print('')
            var.aluno.append(input('Nome do Aluno: ')) # Atribui o valor no vetor Aluno, realizando o cadastro
            os.system(var.limpar) # Limpa tela de cadastro

            # Questiona se usuário deseja cadastrar novamente atribuindo 1/2 a variável de condição
            cond = int(input('Deseja cadastrar outro Aluno (1 - Sim/2 - Não)? '))

            # Verificação se usuário digitou 1/2, caso não, entra em loop com menssagem de erro até usuário digitar 1/2
            while cond != 1 and cond != 2 :
                os.system(var.limpar) # Limpa tela de questionamento anterior
                print('ERRO: Selecione um valor entre 1 e 2')
                print('')
                # Após menssagem de erro, questiona novamente usuário e atribui o valor 1/2 a variavel de condição
                cond = int(input('Deseja cadastrar outro Aluno (1 - Sim/2 - Não)? ')) 
                os.system(var.limpar) # Limpa tela de erro e novo questionamento
            
            os.system(var.limpar) # Limpa tela de questionamento

# Função de lançamento de nota
def lancaNota():
    #Função que renderiza em tela os Alunos cadastrados com a posição de seu vetor, sera usada mais de 1 vez do programa
    def renderCadNota():
        print('***** Lancamento de notas *****')
        print('')
        for i in range(len(var.aluno)):
            print(i,'-',var.aluno[i])
        # Questiona usuário qual Aluno ira inserir a nota
        codAluno = int(input('Qual Aluno deseja lançar nota (Digite o código)? '))
        os.system(var.limpar) #Limpa tela de questionamento
        return codAluno
    
    def renderDisciplina():
        print('***** Lancamento de notas *****')
        print('')
        for i in range(len(var.disciplina)):
            print(i,'-',var.disciplina[i])
        # Questiona usuário qual Disciplina ira inserir a nota
        codDisciplina = int(input('Qual Disciplina deseja lançar nota (Digite o código)? '))
        os.system(var.limpar) #Limpa tela de questionamento
        return codDisciplina
    
    # Chamando Função de render Tela de cadastro
    codAluno = renderCadNota()
    # Verifica se valor digitado por usuário é válido, entrando em loop caso não seja, até usuario digitar valor correto
    while codAluno < 0 or codAluno >= len(var.aluno) :
        print('WARNING: Digite um valor entre ',0,' e ',len(var.aluno)-1)
        input('Precione Enter')
        os.system(var.limpar) #Limpa tela de Erro
        codAluno = renderCadNota()
    
    # Chamando Função de render Tela de seleção de disciplina
    codDisciplina = renderDisciplina()
    # Verifica se valor digitado por usuário é válido, entrando em loop caso não seja, até usuario digitar valor correto
    while codDisciplina < 0 or codDisciplina >= len(var.disciplina) :
        print('WARNING: Digite um valor entre ',0,' e ',len(var.disciplina)-1)
        input('Precione Enter')
        os.system(var.limpar) #Limpa tela de Erro
        codDisciplina = renderDisciplina()

    # Lançando notas do aluno selecionado
    print('Digite as notas do Aluno - ',var.aluno[codAluno])
    var.notas[codAluno][codDisciplina][0] = float(input('Nota da P1: '))
    var.notas[codAluno][codDisciplina][1] = float(input('Nota da P2: '))
    var.notas[codAluno][codDisciplina][2] = float(input('Nota da P3: '))

    if var.notas[codAluno][codDisciplina][0] < 7 or var.notas[codAluno][codDisciplina][1] < 7 or var.notas[codAluno][codDisciplina][2] < 7:
        subst = float(input('Nota da Substitutiva: '))
        if var.notas[codAluno][codDisciplina][0] < var.notas[codAluno][codDisciplina][1] and var.notas[codAluno][codDisciplina][0] < var.notas[codAluno][codDisciplina][2]:
            var.notas[codAluno][codDisciplina][0] = subst
        elif var.notas[codAluno][codDisciplina][1] < var.notas[codAluno][codDisciplina][0] and var.notas[codAluno][codDisciplina][1] < var.notas[codAluno][codDisciplina][2]:
            var.notas[codAluno][codDisciplina][1] = subst
        elif var.notas[codAluno][codDisciplina][2] < var.notas[codAluno][codDisciplina][1] and var.notas[codAluno][codDisciplina][2] < var.notas[codAluno][codDisciplina][0]:
            var.notas[codAluno][codDisciplina][2] = subst

    media = (var.notas[codAluno][codDisciplina][0] + var.notas[codAluno][codDisciplina][1] + var.notas[codAluno][codDisciplina][2]) / 3
    os.system(var.limpar)
    if media < 7.0:
        print ('Media do aluno ',var.aluno[codAluno],' ',media,' abaixo da média 7.0')
        var.notas[codAluno][codDisciplina].append(float(input('Digite a nota Final do Aluno: ')))
    os.system(var.limpar)