# ========================================================================== #
#                           Junior School and College
#                    A School Management System with FLASK
#
#       Create by some intelligent programmer
#       Full CRUD facility
#
#       Github: https://github.com/mr-teslaa/Junior_School_and_College
# ========================================================================== #

from main_app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)