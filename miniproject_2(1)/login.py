from database import verify_user
from exception import InvalidLogError, WrongLogError

class signin:
    def valid_proc(self, nama):
        if nama == '':
            raise InvalidLogError('Data yang diinput tidak valid')

    def signin_proc(self, nama, password):
        self.valid_proc(nama)
        if not verify_user(nama, password):
            raise WrongLogError('Username atau password salah')
        return 'Login berhasil'