import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import markdownify
import os
import time

BASE_URL = "https://docs.sun.io"
OUTPUT_DIR = "sun_docs_md"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def scrape_page(url, filepath):
    print(f" Extraindo: {url} -> {filepath}")
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Pega o conteúdo principal do Docusaurus
        content = soup.find('article')
        
        if content:
            md_content = markdownify.markdownify(str(content), heading_style="ATX")
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(f"\n\n")
                f.write(md_content)
        time.sleep(0.5) 
    except Exception as e:
        print(f"[!] Erro ao raspar {url}: {e}")

def crawl_sun_sitemap():
    print(f"\n[*] Mapeando ecossistema SUN.io via Sitemap: {BASE_URL}/sitemap.xml...")
    try:
        response = requests.get(BASE_URL + "/sitemap.xml", headers=HEADERS)
        response.raise_for_status()
        root = ET.fromstring(response.content)
        urls = [elem.text for elem in root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
        
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        
        for url in urls:
            # Ignora a raiz vazia se vier só o domínio base
            if url == BASE_URL or url == BASE_URL + "/":
                filepath = os.path.join(OUTPUT_DIR, "SUN.io Overview.md")
            else:
                # Remove o domínio para pegar só o caminho (ex: /V4Protocol/V4Contract)
                path = url.replace(BASE_URL, "").strip("/")
                path_parts = path.split("/")
                
                # Se a URL não tiver partes (algo muito estranho), pula
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
        print(f"[!] Erro crítico ao acessar sitemap do SUN.io: {e}")

def main():
    print("==================================================")
    print("🌞 INICIALIZANDO SLEDGEHAMMER DO SUN.IO (DEFI) 🌞")
    print("==================================================")
    crawl_sun_sitemap()
    print("\n[*] Extração do SUN.io Concluída! Você tem o poder total do DeFi em mãos.")

if __name__ == "__main__":
    main()
