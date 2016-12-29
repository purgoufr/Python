'''
Created on 26 Ara 2016

@author: Purgoufr
'''
#----------------------------------------------------------------------------------------
# #ornek program karikatur yayinlayan bir site de her gun yeni resimler ekleniyor.ilk sayfada(main page) en guncel en son eklenen
# #resmi gorursunuz. 5 gun sonra girdiginizde en son girdiginizden bu yana 5 tane resim eklenmis olacak ve siz her birini gormek
# #icin 4 kere previous yani onceki butonuna tiklayacaksiniz.Bunun yerine resimleri otomatik indiren bir script yazacagiz 
# #web adresimiz http://xkcd.com/ olacak.Asamalar;
# #Loads the XKCD home page.
# #Saves the comic image on that page.
# #Follows the Previous Comic link.
# #Repeats until it reaches the first comic.
# 
# #Download pages with the requests module.
# #Find the URL of the comic image for a page using Beautiful Soup.
# #Download and save the comic image to the hard drive with iter_content().
# #Find the URL of the Previous Comic link, and repeat.
# 
# #The URL of the comic’s image file is given by the href attribute of an <img> element.
# #The <img> element is inside a <div id="comic"> element.
# #The Prev button has a rel HTML attribute with the value prev.
# #The first comic’s Prev button links to the http://xkcd.com/# URL, indicating that there are no more previous pages.
# 
import requests, os, bs4
url = 'http://xkcd.com'              # starting url
#os.makedirs('xkcd')                #Eger python3 veya daha ust surum kullaniyorsan 188 i aktif et, 189-190 comment yap
if not os.path.exists('xkcd'):
    os.makedirs('xkcd')   # store comics in ./xkcd
while not url.endswith('#'):         #URL '#' ile biterse ilk resme ulastin demektir.sayfada oyle cunku
     
    # Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()
 
    soup = bs4.BeautifulSoup(res.text)
 
    # Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        try:
            comicUrl = 'http:' + comicElem[0].get('src')
            # Download the image.
            print('Downloading image %s...' % (comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()
        except requests.exceptions.MissingSchema:
            # skip this comic
            prevLink = soup.select('a[rel="prev"]')[0]
            url = 'http://xkcd.com' + prevLink.get('href')
            continue
 
        # Save the image to ./xkcd.
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
 
    # Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')
 
print('Done.')