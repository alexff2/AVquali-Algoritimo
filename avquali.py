# Importação de bibliotecas e arquivos externos
import os # Biblioteca com função de limpeza de tela de terminal
import variaveis as var # Arquivo externo de variáveis
import func # Arquivo externo de funções

# Limpando Tela inicialmente
os.system(var.limpar)

# Declarando variável do menu e imprimindo o menu dentro de uma repetição
op = 0
while op != 5:
    print('***** MENU INICIAL *****')
    print('')
    print('1 - Cadastrar Aluno')
    print('2 - Lançar Notas')
    print('3 - Lançar Faltas')
    print('4 - Relatórios')
    print('5 - Sair')
    print('')

    #Tratando valores diferente de inteiro que o usuário passar
    '''try:'''
    op = int(input('Selecione uma das opões entre 1 e 5: ')) # Recebendo inteiro valor que usuário passar
    os.system(var.limpar) # Limpando tela para receber tela que usuário selecionou 
    
    # Condições que recebem valor digitado pelo usuário e direcionam para as telas que estão dentro das funções
    if op == 1:
        func.cadAluno() # Função que chama tela de cadastro passando e recebendo o valor do Aluno a ser inserido
    elif op == 2:
        func.lancaNota()
    elif op == 3:
        print('***** Lancamento de Faltas *****')
        os.system(var.limpar)
    elif op == 4:
        print('***** Relatórios *****')
        print(var.notas)
        input('Apresione Enter para sair')
        os.system(var.limpar)
    elif op <= 0 or op >= 6:
        print('ERRO: Selecione um valor entre 1 e 5')
        print('')
    else:
        print('ERRO: Valor digitado não compatível')
    '''except:
        os.system(var.limpar)
        print('WARNING: Parametro digitado inválido, digite um número inteiro') # Menssagem de erro caso usuário digite valor diferente de um inteiro'''
print('***** SITEMA DESLOGADO *****')