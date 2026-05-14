import requests
from bs4 import BeautifulSoup
import markdownify
import os
import time

BASE_DOMAIN = "https://doc.winklink.org"
START_PAGE = "/v2/doc/"
OUTPUT_DIR = "winklink_docs_md"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def scrape_page(url, filepath):
    print(f" Extraindo: {url} -> {filepath}")
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # O VuePress envelopa o conteúdo útil aqui
        content = soup.find('div', class_='theme-default-content') or soup.find('main', class_='page')
        
        if content:
            md_content = markdownify.markdownify(str(content), heading_style="ATX")
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(f"\n\n")
                f.write(md_content)
        time.sleep(0.5)
    except Exception as e:
        print(f"[!] Erro ao raspar {url}: {e}")

def crawl_winklink():
    print(f"\n[*] Mapeando Oráculos WINkLink a partir de: {BASE_DOMAIN}{START_PAGE}...")
    try:
        response = requests.get(BASE_DOMAIN + START_PAGE, headers=HEADERS)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Pega a barra lateral do VuePress
        sidebar = soup.find('ul', class_='sidebar-links')
        if not sidebar:
            print("[!] Barra lateral do WINkLink não encontrada.")
            return

        os.makedirs(OUTPUT_DIR, exist_ok=True)
        
        links = sidebar.find_all('a', class_='sidebar-link')
        visited_urls = set()
        
        for link in links:
            href = link.get('href')
            if not href: continue
            
            # Corta as âncoras (#) para não raspar a mesma página múltiplas vezes
            clean_href = href.split('#')[0]
            
            # Só aceita links que comecem com /v2/doc/
            if clean_href in visited_urls or not clean_href.startswith('/v2/doc/'):
                continue
            
            visited_urls.add(clean_href)
            full_url = BASE_DOMAIN + clean_href
            
            # Define um nome limpo para o arquivo Markdown
            if clean_href == "/v2/doc/":
                filename = "Introduction.md"
            else:
                # Exemplo: /v2/doc/node.html -> Node.md
                raw_name = clean_href.replace("/v2/doc/", "").replace(".html", "")
                filename = raw_name.replace("-", " ").title() + ".md"
            
            filepath = os.path.join(OUTPUT_DIR, filename)
            scrape_page(full_url, filepath)
            
    except Exception as e:
        print(f"[!] Erro crítico ao acessar WINkLink: {e}")

def main():
    print("=============================================")
    print("🔮 INICIALIZANDO CRAWLER DO WINKLINK (ORACLE) 🔮")
    print("=============================================")
    crawl_winklink()
    print("\n[*] Extração do WINkLink Concluída! O GlitchTRON agora possui visão on-chain.")

if __name__ == "__main__":
    main()
