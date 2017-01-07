# -*- coding: utf-8 -*-
'''
Created on 5 Oca 2017

@author: Purgoufr
'''

# #Unix caginda, programlamada siklikla kullanilan bir zaman referansi vardir: 12 Ocak, 1 Ocak 1970, Esgudumsel Evrensel Saat (UTC).
# #Bu kodda suanki zamani UTC referans saatinden cikarip saniyeye cevirdik
# import time
# print(time.time())

#----------------------------------------------------------------------------------------
# #islemlerin calisma surelerini hesaplama
# import time
# def calcProd():
#     # Calculate the product of the first 100,000 numbers.
#     product = 1
#     for i in range(1, 100000):
#         product = product * i
#     return product
# 
# startTime = time.time()
# prod = calcProd()
# endTime = time.time()
# print('The result is %s digits long.' % (len(str(prod))))
# print('Took %s seconds to calculate.' % (endTime - startTime))

#----------------------------------------------------------------------------------------
##programi bir sure dondurmak icin(pause); time.sleep() fonksiyonu kullanilir
# 1 saniye dondurup geri baslatiyoruz
# import time
# for i in range(3):
#     print('Tick')
#     time.sleep(1)
#     print('Tock')
#     time.sleep(1)

#----------------------------------------------------------------------------------------
# #zamandaki saniyenin virgulden sonra kac hanesini gormek istiyorsan round() function kullanacaksin
# import time
# now = time.time()
# print(round(now, 2))
# print(round(now, 4))
# print(round(now))

#----------------------------------------------------------------------------------------
# #ornek Stopwatch uygulamasi
# import time
# 
# # Display the program's instructions.
# print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch.Press Ctrl-C to quit.')
# input()                    # press Enter to begin
# print('Started.')
# startTime = time.time()    # get the first lap's start time
# lastTime = startTime
# lapNum = 1
# 
# # Start tracking the lap times.
# try:
#     while True:
#         input()
#         lapTime = round(time.time() - lastTime, 2)
#         totalTime = round(time.time() - startTime, 2)
#         print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
#         lapNum += 1
#         lastTime = time.time() # reset the last lap time
# except Keyboardinterrupt:
#     # Handle the Ctrl-C exception to keep its error message from displaying.
#     print('\nDone.')

#----------------------------------------------------------------------------------------
# #suanki zamani getir
# import datetime
# x=datetime.datetime.now()
# print(x)
# 
# #tarih olusturma
# dt = datetime.datetime(2015, 10, 21, 16, 29, 0)
# print(dt.year, dt.month, dt.day)
# print(dt.hour, dt.minute, dt.second)
# 
# #tarih olusturma
# halloween2015 = datetime.datetime(2015, 10, 31, 0, 0, 0)
# newyears2016 = datetime.datetime(2016, 1, 1, 0, 0, 0)
# oct31_2015 = datetime.datetime(2015, 10, 31, 0, 0, 0)
# 
# print(newyears2016 > halloween2015)
# print(halloween2015 == oct31_2015)
# 
# #tarih olusturma
# delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
# delta.days, delta.seconds, delta.microseconds
# 
# #UTC unix time 
# print(datetime.datetime.fromtimestamp(1000000))
# #UTC unix time seconds
# print(delta.total_seconds())
# 
# #suanki zamana 1000 gun ekleme
# dt = datetime.datetime.now()
# print(dt)
# datetime.datetime(2015, 2, 27, 18, 38, 50, 636181)
# thousandDays = datetime.timedelta(days=1000)
# print(dt + thousandDays)
# 
# #zamandan zaman cikarmak
# oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
# aboutThirtyYears = datetime.timedelta(days=365 * 30)
# print(oct21st)
# print(oct21st - aboutThirtyYears)
# print(oct21st - (2 * aboutThirtyYears))

# #tarihleri duzenli goster
# oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
# print(oct21st.strftime('%Y/%m/%d %H:%M:%S'))
# 
# #am pm gosterme
# print(oct21st.strftime('%i:%M %p'))
# 
# #tum ismi goster
# print(oct21st.strftime("%B of '%y"))
# 
# print(datetime.datetime.strptime('October 21, 2015', '%B %d, %Y'))
# 
# print(datetime.datetime.strptime('2015/10/21 16:29:00', '%Y/%m/%d %H:%M:%S'))
# 
# #ay isminin tamamini girip sonucu kisaltma
# print(datetime.datetime.strptime("October of '15", "%B of '%y"))
# 
# print(datetime.datetime.strptime("November of '63", "%B of '%y"))

