from flask import Flask, render_template, request, url_for
from snowflake import connector
import pandas as pd

app = Flask("my website")

@app.route('/')
def homepage():
    return render_template('index.html', colors_table = dfhtml)

@app.route('/submit')
def submitpage():
    return render_template('submit.html')

@app.route('/thanks4submit', methods=['POST'])
def thanks4submit():
    colorname = request.form.get('cname')
    username = request.form.get('uname')
    return render_template('thanks4submit.html'
                        , colorname=colorname
                        , username=username)

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

# dataframe as html, built-in method for pandas dataframe
dfhtml = rows.to_html()

app.run()
