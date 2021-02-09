from flask import Flask, render_template
from snowflake import connector
import pandas as pd

app = Flask("my website")

@app.route('/')
def homepage():
    return render_template('index.html', colors_table = dfhtml)

# Snowflake
cnx = connector.connect(
    account='BLANK',
    user='BLANK',
    password='BLANK',
    warehouse='COMPUTE_WH',
    database='DEMO_DB',
    schema='PUBLIC'
)
cur = cnx.cursor()
cur.execute('SELECT * FROM COLORS')
rows=pd.DataFrame(cur.fetchall(),columns=['Color UID', 'Color Name'])
# print(rows)

# test dataframe as html, built-in method for pandas dataframe
dfhtml = rows.to_html()
print(dfhtml)

app.run()
