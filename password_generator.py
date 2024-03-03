import random
import string

rand_num = string.ascii_letters + string.digits + string.punctuation

pass_len = 12

password = ""

for i in range(pass_len):
    password += random.choice(rand_num)

print("Your random password is : ",password)



