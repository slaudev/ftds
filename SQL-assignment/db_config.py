import configparser
import mysql.connector

def get_db_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    db_config = {
        'host': config['mysql']['host'],
        'port': config['mysql']['port'],
        'user': config['mysql']['user'],
        'password': config['mysql']['password'],
        'database': config['mysql']['database']
    }
    return db_config

def connect_to_db():
    db_config = get_db_config()
    connection = mysql.connector.connect(
        host=db_config['host'],
        port=db_config['port'],
        user=db_config['user'],
        password=db_config['password'],
        database=db_config['database']
    )
    return connection
