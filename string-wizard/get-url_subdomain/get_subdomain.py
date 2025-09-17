import re

url = input('Enter your url here: ')

def subdomain_extractor(url: str) -> str | None:
    if url.startswith('http'):
        # Extract the subdomain using regex
        match = re.search(r'(?<=https://).*', url)
        if match:
            subdomain = match.group(1).split('.')[0]
            return subdomain
        else:
            return None


if __name__ == '__main__':
    subdomain = subdomain_extractor(url)