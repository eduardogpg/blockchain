from app import create_app

from flask_script import Manager

class DevelopmentConfig():
    DEBUG = True

app = create_app(DevelopmentConfig)

if __name__ == '__main__':
    manager = Manager(app)
    manager.run()
