from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient

endpoint = "https://sotuken-beta.search.windows.net/"
key = "RvICL223LXinONIZB3GHMoQTP5MfmCUmoH4iav37B3AzSeA918fw"

credential = AzureKeyCredential(key)

client = SearchClient(endpoint=endpoint,index_name="book-search",credential=credential)

search_text = "Azure Search Tutorial"
search_results = client.search(search_text)

for result in search_results:
    print(result)