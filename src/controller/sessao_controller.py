class SessaoController:

    def __init__(self, service):
        self.service = service

    def cadastrar_sessao(self, sessao):

        try:
            self.service.cadastrar(sessao)
            print("Sessão cadastrada com sucesso")

        except Exception as e:
            print(f"Erro: {e}")
