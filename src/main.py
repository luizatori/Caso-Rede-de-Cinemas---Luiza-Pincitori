import sqlite3

from model.sessao import Sessao
from repository.sessao_repository import SessaoRepository
from service.sessao_service import SessaoService
from controller.sessao_controller import SessaoController

connection = sqlite3.connect("cinema.db")

repository = SessaoRepository(connection)
service = SessaoService(repository)
controller = SessaoController(service)

sessao = Sessao(
    horario_inicio="18:00",
    horario_fim="20:00",
    filme_id=1,
    cinema_id=1
)

controller.cadastrar_sessao(sessao)
