import hashlib
import requests
def check_hibp(password):
    password_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = password_hash[:5]
    url = f'https://api.pwnedpasswords.com/range/{prefix}'
    response  = requests.get(url)
    if response.status_code == 200:
        hashes = response.text.splitlines()
        for line in hashes:
            hash_suffix, count = line.split(':')
            if hash_suffix == password_hash[5:]:
                return int(count)
    return 0 

