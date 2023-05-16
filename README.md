# fastDownloader
selfuse
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
```python
['url1','url2'...]
```
## Example
```bash
python3 main.py --src ./test_failed.json --max 3 --chunk 1024
```