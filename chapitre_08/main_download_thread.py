from pprint import pprint
import requests
from bs4 import BeautifulSoup
from pathlib import Path
import time
import threading

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

    # for a in all_a:
    #     if a["href"].endswith('.log'):
    #         print(a["href"])
    # print(all_a)
    
    all_threads = [threading.Thread(target=download_and_save,args=(url,a,download_dir)) for a in all_a]
    [th.start() for th in all_threads]
    [th.join() for th in all_threads]
    
    
    # for a in all_a:
    #     th = threading.Thread(target=download_and_save,args=(url,a,download_dir))
    #     th.start()
    #     all_threads.append(th)

    # for th in all_threads:
    #     th.join()
        
    end = time.perf_counter()    
    
    print(f"{end-start:0.3f}s")
    

if __name__=='__main__':
    main()
