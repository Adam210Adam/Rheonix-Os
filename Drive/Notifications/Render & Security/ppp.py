import requests
import hashlib
import sys

def request_api_data(query_char):
    url = "https://api.pwnedpasswords.com/range/" + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError()
    return res

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0
    

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode("UTF-8")).hexdigest().upper()
    passsword = sha1password[:5]
    tail = sha1password[5:]
    return get_password_leaks_count(request_api_data(passsword), tail)

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f"{password} was found {count} times...You should probably change your password")
        else:
            print(f"{password} was NOT found... Carry on!")






main(sys.argv[1:])