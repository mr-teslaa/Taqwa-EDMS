# ========================================================================== #
#                           Junior School and College
#                    A School Management System with FLASK
#   
#       Create by some intelligent programmer
#       Full CRUD facility
#   
#       Github: https://github.com/mr-teslaa/Junior_School_and_College
# ========================================================================== #

from flask import Flask

def create_app(config_file="config.py"):

    app = Flask(__name__)
    app.config.from_pyfile(config_file)

    with app.app_context():
        from .models import db
        db.init_app(app)
        print(f"DB: {db.engine}")

        from .commands import create_tables
        app.cli.add_command(create_tables)

        # from . import algemeen
        from .login         import login
        from .login_parents import login_parents
        from .admission     import admission
        from .apply_parents import apply_parents
        from .apply_teacher import apply_teacher

        from .              import routes

        app.register_blueprint(login.login_bp)
        app.register_blueprint(login_parents.login_parents_bp)
        app.register_blueprint(admission.admission_bp)
        app.register_blueprint(apply_parents.apply_parents_bp)
        app.register_blueprint(apply_teacher.apply_teacher_bp)

        # print(f"APP: {app.url_map}")

    return app
