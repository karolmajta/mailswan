from flask.ext.script import Manager
from flask.ext.migrate import MigrateCommand

import wsgi
import db
import api

manager = Manager(wsgi.app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
