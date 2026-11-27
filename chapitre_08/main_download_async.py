from pprint import pprint
import requests
from bs4 import BeautifulSoup
from pathlib import Path
import time
import asyncio
import httpx

async def download_and_save(url,a,download_dir):
    url_file = f"{url}{a}"
    dest_file = download_dir / a
    r =requests.get(url_file)
    with open(dest_file,'w') as f:
        f.write(r.text)

async def async_requests_download_and_save(url,log_file,download_dir):
    url_log_file = f"{url}/{log_file}"
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None, requests.get, url_log_file)
    
    dest = download_dir / log_file
    with open(dest,'w') as f:
        f.write(response.text)

async def httpx_download_and_save(url,a,download_dir,client):
    url_file = f"{url}{a}"
    dest_file = download_dir / a
    r =await client.get(url_file)
    with open(dest_file,'w') as f:
        f.write(r.text)              
        
async def main():
    start = time.perf_counter()
    url = "https://logs.eolem.com/"
    r = requests.get(url)

    #Création du dossier, pas d'erreur s'il existe
    download_dir = Path('chapitre_08') / "download"
    download_dir.mkdir(exist_ok=True)
    soup = BeautifulSoup(r.text, 'html.parser')
    all_a = [a["href"] for a in soup.find_all("a") if a["href"].endswith('.log')]
    
    # all_coroutine = []
    # for a in all_a:
    #     all_coroutine.append(async_requests_download_and_save(url,a,download_dir))

    all_coroutine = []
    async with httpx.AsyncClient() as client:
        for a in all_a:
            all_coroutine.append(httpx_download_and_save(url,a,download_dir,client))
    
        await asyncio.gather(*all_coroutine)

    end = time.perf_counter()    
    
    print(f"{end-start:0.3f}s")
    

if __name__=='__main__':
    asyncio.run(main())
    
