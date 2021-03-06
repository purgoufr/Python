# -*- coding: utf-8 -*-
'''
Created on 24 Ara 2016

@author: Purgoufr
'''

#Genel olarak yaptigimiz olayin adi web scraping
#web scraping: cesitli yazilim ve metotlar ile hedef web sitelerinden icerik kopyalama* veya belli bilgileri alma islemine verilen isim
# #istedi�in URL i a�ma
# import webbrowser
# webbrowser.open('http://inventwithpython.com/')

#----------------------------------------------------------------------------------------
# #ornek program kopyaladigin adresi google maps te uygulamayi calistirdiginda acar(Ctrl+C yap ve run a bas)
# import webbrowser, sys, pyperclip
# if len(sys.argv) > 1:
#     # Get address from command line.
#     address = ' '.join(sys.argv[1:])
# else:
#     # Get address from clipboard.
#     address = pyperclip.paste()
# 
# webbrowser.open('https://www.google.com/maps/place/' + address)

#----------------------------------------------------------------------------------------
#URL to download (internetten text indirdik)
#len(res.text) ile text dosyasinin boyutunu ogrendik
#printlen(res.text[:500]) yaparak 500 karakterlik kismini yazdirdik dosyada 178.000 karakter var

# import requests 
# res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
# type(res)
# #res.status_code == requests.codes.ok    #kod calismadi(bu kodda istek yaptigimiz link durumunu sorguladik(true or false?)
# print(res.raise_for_status())  #linki kontrol eder problem varsa hata verir
# print(len(res.text))
# print(res.text[:500])

#----------------------------------------------------------------------------------------
# #Linkteki sorunu debugla bulalim
# #request.get ile linki yazdik ve res.raise_for_status() ile linki kontrol ettik
# 
# import requests
# res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
# try:
#     res.raise_for_status()
# except Exception as exc:
#     print('There was a problem: %s' % (exc))

#----------------------------------------------------------------------------------------
#Dosyayi bilgisayara kaydetme
#Note: write binary mode yani wb. Metnin Unicode kodlamasini korumak icin metin(string)
#verileri yerine ikili veri(binary) yazmaniz gerekir.
#open komuyla text dosyasi olusturduk
#response objesini donguye almak icin for loop icinde iter_content() kullandik
#playFile.write ile text dosyasina request ettigimiz icerigi yazdik
# import requests
# res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
# res.raise_for_status()
# playFile = open('C:\\Users\\Purgoufr\\Documents\\Eclipse Projects\\Python\\Web_Scraping\\web_test_folder\\RomeoAndJuliet.txt', 'wb')
# for chunk in res.iter_content(100000):
#     playFile.write(chunk)
# playFile.close()

#----------------------------------------------------------------------------------------
# #Parsing HTML with the BeautifulSoup Module(siteden istedigin kismi cekme(istedigin class i cekme parse etme))
# #Parse icin Beautiful Soup modulunu kullanacagiz
# #Bu kodda requests.get() il No Starch Press in ana sayfasini indirmek icin kullandik
# #BeautifulSoup nesnesi noStarchSoup adli bir degiskende depolanir.
# import requests, bs4
# res = requests.get('http://nostarch.com')
# res.raise_for_status()
# noStarchSoup = bs4.BeautifulSoup(res.text)
# print(type(noStarchSoup))
# exampleFile = open('example.html')
# exampleSoup = bs4.BeautifulSoup(exampleFile)
# print(type(exampleSoup))
#     
#----------------------------------------------------------------------------------------
# select() sorgulari
#soup.select('div')          All elements named <div> (<div> adli tum elemanlar)

#soup.select('#author')      The element with an id attribute of author( author id ozellikli tum elemanlar )

#soup.select('.notice')      All elements that use a CSS class attribute named notice(notice adli CSS class ozellikli tum elemanlar):

#soup.select('div span')     All elements named <span> that are within an element named <div>(<div> ve <span> adli tum elemanlar)

