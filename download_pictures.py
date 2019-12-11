import os
import urllib.request
from bs4 import BeautifulSoup




#"https://www.pexels.com/search/blonde/"
#https://pixabay.com/es/images/search/blonde%20hair/?pagi=4
mainPath = 'download/'
urls = [("https://www.pexels.com/search/blonde/?page=1", "Blonde"),]

if __name__ == '__main__':
    class AppURLopener(urllib.request.FancyURLopener):
        version = "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.69 Safari/537.36"

    urllib._urlopener = AppURLopener()
    for u in urls:

        if not os.path.exists(mainPath):
            os.mkdir(mainPath)

        download_path = os.path.join(mainPath, u[1])
        if not os.path.exists(download_path):
            os.mkdir(download_path)

        headers = {'User-Agent': 'Mozilla/5.0'}
        request = urllib.request.Request(u[0], headers=headers)
        html = urllib.request.urlopen(request).read()
        soup = BeautifulSoup(html)

        total_pages = [a for a in soup.find_all('a', href=True) if "?page=" in str(a)]
        total_pages = total_pages[-2]
        total_pages = [int(s) for s in total_pages if s.isdigit()]

        for page in range(1, total_pages[0]):
            print("Downloading Page %s of %s ." % (page, total_pages))

            newFolder = os.path.join(download_path, str(page))
            if not os.path.exists(newFolder):
                os.mkdir(newFolder)
            url = u[0]
            new_url = url.replace(url[-1], str(page))
            headers = {'User-Agent': 'Mozilla/5.0'}
            request = urllib.request.Request(new_url, headers=headers)
            html = urllib.request.urlopen(request).read()
            soup = BeautifulSoup(html)

            links = soup.findAll('img')
            c = 1
            for link in (links):
                if str(link['src']).endswith('500'):
                    urllib._urlopener.retrieve(str(link['src']), os.path.join(newFolder, str(c) + ".jpg"))
                    c += 1
