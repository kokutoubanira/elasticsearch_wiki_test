import glob 
import json

from elasticsearch import Elasticsearch
from elasticsearch import helpers
import elasticsearch
# Elasticsearchクライアント作成
es = Elasticsearch("http://localhost:9200")
mapping = {
    "settings": {
        "analysis": {
        "filter": {
            "my_ngram": {
            "type": "ngram",
            "min_gram": 2,
            "max_gram": 3
            }
        },
        "analyzer": {
            "my_kuromoji_analyzer_ngram": {
            "type": "custom",
            "tokenizer": "kuromoji_tokenizer",
            "char_filter" : ["icu_normalizer"],
            "filter": ["kuromoji_stemmer","my_ngram"]
            },
            "my_kuromoji_analyzer_token": {
            "type": "custom",
            "tokenizer": "kuromoji_tokenizer",
            "char_filter" : ["icu_normalizer"],
                "filter": ["kuromoji_stemmer"]
            }
        }
        }
    },
    "mappings": {
        "properties": {
            "id": {"type": "keyword"},
            "title": {"analyzer": "my_kuromoji_analyzer_ngram","type": "text"},
            "url": {"type": "keyword"},
            "text_ngram": {"analyzer": "my_kuromoji_analyzer_ngram","type": "text"},
            "text_token": {"analyzer": "my_kuromoji_analyzer_token","type": "text"},
        }
    }
}
# es.indices.create(index='jpwiki', body=mapping)
import tqdm 
import time 

def create_documents():
    actions = []
    filelist = glob.glob("extracted/AA/*")
    for filename in tqdm.tqdm(filelist):
        with open(filename) as f:
            lines = f.readlines()
            for line in tqdm.tqdm(lines):
                j = json.loads(line)
                src = {"id":j["id"], "url":j["url"],'title':j['title'],'text_ngram':j['text'], 'text_token':j['text']}
                yield {'_index':"jpwiki",'_id':j['id'],'_source':src}

elasticsearch.helpers.bulk(es, actions=create_documents(),chunk_size=200)

