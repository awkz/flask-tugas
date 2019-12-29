#!/usr/bin/env python
import os
import time
import subprocess

from flask_script import Manager, Shell
from flask_assets import ManageAssets

from app import create_app
from config import Config

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)


def make_shell_context():
    return dict(app=app)


manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command("assets", ManageAssets())

@manager.command
def format():
    """Runs the yapf and isort formatters over the project."""
    isort = 'isort -rc *.py app/'
    yapf = 'yapf -r -i *.py app/'

    print('Running {}'.format(isort))
    subprocess.call(isort, shell=True)

    print('Running {}'.format(yapf))
    subprocess.call(yapf, shell=True)


if __name__ == '__main__':
    manager.run()