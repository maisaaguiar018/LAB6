from cliente import Cliente
from funcionario import Funcionario
from livro import Livro
from item_emprestimo import ItemEmprestimo
from termcolor import colored, cprint

biblioteca = []
clientes = []
funcionarios = []
emprestimos = []

def cadastrar_livro():
        print("CADASTRAR LIVRO")

        codigo = input("Código: ")
        titulo = input("Título: ")
        autor = input("Autor: ")

        livro = Livro(codigo, titulo, autor)
        biblioteca.append(livro)
        print("Livro cadastrado!")

def cadastrar_cliente():
    print("CADASTRAR CLIENTE")
    codigo = input("Código: ")
    nome = input("Nome: ")
    cliente = Cliente(codigo, nome)
    clientes.append(cliente)
    print("Cliente cadastrado!")

def cadastrar_funcionario():
    print("CADASTRAR FUNCIONÁRIO")
    codigo = input("Código: ")
    nome = input("Nome: ")
    cargo = input("Cargo: ")

    funcionario = Funcionario(codigo, nome, cargo)
    funcionarios.append(funcionario)
    print("Funcionário cadastrado com sucesso!")

def listar_livros():
    print("LIVROS")

    if not biblioteca:
        print("Nenhum livro cadastrado.")
        return

    for livro in biblioteca:
        status = "Disponível" if livro.disponivel else "Emprestado"

        print(
            f"{livro.exibir_info()} | "
            f"Status: {status}"
        )


def listar_clientes():
    print("CLIENTES")

    for cliente in clientes:
        print(
            f"Código: {cliente.codigo} | "
            f"Nome: {cliente.nome}"
        )


def realizar_emprestimo():
    print("EMPRÉSTIMO")

    codigo_cliente = input("Código do cliente: ")
    codigo_livro = input("Código do livro: ")

    cliente = None
    livro = None

    for c in clientes:
        if c.codigo == codigo_cliente:
            cliente = c

    for l in biblioteca:
        if l.codigo == codigo_livro:
            livro = l

    if cliente is None:
        print("Cliente não encontrado.")
        return

    if livro is None:
        print("Livro não encontrado.")
        return

    item = ItemEmprestimo(livro, cliente)

    if item.realizar_emprestimo():
        emprestimos.append(item)
        print(colored("Empréstimo realizado com sucesso!", "blue"))
    else:
        print(colored("Livro indisponível.", "blue"))


def devolver_livro():
    print(colored("DEVOLUÇÃO", "blue"))

    codigo_livro = input("Código do livro: ")

    for item in emprestimos:
        if item.livro.codigo == codigo_livro:
            item.devolver()
            emprestimos.remove(item) 
            print(colored("Livro devolvido com sucesso!", "blue"))
            return

    print(colored("Empréstimo não encontrado.", "light_grey"))


def listar_emprestimos():
    print(colored("EMPRÉSTIMOS", "light_grey"))

    if not emprestimos:
        print(colored("Nenhum empréstimo realizado.", "light_grey"))
        return

    for item in emprestimos:
        status = (
            "Disponível"
            if item.livro.disponivel
            else "Emprestado"
        )

        print(
            f"Cliente: {item.cliente.nome}  "
            f"Livro: {item.livro.titulo}  "
            f"Status: {status}"
        )


def menu():
    while True:
        print(colored("SISTEMA BIBLIOTECA", "magenta"))
        print(colored("1 - Cadastrar livro", "green"))
        print(colored("2 - Cadastrar cliente", "green"))
        print(colored("3 - Cadastrar funcionário", "green"))
        print(colored("4 - Listar livros", "green"))
        print(colored("5 - Listar clientes", "green"))
        print(colored("6 - Realizar empréstimo", "green"))
        print(colored("7 - Devolver livro", "green"))
        print(colored("8 - Listar empréstimos", "green"))
        print(colored("0 - Sair", "red"))

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_livro()

        elif opcao == "2":
            cadastrar_cliente()

        elif opcao == "3":
            cadastrar_funcionario()

        elif opcao == "4":
            listar_livros()

        elif opcao == "5":
            listar_clientes()

        elif opcao == "6":
            realizar_emprestimo()

        elif opcao == "7":
            devolver_livro()

        elif opcao == "8":
            listar_emprestimos()

        elif opcao == "0":
            print(colored("Sistema encerrado.", "cyan"))
            break

        else:
            print(colored("Opção inválida.", "red"))


if __name__ == "__main__":
    menu()
