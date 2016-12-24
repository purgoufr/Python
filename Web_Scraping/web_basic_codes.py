# -*- coding: utf-8 -*-
'''
Created on 24 Ara 2016

@author: Purgoufr
'''

#Genel olarak yaptığımız olayın adı web scraping
#web scraping: çeşitli yazılım ve metotlar ile hedef web sitelerinden içerik kopyalama* veya belli bilgileri alma işlemine verilen isim
# #istedi�in URL i a�ma
# import webbrowser
# webbrowser.open('http://inventwithpython.com/')

#----------------------------------------------------------------------------------------
# #Örnek program kopyaladığın adresi google maps te uygulamayı çalıştırdığında açar(Ctrl+C yap ve run a bas)
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
#len(res.text) ile text dosyasının boyutunu öğrendik
#printlen(res.text[:500]) yaparak 500 karakterlik kısmını yazdırdık dosyada 178.000 karakter var

# import requests 
# res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
# type(res)
# #res.status_code == requests.codes.ok    #kod çalışmadı(bu kodda istek yaptığımız link durumunu sorguladık(true or false?)
# print(res.raise_for_status())  #linki kontrol eder problem varsa hata verir
# print(len(res.text))
# print(res.text[:500])

#----------------------------------------------------------------------------------------
# #Linkteki sorunu debugla bulalım
# #request.get ile linki yazdık ve res.raise_for_status() ile linki kontrol ettik
# 
# import requests
# res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
# try:
#     res.raise_for_status()
# except Exception as exc:
#     print('There was a problem: %s' % (exc))

#----------------------------------------------------------------------------------------
#Dosyayı bilgisayara kaydetme
#Note: write binary mode yani wb. Metnin Unicode kodlamasını korumak için metin(string)
#verileri yerine ikili veri(binary) yazmanız gerekir.
#open komuyla text dosyası oluşturduk
#response objesini döngüye almak için for loop içinde iter_content() kullandık
#playFile.write ile text dosyasına request ettiğimiz içeriği yazdık
# import requests
# res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
# res.raise_for_status()
# playFile = open('C:\\Users\\Purgoufr\\Documents\\Eclipse Projects\\Python\\Web_Scraping\\web_test_folder\\RomeoAndJuliet.txt', 'wb')
# for chunk in res.iter_content(100000):
#     playFile.write(chunk)
# playFile.close()

#----------------------------------------------------------------------------------------
# #Parsing HTML with the BeautifulSoup Module(siteden istediğin kısmı çekme(istediğin class ı çekme parse etme))
# #Parse için Beautiful Soup modülünü kullanacağız
# #Bu kodda requests.get() il No Starch Press in ana sayfasını indirmek için kullandık
# #BeautifulSoup nesnesi noStarchSoup adlı bir değişkende depolanır.
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
# select() sorguları
#soup.select('div')          All elements named <div> (<div> adlı tüm elemanlar)

#soup.select('#author')      The element with an id attribute of author( author id özellikli tüm elemanlar )

#soup.select('.notice')      All elements that use a CSS class attribute named notice(notice adlı CSS class özellikli tüm elemanlar):

#soup.select('div span')     All elements named <span> that are within an element named <div>(<div> ve <span> adlı tüm elemanlar)

#soup.select('div > span')   All elements named <span> that are directly within an element named <div>, with no other
#                            element in between(<Span> adlı ve doğrudan <div> adlı bir öğenin içinde bulunan ve arasında
#                            başka bir öğe bulunmayan tüm öğeler)

#soup.select('input[name]')  All elements named <input> that have a name attribute with any value(Herhangi bir değere sahip 
#                            name özniteliğine sahip <input> isimli tüm öğeler)

#soup.select('input[type="button"]')  All elements named <input> that have an attribute named type with value button 
#                                     input adında buton değerine sahip(buton) özelliği taşıyan bütün elemanlar  
    
#----------------------------------------------------------------------------------------
#daha önce oluşturduğumuz example.html dosyasından author ile ilgili bilgileri getirdik bu bilgiler
import bs4
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read())
elems = exampleSoup.select('#author')
print(type(elems))
print(len(elems))
print(type(elems[0]))
print(elems[0].getText())
print(str(elems[0]))
print(elems[0].attrs)

pElems = exampleSoup.select('p')
print(str(pElems[0]))
print(pElems[0].getText())
print(str(pElems[1]))
print(pElems[1].getText())
print(str(pElems[2]))
print(pElems[2].getText())

    

   
    
    
    
    
    
    
    
    
    