# Amazing Multi-Threaded Downloader
# Author: @lzhbhlrPython

import requests
import threading
import time
import os
import fake_useragent
import tqdm

class Downloader:
    def __init__(self, url, filename, thread_count=10):
        self.url = url
        self.filename = filename
        self.thread_count = thread_count
        self.headers = {'User-Agent': fake_useragent.UserAgent().random}
        self.file_size = int(requests.head(self.url, headers=self.headers).headers['Content-Length'])
        self.block_size = self.file_size // self.thread_count
        self.threads = []
        self.start_time = time.time()
        self.end_time = None
        self.finished = False
        self.progress_bar = tqdm.tqdm(total=self.file_size, unit='B', unit_scale=True, desc=self.filename)
        self.progress_bar.update(0)
    def download(self, start, end, filename):
        headers = self.headers
        headers['Range'] = 'bytes=%d-%d' % (start, end)
        r = requests.get(self.url, headers=headers, stream=True)
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    self.progress_bar.update(1024)
        self.threads.remove(threading.current_thread())
        if not self.threads:
            self.finished = True
            self.end_time = time.time()
            self.progress_bar.close()
    def start(self):
        for i in range(self.thread_count):
            start = self.block_size * i
            if i == self.thread_count - 1:
                end = self.file_size
            else:
                end = start + self.block_size - 1
            t = threading.Thread(target=self.download, args=(start, end, self.filename + '.part%d' % i))
            t.start()
            self.threads.append(t)
    def wait(self):
        while not self.finished:
            time.sleep(1)
        return self.merge()
    def merge(self):
        with open(self.filename, 'wb') as f:
            for i in range(self.thread_count):
                with open(self.filename + '.part%d' % i, 'rb') as f2:
                    f.write(f2.read())
                os.remove(self.filename + '.part%d' % i)
        return self.end_time - self.start_time
    
