from bs4 import BeautifulSoup
import sys
import argparse
from pathlib import Path

class Analysis:
    def __init__(self, takeout=None, outpath='data', delay=0):
        self.takeout = Path(takeout).expanduser()
        self.path = Path(outpath)

    def run(self):
        """Uses Takeout to download individual json files for each video."""
        watch_history = self.takeout / 'YouTube and YouTube Music/history/watch-history.html'
        if not watch_history.is_file():
            raise ValueError(f'"{watch_history}" is not a file. Did you download your YouTube data? ')
        print('Extracting video urls from Takeout.'); sys.stdout.flush()
        try:
            text = watch_history.read_text()
        except UnicodeDecodeError:
            text = watch_history.read_text(encoding='utf-8')

        soup = BeautifulSoup(text, 'html.parser')

        urls = [u.get('href') for u in soup.find_all('a')]
        print(urls)
        videos = [u for u in urls if 'www.youtube.com/watch' in u]
        url_path = self.path / 'urls.txt'
        url_path.write_text('\n'.join(videos))
        print('done!')

if __name__ == '__main__':
    print('Welcome!'); sys.stdout.flush()
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", '--out', default='data',
                        help="Path to empty directory for data storage.")
    parser.add_argument('-d', '--delay', default=0,
                        help='Time to wait between requests. May help avoid 2FA.')
    parser.add_argument('-t', '--takeout',
                        help='Path to an unzipped Takeout folder downloaded from https://takeout.google.com/')
    args = parser.parse_args()
    analysis = Analysis(args.takeout, args.out, float(args.delay))
    analysis.run()
