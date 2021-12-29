import urllib.parse

def get_domain(url):
    netloc = urllib.parse.urlparse(url).netloc

    return ".".join(netloc.split(".")[-2:])

def get_subdomain(url):
    netloc = urllib.parse.urlparse(url).netloc

    return ".".join(netloc.split(".")[:-2])
