import trafilatura

def blogtext(url):
    downloaded = trafilatura.fetch_url(url)
    result = trafilatura.extract(downloaded, include_comments=False, include_tables=True, no_fallback=True)
    return result
