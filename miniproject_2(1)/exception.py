class InvalidLogError(Exception):
    '''Data tidak valid'''

class DataLogError(Exception):
    '''user belum ada harap daftar terlebih dahulu'''

class WrongLogError(Exception):
    '''Username atau password salah'''

class PassLogError(Exception):
    '''Password minimal 8 karakter'''