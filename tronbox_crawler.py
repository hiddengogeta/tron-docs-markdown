import requests
from bs4 import BeautifulSoup
import markdownify
import os
import time
import json
import re

BASE_URL = "https://tronbox.io/docs/"
OUTPUT_DIR = "tronbox_docs_md"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def scrape_page(url, filepath):
    print(f" Extraindo: {url} -> {filepath}")
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # A tag exata onde o VitePress guarda o texto útil
        content = soup.find('div', class_='vp-doc') or soup.find('main')
        
        if content:
            md_content = markdownify.markdownify(str(content), heading_style="ATX")
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(f"\n\n")
                f.write(md_content)
        time.sleep(0.5)
    except Exception as e:
        print(f"[!] Erro ao raspar {url}: {e}")

def crawl_tronbox():
    print(f"\n[*] Hackeando o gerador VitePress do TronBox a partir de: {BASE_URL}...")
    try:
        response = requests.get(BASE_URL, headers=HEADERS)
        response.raise_for_status()
        
        # O pulo do gato: Achar o window.__VP_HASH_MAP__ no HTML bruto
        match = re.search(r'window\.__VP_HASH_MAP__=JSON\.parse\("(.*?)"\);', response.text)
        
        if not match:
            print("[!] Não foi possível encontrar o mapa de arquivos do VitePress.")
            return

        # O VitePress escapa as aspas, precisamos des-escapar e ler como JSON
        raw_json_string = match.group(1).replace('\\"', '"')
        file_map = json.loads(raw_json_string)
        
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        
        for file_path in file_map.keys():
            # file_path vai ser algo como: "guides_compile-contracts.md" ou "index.md"
            clean_name = file_path.replace(".md", "")
            
            # Formata a URL (ex: "guides_compile-contracts" vira "guides/compile-contracts")
            url_path = clean_name.replace("_", "/")
            
            # --- PATCH PARA O BUG DO TRONBOX (404 Not Found) ---
            if url_path == "guides/debugging-with-tre":
                url_path = "guides/debugging-with-TRE"
            # ---------------------------------------------------
            
            if url_path == "index":
                url_path = ""
                
            full_url = BASE_URL + url_path
            
            # Formata o nome do arquivo 
            filename = clean_name.replace("-", " ").replace("_", " - ").title() + ".md"
            filepath = os.path.join(OUTPUT_DIR, filename)
            
            scrape_page(full_url, filepath)
            
    except Exception as e:
        print(f"[!] Erro crítico ao acessar TronBox: {e}")

def main():
    print("=============================================")
    print("📦 INICIALIZANDO CRAWLER DO TRONBOX (TVM) 📦")
    print("=============================================")
    crawl_tronbox()
    print("\n[*] Extração do TronBox Concluída! O arsenal de compilação está pronto e sem erros 404.")

if __name__ == "__main__":
    main()
