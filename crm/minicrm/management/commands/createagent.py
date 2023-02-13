from django.core.management.base import BaseCommand
from faker import Faker
from minicrm.models import Agent, User, Message, Contact, File
from pathlib import Path
import random
import time
import os
from django.contrib.auth.hashers import make_password, check_password, is_password_usable

"""
This script was inspired from the following tutorial:
https://www.youtube.com/watch?v=8LHdbaV7Dvo
"""

class Command(BaseCommand):
    help = 'Command information'

    def handle(self, *args, **kwargs):
        
        myfile = open('passwords.txt', 'a')

        fake = Faker()

        random.seed(time.time())

        for _ in range(1):
            try:

                fname, lname, *args = fake.name().split(' ')
                print('ok here')
                image = randomImage()
                
                fakepassword = fake.password()
                fakeusername = fake.user_name()

                myfile.write(fakeusername + ': ' + fakepassword + '\n')

                newuser = User.objects.create(
                    first_name = fname,
                    last_name = lname,
                    email = fake.email(),
                    password = make_password(fakepassword, salt='caco3cuso4'),
                    username = fakeusername,
                )

                newuser.save()

                fakephonenumber = fake.phone_number()
                phonenumber = fakephonenumber
                if len(fakephonenumber) > 10 :
                    phonenumber = fakephonenumber[:10]

                print(phonenumber)

                agent = Agent.objects.create(
                    user = newuser,
                    agent_phone = phonenumber,
                    agent_photo = os.path.join('images/', image),
                    agent_levelaccess = 1
                )

                agent.save()

                newuser = None
                agent = None
                print('agent saved')

            except:
                continue
            
            myfile.close()

            
def randomImage():
    number = random.randint(1,6)
    imageFile = ''

    if number == 1:
        imageFile = 'person1.png'

    if number == 2:
        imageFile = 'person2.jpg'
    
    if number == 3:
        imageFile = 'person3.jpg'
    
    if number == 4:
        imageFile = 'person4.jpg'

    if number == 5:
        imageFile = 'person5.jpg'

    if number == 6:
        imageFile = 'person6.jpg'
            
    return imageFile