""" Create a airflow user
"""
import os
import logging
import argparse

from airflow import models, settings
from airflow.contrib.auth.backends.password_auth import PasswordUser

def create(username, email, password, passive=True):
    """ Create an airflow user. If passive=False, an error will be raised if a matching user exists.
    """
    session = settings.Session()
    existing = session.query(models.User).filter(models.User.username == username).one_or_none()
    if existing:
        if not passive:
            raise ValueError("User '{}' already exists!".format(username))
        logging.info("Skipping... User '{}' already exists.".format(username))
        return
    user = PasswordUser(models.User())
    user.username = username
    user.email = email
    # This should be: user.password = password
    # Seems SQLA broke things in 1.2 with `hybrid_property`s. Could lower that version, or...
    user._set_password = password
    session.add(user)
    session.commit()
    session.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        "--username",
        default=os.getenv("USERNAME"),
        required=not(os.getenv("USERNAME")),
    )
    parser.add_argument(
        "--email",
        default=os.getenv("EMAIL"),
        required=not(os.getenv("EMAIL")),
    )
    parser.add_argument(
        "--password",
        default=os.getenv("PASSWORD"),
        required=not(os.getenv("PASSWORD")),
    )
    args = parser.parse_args()
    create(args.username, args.email, args.password)
