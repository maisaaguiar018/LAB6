class Livro:
    def __init__(self, codigo, titulo, autor):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True
        
    def exibir_info(self):
        return f"{self.codigo} - {self.titulo} - {self.autor}"

    def emprestar(self):
        if self.disponivel:
           self.disponivel = False
           return True
        return False

    def devolver(self):
        self.disponivel = True

