from flask import Flask, render_template, request, url_for
from config import Config
from snowflake import connector
import pandas as pd

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def homepage():
    cur.execute('SELECT * FROM COLORS')
    rows = pd.DataFrame(cur.fetchall(), columns=['Color UID', 'Color Name'])

    dfhtml = rows.to_html()
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

# Snowflake
cnx = connector.connect(
    account=app.config['SNOWFLAKE_ACCOUNT'],
    user=app.config['SNOWFLAKE_USER'],
    password=app.config['SNOWFLAKE_PASSWORD'],
    warehouse='COMPUTE_WH',
    database='DEMO_DB',
    schema='PUBLIC'
)
cur = cnx.cursor()
# cur.execute('SELECT * FROM COLORS')
# rows=pd.DataFrame(cur.fetchall(),columns=['Color UID', 'Color Name'])
#
# # dataframe as html, built-in method for pandas dataframe
# dfhtml = rows.to_html()

app.run()
