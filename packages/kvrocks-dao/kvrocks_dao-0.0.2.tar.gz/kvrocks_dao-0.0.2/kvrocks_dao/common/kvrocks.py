from redis import Redis
from dotenv import load_dotenv
import os
from kvrocks_cli_hoangtran.common.entity import KvEntity
import kvrocks_cli_hoangtran.common.utils as utils

load_dotenv()

HOST = os.getenv("KVROCK_HOST")
PORT = os.getenv("KVROCK_PORT")


class Kvrocks:
    def __init__(self):
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
