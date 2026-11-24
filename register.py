from database import save_reg, check_user_exist, verify_user, init_db
from exception import WrongLogError, InvalidLogError, DataLogError, PassLogError

class reg_database():
    def __init__(self, nama, password):
        self.nama = nama
        self. password = password

class register_proc():
    def __init__(self, database_reg):
        self.database_reg = reg_database

    def check_valid(nama):
        if nama == '':
            raise InvalidLogError('Data yang diiinput tidak valid')

    def check_uname(self, nama):
        self.check_valid(nama)
        if check_user_exist(nama):
            raise DataLogError('Username sudah terpakai')

    def main_reg(self, nama, password):
        self.check_uname(nama)
        if len(password) < 8:
            raise PassLogError('Password minimal 8 karakter')

        save_reg(nama, password)
        return 'Berhasil mendaftarkan akun'

reg_proc = register_proc(init_db)

