import secrets
import string

alphabet=string.ascii_letters + string.digits
pas=''.join(secrets.choice(alphabet)for i in range(10))
print (pas)

import secrets
passwd=secrets.randbelow(20)
print(passwd)

import secrets
import string

alphabet=string.ascii_letters + string.digits
while True:
        pasw=''.join(secrets.choice(alphabet)for i in range(10))
        if (any(c.islower() for c in pasw) and any(c.isupper()
        for c in pasw)and sum(c.isdigit()for c in pasw)>=3):
                print (pasw)
                break
