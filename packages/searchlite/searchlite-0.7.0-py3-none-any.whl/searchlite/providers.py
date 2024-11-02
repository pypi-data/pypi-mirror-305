from .searcher import RealTimeGoogleSearchProvider

def google(query,max_urls=5,animation=False):
    search = RealTimeGoogleSearchProvider(animation=animation)
    return search.search(query,max_urls=max_urls)

def bing(query,max_urls=5,animation=False):
    search = RealTimeGoogleSearchProvider(search_provider="bing",
                                          animation=animation)
    return search.search(query, max_urls=max_urls)