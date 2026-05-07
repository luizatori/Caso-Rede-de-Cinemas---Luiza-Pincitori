class SessaoService:

    def __init__(self, repository):
        self.repository = repository

    def cadastrar(self, sessao):

        if not sessao.horario_inicio:
            raise Exception("Horário inválido")

        self.repository.salvar(sessao)
