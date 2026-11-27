from pprint import pprint
import requests
from bs4 import BeautifulSoup
from pathlib import Path
import time
import asyncio
import httpx


async def download(queue_download:asyncio.Queue,queue_save:asyncio.Queue):
    while True:
        url,a,download_dir,client = await queue_download.get()
        url_file = f"{url}{a}"
        r =await client.get(url_file)
        params = a,download_dir,r.text
        queue_save.put_nowait(params)
        queue_download.task_done()
        

async def save(queue_save:asyncio.Queue):
    while True:
        a,download_dir,text = await queue_save.get()
        dest = download_dir / a
        with open(dest,"w") as f:
            f.write(text)
            queue_save.task_done()
        
async def main():
    start = time.perf_counter()

    queue_download = asyncio.Queue()
    queue_save = asyncio.Queue()

    nb_download_workers = 10
    nb_save_workers = 5
    
    tasks = []
    
    
    for i in range(nb_download_workers):
        t = asyncio.create_task(download(queue_download,queue_save))
        tasks.append(t)

    for i in range(nb_save_workers):
        t = asyncio.create_task(save(queue_save))
        tasks.append(t)

    url = "https://logs.eolem.com/"
    r = requests.get(url)

    #Création du dossier, pas d'erreur s'il existe
    download_dir = Path('chapitre_08') / "download"
    download_dir.mkdir(exist_ok=True)
    soup = BeautifulSoup(r.text, 'html.parser')
    all_a = [a["href"] for a in soup.find_all("a") if a["href"].endswith('.log')]

    async with httpx.AsyncClient() as client:
        for a in all_a:
            params = url,a,download_dir,client
            queue_download.put_nowait(params)
        
        await queue_download.join()    
        await queue_save.join()    

    [t.cancel() for t in tasks]
    
    
    end = time.perf_counter()    
    
    print(f"{end-start:0.3f}s")
    

if __name__=='__main__':
    asyncio.run(main())
    
