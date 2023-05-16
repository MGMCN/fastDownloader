# fastDownloader
A downloader developed for myself.(selfuse)
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
👉 Downloading -3557342921266950271_500 now!                                                                                                                                              
👉 Downloading -2865197712751752189_300 now!                                                                                                                                              
👉 Downloading -700390739090695736_600 now!                                                                                                                                               
👉 Downloading 5636641034660171054_700 now!                                                                                                                                               
👉 Downloading 5773939477608183504_400 now!                                                                                                                                               
👉 Downloading 1310250945337633844_200 now!                                                                                                                                                                   
✅ All resources have been successfully downloaded!                                                                                                                                        
Downloaded 6 Failed 0 Left 0: 100%|████████████████████████████████████████████| 6/6 [00:01<00:00,  4.33it/s]
# Notice : The long string of characters in front of the file name is 
# a unique hash code used to ensure the uniqueness of the file naming.  
```
Failed
```bash
$ python3 main.py --src ./test_failed.json --max 3 --chunk 1024
👉 Downloading -6762229335681689814_700 now!                                                                                                                                              
👉 Downloading -55066400530373971_600 now!                                                                                                                                                
👉 Downloading -2931830335596416142_500 now!                                                                                                                                              
👉 Downloading 2353655904693015958_300 now!                                                                                                                                               
👉 Downloading -5222952479054798371_non-existent-url now!                                                                                                                                                                  
❌ 1 files failed to download!                                                                                                                                                             
👉 Plz rerun with "python3 main.py --src failed.json --save . --max 3 --interval 0.5 --chunk 1024"                                                                                        
Downloaded 4 Failed 1 Left 0: 100%|████████████████████████████████████████████| 5/5 [00:01<00:00,  4.53it/s]
```
Please follow the instructions to rerun.
