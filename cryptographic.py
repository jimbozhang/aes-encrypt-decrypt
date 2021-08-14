# Most codes below are from https://stackoverflow.com/a/20457519

from hashlib import md5
from Crypto.Cipher import AES
from Crypto import Random


bs = AES.block_size
chunk_block_num = 1024
key_length = 32
salt_header = 'Salted__'


def derive_key_and_iv(password, salt):
    d = d_i = b''
    while len(d) < key_length + bs:
        d_i = md5(d_i + str.encode(password) + salt).digest()
        d += d_i
    return d[:key_length], d[key_length:key_length+bs]


def encrypt(in_path, out_path, password):
    with open(in_path, 'rb') as in_file, open(out_path, 'wb') as out_file:
        bs = AES.block_size
        salt = Random.new().read(bs - len(salt_header))
        key, iv = derive_key_and_iv(password, salt)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        out_file.write(str.encode(salt_header) + salt)
        finished = False
        while not finished:
            chunk = in_file.read(chunk_block_num * bs) 
            if len(chunk) == 0 or len(chunk) % bs != 0:
                padding_length = (bs - len(chunk) % bs) or bs
                chunk += str.encode(padding_length * chr(padding_length))
                finished = True
            out_file.write(cipher.encrypt(chunk))


def decrypt(in_path, out_path, password):
    with open(in_path, 'rb') as in_file, open(out_path, 'wb') as out_file:
        bs = AES.block_size
        salt = in_file.read(bs)[len(salt_header):]
        key, iv = derive_key_and_iv(password, salt)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        next_chunk = ''
        finished = False
        while not finished:
            chunk, next_chunk = next_chunk, cipher.decrypt(in_file.read(chunk_block_num * bs))
            if len(next_chunk) == 0:
                padding_length = chunk[-1]
                chunk = chunk[:-padding_length]
                finished = True
            out_file.write(bytes(x for x in chunk))
