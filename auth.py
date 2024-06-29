from config import *
from constants import *

import streamlit as st
import streamlit_authenticator as stauth

import yaml
from yaml.loader import SafeLoader

import os

# Simple authentication
load_dotenv()
password = os.getenv('PASSWORD')


def auth():
    with open('config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)

    for username in config['credentials']['usernames']:
        config['credentials']['usernames'][username]['password'] = password

    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
    )

    name, authentication_status, username = authenticator.login()
    return name, authentication_status, username, authenticator