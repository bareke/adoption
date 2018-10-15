from adoption.app import db
from adoption.app import create_app
from adoption.models import *

app = create_app()


@app.shell_context_processor
def make_shell_context():
    """
    Create an environment variable that points to shell.py to import the models automatically and use them with the command flask shell
    """
    return {
            'db': db,
            'Adoption': Adoption,
            'Client': Client,
            'Contact': Contact,
            'Image': Image,
            'Pet': Pet,
            'Register': Register,
            'User': User
            }
