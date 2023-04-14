import math, random

def generateOTP():
    digits='0123456789'
    OTP=""
    for i in range(4):
        OTP+=digits[math.floor(random.random()*10)]
    return OTP

if __name__=='__main__':
    print('OTP of 4 digits:',generateOTP())




import string

def rand_pass(size):
    generate_pass=''.join([random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)for n in range(size)])

    return generate_pass

password = rand_pass(10)
print(password)

import math, random

def generateOTP():
    string='0123456789abcdefghijklmnopqrstvwyzABCDEFGHIJKLMNOPQRSTVWYZ'
    OTP=""
    length=len(string)
    for i in range(4):
        OTP+=string[math.floor(random.random()*length)]
    return OTP

if __name__=='__main__':
    print('OTP of 4 digits:',generateOTP())





