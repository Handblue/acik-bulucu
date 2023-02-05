import requests
import re

def scan_dorks(dorks, pages=1):
    for dork in dorks:
        for page in range(pages):
            
            url = f'https://www.google.com/search?q={dork}&start={page * 10}'
            response = requests.get(url)
            content = response.content.decode(errors='ignore', encoding='latin-1')
            
            for match in re.finditer(r'<a href="(https?://[^"]+)"', content):
                url = match.group(1)
               
                response = requests.get(url)
                content = response.content.decode(errors='ignore', encoding='latin-1')
                
                if any(keyword in content.lower() for keyword in ('sql injection', 'xss vulnerability', 'command injection', 'remote code execution')):
                    print(f'{url} - Açık bulundu')
                else:
                    print(f'{url} - Açık bulunamadı')

scan_dorks(['inurl:index.php?id=', 'inurl:product.php?id=', 'inurl:article.php?id='], pages=2)
