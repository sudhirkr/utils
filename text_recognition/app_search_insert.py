from elastic_app_search import Client
import json
client = Client(
    base_endpoint='34.87.101.217:3002/api/as/v1',
    api_key='private-15enfbz3zdf59jvchr94mu7k',
    use_https=False
)

engine_name = "sensitive-data-engine"

# load data from json file
with open("outfile.json", "r") as fp:
    documents = json.load(fp)


print (documents)

# update the appsearch
client.index_documents(engine_name, documents)

