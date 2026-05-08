import sqlite3

from model.sessao import Sessao
from repository.sessao_repository import SessaoRepository
from service.sessao_service import SessaoService
from controller.sessao_controller import SessaoController

connection = sqlite3.connect("cinema.db")

repository = SessaoRepository(connection)
service = SessaoService(repository)
controller = SessaoController(service)

print("=== CADASTRO DE SESSÃO ===")

inicio = input("Horário de início: ")
fim = input("Horário de fim: ")
filme_id = int(input("ID do filme: "))
cinema_id = int(input("ID do cinema: "))

sessao = Sessao(
    horario_inicio=inicio,
    horario_fim=fim,
    filme_id=filme_id,
    cinema_id=cinema_id
)

controller.cadastrar_sessao(sessao)

print("\n=== SESSÕES CADASTRADAS ===")

cursor = connection.cursor()

cursor.execute("SELECT * FROM sessao")

for sessao in cursor.fetchall():
    print(sessao)

connection.close()
