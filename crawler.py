import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import markdownify
import os
import time
from urllib.parse import urlparse

BASE_URL = "https://developers.tron.network"
# Agora a Sidebar só processa o Core Protocol
ENTRY_PAGES = ["/docs/getting-start"]
OUTPUT_DIR = "tron_docs_md"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def scrape_page(url, filepath):
    full_url = BASE_URL + url if url.startswith("/") else url
    print(f" Extraindo: {full_url} -> {filepath}")
    
    try:
        response = requests.get(full_url, headers=HEADERS)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        content = soup.find('main') or soup.find('article') or soup.body
        
        if content:
            md_content = markdownify.markdownify(str(content), heading_style="ATX")
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(f"\n\n")
                f.write(md_content)
        time.sleep(0.5) 
    except Exception as e:
        print(f"[!] Erro ao raspar {full_url}: {e}")

def crawl_sidebar(start_page):
    print(f"\n[*] Iniciando mapeamento da Sidebar: {start_page}...")
    
    try:
        response = requests.get(BASE_URL + start_page, headers=HEADERS)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        sidebar = soup.find('nav', class_='rm-Sidebar')
        if not sidebar:
            print(f"[!] Barra lateral vazia ou bloqueada em {start_page}.")
            return

        sections = sidebar.find_all('section', class_='rm-Sidebar-section')
        
        for section in sections:
            heading_btn = section.find('button', class_='rm-Sidebar-category')
            if not heading_btn: continue
            
            category_name = heading_btn.get_text(strip=True)
            safe_category = "".join([c for c in category_name if c.isalpha() or c.isdigit() or c==' ']).rstrip()
            
            category_path = os.path.join(OUTPUT_DIR, safe_category)
            os.makedirs(category_path, exist_ok=True)
            
            links = section.find_all('a', class_='rm-Sidebar-link')
            for link in links:
                page_url = link.get('href')
                if not page_url or page_url.startswith('http'): continue 
                    
                page_name_span = link.find('span', class_='Sidebar-link-text_label1gCT_uPnx7Gu')
                page_name = page_name_span.get_text(strip=True) if page_name_span else link.get_text(strip=True)
                if not page_name: continue
                
                safe_page_name = "".join([c for c in page_name if c.isalpha() or c.isdigit() or c==' ']).rstrip()
                filepath = os.path.join(category_path, f"{safe_page_name}.md")
                
                scrape_page(page_url, filepath)
                
    except Exception as e:
        print(f"[!] Erro crítico ao acessar {start_page}: {e}")

def crawl_from_sitemap():
    """Usa o sitemap para varrer /reference e /recipes que falham na sidebar dinâmica"""
    print("\n[*] Ativando o Radar do Sitemap para caçar APIs e Receitas...")
    sitemap_url = BASE_URL + "/sitemap.xml"
    
    try:
        response = requests.get(sitemap_url, headers=HEADERS)
        response.raise_for_status()
        root = ET.fromstring(response.content)
        urls = [elem.text for elem in root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
        
        # Filtra os links de interesse
        api_urls = [u for u in urls if "/reference/" in u]
        recipe_urls = [u for u in urls if "/recipes/" in u]
        
        # --- PROCESSA RECEITAS ---
        if recipe_urls:
            recipe_dir = os.path.join(OUTPUT_DIR, "Recipes")
            os.makedirs(recipe_dir, exist_ok=True)
            for url in recipe_urls:
                recipe_name = url.split("/")[-1].replace("-", " ").title()
                filepath = os.path.join(recipe_dir, f"{recipe_name}.md")
                scrape_page(url, filepath)
                
        # --- PROCESSA API REFERENCE ---
        if api_urls:
            api_dir = os.path.join(OUTPUT_DIR, "API Reference")
            os.makedirs(api_dir, exist_ok=True)
            for url in api_urls:
                # O nome do arquivo será o endpoint (ex: getaccountbalance.md)
                api_name = url.split("/")[-1]
                filepath = os.path.join(api_dir, f"{api_name}.md")
                scrape_page(url, filepath)
                
    except Exception as e:
        print(f"[!] Erro ao buscar dados do sitemap: {e}")

def main():
    print("=============================================")
    print("🚀 INICIALIZANDO GLITCHTRON V1.2 (SLEDGEHAMMER) 🚀")
    print("=============================================")
    
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    crawl_sidebar(ENTRY_PAGES[0])
    crawl_from_sitemap()
        
    print("\n[*] Extração 100% Completa! Core Protocol, Recipes e toda a API Reference mapeados.")

if __name__ == "__main__":
    main()
