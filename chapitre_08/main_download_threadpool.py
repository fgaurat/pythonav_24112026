from pprint import pprint
import requests
from bs4 import BeautifulSoup
from pathlib import Path
import time
import threading
import concurrent.futures

def download_and_save(url,a,download_dir):
    url_file = f"{url}{a}"
    dest_file = download_dir / a
    r =requests.get(url_file)
    with open(dest_file,'w') as f:
        f.write(r.text)
        
        
def main():
    start = time.perf_counter()
    url = "https://logs.eolem.com/"
    r = requests.get(url)

    #Création du dossier, pas d'erreur s'il existe
    download_dir = Path('chapitre_08') / "download"
    download_dir.mkdir(exist_ok=True)
    
    soup = BeautifulSoup(r.text, 'html.parser')
    all_a = [a["href"] for a in soup.find_all("a") if a["href"].endswith('.log')]

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        all_root_url = [url]*len(all_a)
        all_download_dir = [download_dir]*len(all_a)
        executor.map(download_and_save,all_root_url,all_a,all_download_dir)
    # download_and_save(url,a,download_dir)
    # download_and_save("https://logs.eolem.com/", apache_logs_01.log, './download')
    # download_and_save("https://logs.eolem.com/", apache_logs_02.log, './download')
    # download_and_save("https://logs.eolem.com/", apache_logs_03.log, './download')
    # download_and_save("https://logs.eolem.com/", apache_logs_04.log, './download')
    end = time.perf_counter()    
    
    print(f"{end-start:0.3f}s")
    

if __name__=='__main__':
    main()
