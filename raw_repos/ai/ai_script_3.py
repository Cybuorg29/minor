def get_domain_name(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc