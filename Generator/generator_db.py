import sqlite3 as sq3


class GenoratorDB:
    def __init__(self, conn = None):
        self._conn = conn

    def connect_to_db_and_create_table(self):
        """connect and create table if 'passwords' table does not already exist"""
        try:
            conn = sq3.connect("{}.db".format(self._conn))
            table = conn.cursor()
            table.execute("CREATE TABLE IF NOT EXISTS passwords(id INTEGER PRIMARY KEY, Username TEXT NOT NULL, Password TEXT NOT NULL, Service TEXT NOT NULL)")
            conn.commit()
            conn.close()
        except ValueError as e:
            print(e)


    def add_a_new_password(self,user, pswrd, service):
        """ insert a new entry to the db """
        conn = sq3.connect("{}.db".format(self._conn))
        add = conn.cursor()
        add.execute("INSERT INTO passwords(id, Username, Password, Service) VALUES(NULL, ?, ?, ?)",(user, pswrd, service))
        conn.commit()
        conn.close()

    def show_all_entries(self):
        """ display all entries in list """
        conn = sq3.connect("{}.db".format(self._conn))
        show = conn.cursor()
        show.execute("SELECT * FROM passwords")
        rows = show.fetchall()
        return rows

    def search_by_service(self, service):
        """ search entry by service name"""
        conn = sq3.connect("{}.db".format(self._conn))
        search = conn.cursor()
        search.execute("SELECT * FROM passwords WHERE Service LIKE ? ", ("%"+service+"%",))
        rows = search.fetchall()
        return rows

    def search_by_user(self,username):
        conn = sq3.connect("{}.db".format(self._conn))
        curs = conn.cursor()
        curs.execute("SELECT * FROM passwords WHERE Username LIKE ?", ("%"+username+"%",))
        rows = curs.fetchall()
        return rows


    def select_by_id(self, id):
        conn = sq3.connect("{}.db".format(self._conn))
        curs = conn.cursor()
        curs.execute("SELECT * FROM passwords WHERE id = ?" ,(id,))
        row = curs.fetchall()
        return row

    def delete_row(self, id):
        conn = sq3.connect("{}.db".format(self._conn))
        curs = conn.cursor()
        curs.execute("DELETE FROM passwords WHERE id = ?",(id,))
        conn.commit()
        conn.close()

    




db = GenoratorDB('test_passwords')

print(db.connect_to_db_and_create_table())
#db.add_a_new_password('Santiro','123123123','Reddit')
#print(db.show_all_entries())
#print(db.select_by_id(2))
#db.delete_row(1)