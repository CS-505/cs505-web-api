import logging
import os

DEBUG = os.getenv("ENVIRONEMENT") == "DEV"
APPLICATION_ROOT = os.getenv("APPLICATION_APPLICATION_ROOT", "/application")
HOST = os.getenv("APPLICATION_HOST")
PORT = int(os.getenv("APPLICATION_PORT", "3000"))
SQLALCHEMY_TRACK_MODIFICATIONS = False

DB_CONTAINER = os.getenv("APPLICATION_DB_CONTAINER", "db")
POSTGRES = {
    "user": os.getenv("MYSQL_USER", "root"),
    "pw": os.getenv("MYSQL_PASSWORD", ""),
    "host": DB_CONTAINER,
    "port": os.getenv("APPLICATION_MYSQL_PORT", 3306),
    "db": os.getenv("MYSQL_DATABASE", "mysql"),
}

DB_URI = "mysql+mysqldb://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s" % POSTGRES

logging.basicConfig(
    filename=os.getenv("SERVICE_LOG", "server.log"),
    level=logging.DEBUG,
    format="%(levelname)s: %(asctime)s \
        pid:%(process)s module:%(module)s %(message)s",
    datefmt="%d/%m/%y %H:%M:%S",
)
