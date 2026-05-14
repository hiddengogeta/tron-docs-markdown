import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import markdownify
import os
import time
from urllib.parse import unquote

BASE_URL = "https://tronprotocol.github.io/trident"
SITEMAP_URL = f"{BASE_URL}/sitemap.xml"
OUTPUT_DIR = "trident_docs_md"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def scrape_mkdocs_page(url, filepath):
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        content = soup.find('article', class_='md-content__inner')
        
        if content:
            md_content = markdownify.markdownify(str(content), heading_style="ATX")
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(f"\n\n")
                f.write(md_content)
            print(f" [MkDocs] Extraído: {filepath}")
        time.sleep(0.5)
    except Exception as e:
        print(f"[!] Erro ao raspar {url}: {e}")

def scrape_javadoc_page(url, filepath):
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Estrutura clássica do JavaDoc
        header = soup.find('div', class_='header')
        content = soup.find('div', class_='contentContainer')
        
        if content:
            md_text = ""
            if header:
                md_text += markdownify.markdownify(str(header), heading_style="ATX") + "\n\n"
            md_text += markdownify.markdownify(str(content), heading_style="ATX")
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(f"\n\n")
                f.write(md_text)
            print(f" [JavaDoc] Extraído: {filepath}")
        time.sleep(0.2) # Pode ser mais rápido pois os arquivos são leves
    except Exception as e:
        print(f"[!] Erro ao raspar JavaDoc {url}: {e}")

def crawl_trident_sitemap():
    print(f"\n[*] FASE 1: Mapeando Guias MkDocs via Sitemap...")
    try:
        response = requests.get(SITEMAP_URL, headers=HEADERS)
        response.raise_for_status()
        root = ET.fromstring(response.content)
        
        urls = [elem.text for elem in root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        
        for url in urls:
            if "site-packages" in url or "lib/python" in url:
                continue
                
            decoded_url = unquote(url)
            path = decoded_url.replace(BASE_URL, "").strip("/")
            
            if not path or path == "index.html":
                filename = "Overview.md"
                dir_path = OUTPUT_DIR
            else:
                path_parts = path.replace(".html", "").split("/")
                filename = f"{path_parts.pop()}.md".replace("-", " ").title()
                
                if path_parts:
                    dir_path = os.path.join(OUTPUT_DIR, *[p.replace("-", " ").title() for p in path_parts])
                else:
                    dir_path = OUTPUT_DIR
                    
            os.makedirs(dir_path, exist_ok=True)
            filepath = os.path.join(dir_path, filename)
            
            scrape_mkdocs_page(url, filepath)
            
    except Exception as e:
        print(f"[!] Erro no sitemap do Trident: {e}")

def crawl_javadoc():
    print(f"\n[*] FASE 2: Invadindo o diretório oculto do JavaDoc...")
    javadoc_base = f"{BASE_URL}/javadoc"
    index_url = f"{javadoc_base}/allclasses-noframe.html"
    
    try:
        response = requests.get(index_url, headers=HEADERS)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Captura todos os links de classes listados no índice
        links = soup.find_all('a')
        
        javadoc_dir = os.path.join(OUTPUT_DIR, "API_Reference_JavaDoc")
        os.makedirs(javadoc_dir, exist_ok=True)
        
        if not links:
            print("[!] Nenhuma classe JavaDoc encontrada.")
            return
            
        for link in links:
            href = link.get('href')
            if not href: continue
            
            class_url = f"{javadoc_base}/{href}"
            
            # Limpa o nome do arquivo (ex: org/tron/trident/core/ApiWrapper.html -> ApiWrapper.md)
            filename = href.split("/")[-1].replace(".html", ".md")
            filepath = os.path.join(javadoc_dir, filename)
            
            scrape_javadoc_page(class_url, filepath)
            
    except Exception as e:
        print(f"[!] Erro ao indexar JavaDoc: {e}")

def main():
    print("==================================================")
    print("☕ INICIALIZANDO CRAWLER DO TRIDENT (JAVA SDK) ☕")
    print("==================================================")
    crawl_trident_sitemap()
    crawl_javadoc()
    print("\n[*] Extração do Trident Concluída! Classes Java 100% documentadas.")

if __name__ == "__main__":
    main()
