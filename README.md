# fastDownloader
A downloader coded for myself.(selfuse)
## Usage
Install dependencies.
```bash
$ pip3 install -r requirements.txt
```
Check usage.
```
$ python3 main.py -h
usage: main.py [-h] [--src SRC] [--save SAVE] [--max MAX] [--interval INTERVAL] [--chunk CHUNK]

fastDownloader v0.0.1

options:
  -h, --help           show this help message and exit
  --src SRC            This parameter specifies the file path where the links to be downloaded are stored.
  --save SAVE          This parameter specifies the path for storing the downloaded files. No / at the end.
  --max MAX            This parameter specifies the concurrency level.
  --interval INTERVAL  This parameter specifies the interval of requests.
  --chunk CHUNK        This parameter specifies the number of bytes to be read per download.
```
## Src file should be like 👇🏻
```bash
["url1","url2"...]
```
## Example
Success
```bash
$ python3 main.py --src ./test_success.json --max 3 --chunk 1024
👉 Downloading 700 now!                                                                                                                                                                   
👉 Downloading 500 now!                                                                                                                                                                   
👉 Downloading 400 now!                                                                                                                                                                   
👉 Downloading 300 now!                                                                                                                                                                   
👉 Downloading 600 now!                                                                                                                                                                   
👉 Downloading 200 now!                                                                                                                                                                   
✅ All resources have been successfully downloaded!                                                                                                                                        
Downloaded 6 Failed 0 Left 0: 100%|████████████████████████████████████████████| 6/6 [00:01<00:00,  4.33it/s]
```
Failed
```bash
$ python3 main.py --src ./test_failed.json --max 3 --chunk 1024
👉 Downloading 500 now!                                                                                                                                                                   
👉 Downloading non-existent-url now!                                                                                                                                                      
👉 Downloading 700 now!                                                                                                                                                                   
👉 Downloading 600 now!                                                                                                                                                                   
👉 Downloading 300 now!                                                                                                                                                                   
❌ 1 files failed to download!                                                                                                                                                             
👉 Plz rerun with "python3 main.py --src failed.json --save . --max 3 --interval 0.5 --chunk 1024"                                                                                        
Downloaded 4 Failed 1 Left 0: 100%|████████████████████████████████████████████| 5/5 [00:01<00:00,  4.53it/s]
```
Please follow the instructions to rerun.
