import logging
import streamlit as st
from auth import auth

from config import *
from constants import *
from exceptions import *
from admin import *
from user import *


def main():
# Setup
    st.set_page_config(page_title = UIConstants.PAGE_TITLE, 
                    layout=UIConstants.LAYOUT)
                        # page_icon="./assets/images/icon.png")
    st.warning(UIConstants.WARNING)

    name, authentication_status, username, authenticator = auth()

    if authentication_status != True:
        if authentication_status is False:
            st.error('Username/password is incorrect.')
        st.info(UIConstants.CONTACT_INFO)

    # Main Page
    if authentication_status == True:
        if (username == "user"):
            user(authenticator, name)
        else:
            admin(authenticator, name)
        # else:
        #     st.write("admin")
        
if __name__ == "__main__":
    main()
                