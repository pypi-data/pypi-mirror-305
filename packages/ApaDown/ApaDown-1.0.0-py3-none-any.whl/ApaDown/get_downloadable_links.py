import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

def get_links(base_url=None, output_file='./links.txt'):
    """
    Spider a website to find links to specific file types and save them to a file.
    
    Args:
        base_url (str): The base URL to start crawling from
        output_file (str): The file to save the links to
    """
    if base_url is None:
        return set()
    visited = set()
    file_links = set()
    
    file_patterns = r'\.(csv|zip|rar|gz|pdf|pcap|py|txt|ipynb)$'
    
    def crawl(url):
        if url in visited:
            return
        
        visited.add(url)
        
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            for link in soup.find_all('a', href=True):
                href = link['href']
                full_url = urljoin(url, href)
                
                if base_url in full_url:
                    if re.search(file_patterns, full_url, re.IGNORECASE):
                        file_links.add(full_url)
                    elif not re.search(file_patterns, full_url, re.IGNORECASE):
                        crawl(full_url)
                        
        except Exception as e:
            print(f"Error crawling {url}: {str(e)}")
    
    crawl(base_url)
    
    with open(output_file, 'w') as f:
        for link in sorted(file_links):
            f.write(f"{link}\n")

    
    
    print(f"Found {len(file_links)} file links. Results saved to {output_file}")

    return file_links, output_file