#soup.select('div > span')   All elements named <span> that are directly within an element named <div>, with no other
#                            element in between(<Span> adli ve dogrudan <div> adli bir ogenin icinde bulunan ve arasinda
#                            baska bir oge bulunmayan tum ogeler)

#soup.select('input[name]')  All elements named <input> that have a name attribute with any value(Herhangi bir degere sahip 
#                            name ozniteligine sahip <input> isimli tum ogeler)

#soup.select('input[type="button"]')  All elements named <input> that have an attribute named type with value button 
#                                     input adinda buton degerine sahip(buton) ozelligi tasiyan butun elemanlar  
    
#----------------------------------------------------------------------------------------
# #daha once olusturdugumuz example.html dosyasindan author ile ilgili bilgileri getirdik bu bilgiler
#bu ornek program html kodundaki <p> elemanlarini getirir
# import bs4
# exampleFile = open('example.html')
# exampleSoup = bs4.BeautifulSoup(exampleFile.read())
# elems = exampleSoup.select('#author')
# print(type(elems))
# print(len(elems))
# print(type(elems[0]))
# print(elems[0].getText())
# print(str(elems[0]))
# print(elems[0].attrs)
# 
# pElems = exampleSoup.select('p')
# print(str(pElems[0]))
# print(pElems[0].getText())
# print(str(pElems[1]))
# print(pElems[1].getText())
# print(str(pElems[2]))
# print(pElems[2].getText())

#----------------------------------------------------------------------------------------
##bu ornek program html kodundaki <span> elemanlarini getirir
# import bs4
# soup = bs4.BeautifulSoup(open('example.html'))
# spanElem = soup.select('span')[0]
# print(str(spanElem))
# print(spanElem.get('id'))
# print(spanElem.get('some_nonexistent_addr') == None)
# print(spanElem.attrs)
    
#----------------------------------------------------------------------------------------
# #ornek program google da birsey aratip birkac farkli linki tek tek yeni sekmede acmadan
# #sadece komut satirina aramak istedigin seyi yazacaksin ve onunla ilgili sayfalar web browser da otomatik acilacak
# #
# #komut satirina yazilanlari okumasi icin sys.argv kullanicaz
# #arama sonuclarini cekmek getirmek(fetch) icin request module kullancaz
# #her arama sonucu icin linkleri bulacagiz
# #webbrowser.open() i kullanarak web sayfalarini acacagiz.
# #google arama url i 'https://www.google.com.tr/search?q=' esittirden sonra aranacak kelime gelir
# 
# import requests, sys, webbrowser, bs4
# 
# print('Googling...') # display text while downloading the Google page
# res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
# res.raise_for_status()  
# #simdi indirdiginiz HTML'den en iyi arama sonucu baglantilarini cikarmak icin "Beautiful Soup" u kullanmaniz gerekiyor.
# 
# # Retrieve top search result links.
# soup = bs4.BeautifulSoup(res.text)   
#  
# # Open a browser tab for each result.
# linkElems = soup.select('.r a')  #buradaki en onemli nokta burasi.Arama sonuclarinin getirildigi kisim <h3 class="r">.Bu bilgiye
# # google da arama yapip sag tiklayip sayfayi incele(inspect element) e tiklayarak ulasabilirsin
# #HTML text and then use the selector '.r a' to find all <a> elements that are within an element that has the r CSS class.
# 
# # Open a browser tab for each result.
# linkElems = soup.select('.r a')
# numOpen = min(5, len(linkElems))           #ilk bes sonucu getirecek
# for i in range(numOpen):
#     webbrowser.open('http://google.com' + linkElems[i].get('href'))  
#     
# #NOTE!! Programi calistirmak icin cmd ye gir C:\Users\Purgoufr\Documents\Eclipse Projects\Python\Web_Scraping adresine gir
# #komut satirina>>> web_basic_codes.py yazip bosluk birakip aranacak seyi yazariz
# #ornek "web_basic_codes.py ugur" yazdigimizda ugur u aratacak   

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
# import requests, os, bs4
# url = 'http://xkcd.com'              # starting url
# #os.makedirs('xkcd')                #Eger python3 veya daha ust surum kullaniyorsan 188 i aktif et, 189-190 comment yap
# if not os.path.exists('xkcd'):
#     os.makedirs('xkcd')   # store comics in ./xkcd
# while not url.endswith('#'):         #URL '#' ile biterse ilk resme ulastin demektir.sayfada oyle cunku
#     
#     # Download the page.
#     print('Downloading page %s...' % url)
#     res = requests.get(url)
#     res.raise_for_status()
# 
#     soup = bs4.BeautifulSoup(res.text)
# 
#     # Find the URL of the comic image.
#     comicElem = soup.select('#comic img')
#     if comicElem == []:
#         print('Could not find comic image.')
#     else:
#         try:
#             comicUrl = 'http:' + comicElem[0].get('src')
#             # Download the image.
#             print('Downloading image %s...' % (comicUrl))
#             res = requests.get(comicUrl)
#             res.raise_for_status()
#         except requests.exceptions.MissingSchema:
#             # skip this comic
#             prevLink = soup.select('a[rel="prev"]')[0]
#             url = 'http://xkcd.com' + prevLink.get('href')
#             continue
# 
#         # Save the image to ./xkcd.
#         imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
#         for chunk in res.iter_content(100000):
#             imageFile.write(chunk)
#         imageFile.close()
# 
#     # Get the Prev button's url.
#     prevLink = soup.select('a[rel="prev"]')[0]
#     url = 'http://xkcd.com' + prevLink.get('href')
# 
# print('Done.')

