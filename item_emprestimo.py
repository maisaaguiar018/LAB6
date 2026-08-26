class ItemEmprestimo:
    def __init__(self, livro, cliente):
        self.livro = livro
        self.cliente = cliente

    def realizar_emprestimo(self):
        if self.livro.emprestar():
           self.cliente.adicionar_emprestimo(self)
           return True
        return False
            
    def devolver(self):
        self.livro.devolver()