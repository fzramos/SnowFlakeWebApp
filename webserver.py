# Import packages
from flask import Flask, render_template, request, url_for
from config import Config
from snowflake import connector
import pandas as pd

# Flask Web Application
app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def homepage():
    cur.execute('SELECT COLOR_NAME, COUNT(*) '\
                + 'FROM COLORS '\
                + 'GROUP BY COLOR_NAME '\
                + 'HAVING COUNT(*)>50'\
                + 'ORDER BY COUNT(*) DESC; ')
    rows = pd.DataFrame(cur.fetchall(), columns=['Color Name', 'Votes'])
    # dataframe as html, built-in method for pandas dataframe
    dfhtml = rows.to_html(index=False)
    return render_template('index.html', colors_table = dfhtml)

@app.route('/submit')
def submitpage():
    return render_template('submit.html')

@app.route('/thanks4submit', methods=['POST'])
def thanks4submit():
    colorname = request.form.get('cname')
    username = request.form.get('uname')
    cur.execute('INSERT INTO COLORS(COLOR_UID, COLOR_NAME) '
                + 'SELECT COLOR_UID_SEQ.nextval, ' + "'" + colorname
                + "';")
    return render_template('thanks4submit.html'
                        , colorname=colorname
                        , username=username)

@app.route('/coolcharts')
def coolcharts():
    cur.execute('SELECT COLOR_NAME, COUNT(*) '\
                + 'FROM COLORS '\
                + 'GROUP BY COLOR_NAME '\
                + 'ORDER BY COUNT(*) DESC; ')
    data4Charts = pd.DataFrame(cur.fetchall(), columns=['color', 'votes'])
    data4Charts.to_csv('data4charts.csv', index=False)
    data4ChartsJSON = data4Charts.to_json('data4ChartsJSON.json', orient='records')
    return render_template('coolcharts.html')

# Snowflake
cnx = connector.connect(
    account=app.config['SNOWFLAKE_ACCOUNT'],
    user=app.config['SNOWFLAKE_USER'],
    password=app.config['SNOWFLAKE_PASSWORD'],
    warehouse='COMPUTE_WH',
    database='DEMO_DB',
    schema='PUBLIC'
)
# or could use snowflakeConnection.py
# from snowflakeConnection import sfconnect
# cnx = sfconnect()

cur = cnx.cursor()

app.run()
