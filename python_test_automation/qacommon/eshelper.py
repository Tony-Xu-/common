from elasticsearch import Elasticsearch

class ESUtil:
    hosts = [
        "https://user:password@ip:port",
        "https://user:password@ip:port",
        "https://user:password@ip:port"
    ]

    def __init__(self):
        self.es = Elasticsearch(self.hosts, verify_certs=False, timeout=60)
        self.index = "es-index-*"
