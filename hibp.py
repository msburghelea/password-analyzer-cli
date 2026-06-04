import hashlib
import requests
def comprobar_hibp(password):
    password_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = password_hash[:5]
    url = f'https://api.pwnedpasswords.com/range/{prefix}'
    request = requests.get(url)
    if request.status_code == 200:
        hashes = request.text.splitlines()
        for line in hashes:
            hash_suffix, count = line.split(':')
            if hash_suffix == password_hash[5:]:
                return int(count)
    return 0 

