# books/views.py
from django.shortcuts import render
from django.http import HttpResponse
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient

def search_books(request):
    if request.method == 'POST':
        search_text = request.POST.get('search_text', '')

        # Azure Cognitive Searchサービスの情報
        service_endpoint = "https://sotuken-beta.search.windows.net"
        index_name = "book-search"
        api_key = "RvICL223LXinONIZB3GHMoQTP5MfmCUmoH4iav37B3AzSeA918fw"

        # クライアントの作成
        credential = AzureKeyCredential(api_key)
        client = SearchClient(service_endpoint, index_name, credential)

        # 検索クエリの実行
        results = client.search(search_text)

        # 検索結果をテンプレートに渡して表示
        return render(request, 'books/search_results.html', {'results': results, 'search_text': search_text})

    return render(request, 'books/search_books.html')
