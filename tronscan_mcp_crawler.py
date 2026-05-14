import requests
from bs4 import BeautifulSoup
import markdownify
import os
import time

BASE_URL = "https://mcpdoc.tronscan.org"
OUTPUT_DIR = "tronscan_mcp_docs_md"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def scrape_page(url, filepath):
    print(f" Extraindo: {url} -> {filepath}")
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # O Nextra guarda o conteúdo limpo aqui
        content = soup.find('main', {'data-pagefind-body': 'true'}) or soup.find('article')
        
        if content:
            md_content = markdownify.markdownify(str(content), heading_style="ATX")
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(f"\n\n")
                f.write(md_content)
        time.sleep(0.5)
    except Exception as e:
        print(f"[!] Erro ao raspar {url}: {e}")

def crawl_mcp():
    print(f"\n[*] Hackeando o Nextra do TronScan MCP a partir de: {BASE_URL}...")
    try:
        response = requests.get(BASE_URL + "/en/mcp", headers=HEADERS)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        
        # O Nextra renderiza todos os links na barra lateral (tag <a>)
        links = soup.find_all('a', href=True)
        visited_urls = set()
        
        for link in links:
            href = link['href']
            
            # Queremos apenas as rotas de documentação
            if not href.startswith('/en/'):
                continue
                
            clean_href = href.split('#')[0]
            
            if clean_href in visited_urls:
                continue
                
            visited_urls.add(clean_href)
            full_url = BASE_URL + clean_href
            
            # Cria a estrutura de pastas (ex: /en/api/account -> Api / Account.md)
            path_parts = [p for p in clean_href.split("/") if p]
            
            # Remove o "en" da pasta
            if len(path_parts) > 1 and path_parts[0] == 'en':
                path_parts = path_parts[1:]
                
            filename = f"{path_parts.pop()}.md".replace("-", " ").title()
            
            if path_parts:
                dir_path = os.path.join(OUTPUT_DIR, *[p.title() for p in path_parts])
            else:
                dir_path = OUTPUT_DIR
                
            os.makedirs(dir_path, exist_ok=True)
            filepath = os.path.join(dir_path, filename)
            
            scrape_page(full_url, filepath)
            
    except Exception as e:
        print(f"[!] Erro crítico ao acessar TronScan MCP: {e}")

def main():
    print("=============================================")
    print("🤖 INICIALIZANDO CRAWLER DO TRONSCAN MCP 🤖")
    print("=============================================")
    crawl_mcp()
    print("\n[*] Extração do MCP Concluída! O GlitchTRON agora pode se plugar à IA.")

if __name__ == "__main__":
    main()
