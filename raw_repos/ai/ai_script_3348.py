def get_title(url): 
    url_parsed = urlparse(url)
    query_parsed = parse_qs(url_parsed.query)
    title = query_parsed['q'][0]
    return title

print(get_title(url))

# Output: GPT 3