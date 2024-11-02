from .searcher import RealTimeGoogleSearchProvider

def google(query,max_urls=5):
    search = RealTimeGoogleSearchProvider()
    return search.search(query,max_urls=max_urls)

def bing(query,max_urls=5):
    search = RealTimeGoogleSearchProvider(search_provider="bing")
    return search.search(query, max_urls=max_urls)

def duckduckgo(query,max_urls=5):
    search = RealTimeGoogleSearchProvider(search_provider="duckduckgo")
    return search.search(query, max_urls=max_urls)

def yahoo(query,max_urls=5):
    search = RealTimeGoogleSearchProvider(search_provider="yahoo")
    return search.search(query, max_urls=max_urls)

def ask(query,max_urls=5):
    search = RealTimeGoogleSearchProvider(search_provider="ask")
    return search.search(query, max_urls=max_urls)