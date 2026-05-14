import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import markdownify
import os
import time

BASE_URL = "https://docs.justlend.org"
OUTPUT_DIR = "justlend_docs_md"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def scrape_page(url, filepath):
    print(f" Extraindo: {url} -> {filepath}")
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # A tag de ouro do MkDocs Material
        content = soup.find('article', class_='md-content__inner')
        
        if content:
            md_content = markdownify.markdownify(str(content), heading_style="ATX")
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(f"\n\n")
                f.write(md_content)
        time.sleep(0.5)
    except Exception as e:
        print(f"[!] Erro ao raspar {url}: {e}")

def crawl_justlend_sitemap():
    print(f"\n[*] Mapeando ecossistema JustLend DAO via Sitemap: {BASE_URL}/sitemap.xml...")
    try:
        response = requests.get(BASE_URL + "/sitemap.xml", headers=HEADERS)
        response.raise_for_status()
        root = ET.fromstring(response.content)
        urls = [elem.text for elem in root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
        
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        
        for url in urls:
            # Pula a raiz base se vier vazia
            if url == BASE_URL or url == BASE_URL + "/":
                filepath = os.path.join(OUTPUT_DIR, "JustLend Overview.md")
            else:
                # Transforma a URL em estrutura de pastas (ex: /concepts/supply/)
                path = url.replace(BASE_URL, "").strip("/")
                path_parts = [p for p in path.split("/") if p]
                
                if not path_parts:
                    continue
                    
                filename = f"{path_parts.pop()}.md"
                
                if path_parts:
                    dir_path = os.path.join(OUTPUT_DIR, *path_parts)
                else:
                    dir_path = OUTPUT_DIR
                    
                os.makedirs(dir_path, exist_ok=True)
                filepath = os.path.join(dir_path, filename)
            
            scrape_page(url, filepath)
            
    except Exception as e:
        print(f"[!] Erro crítico ao acessar sitemap do JustLend: {e}")

def main():
    print("=====================================================")
    print("🏦 INICIALIZANDO CRAWLER DO JUSTLEND (LENDING DAO) 🏦")
    print("=====================================================")
    crawl_justlend_sitemap()
    print("\n[*] Extração do JustLend Concluída! Você tem as chaves do Banco.")

if __name__ == "__main__":
    main()
