import sqlite3

class SessaoRepository:

    def __init__(self, connection):
        self.connection = connection

    def salvar(self, sessao):

        cursor = self.connection.cursor()

        sql = """
        INSERT INTO sessao
        (horario_inicio, horario_fim, filme_id, cinema_id)
        VALUES (?, ?, ?, ?)
        """

        cursor.execute(sql, (
            sessao.horario_inicio,
            sessao.horario_fim,
            sessao.filme_id,
            sessao.cinema_id
        ))

        self.connection.commit()
