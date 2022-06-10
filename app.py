#tratamento de erro try
#upper() é um método embutido usado para manipulação de strings. 
# Os métodos upper()retornam a string em maiúsculas da string fornecida. Ele converte todos os caracteres minúsculos em maiúsculas. 
# Se não houver caracteres minúsculos, ele retornará a string original.
# def cria um metodo
# ----() chama o metodo
# while estrutura de repetição
#input guarda uma variavel 

def menu():
    voltarMenuPrincipal = 's'
    while voltarMenuPrincipal == 's':

        opcao= input('''
        ===============================================
                        PROJETO AGENDA EM PYTHON
        MENU:
        [1] CADASTRA CONTATO
        [2] LISTA DE CONTATO
        [3] DELETAR CONTATO
        [4] BUSCAR CONTATO PELO ID
        [5] CADASTRA CONTATO

        ===============================================
        ESCOLHA UMA OPÇÃO ACIMA:
        ''')
        if opcao =="1":
            cadastrarContato()
        elif opcao=="2":
            listarContato()
        elif opcao =="3":
            deletarContato()
        elif opcao =="4":
            buscarContatoPeloNome()
        else:
            sair()
        voltarMenuPrincipal=input("Deseja voltar ao menu principal ? (s/n)").lower()

def cadastrarContato():
    idContato = input("Escolha o Id do seu contato: ")
    nome = input("Escreva o nome do seu contato: ")
    telefone = input ("Escreva o telefone do seu contato: ")
    email = input("escreva o email do contato: ")
    try:
        agenda = open("agenda.txt","a")
        dados = f'{idContato};{nome};{telefone};{email} \n'
        agenda.write(dados)
        agenda.close()
        print(f'Contato gravado com sucesso!!!!')
    except:
        print("ERRO na gravação do contato")

def listarContato():
    agenda =open("agenda.txt","r")
    for contato in agenda:
        print(contato)
    agenda.close()

def deletarContato():
    nomeDeletado = input ("Digite o nome para ser deletado: ").lower()
    agenda = open ("agenda.txt","r")
    aux = []
    aux2= []
    for i in agenda:
        aux.append(i)
    for i in range(0, len(aux)):
        if nomeDeletado not in aux[i].lower():
            aux2.append(aux[i])
    agenda = open ("agenda.txt","w")
    for i in aux2:
        agenda.write(i)
    print(f'Contato deletado com sucesso')

listarContato()


def buscarContatoPeloNome():
    nome=input(f'digite o nome a ser procurado: ').upper()
    agenda =open("agenda.txt","r")
    for contato in agenda:
       if nome in contato.split(";")[1].upper():
           print(contato)
    agenda.close()
    

def sair():
    print(f'SAINDO....')
    exit()

def main():
    menu()

main()
