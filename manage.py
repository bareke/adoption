from flask_script import Manager
from flask_migrate import Migrate
from flask_migrate import MigrateCommand

from adoption.app import db
from adoption.app import create_app

migrate = Migrate()


def create_manager():
    app = create_app()
    migrate.init_app(app, db)
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)

    return manager


if __name__ == '__main__':
    manager = create_manager()
    manager.run()
