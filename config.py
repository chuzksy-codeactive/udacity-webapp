import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'articlestoragev1'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or '9Tf/G/70orV3s1HFjGSEC6pLUhzivmJkohkRzuzRwnyFl4dBVK99xXFSoFXw4P9dSiFLG130p81L+ASt98RykQ=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'articleimages'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'chuzksy.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'articles'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'chuzksyadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Admin123@'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    CLIENT_SECRET = "HxV8Q~UJoVxcVEnALta0cQzgxcwfVoawPIOIFc~i"
    CLIENT_ID = "e25d35da-984f-4291-b136-85ccc23cff05"
    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD
    ENDPOINT = 'https://graph.microsoft.com/v1.0/users' 
    SCOPE = ["User.ReadBasic.All"] # Only need to read user profile for this app
    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session