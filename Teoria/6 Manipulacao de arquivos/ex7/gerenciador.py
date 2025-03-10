class GerenciadorTarefas:
    def __init__(self, arquivo_dados="tarefas.json"):
        self._tarefas = []
        self._arquivo_dados = arquivo_dados
        self.carregar_tarefas()

    def adicionar_tarefa(self, descricao):
        self._tarefas.append(Tarefa(descricao))

    def marcar_tarefa_como_concluida(self, indice):
        if 0 <= indice < len(self._tarefas):
            self._tarefas[indice].marcar_como_concluida()
        else:
            print("Índice inválido.")

    def listar_tarefas(self):
        if not self._tarefas:
            print("Nenhuma tarefa na lista.")
        else:
            for i, tarefa in enumerate(self._tarefas):
                print(f"{i}: {tarefa.descricao()}")

    def excluir_tarefa(self, indice):
        if 0 <= indice < len(self._tarefas):
            del self._tarefas[indice]
        else:
            print("Índice inválido.")

    def salvar_tarefas(self):
        with open(self._arquivo_dados, "w") as arquivo:
            json.dump([tarefa.para_dicionario() for tarefa in self._tarefas], arquivo, indent=4)

    def carregar_tarefas(self):
        try:
            with open(self._arquivo_dados, "r") as arquivo:
                dados = json.load(arquivo)
                self._tarefas = [Tarefa.de_dicionario(tarefa) for tarefa in dados]
        except FileNotFoundError:
            self._tarefas = []
        except json.JSONDecodeError:
            print("Erro ao carregar as tarefas. O arquivo pode estar corrompido.")
            self._tarefas = []