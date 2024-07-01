# RAG Chatbot

Simple RAG Chatbot with upload document function. Built with GPT, Streamlit and langchain. This version uses Python 3.9.6. You will need your own openai API for this app to work.

## Short Demo Video

[![Short Demo Video](http://img.youtube.com/vi/4DiOteyRn18/0.jpg)](https://youtu.be/4DiOteyRn18)

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/jhjhajh/genaibootcampproj

cd genaibootcampproj
```
### 2. Create a virtual environment

Create a virtual environment to ensure that all the dependencies you install doesn't mess up your system.

```bash
# The second 'venv' is the name of the virtual environment. You can name it whatever you want.

python3 -m venv venv
```

Activate the virtual environment.

```bash
source venv/bin/activate
```
Deactivate the virtual environment.

```bash
deactivate
```
If you do not already have Pip installed, you can install it with the following command.

Unix/macOS
```bash
python3 -m pip install --upgrade pip
python3 -m pip --version
```
Windows:
```bash
py -m pip install --upgrade pip
py -m pip --version
```

Refer to this python [documentation](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) for more detailed information on virtual environments and pip installation.

### 3. Install Requirements and Setting up Environment Variables

```bash
pip install -r requirements.txt
```

Create a .env file in the root directory of the project.

Add the following lines to the .env file.

```bash
OPENAI_API_KEY=YOUR_OPENAI_API_KEY
PASSWORD=YOUR_LOGIN_PASSWORDS
```

Replace YOUR_OPENAI_API_KEY with your own openai API key.

Replace YOUR_LOGIN_PASSWORDS with your own login passwords.

### 4. Run the app

1. Starting the app
```bash
streamlit run main.py
```

If all your dependencies and requirements are installed correctly, you should be able to see the login page like in the demo video. 

Login Credentials:

Refer to config.yaml for username. You can put your desired password in the .env file. Note that the password will be shared across both "admin" and "user" accounts, unless you make modifications to the code.

2. Open your web browswer and go to http://localhost:8501/ unless you ran with another port.

3. Logging into admin account will enable the upload document function. If you login with a user account, you will only be able to chat with the bot.
