from flask_script import Server, Manager
from flask_migrate import Migrate, MigrateCommand
from app.app import app, db


manager = Manager(app)
migrate = Migrate(app, db)

server = Server(host="0.0.0.0", port=5000)

manager.add_command("db", MigrateCommand)


@manager.command
def runserver():
    app.run(debug=True, host="0.0.0.0", port=5000, use_reloader=True)


if __name__ == "__main__":
    manager.run()
