from config.default import *

#SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{pw}@{uri}/{db}'.format(
    user = 'postgres',
    pw = '9906',
    uri = 'localhost',
    db = 'pybo'
)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "dev"