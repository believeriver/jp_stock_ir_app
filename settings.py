LOG_FILE = 'appserver.log'
PORT = 8000
DEBUG = False

if DEBUG:
    DB_NAME = 'test_db.sql'
else:
    DB_NAME = 'IRBank_database.sql'