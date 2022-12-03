from MultiThreadDownloader import Downloader


def test_Downloader():
    url = input("Enter the url of the file to download:")
    filename = input("Enter the filename to save:")
    thread_count = int(input("Enter the number of threads to use:"))
    downloader = Downloader(url, filename, thread_count)
    downloader.start()
    finish_time = downloader.wait()
    print("Download finished in %.2f seconds." % finish_time)


if __name__ == "__main__":
    test_Downloader()
