class Funcionario:
    def __init__(self, codigo, nome, cargo):
        self.codigo = codigo
        self.nome = nome
        self.cargo = cargo

    def cadastrar_livro(self, biblioteca, livro):
        print("Livro cadastrado")

    def exibir (self):
        return f"{self.codigo} - {self.nome} {self.cargo}"