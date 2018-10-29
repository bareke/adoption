from flask_testing import TestCase

from adoption.app import db
from adoption.app import create_app
from adoption.config.testing import TestingConfig
from adoption.models import *


class TestBase(TestCase):

    def create_app(self):
        app = create_app(TestingConfig)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        # db.drop_all()


class TestModel(TestBase):

    def test_1_client_model(self):
        client = Client(name='Guido van', last_name='Rossum', telephone=123456)
        db.session.add(client)
        db.session.commit()

        assert client in db.session

    def test_2_pet_model(self):
        pet = Pet(name='Monty python', type='cat', age=3, gender='m')
        db.session.add(pet)
        db.session.commit()

        assert pet in db.session

    def test_3_contact_model(self):
        client = Client.query.get(1)

        contact = Contact(address='742',
                          neighborhood='Evergreen terrace',
                          department='Springfield')
        contact.client = client

        db.session.add(contact)
        db.session.commit()

        assert contact in db.session

    def test_4_image_client(self):
        client = Client.query.get(1)

        image = Image(name='profile_client.png', url='example/img/profile.png')
        image.client = client

        db.session.add(image)
        db.session.commit()

        assert image in db.session

    def test_5_image_pet(self):
        pet = Pet.query.get(1)

        image = Image(name='profile_pet.png', url='example/img/profile.png')
        image.pet = pet

        db.session.add(image)
        db.session.commit()

        assert image in db.session

    def test_6_user_model(self):
        client = Client.query.get(1)

        user = User(username='nickname',
                    email='example@example.com',
                    password='pass')
        user.client = client

        db.session.add(user)
        db.session.commit()

        assert user in db.session

    def test_7_register_model(self):
        client = Client.query.get(1)
        pet = Pet.query.get(1)

        register = Register(comment='this is comment')
        register.old_owner = client
        register.old_pet = pet

        db.session.add(register)
        db.session.commit()

        assert register in db.session

    def test_8_adoption_model(self):
        client = Client(name='Richard', last_name='Stallman', telephone=987765)
        pet = Pet.query.get(1)

        adoption = Adoption()
        adoption.new_owner = client
        adoption.new_pet = pet

        db.session.add(client)
        db.session.add(adoption)
        db.session.commit()

        assert adoption in db.session
