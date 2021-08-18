from SPARQLWrapper import SPARQLWrapper, JSON
from pprint import pprint
sparql = SPARQLWrapper("http://localhost:8000/repositories/semantic")
sparql.setQuery("""select * from <http://go.org> 
where { ?s ?p ?o.}""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()
pprint(results)
# for result in results["results"]["bindings"]:
#     print(result["label"]["value"])

print('---------------------------')

for result in results["results"]["bindings"]:
    print('%s: %s' % (result["label"]["xml:lang"], result["label"]["value"]))
