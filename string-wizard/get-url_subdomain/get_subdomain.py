import re

url = input('Enter your url here: ')

def subdomain_extractor(url: str) -> str | None:
    if url.startswith('http'):
        # Extract the subdomain using regex
        match1 = re.search(r'(?<=https://).*', url)
        match2 = re.search(r'(?<=http://).*', url)

        if match1 or match1:
            subdomain = match1.group(0).split('.')[0]
            return subdomain
            
        elif match1 or match2:
            subdomain = match2.group(0).split('.')[0]
            return subdomain
            

if __name__ == '__main__':
    subdomain = subdomain_extractor(url)
