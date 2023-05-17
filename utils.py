import asyncio
import aiohttp
import json
import os
from tqdm import tqdm
import re

# Not graceful
failed = []
success = 0
counts = 0


def preprocessing(src_path) -> list:
    tasks = []
    if src_path is not None:
        with open(src_path, 'r') as file:
            tasks.extend(json.load(file))
    tasks = list(set(tasks))  # remove duplicate task
    return tasks


def generate_progress_bar():
    fa = len(failed)
    progress_bar = tqdm(total=counts, desc=f"Downloaded {success} Failed {fa} Left {counts - fa - success}")
    return progress_bar


def update_progress_bar(progress_bar):
    fa = len(failed)
    progress_bar.desc = f"Downloaded {success} Failed {fa} Left {counts - fa - success}"
    progress_bar.update(1)


def get_file_name(url) -> str:
    path_parts = url.split('/')
    file_name = path_parts[-1]
    file_name = f'{hash(url)}_{file_name}'
    file_name = re.sub(r'[^\w\-_.()]', '_', file_name)
    return file_name


async def download(session,
                   url,
                   semaphore,
                   save_dir,
                   request_interval,
                   chunk_size,
                   progress_bar):
    global success, failed
    async with semaphore:
        file_name = get_file_name(url)
        save_path = f"{save_dir}/{file_name}"
        try:
            tqdm.write(f'> Downloading {file_name} now!')
            async with session.get(url) as response:
                await asyncio.sleep(request_interval)
                with open(save_path, 'wb') as f:
                    while True:
                        chunk = await response.content.read(chunk_size)
                        if not chunk:
                            break
                        f.write(chunk)
            success += 1
        except:
            if os.path.exists(save_path):
                os.remove(save_path)
            failed.append(url)
        finally:
            update_progress_bar(progress_bar)


async def main(tasks, args, progress_bar):
    Max = args.max
    semaphore = asyncio.Semaphore(Max)
    save = args.save
    interval = args.interval
    chunk = args.chunk
    session = aiohttp.ClientSession()
    tasks = [asyncio.ensure_future(download(session, url, semaphore, save, interval, chunk, progress_bar)) for url in
             tasks]
    await asyncio.gather(*tasks)
    await session.close()
    fa = len(failed)
    if fa > 0:
        tqdm.write(f'> {fa} files failed to download!')
        tqdm.write(
            f'> Plz rerun with \"python3 main.py --src failed.json --save {save} --max {Max} --interval {interval} --chunk {chunk}\"')
        with open("failed.json", 'w') as f:
            f.write(json.dumps(failed))
    else:
        tqdm.write('> All resources have been successfully downloaded!')


def run(tasks, args, progress_bar):
    asyncio.get_event_loop().run_until_complete(main(tasks, args, progress_bar))
