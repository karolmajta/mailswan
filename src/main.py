from flask.ext.script import Manager
from flask.ext.migrate import MigrateCommand

import mailswan.wsgi
import mailswan.db
import mailswan.api

manager = Manager(mailswan.wsgi.app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
