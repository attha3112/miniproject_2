class InvalidLogError(Exception):
    '''Data tidak valid'''

class DataLogError(Exception):
    '''user belum ada harap daftar terlebih dahulu'''

class WrongLogError(Exception):
    '''Username atau password salah'''

class PassLogError(Exception):
    '''Password minimal 8 karakter'''

# === Server Exception ===

class invalidataerror(Exception):
    '''Data server tidak valid'''

class duplicatedataerror(Exception):
    '''Duplikasi server ditemukan di database'''