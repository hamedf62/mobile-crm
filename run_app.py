from sys import exit
from decouple import config
from backend.app.config import config_dict
from backend.app import create_app

# from flask import g
# from flask_cors import CORS

# WARNING: Don't run with debug turned on in production!
DEBUG = config("DEBUG", default=True, cast=bool)

# The configuration
get_config_mode = "Debug" if DEBUG else "Production"

try:

    # Load the configuration using the default values
    app_config = config_dict[get_config_mode.capitalize()]

except KeyError:
    exit("Error: Invalid <config_mode>. Expected values [Debug, Production] ")

app = create_app(app_config)
# Session(app)
# enable CORS
# CORS(app, resources={r"/*": {"origins": "*"}})
# CORS(app)
# Migrate(app, db)

if DEBUG:
    app.logger.info("DEBUG       = " + str(DEBUG))
    app.logger.info("Environment = " + get_config_mode)
    # app.logger.info('DBMS        = ' + app_config.SQLALCHEMY_DATABASE_URI)

if __name__ == "__main__":
    # input(g.lang_code)
    app.run(
        # host="localhost",
        # host="0.0.0.0",
        port=5050,
        # ssl_context="adhoc"
        # ssl_context=(
        #     "/etc/letsencrypt/live/terms.sau.ac.ir/fullchain.pem",
        #     "/etc/letsencrypt/live/terms.sau.ac.ir/privkey.pem",
        # )
        # fuser 5000/tcp -k
    )
