import hashlib
import string
from tqdm import tqdm
import itertools




PASSWORD_LENGTH = 5
CHARS = string.ascii_letters + string.digits + string.punctuation
CHARS = string.ascii_lowercase
CHARS = ('', ) + tuple(CHARS)

n_passwords = len(CHARS) ** PASSWORD_LENGTH

md5_to_crack = "dcddb75469b4b4875094e14561e573d8"

for password in tqdm(itertools.product(CHARS, repeat=PASSWORD_LENGTH), total=n_passwords):
    pass_str = "".join(password)
    pass_md5 = hashlib.md5(pass_str.encode()).hexdigest()
    if pass_md5==md5_to_crack:
        print(f"O kodikos einai {pass_str}")
        break