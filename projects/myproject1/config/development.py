from config.default import *
from logging.config import dictConfig

#SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'bbs.db'))
SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{pw}@{uri}/{db}'.format(
    user = 'postgres',
    pw = '9906',
    uri = 'localhost',
    db = 'diary'
)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "dev"

dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/myproject.log'),
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
            'formatter': 'default',
        },
    },
    'root': {
        'level': 'INFO',
        'handlers': ['file']
    }
})