from MultiThreadDownloader import Downloader

def test_Downloader():
    url = "https://www.python.org/ftp/python/3.7.4/python-3.7.4-amd64.exe"
    filename = "python-3.7.4-amd64.exe"
    downloader = Downloader(url, filename)
    downloader.start()
    downloader.wait()

if __name__ == "__main__":  
    test_Downloader()
    