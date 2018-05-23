""" Create a airflow user
"""
import os
import argparse

from airflow import models, settings
from airflow.contrib.auth.backends.password_auth import PasswordUser

def create(username, email, password):
    user = PasswordUser(models.User())
    user.username = username
    user.email = email
    user.password = password
    session = settings.Session()
    session.add(user)
    session.commit()
    session.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        "username",
        default=os.getenv("USERNAME"),
        required=not(os.getenv("USERNAME")),
    )
    parser.add_argument(
        "email",
        default=os.getenv("email"),
        required=not(os.getenv("email")),
    )
    parser.add_argument(
        "password",
        default=os.getenv("password"),
        required=not(os.getenv("password")),
    )
    args = parser.parse_args()
    create(args.username, args.email, args.password)
