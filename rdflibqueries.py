from SPARQLWrapper import SPARQLWrapper, JSON
from rdflib.plugins.stores.sparqlstore import SPARQLUpdateStore
import rdflib
from requests.auth import HTTPDigestAuth
ENDPOINT = "http://gaurav-HP-Notebook:8000/repositories/semantic"

store = SPARQLUpdateStore(queryEndpoint=ENDPOINT, update_endpoint=ENDPOINT, context_aware=True,
                              postAsEncoded=False)
store.setReturnFormat(JSON)
store.method = 'POST'
g = Graph(store=store, identifier=config.DEFAULT_GRAPH_URI)

set_store_header_update(store)
g.add((URIRef('http://wine.org/manual'), RDF.type, OWL.Ontology))

set_store_header_read(store)
for triple in g.triples((None, None, None)):
    print(triple)
