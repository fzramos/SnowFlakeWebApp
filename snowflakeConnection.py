# not used because I went with .env to protect snowflake credentials
# from snowflake import connector

# def sfconnect():
#     cnx = connector.connect(
#         account=app.config['SNOWFLAKE_ACCOUNT'],
#         user=app.config['SNOWFLAKE_USER'],
#         password=app.config['SNOWFLAKE_PASSWORD'],
#         warehouse='COMPUTE_WH',
#         database='DEMO_DB',
#         schema='PUBLIC'
#     )
#     return cnx
# )