from elasticsearch import Elasticsearch, helpers
import json
import sys
es = Elasticsearch('http://seer.r-pkg.org:9200')
# page = es.search(index='cran', doc_type='cran',
#                 scroll='2m', search_type='scan', q='*')
# sid = page['_scroll_id']
# scroll_size = page['hits']['total']

'''
query = {
    'query': {
        "bool": {
            "must": [
                {
                    "match": {"_source.Package": "ggplot2"}
                },
            ]
        }
    }
}
'''
# print(query)
'''
gene = helpers.scan(
    es,
    scroll='2m',
    q='*',
    index='cran', doc_type='cran',
)
'''
result = []
for packagename in sys.stdin:

    l = es.search(q="Package:" + packagename.strip())
    for th in range(int(l['hits']['total'])):
        # print(th)
        # print()
        # try:
        result += l['hits']['hits']
        # print(type(l))
        # json.loads(l)
        # print(l['hits']['hits'][th]['_source']['Author'])
        # except Exception as e:
        #print(packagename.strip() + ' ERROR!\n' + e.message)
f = open('R_CRAN_fromMetaCRAN', 'w')
json.dump(result, f)
f.close()
print(len(result))


# page = es.scroll(scroll_id=sid, scroll='2m')
