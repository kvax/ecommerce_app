from elasticsearch import Elasticsearch
from config import Config

es = Elasticsearch([Config.ELASTICSEARCH_URL])

def index_product(product):
    es.index(index="products", id=product['id'], body=product)

def search_product(query):
    results = es.search(index="products", body={"query": {"match": {"name": query}}})
    return [hit['_source'] for hit in results['hits']['hits']]
