import re 

def extract_features(url):
    return {
        "url_length": len(url),
        "has_https": int(url.startswith("https")),
        "count_dots": url.count('.'),
        "count_at": url.count('@'),
        "count_hyphens": url.count('-'),
        "has_ip": int(re.search(r'\d+\.\d+\.\d+\.\d+', url) is not None),
        "suspicious_words": int(any(word in url.lower() for word in ['login', 'verify', 'update', 'secure', 'bank']))
    }
    
