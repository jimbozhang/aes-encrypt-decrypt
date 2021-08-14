import os
from cryptographic import encrypt, decrypt


# Create a file (~500Mb) for testing
os.makedirs('env', exist_ok=True)
example_path = 'env/example.txt'
with open(example_path, 'w') as f:
    for line_num in range(50000000):
        f.write('1234567890\n')

# Encrypt & decrypt
password = '.2/lor.SedutperspiciDndeomnis'
encrypt(example_path, f'{example_path}.aes', password)
decrypt(f'{example_path}.aes', f'{example_path}.dec', password)
