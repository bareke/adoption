from adoption.app import create_app
from adoption.views.home import home

if __name__ == '__main__':
    app = create_app()
    app.register_blueprint(home)

    app.run()