#----------------------------------------------------------------------------------------
#                            THREAD
#----------------------------------------------------------------------------------------

# import threading
# threadObj = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'],kwargs={'sep': ' & '})
# print(threadObj.start())

#----------------------------------------------------------------------------------------
# #ornek program XKCD den resim indirecegiz fakat resimleri teker teker degil coklu indirecegiz
# import requests, os, bs4, threading
# 
# #os.makedirs('xkcd')
#             
# #os.makedirs('xkcd', exist_ok=True) # store comics in ./xkcd
# 
# if not os.path.exists('xkcd'):
#     os.makedirs('xkcd')   # store comics in ./xkcd
# 
# def downloadXkcd(startComic, endComic):
#     for urlNumber in range(startComic, endComic):
#         # Download the page.
#         print('Downloading page http://xkcd.com/%s...' % (urlNumber))
#         res = requests.get('http://xkcd.com/%s' % (urlNumber))
#         res.raise_for_status()
#         
#         soup = bs4.BeautifulSoup(res.text)
#         
#         # Find the URL of the comic image.
#         comicElem = soup.select('#comic img')
#         if comicElem == []:
#             print('Could not find comic image.')
#         else:
#             comicUrl = comicElem[0].get('src')
#             # Download the image.
#             print('Downloading image %s...' % (comicUrl))
#             res = requests.get(comicUrl)
#             res.raise_for_status()
#             
#             # Save the image to ./xkcd.
#             imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
#             for chunk in res.iter_content(100000):
#                 imageFile.write(chunk)
#                 imageFile.close()
#                 
# # Create and start the Thread objects.
# downloadThreads = []             # a list of all the Thread objects
# for i in range(0, 1400, 100):    # loops 14 times, creates 14 threads
#     downloadThread = threading.Thread(target=downloadXkcd, args=(i, i + 99))
#     downloadThreads.append(downloadThread)
#     downloadThread.start()
#     
# # Wait for all threads to end.
# for downloadThread in downloadThreads:
#     downloadThread.join()
# print('Done.')

#----------------------------------------------------------------------------------------
# #pythonla programlari calistirma
# #ornek hesap makinesi calistirma
# import subprocess
# subprocess.Popen('C:\\Windows\\System32\\calc.exe')

#----------------------------------------------------------------------------------------
# import subprocess
# #Poll () yontemi, surec hala poll () cagrildiginda calistiriliyorsa None dondurur.
# #NOTE DEBUG yaparak nasil calistigini gorebilirsin.Debug modda hesap makinesi 
# #acildiginda bir sonraki step e gecmeden kapat ve false dondugunu gor
# calcProc = subprocess.Popen('c:\\Windows\\System32\\calc.exe')
# print(calcProc.poll() == None)
# 
# #Wait () yontemi, arkadasiniz sizinle calismaya baslamadan once kodunu bitirmesini beklemek gibidir.
# print(calcProc.wait())
# print(calcProc.poll())

#----------------------------------------------------------------------------------------
# #Dosya olusturma, dosyaya yazi yazma, dosyayi acma
# fileObj = open('hello.txt', 'w')
# fileObj.write('Hello world!')
# 
# fileObj.close()
# import subprocess
# subprocess.Popen(['start', 'hello.txt'], shell=True)

#----------------------------------------------------------------------------------------
# #ornek script geri sayim sayaci, sayac 0 olunca muzik calacak
# #her bir saniye beklemek icin time.sleep() fonksiyonu kullanilacak
# #sayac 0 olunca muzik dosyasini acmak icin subprocess.Popen() kullanacaz
# 
# import time, subprocess
# 
# timeLeft = 60
# while timeLeft > 0:
#     print(timeLeft)
#     time.sleep(1)
#     timeLeft = timeLeft - 1
#     
# # At the end of the countdown, play a sound file.
# subprocess.Popen(['start', 'alarm.wav'], shell=True)

#----------------------------------------------------------------------------------------


























