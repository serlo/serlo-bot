import urllib.parse

def get_domain(url):
    return ".".join(get_domain_parts(url)[-2:])

def get_subdomain(url):
    return ".".join(get_domain_parts(url)[:-2])

def get_domain_parts(url):
    return urllib.parse.urlparse(url).netloc.split(".")
