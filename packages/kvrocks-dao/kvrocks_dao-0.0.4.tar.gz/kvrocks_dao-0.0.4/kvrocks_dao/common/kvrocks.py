from redis import Redis

# from dotenv import load_dotenv
import os
from kvrocks_dao.common.entity import KvEntity
import kvrocks_dao.common.utils as utils
import configparser

config = configparser.ConfigParser()

config.read("config.ini")

# load_dotenv()

HOST = config["kvrocks"]["host"]
PORT = config["kvrocks"]["port"]

print(f"HOST: {HOST} - PORT {PORT}")


class Kvrocks:
    def __init__(self):

        h = config["kvrocks"]["host"]
        p = config["kvrocks"]["port"]

        print(f"h: {h} - p {p}")

        self.conn = Redis(host=HOST, port=PORT, decode_responses=True)
        print(f"Connected to kvrocks on port {PORT}")

    def __del__(self):
        self.conn.close()
        print(f"Connection closed")


class KvDao:
    def __init__(self, name, conn):
        self.conn = conn
        self.name = name
        if self.conn == None:
            self.conn = Redis(host=HOST, port=PORT, decode_responses=True)
            print(f"Dao Connected to kvrocks on port {PORT}")

    def __del__(self):
        self.conn.close()
        print(f"Dao Connection closed")

    def set(self, document: KvEntity):
        key = utils.gen_key(self.name, document._id)
        return self.conn.set(key, document.name)

    def get(self, _id: int):
        return self.conn.get(utils.gen_key(self.name, _id))

    def mget(self, _ids: list[int]):
        ls = []
        for _id in _ids:
            ls.append(self.get(_id))
        return ls
