class Cliente:
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome
        self.emprestimos = []

    def adicionar_emprestimo(self, item):
        self.emprestimos.append(item)

    def listar_emprestimos(self):
        if not self.emprestimos:
            print("Não existe empréstimo.")
            return

        for item in self.emprestimos:
            print(item)
