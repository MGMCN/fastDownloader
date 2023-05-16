import argparse
import utils as downloader


def get_args():
    parser = argparse.ArgumentParser(description='fastDownloader v0.0.1')
    parser.add_argument('--src', type=str, default=None,
                        help='This parameter specifies the file path where the links to be '
                             'downloaded are stored.')
    parser.add_argument('--save', type=str, default='.',
                        help='This parameter specifies the path for storing the downloaded files. No / at the end.')
    parser.add_argument('--max', type=int, default=10, help='This parameter specifies the concurrency level.')
    parser.add_argument('--interval', type=float, default=0.5,
                        help='This parameter specifies the interval of requests.')
    parser.add_argument('--chunk', type=int, default=1024,
                        help='This parameter specifies the number of bytes to be read per '
                             'download.')
    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()
    tasks = downloader.preprocessing(args.src)
    length = len(tasks)
    if length != 0:
        downloader.counts = len(tasks)
        progress_bar = downloader.generate_progress_bar()
        downloader.run(tasks, args, progress_bar)
    else:
        print('There are no resources that need to be downloaded!')
