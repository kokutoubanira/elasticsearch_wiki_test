import glob 
import json
from elasticsearch import Elasticsearch
from elasticsearch import helpers

actions = []
filelist = glob.glob("extracted/AA/*")
for filename in filelist:
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            j = json.loads(line)
            src = {'title':j['title'],'text':j['text']}
            #actions.append({'_index':indexName,'_type':typeName,'_id':j['id'],'_source':src})
