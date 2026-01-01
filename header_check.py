import requests

def check_headers(url):
    response = requests.get(url, timeout=5)
    headers = response.headers

    security_headers = [
        "X-Frame-Options",
        "Content-Security-Policy",
        "X-XSS-Protection",
        "Strict-Transport-Security"
    ]

    missing = []

    for h in security_headers:
        if h not in headers:
            missing.append(h)

    return missing
