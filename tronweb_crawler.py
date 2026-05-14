import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import markdownify
import os
import time
from urllib.parse import unquote
import re

BASE_DOMAIN = "https://tronweb.network"
SITEMAP_URL = "https://tronweb.network/docu/sitemap.xml"
OUTPUT_DIR = "tronweb_docs_md"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def scrape_page(url, filepath):
    print(f" Extraindo: {url} -> {filepath}")
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        content = soup.find('article')
        
        if content:
            md_content = markdownify.markdownify(str(content), heading_style="ATX")
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(f"\n\n")
                f.write(md_content)
        time.sleep(0.5)
    except Exception as e:
        print(f"[!] Erro ao raspar {url}: {e}")

def crawl_tronweb_sitemap():
    print(f"\n[*] Ativando o Radar do Sitemap para o TronWeb: {SITEMAP_URL}...")
    try:
        try:
            response = requests.get(SITEMAP_URL, headers=HEADERS)
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            print("[*] Redirecionando radar para sitemap raiz...")
            response = requests.get(BASE_DOMAIN + "/sitemap.xml", headers=HEADERS)
            response.raise_for_status()

        root = ET.fromstring(response.content)
        urls = [elem.text for elem in root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
        
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        
        for url in urls:
            if "/docu/docs/" not in url:
                continue
                
            decoded_url = unquote(url)
            path = decoded_url.split("/docu/docs/")[-1].strip("/")
            
            # --- PATCH: FILTRO DE CÓDIGO LEGADO ---
            # Ignora rotas que começam com números (ex: 5.0.0/, 6.2.2/)
            if re.match(r'^\d+\.\d+\.\d+', path):
                continue
            # --------------------------------------
            
            if not path:
                filename = "Intro.md"
                dir_path = OUTPUT_DIR
            else:
                path_parts = path.split("/")
                filename = f"{path_parts.pop()}.md".replace("-", " ").title()
                
                if path_parts:
                    dir_path = os.path.join(OUTPUT_DIR, *[p.replace("-", " ").title() for p in path_parts])
                else:
                    dir_path = OUTPUT_DIR
                    
            os.makedirs(dir_path, exist_ok=True)
            filepath = os.path.join(dir_path, filename)
            
            scrape_page(url, filepath)
            
    except Exception as e:
        print(f"[!] Erro crítico ao acessar sitemap do TronWeb: {e}")

def main():
    print("=============================================")
    print("🕸️ INICIALIZANDO SLEDGEHAMMER DO TRONWEB 🕸️")
    print("=============================================")
    crawl_tronweb_sitemap()
    print("\n[*] Extração Completa! Apenas a versão mais recente do SDK foi mapeada.")

if __name__ == "__main__":
    main()
