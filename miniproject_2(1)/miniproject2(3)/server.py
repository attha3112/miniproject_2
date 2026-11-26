from database import add_server, check_server_exist
from exception import invalidataerror, duplicatedataerror

class server_db():
    def __init__(self, server_id, ssh_port, status = 'off'):
        self.server_id = server_id
        self.ssh_port = ssh_port
        self.status = status

class server_proc():
    def check_validation(server_id):
        if server_id == '':
            raise invalidataerror('Data yang dimasukkan tidak valid')

    def check_dupli(self, server_id):
        self.check_validation(server_id)
        if check_server_exist(server_id):
            raise duplicatedataerror('server id sudah terpakai')

    def server_proc(self, server_id, ssh_port):
        self.check_dupli(server_id)
        
        off = server_db(server_id, ssh_port)
        add_server(off.server_id, off.ssh_port, off.status)
        return 'Berhasil menambahkan server ke database'