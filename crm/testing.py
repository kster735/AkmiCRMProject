from faker import Faker
import random
import time
import os

fake = Faker()

# for _ in range(5):
#     fakephonenumber = fake.phone_number()

#     if len(fakephonenumber) > 10 :
#         phonenumber = fakephonenumber[:10]
#     else:
#         phonenumber = fakephonenumber

#     print(phonenumber)


for _ in range(5):
    fname, lname, *args = fake.name().split(' ')
    print(fname)
    print(lname)

print(args)