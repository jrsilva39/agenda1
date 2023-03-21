'''Aluno : Valdiro Ferreira da Silva Júnior                         CPF: 010.852.561-97                                           
•	Disciplina: FUNDAMENTOS DE PROGRAMAÇÃO COM PYTHON ESP

Curso: Desenvolvimento de Sistemas em Python'''                              	



def salvar_agenda(lista):
    arquivo = open("contatos.txt", "w")

    for cadastropessoas in lista:
        arquivo.write("{}#{}#{}#{}#{}\n" .format(cadastropessoas['nome'], cadastropessoas['telefone'], cadastropessoas['cidade'], cadastropessoas['estado'], cadastropessoas['status']))
    arquivo.close( )


def carregar_agenda( ):
    lista = []

    try:
        arquivo = open("contatos.txt", "r")

        for linha in arquivo.readlines( ):
            coluna = linha.strip().split ("#")

            cadastropessoas = {
                "telefone" : coluna [1],  
                "nome" : coluna [0],
                "cidade" : coluna [2],
                "estado" : coluna [3],
                "status" : coluna [4]
            }

            lista.append(cadastropessoas)

        arquivo.close( )
    except FileNotFoundError:
        pass
    return lista
    
def numtelefone(lista, telefone):
    if len(lista) > 0:
        for cadastropessoas in lista:
            if cadastropessoas ['telefone'] == telefone:
                return True
        
    return False

def cadastrar(lista):

    while True:
        telefone = input("Digite seu núnero de telefone: \n")

        if not numtelefone(lista, telefone):
            break
        else:
            print("Telefone já utilizado, por favor tente outro número !\n")

    cadastropessoas = {
        "telefone" : telefone,  
        "nome" : str (input ("Digite seu nome: \n")),
        "cidade" : str (input ("Digite a cidade onde reside: \n")),
        "estado" : str (input ("Digite o estado onde reside: \n")),
        "status" : input ("P -> Pessoal C -> Comercial: ")
    }

    lista.append(cadastropessoas)

    print ("O cadastro de {} foi efetuado com sucesso!\n".format (cadastropessoas ['nome']))

def alterar (lista):
    print (" == Alterar Contato == ")
    if len(lista) > 0:
        telefone = input ("Digite o telefone do contato que deseja alterar:\n")
        if numtelefone (lista, telefone):
            print ("O contato foi encontrado!")
            for cadastropessoas in lista:
                if cadastropessoas ['telefone'] == telefone:
                    print("Nome: {}" .format (cadastropessoas['nome']))
                    print("Telefone: {}" .format (cadastropessoas['telefone']))
                    print("Cidade: {}" .format (cadastropessoas['cidade']))
                    print("Estado: {}" .format (cadastropessoas['estado']))
                    print("status: {}" .format (cadastropessoas['status']))
                    print("===================================================\n")

                    cadastropessoas ['nome'] = input ("Digite o novo nome do contato: ")
                    cadastropessoas ['cidade'] = input ("Digite a nova cidade do contato: ")
                    cadastropessoas ['estado'] = input ("Digite o novo estado do contato: ")
                    cadastropessoas ['status'] = input ("Digite o novo status do contato: ")

                    print ("Os dados do contato com telefone {}, foram alterados com sucesso."
                           .format (cadastropessoas ['telefone']))
                    break
        else:
            print ("Não existe contato cadastrado no sistema com o telefone {}.\n" .format (telefone))
    else:
        print("Não existe nenhum contato cadastrado no sistema.\n")


def listar (lista):
    print (" == Listar Contatos ==")
    if len(lista) > 0:
        for i, cadastropessoas in enumerate(lista):
            print("Contato {}:" .format (i + 1))
            print("\tNome: {}" .format (cadastropessoas['nome']))
            print("\tTelefone: {}" .format (cadastropessoas['telefone']))
            print("\tCidade: {}" .format (cadastropessoas['cidade']))
            print("\tEstado: {}" .format (cadastropessoas['estado']))
            print("\tstatus: {}" .format (cadastropessoas['status']))
            print("===================================================")
        
        print ("Quantidade de contatos: {}\n" .format(len(lista))) 
    else:
        print("Não existe nenhum contato cadastrado no sistema.\n")
            

def procurar (lista):
    print (" == Procurar Contato == ")
    if len(lista) > 0:
        telefone = input ("Digite o telefone do contato que procura:\n")
        if numtelefone (lista, telefone):
            print ("O contato foi encontrado!")
            for cadastropessoas in lista:
                if cadastropessoas ['telefone'] == telefone:
                    print("Nome: {}" .format (cadastropessoas['nome']))
                    print("Telefone: {}" .format (cadastropessoas['telefone']))
                    print("Cidade: {}" .format (cadastropessoas['cidade']))
                    print("Estado: {}" .format (cadastropessoas['estado']))
                    print("status: {}" .format (cadastropessoas['status']))
                    print("===================================================\n")
                    break
        else:
            print ("Pessoa com o telefone {} não encontrada.\n" .format (telefone))
        
    else:
        print("Não existe nenhum contato cadastrado no sistema.\n")

def excluir (lista):
    print (" == Excluir Contato == ")
    if len(lista) > 0:
        telefone = input ("Digite o telefone do contato que deseja excluir:\n")
        if numtelefone (lista, telefone):
            print ("O contato foi encontrado!")
            for i, cadastropessoas in enumerate (lista):
                if cadastropessoas ['telefone'] == telefone:
                    print("Nome: {}" .format (cadastropessoas['nome']))
                    print("Telefone: {}" .format (cadastropessoas['telefone']))
                    print("Cidade: {}" .format (cadastropessoas['cidade']))
                    print("Estado: {}" .format (cadastropessoas['estado']))
                    print("status: {}" .format (cadastropessoas['status']))
                    print("===================================================\n")

                    del lista[i]

                    print ("Contato excluído com sucesso.")
                    break
        else:
            print ("Pessoa com o telefone {} não encontrada.\n" .format (telefone))
        
    else:
        print("Não existe nenhum contato cadastrado no sistema.\n")

def principal ( ):

    lista = carregar_agenda( )

    while True:

        print ("===================")
        print (" Escolha uma Opção")
        print ("===================\n")

        print ("[ 1 ] CADASTRAR DADOS")
        print ("[ 2 ] ALTERAR DADOS")
        print ("[ 3 ] LISTAR AGENDA")
        print ("[ 4 ] PROCURAR DADOS")
        print ("[ 5 ] EXCLUIR DADOS")
        print ("[ 6 ] SAIR DO SISTEMA\n\n")
        opcao = int(input("Qual sua opção ?\n"))

        if opcao == 1:
            cadastrar (lista)
            salvar_agenda(lista)
        elif opcao == 2:
            alterar (lista)
            salvar_agenda(lista)
        elif opcao == 3:
            listar (lista)
        elif opcao == 4:
            procurar (lista)
        elif opcao == 5:
            excluir (lista)
            salvar_agenda(lista)
        elif opcao == 6:
            print ("Obrigado por utilizar nosso sistema !")
            break
        else:
            print ("Opção inválida. Por favor tente novamente !")

principal( )