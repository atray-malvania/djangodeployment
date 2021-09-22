import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'second_project.settings')

import django
django.setup()

from second_app.models import User
from faker import Faker

fakegen = Faker()

def populate(N):
    for items in range(N):

        fake_name = fakegen.name()
        fake_fname = fake_name.split(" ")[0]
        fake_lname = fake_name.split(" ")[1]
        fake_email = fakegen.email()

        user = User.objects.get_or_create(first_name=fake_fname, last_name=fake_lname, email=fake_email)
if __name__ == '__main__':
    populate(20)