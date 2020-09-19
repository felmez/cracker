import hashlib

def crack_sha1_hash(password_hash, use_salts=False):
    with open('top-10000-passwords.txt', 'r') as passwords_file:
        passwords = [password.strip() for password in passwords_file]
    with open('known-salts.txt', 'r') as salts_file:
        salts = [salt.strip() for salt in salts_file]
    for item in passwords:
        test = item
        if use_salts:
            for x in salts:
                test = item + x
                key = bytes(test, encoding='utf-8')
                hashed_password = hashlib.sha1(key).hexdigest()
                if hashed_password == password_hash:
                    return item
                test = x + item
                key = bytes(test, encoding='utf-8')
                hashed_password = hashlib.sha1(key).hexdigest()
                if hashed_password == password_hash:
                    return item
        else:
            key = bytes(test, encoding='utf-8')
            hashed_password = hashlib.sha1(key).hexdigest()
            if hashed_password == password_hash:
                return item
    return 'PASSWORD NOT IN DATABASE'