#----------------------------------------------------------------------------------------
#ornek program; Selenyum modulu, sayfayla etkilesime giren bir insan varmis gibi, programatik olarak baglantilari tiklayarak
#ve oturum acma bilgilerini doldurarak Python'un tarayiciyi dogrudan kontrol etmesini saglar.

#METHOD NAME                                        #WebElement OBJECT/LiST RETURNED

#browser.find_element_by_class_name(name)           #Elements that use the CSS class 
#browser.find_elements_by_class_name(name)          #name

#browser.find_element_by_css_selector(selector)     #Elements that match the CSS 
#browser.find_elements_by_css_selector(selector)    #selector

#browser.find_element_by_id(id)                     #Elements with a matching id attribute value
#browser.find_elements_by_id(id)

#browser.find_element_by_link_text(text)            #<a> elements that completely match the text provided
#browser.find_elements_by_link_text(text)        

#browser.find_element_by_name(name)                 #Elements with a matching name attribute value
#browser.find_elements_by_name(name)

#browser.find_element_by_tag_name(name)             #Elements with a matching tag name (case insensitive; an <a> element 
#browser.find_elements_by_tag_name(name)            #is matched by 'a' and 'A')


#ATTRiBUTE OR METHOD                                #DESCRiPTiON
#tag_name                                           #The tag name, such as 'a' for an <a> element

#get_attribute(name)                                #The value for the element’s name attribute

#text                                               #The text within the element, such as 'hello' in <span>hello</span>

#clear()                                            #For text field or text area elements, clears the text typed into it

#is_displayed()                                     #Returns True if the element is visible; otherwise returns False

#is_enabled()                                       #For input elements, returns True if the element is enabled; otherwise returns False

#is_selected()                                      #For checkbox or radio button elements, returns True if the element is selected; otherwise returns False

#location                                           #A dictionary with keys 'x' and 'y' for the position of the element in the page


#ATTRiBUTES                                         #MEANiNGS
#Keys.DOWN, Keys.UP, Keys.LEFT, Keys.RiGHT          #The keyboard arrow keys

#Keys.ENTER, Keys.RETURN                            #The ENTER and RETURN keys

#Keys.HOME, Keys.END, Keys.PAGE_DOWN, Keys.PAGE_UP  #The home, end, pagedown, and pageup keys

#Keys.ESCAPE, Keys.BACK_SPACE, Keys.DELETE          #The ESC, BACKSPACE, and DELETE keys

#Keys.F1, Keys.F2,..., Keys.F12                     #The F1 to F12 keys at the top of the keyboard

#Keys.TAB                                           #The TAB key




    
    
    
    
    