from database import save_reg, check_user_exist
from exception import InvalidLogError, DataLogError, PassLogError

class reg_database():
    def __init__(self, nama, password, role='user'):
        self.nama = nama
        self.password = password
        self.role = role

class register_proc():
    def check_valid(nama):
        if nama == '':
            raise InvalidLogError('Data yang diinput tidak valid')

    def check_uname(self, nama):
        self.check_valid(nama)
        if check_user_exist(nama):
            raise DataLogError('Username sudah terpakai')

    def main_reg(self, nama, password):
        self.check_uname(nama)
        if len(password) < 8:
            raise PassLogError('Password minimal 8 karakter')

        user = reg_database(nama,password)
        save_reg(user.nama, user.password, user.role)
        return 'Berhasil mendaftarkan akun'