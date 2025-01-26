import json

class Tarefa:
    def __init__(self, descricao):
        self._descricao = descricao
        self._concluida = False

    def marcar_como_concluida(self):
        self._concluida = True

    def descricao(self):
        status = "[x]" if self._concluida else "[ ]"
        return f"{status} {self._descricao}"

    def para_dicionario(self):
        return {"descricao": self._descricao, "concluida": self._concluida}

    @staticmethod
    def de_dicionario(dados):
        tarefa = Tarefa(dados["descricao"])
        tarefa._concluida = dados["concluida"]
        return tarefa