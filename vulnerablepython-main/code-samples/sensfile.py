import requests
import logging
import configparser
import smtplib
import psycopg2

# Configuration file with sensitive data
config = configparser.ConfigParser()
config.read('config.ini')

# Sensitive database credentials hard-coded
db_conn = psycopg2.connect(
    database="mydb",
    user="dbuser",
    password="dbpassword",
    host="localhost",
    port="5432"
)

# Sensitive email credentials hard-coded
smtp = smtplib.SMTP("smtp.example.com")
smtp.login("user@example.com", "password123")

# Sensitive API key hard-coded
api_key = "my_secret_api_key"

# Logging sensitive data
logging.info(f"User password: {api_key}")


def connect_to_api():
    # Sensitive API key used in the header
    api_url = "https://api.example.com"
    response = requests.get(api_url, headers={"Authorization": "Bearer " + api_key})

    if response.status_code == 200:
        return response.json()
    else:
        return "Failed to connect to the API"


# Imagine this function is used elsewhere in the code
data = connect_to_api()
print(data)

# ##InstructLLM response:
# 1. Hard-coded sensitive data: The code hard-codes sensitive data such as the database credentials, email credentials, and API key in the code itself. This means that if the code is compromised, an attacker could easily access these sensitive details.
# 2. Logging sensitive data: The code logs sensitive data such as the API key using the logging module. This could potentially expose the sensitive data if the logs are not properly secured.
