import configparser
import snowflake.connector

def get_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['snowflake']

def get_connection():
    cfg = get_config()
    conn = snowflake.connector.connect(
        user=cfg['user'],
        password=cfg['password'],
        account=cfg['account'],
        warehouse=cfg['warehouse'],
        database=cfg['database'],
        schema=cfg['schema']
    )
    return conn
