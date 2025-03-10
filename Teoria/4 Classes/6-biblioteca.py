class Livro:
    def __init__(self, titulo, autor, isbn):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn
        self.__emprestado = False

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_isbn(self):
        return self.__isbn

    def is_emprestado(self):
        return self.__emprestado

    def exibir_informacoes(self):
        return f"Título: {self.__titulo}, Autor: {self.__autor}, ISBN: {self.__isbn}, Emprestado: {self.__emprestado}"

    def emprestar(self):
        if not self.__emprestado:
            self.__emprestado = True
            return True
        return False

    def devolver(self):
        if self.__emprestado:
            self.__emprestado = False
            return True
        return False


class Usuario:
    def __init__(self, nome, id):
        self.__nome = nome
        self.__id = id
        self.__livros_emprestados = []

    def get_nome(self):
        return self.__nome

    def get_id(self):
        return self.__id

    def emprestar_livro(self, livro):
        if len(self.__livros_emprestados) < 3 and livro.emprestar():
            self.__livros_emprestados.append(livro)
            return True
        return False

    def devolver_livro(self, livro):
        if livro in self.__livros_emprestados and livro.devolver():
            self.__livros_emprestados.remove(livro)
            return True
        return False

    def listar_livros_emprestados(self):
        return [livro.exibir_informacoes() for livro in self.__livros_emprestados]

    def quantidade_livros_emprestados(self):
        return len(self.__livros_emprestados)


class Biblioteca:
    def __init__(self):
        self.__acervo = []
        self.__usuarios = []

    def cadastrar_livro(self, livro):
        if not any(l.get_isbn() == livro.get_isbn() for l in self.__acervo):
            self.__acervo.append(livro)
            return True
        return False

    def cadastrar_usuario(self, usuario):
        if not any(u.get_id() == usuario.get_id() for u in self.__usuarios):
            self.__usuarios.append(usuario)
            return True
        return False

    def emprestar_livro(self, id_usuario, isbn_livro):
        usuario = next((u for u in self.__usuarios if u.get_id() == id_usuario), None)
        livro = next((l for l in self.__acervo if l.get_isbn() == isbn_livro), None)
        if usuario and livro and not livro.is_emprestado():
            return usuario.emprestar_livro(livro)
        return False

    def receber_livro_devolvido(self, id_usuario, isbn_livro):
        usuario = next((u for u in self.__usuarios if u.get_id() == id_usuario), None)
        livro = next((l for l in self.__acervo if l.get_isbn() == isbn_livro), None)
        if usuario and livro:
            return usuario.devolver_livro(livro)
        return False

    def pesquisar_livro(self, termo):
        return [livro.exibir_informacoes() for livro in self.__acervo if termo.lower() in livro.get_titulo().lower() or termo.lower() in livro.get_autor().lower()]

    def listar_todos_livros(self):
        return [livro.exibir_informacoes() for livro in self.__acervo]

    def listar_livros_emprestados(self):
        return [livro.exibir_informacoes() for livro in self.__acervo if livro.is_emprestado()]

    def listar_livros_disponiveis(self):
        return [livro.exibir_informacoes() for livro in self.__acervo if not livro.is_emprestado()]


def cadastrar_livro(biblioteca):
    titulo = input("Título do livro: ")
    autor = input("Autor do livro: ")
    isbn = input("ISBN do livro: ")
    livro = Livro(titulo, autor, isbn)
    if biblioteca.cadastrar_livro(livro):
        print("Livro cadastrado com sucesso!")
    else:
        print("Livro com este ISBN já existe.")

def cadastrar_usuario(biblioteca):
    nome = input("Nome do usuário: ")
    id = input("ID do usuário: ")
    usuario = Usuario(nome, id)
    if biblioteca.cadastrar_usuario(usuario):
        print("Usuário cadastrado com sucesso!")
    else:
        print("Usuário com este ID já existe.")

def emprestar_livro(biblioteca):
    id_usuario = input("ID do usuário: ")
    isbn_livro = input("ISBN do livro: ")
    if biblioteca.emprestar_livro(id_usuario, isbn_livro):
        print("Livro emprestado com sucesso!")
    else:
        print("Não foi possível emprestar o livro.")

def devolver_livro(biblioteca):
    id_usuario = input("ID do usuário: ")
    isbn_livro = input("ISBN do livro: ")
    if biblioteca.receber_livro_devolvido(id_usuario, isbn_livro):
        print("Livro devolvido com sucesso!")
    else:
        print("Não foi possível devolver o livro.")

def pesquisar_livro(biblioteca):
    termo = input("Termo de busca: ")
    resultados = biblioteca.pesquisar_livro(termo)
    if resultados:
        print("Livros encontrados:")
        for resultado in resultados:
            print(resultado)
    else:
        print("Nenhum livro encontrado.")

def listar_todos_livros(biblioteca):
    livros = biblioteca.listar_todos_livros()
    if livros:
        print("Todos os livros:")
        for livro in livros:
            print(livro)
    else:
        print("Nenhum livro cadastrado.")

def listar_livros_emprestados(biblioteca):
    livros = biblioteca.listar_livros_emprestados()
    if livros:
        print("Livros emprestados:")
        for livro in livros:
            print(livro)
    else:
        print("Nenhum livro emprestado.")

def listar_livros_disponiveis(biblioteca):
    livros = biblioteca.listar_livros_disponiveis()
    if livros:
        print("Livros disponíveis:")
        for livro in livros:
            print(livro)
    else:
        print("Nenhum livro disponível.")

def sair(biblioteca):
    print("Saindo...")
    exit()

def menu():
    biblioteca = Biblioteca()
    opcoes = {
        "1": cadastrar_livro,
        "2": cadastrar_usuario,
        "3": emprestar_livro,
        "4": devolver_livro,
        "5": pesquisar_livro,
        "6": listar_todos_livros,
        "7": listar_livros_emprestados,
        "8": listar_livros_disponiveis,
        "9": sair
    }

    while True:
        print("\nMenu:")
        print("1. Cadastrar Livro")
        print("2. Cadastrar Usuário")
        print("3. Emprestar Livro")
        print("4. Devolver Livro")
        print("5. Pesquisar Livro")
        print("6. Listar Todos os Livros")
        print("7. Listar Livros Emprestados")
        print("8. Listar Livros Disponíveis")
        print("9. Sair")
        opcao = input("Escolha uma opção: ")

        funcao = opcoes.get(opcao)
        if funcao:
            funcao(biblioteca)
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()