import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project_ex.settings')
import django
django.setup()

from myProject.models import User
from faker import Faker

fakegen = Faker()

def generateUsers(N=5):
    for _ in range(N):
        fake_fname = fakegen.first_name()
        fake_lname = fakegen.last_name()
        fake_email = fakegen.email()

        user = User.objects.get_or_create(f_name = fake_fname, l_name = fake_lname, email = fake_email)[0]

if __name__ == '__main__':
    print("Generating Fake Data")
    generateUsers(10)
    print("Completed")