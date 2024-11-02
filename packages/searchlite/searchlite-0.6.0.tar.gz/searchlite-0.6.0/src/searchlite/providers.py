from .searcher import RealTimeGoogleSearchProvider

def google(query,max_urls=5,animation=False):
    search = RealTimeGoogleSearchProvider(animation=animation)
    return search.search(query,max_urls=max_urls)

def bing(query,max_urls=5,animation=False):
    search = RealTimeGoogleSearchProvider(search_provider="bing",
                                          animation=animation)
    return search.search(query, max_urls=max_urls)

def duckduckgo(query,max_urls=5,animation=False):
    search = RealTimeGoogleSearchProvider(search_provider="duckduckgo",
                                          animation=animation)
    return search.search(query, max_urls=max_urls)

def yahoo(query,max_urls=5,animation=False):
    search = RealTimeGoogleSearchProvider(search_provider="yahoo",
                                          animation=animation)
    return search.search(query, max_urls=max_urls)

def ask(query,max_urls=5,animation=False):
    search = RealTimeGoogleSearchProvider(search_provider="ask",
                                          animation=animation)
    return search.search(query, max_urls=max_urls)