import os


class Config:
    basedir = os.path.abspath(os.path.dirname(__file__))
    DEBUG=1
    SECRET_KEY="ASdasd212312askzxvlzm1k231WL1241k2mkgbdszvmx054"
    # sqlalchemy database config
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    # SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
    # SQLALCHEMY_TRACK_MODIFICATIONS = False

    print("ENV", os.getenv('VK_REDIRECT_URI'))
    # oauth vk config
    OAUTH_CREDENTIALS = {
        'vk': {
            'client_id': os.getenv('VK_CLIENT_ID') or "unknown",
            'client_secret': os.getenv('VK_CLIENT_SECRET') or "unknown",
            'redirect_uri': os.getenv('VK_REDIRECT_URI') or "unknown"
        },
    }
