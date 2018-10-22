from flask_script import Manager
from flask_migrate import Migrate
from flask_migrate import MigrateCommand
from mixer.backend.flask import Mixer

from adoption.app import db
from adoption.app import create_app
from adoption.models import *

app = create_app()
manager = Manager(app)


@manager.option('-c', '--count', help='populate database with fake data')
def populate(count):
    mixer = Mixer(app)
    count = int(count)

    models = [Client, Contact]

    for model in models:
        mixer.cycle(count).blend(model)

    mixer.cycle(count).blend(Pet,
                             neutering=mixer.sequence(True, False, None),
                             gender=mixer.sequence('m', 'f')
                             )

    pets = Pet.query.limit(count)
    clients = Client.query.limit(count)

    mixer.cycle(count).blend(Register,
                             comment=mixer.RANDOM,
                             old_owner=(client for client in clients),
                             old_pet=(pet for pet in pets),
                             )
    mixer.cycle(count).blend(Adoption,
                             status='in process',
                             new_owner=(client for client in clients),
                             new_pet=(pet for pet in pets)
                             )

    mixer.cycle(count).blend(Image, pet=(pet for pet in pets))
    mixer.cycle(count).blend(Image, client=(client for client in clients))

    clients = Client.query.all()
    mixer.cycle(len(clients)).blend(User, client=(client for client in clients))


if __name__ == '__main__':
    migrate = Migrate(app, db)
    manager.add_command('db', MigrateCommand)

    manager.run()
