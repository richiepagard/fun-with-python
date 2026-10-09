import re


def subdomain_extractor(url: str) -> set:
    """
    Extract the main subdomain (or a list of subdomains) from a given URL.

    The function accepts a full URL (with or without scheme such as http/https)
    or a plain domain starting with "www.". It normalizes the input, removes
    the scheme if present, and returns:
      - The first subdomain (e.g. "subdomain" for "https://subdomain.example.com")
      - "www" for standard www-based domains (e.g. "www.example.com")
      - A descriptive string if multiple subdomains are present.

    Parameters:
        url (str): The full URL or domain to extract the subdomain from.

    Returns:
        set: List of all subdomains in the gotten URL.
    """
    subdomains = set()
    url = url.lower().strip()

    if url.startswith('http'):
        # Removes the 'http' and 'https' from the URL
        url = re.sub(r'^https?://', '', url, count=1)
        domain = url.split("/")[0]
        parts = domain.split(".")

        # Validate the URL, it must be at least subdomain + domain + tld
        if len(parts) <= 2:
            return set()

        # Get all subdomains excluding the last two segments
        subdomains = set(sub for sub in parts[:-2])
        return subdomains


def main():
    """
    Main function to run the subdomain extractor and get URL from the user input
    Logs the extracted subdomain information, user inputs, and exceptions.
    """
    url = input('Enter your url here: ')
    subdomain = subdomain_extractor(url.lower())

    print(subdomain)


if __name__ == '__main__':
    main()
