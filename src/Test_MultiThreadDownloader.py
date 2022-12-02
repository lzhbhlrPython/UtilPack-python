from MultiThreadDownloader import Downloader

def test_Downloader():
    url = "https://pub-2fdef7a2969f43289c42ac5ae3412fd4.r2.dev/animefull-latest.tar"
    filename = "animefull-latest.tar"
    downloader = Downloader(url, filename,50)
    downloader.start()
    downloader.wait()

if __name__ == "__main__":  
    test_Downloader()
    