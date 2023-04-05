sql_select = "select * from institution where status = 'A'"

class InstitutionRepository:

    def __init__(self, mysql_client):
        self.session_factory = mysql_client.session_factory

    def get_institution(self):
        with self.session_factory() as session:
            rows = session.execute(sql_select)
            return rows

    def get_institution_by_id(self, institution_id):
        sql_select_id = f"select * from institution where id = '{institution_id}'"
        with self.session_factory() as session:
            rows = session.execute(sql_select_id)
            return rows

    def delete_institution(self, institution_id):
        sql_select_id = f"delete from institution where id = '{institution_id}'"
        with self.session_factory() as session:
            rows = session.execute(sql_select_id)
            session.commit()
            return rows
