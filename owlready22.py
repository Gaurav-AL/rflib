from owlready2 import *
from pprint import pprint
# local machine files
onto = get_ontology("/path.to.your.file/wine.rdf").load()


pprint(list(default_world.sparql("""
	SELECT (COUNT(*) as ?Triples)WHERE {
	?s ?p ?o.
	}""")))
