from flask import Flask
from snowflake import connector
import pandas as pd

app = Flask("my website")

@app.route('/')
def homepage():
    return 'Welcome to my website! My Snowflake Acct # is: ' + str(onerow)

# Snowflake
cnx = connector.connect(
    account='BLANK',
    user='BLANK',
    password='BLANK'
)
cur = cnx.cursor()
cur.execute('SELECT current_account()')
onerow = cur.fetchone()

app.run()
