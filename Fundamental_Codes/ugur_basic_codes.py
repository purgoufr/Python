# -*- coding: utf-8 -*-
'''
Created on 18 Ara 2016

@author: Purgoufr
'''
#----------------------------------------------------------------------------------------
##dizideki değerleri göster
# spam = {'color': 'red', 'age': 42}
# for v in spam.values():
#     print(v)
#     print('\n')
# 
# #dizideki keyleri(kategorileri) göster    
# for k in spam.keys():
#     print(k)
#     print('\n')
#  
##dizideki itemleri sınıflandırarak göster    
# for i in spam.items():
#     print(i)
#     print('\n')
#     
# for k, v in spam.items():
#     print('Key: ' + k + ' Value: ' + str(v))
#     print('\n')    

#----------------------------------------------------------------------------------------
# 
# #Komut satırına 1 ve 2 yi yazarsan ekranda screen satırını görürsün 
# #1picnicItems = {'apples': 5, 'cups': 2}
# #2'I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.'
# #screen=>'I am bringing 2 cups.'
# 
# spamTwo = {'name': 'Pooka', 'age': 5}
# spamTwo.setdefault('color', 'black')    #setdefault değişkenin içine bakar color yoksa değişkende kendisi atar varsa değiştirmez
# spamTwo.setdefault('color', 'white')    #değer bir kere set edilirse bir dahakine değişmez o yüzden color black olarak kalır white olmaz
# print(spamTwo)
# print('\n')

#----------------------------------------------------------------------------------------
# #yazıdaki harflerin kaç kere kullanıldığını göster
# message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
# count = {}
# 
# for character in message:
#     count.setdefault(character, 0)
#     count[character] = count[character] + 1
# 
# print(count)

#----------------------------------------------------------------------------------------
#pprint ; print formatını değiştirir printlenen şeyleri düzgün gösterir(alt alta gösterir)
# import pprint
# messageTwo = 'It was a bright cold day in April, and the clocks were striking thirteen.'
# count = {}
# 
# for character in messageTwo:
#     count.setdefault(character, 0)
#     count[character] = count[character] + 1
# 
# pprint.pprint(count)

#----------------------------------------------------------------------------------------
# # dizideki elemanlardan aynı isme sahip üylerinin değerlerini toplar.Örneğin apples Alice te 5 tane Bob da 2 tane var toplam 7
# allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
# 'Bob': {'ham sandwiches': 3, 'apples': 2},
# 'Carol': {'cups': 3, 'apple pies': 1}}
# 
# def totalBrought(guests, item):
#     numBrought = 0
#     for k, v in guests.items():
#         numBrought = numBrought + v.get(item, 0)
#     return numBrought
# 
# print('Number of things being brought:')
# print(' - Apples         ' + str(totalBrought(allGuests, 'apples')))
# print(' - Cups           ' + str(totalBrought(allGuests, 'cups')))
# print(' - Cakes          ' + str(totalBrought(allGuests, 'cakes')))
# print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
# print(' - Apple Pies     ' + str(totalBrought(allGuests, 'apple pies')))

#----------------------------------------------------------------------------------------
# #Çok satırlı dizeleri kullanmak için çift tırnak kullanılır
# print('''Dear Alice,
# 
# Eve's cat has been arrested for catnapping, cat burglary, and extortion.
# 
# Sincerely,
# Bob''')
#
#print('Dear Alice,\n\nEve\'s cat has been arrested for catnapping, cat burglary, and extortion.\n\nSincerely,\nBob')

##ikiside aynı işi görür

#----------------------------------------------------------------------------------------
#baştan sondan tek veya daha çok eleman getirme
# spam = 'Hello world!'
# print(spam[0])
# print(spam[4])
# print(spam[-1])
# print(spam[0:5])
# print(spam[:5])
# print(spam[6:])

#----------------------------------------------------------------------------------------
# #string in karakterlerini büyük harf ya da küçük harf yapma
# spam = 'Hello world!'
# print(spam.upper())
# print(spam.lower())

#----------------------------------------------------------------------------------------
# #input isteme- input girişi
# print('How are you?')
# feeling = input()
# if feeling.lower() == 'great':
#     print('I feel great too.')
# else:
#     print('I hope the rest of your day is good.')

#----------------------------------------------------------------------------------------
# #string deki yazının karakterlerinin tamamı küçük mü büyük mü kontrol eder
# spam = 'Hello world!'
# 
# print(spam.islower())
# 
# print(spam.isupper())
# 
# print('HELLO'.isupper())
# 
# print('abc12345'.islower())
# 
# print('12345'.islower())
# 
# print('12345'.isupper())

#----------------------------------------------------------------------------------------
# #örnek uygulama input alma hepsi sayı mı hepsi karaktermi kontrol etme
# while True:
#     print('Enter your age:')
#     age = input()
#     if age.isdecimal():
#         break
#     print('Please enter a number for your age.')
# 
# while True:
#     print('Select a new password (letters and numbers only):')
#     password = input()
#     if password.isalnum():
#         break
#     print('Passwords can only have letters and numbers.')

#----------------------------------------------------------------------------------------
##başlangıçta ve sonda(cümlenin başlangıcında ve sonunda) kelimeleri kontrol etmek için kullanılır
# print('Hello world!'.startswith('Hello'))
# 
# print('Hello world!'.endswith('world!'))
# 
# print('abc123'.startswith('abcdef'))
# 
# print('abc123'.endswith('12'))
# 
# print('Hello world!'.startswith('Hello world!'))
# 
# print('Hello world!'.endswith('Hello world!'))

#----------------------------------------------------------------------------------------
##dizinin elemanlarına virgülden sonra tırnak içinde yazdığın şeyleri ekler
# print(', '.join(['cats', 'rats', 'bats']) )
# 
# print(' '.join(['My', 'name', 'is', 'Simon']))
# 
# print('ABC'.join(['My', 'name', 'is', 'Simon']))

#----------------------------------------------------------------------------------------
##join'in tam tersi string i parçalara böler
# print('My name is Simon'.split())
# print('MyABCnameABCisABCSimon'.split('ABC'))
# print('My name is Simon'.split('m'))

# spam = '''Dear Alice,
# How have you been? I am fine.
# There is a container in the fridge
# that is labeled "Milk Experiment".
# 
# Please do not drink it.
# Sincerely,
# Bob'''
# print(spam.split('\n'))

#----------------------------------------------------------------------------------------
# #string in önüne veya arkasına boşluk koymak için kullanılır
# print('Hello'.rjust(10))
# 
# print('Hello'.rjust(20))
# 
# print('Hello World'.rjust(20))
# 
# print('Hello'.ljust(10))
# print('Hello'.rjust(20, '*'))
# print('Hello'.ljust(20, '-'))

#----------------------------------------------------------------------------------------
# #string in başına ve sonuna istediğin karakteri ekler
# print('Hello'.center(20))
# print('Hello'.center(20, '='))

#----------------------------------------------------------------------------------------
# #örnek uygulama liste oluşturma 
# def printPicnic(itemsDict, leftWidth, rightWidth):
#     print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
#     for k, v in itemsDict.items():
#         print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
# picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
# printPicnic(picnicItems, 12, 5)
# printPicnic(picnicItems, 20, 6)

#----------------------------------------------------------------------------------------
# # string deki boşluğu silme sağdaki soldaki boşluğu silme kelime silme
# spam = '    Hello World     '
# print(spam.strip())
# print(spam.lstrip())
# print(spam.rstrip())
#spam = 'SpamSpamBaconSpamEggsSpamSpam'
#print(spam.strip('ampS'))

#----------------------------------------------------------------------------------------
# Örnek program text içindeki yazıdan istenilen kısmı çekme bu örnekte telefon çektik
# def isPhoneNumber(text):
#     if len(text) != 12:
#         return False
#     for i in range(0, 3):
#         if not text[i].isdecimal():
#             return False
#         if text[3] != '-':
#             return False
#         for i in range(4, 7):
#             if not text[i].isdecimal():
#                 return False
#             if text[7] != '-':
#                 return False
#             for i in range(8, 12):
#                 if not text[i].isdecimal():
#                     return False
#                 return True
#             
# 
# print('415-555-4242 is a phone number:')
# print(isPhoneNumber('415-555-4242'))
# 
# message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
# for i in range(len(message)):
#     chunk = message[i:i+12]
#     if isPhoneNumber(chunk):
#         print('Phone number found: ' + chunk)
#         print('Done')

#----------------------------------------------------------------------------------------
# #kelimenin sağına, soluna veya her iki tarafına karakter ekleme
# print('Hello'.rjust(20, '*'))
# print('Hello'.ljust(20, '-'))
#print('Hello'.center(20))
#print('Hello'.center(20, '='))

#----------------------------------------------------------------------------------------
#Creating Regex Objects(regex objesiyle bir string in içerisinden istediğiniz grubu search yapabilirsin 
# arayabilirsin filtreliyebilirsin seçebilirsin 
#Örnek program da bir string oluşturduk ve içinden telefon numarası çektik ya da karşılaştırma yaptık

#import re   #import etmeyi unutma!!!
# #'\d '  Any numeric digit from 0 to 9.

# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# mo = phoneNumRegex.search('My number is 415-555-4242.')
# print('Phone number found: ' + mo.group())
# 
#import re 
# phoneNumRegexTWO = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# moTWO = phoneNumRegexTWO.search('My number is 415-555-4242.')
# print(moTWO.groups())
# print(moTWO.group(0))
# print(moTWO.group(1))
# print(moTWO.group(2))
# areaCode, mainNumber = moTWO.groups()
# print('areaCode is :'+ areaCode +'\n'+ 'mainNumber is:' + mainNumber)

#import re 
# phoneNumRegexThree = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
# mo = phoneNumRegexThree.search('My phone number is (415) 555-4242.')
# print('1. grup=' + mo.group(1) + '\n2. grup =' + mo.group(2))

#import re 
# heroRegex = re.compile (r'Batman|Tina Fey')
# mo1 = heroRegex.search('Batman and Tina Fey.') #benzer kelimeleri seç burada sadece batman uyuyor
# print(mo1.group())
# mo2 = heroRegex.search('Tina Fey') #search ettiğin stringe tamamen bezer olması lazım örneğin FEY aratırsan hata verir
# print(mo2.group())
# mo3 = heroRegex.search('Tina FeyYY and Batman.')
# print(mo3.group())

#import re 
# phoneNumRegexFour = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
# print(phoneNumRegexFour.findall('Cell: 415-555-9999 Work: 212-555-0000')) #arama kalıbına uyanların hepsini getirir
#
#import re  
# phoneNumRegexFive = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
# print(phoneNumRegexFive.findall('Cell: 415-555-9999 Work: 212-555-0000'))

# #sessiz harfleri getir
# import re 
# consonantRegex = re.compile(r'[^aeiouAEIOU]')
# print(consonantRegex.findall('Robocop eats baby food. BABY FOOD.'))

##istediğin harflerle biten kelimeleri getirir
# import re 
# atRegex = re.compile(r'.at')
# print(atRegex.findall('The cat in the hat sat on the flat mat.'))

# #istediğin kelimeleri getirir
# import re 
# nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
# mo = nameRegex.search('First Name: Al Last Name: Sweigart')
# print(mo.group(1))
# print(mo.group(2))

# #belirlediğin simgelerin arasında kalan kelimeleri herşeyi getirir
# import re 
# nongreedyRegex = re.compile(r'<.*?>')
# mo = nongreedyRegex.search('<To serve man> for dinner.>')
# print(mo.group())

# #ilk noktaya kadar olan kelimeleri getir
# import re 
# noNewlineRegex = re.compile('.*')
# print(noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())
# #noktayla biten kelimelerin hepsini getir
# newlineRegexTwo = re.compile('.*', re.DOTALL)
# print(newlineRegexTwo.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())

# #istediğin kelimeyi büyük küçük harf gözetmeksizin getirir
# import re 
# robocop = re.compile(r'robocop', re.I)
# print(robocop.search('Robocop is part man, part machine, all cop.').group())
# print(robocop.search('Al, why does your programming book talk about robocop so much?.').group())

# #istediğin kelimeyi seçeceğin kelime ile yer değiştirme
# import re 
# namesRegex = re.compile(r'Agent \w+')
# print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))

# #istediğin kelimeyi istediğin yerden sonra istediğin karakterle değiştirme
# import re 
# agentNamesRegex = re.compile(r'Agent (\w)\w*')
# print(agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))

#----------------------------------------------------------------------------------------
# #path göstermek için kullanılır. Gerçekte oluşturmuyoruz sadece path gösterdik
# import os
# 
# myFiles = ['A.txt', 'B.csv', 'C.docx']
# for filename in myFiles:
#     print(os.path.join('C:\\Users\\Purgoufr', filename))
  
# #workspace ini (çalıştığın dosyanın konumunu)  otomatik getirir     
# import os
# print(os.getcwd())

# #çalıştığın dosyanın konumunu(path) değiştirir
# import os
# os.chdir('C:\\Windows\\System32')

# #Yeni dosya oluşturma
# import os
# os.makedirs('C:\\Users\\Purgoufr\\Desktop\\test_file')

# #çalıştığın dosya path ini bulur
# import os
# print(os.path.abspath('.'))

# #path belirttiğin uygulamanın .exe ve dosya konumunu ayrı ayrı getirir
# import os
# path = 'C:\\Windows\\System32\\calc.exe'
# print(os.path.basename(path))
# print(os.path.dirname(path))

#calcFilePath = 'C:\\Windows\\System32\\calc.exe'
#print(os.path.split(calcFilePath))
#print(calcFilePath.split(os.path.sep))

##uygulamanın size (boyutunu) getirme -- byte olarak
# import os
# print(os.path.getsize('C:\\Windows\\System32\\calc.exe'))

# #dosyanın içindeki dosyaları listeler getirir
# import os
# print(os.listdir('C:\\Users\\Purgoufr\\Desktop'))

# # Doğrulama işlemleri dosya mıdır? gibi
# import os
# print(os.path.isdir('C:\\Windows\\System32\\calc.exe'))
# print(os.path.isfile('C:\\Windows\\System32\\calc.exe'))

#----------------------------------------------------------------------------------------
# # Var olan dosya içeriğini açma dosya açma
# helloFile = open('C:\\Users\\Purgoufr\\Desktop\\hello.txt')
# helloContent = helloFile.read()
# print(helloContent)

# #Örnek program dosya oluşturma, oluşturulan dosyaya yazı yazma, dosyayı getirme 
# UgurTextFile = open('ugur_text.txt', 'w')
# UgurTextFile.write('Hello world!\n')
# UgurTextFile.close()
# UgurTextFile = open('ugur_text.txt', 'a')
# UgurTextFile.write('Ugur is not a vegetable.')
# UgurTextFile.close()
# UgurTextFile = open('ugur_text.txt')
# content = UgurTextFile.read()
# UgurTextFile.close()
# print(content)

#----------------------------------------------------------------------------------------
# #copy paste yapma(copy file, destination file(paste) (source,destination) 
# #Bu dosyalar varolmadığı için hata verecek gerçekte varolan dosyalarda denersen çalıştığını göreceksin
# import shutil, os
# os.chdir('C:\\')
# shutil.copy('C:\\spam.txt', 'C:\\delicious')
# #eggs.txt dosyasını kopyaladı fakat ismini değiştirerek yapıştırdı eggs2.txt olarak
# shutil.copy('eggs.txt', 'C:\\delicious\\eggs2.txt')
# #sadece tek bir dosya degil ('.txt' gibi değil klasör olarak) dosyanın alt dosyalarını da kopyalamak için
# shutil.copytree('C:\\bacon', 'C:\\bacon_backup')

# #dosya taşımak için(yer değiştirmek)(source,destination) dosya isim değiştirmek için
# import shutil
# shutil.move('C:\\bacon.txt', 'C:\\eggs')

# #Hem yer değiştirip hem de yeni isim vermek için
# shutil.move('C:\\bacon.txt', 'C:\\eggs\\new_bacon.txt')

# #Note: Eğer taşımak istediğin klasör gerçekte yoksa o zaman taşıma olmaz ama 
# #source un ismi değişir aşağıdaki için bacon > eggs olur
# shutil.move('C:\\bacon.txt', 'C:\\eggs')

#----------------------------------------------------------------------------------------
# #path i kalıcı olarak silmek
# import os
# os.unlink(path)
# 
# #path deki dosyayı silme
# os.rmdir(path)
# 
# #path deki dosyayı ve uzantılarını silme(klasörü silme)
# shutil.rmtree(path)

# #örnek program .rxt ile biten dosyaları silecek(önlem olarak 456 ya comment koydum)
# import os
# for filename in os.listdir():
#     if filename.endswith('.rxt'):
#         #os.unlink(filename)
#         print(filename)

#----------------------------------------------------------------------------------------
# #You can install this module by running pip install send2trash from a Terminal window.
# #güvenli dosya silmek için kullanılır.Daha sonra geri dönüşüm kutusundan geri getirebilirsin
# import send2trash
# baconFile = open('bacon.txt', 'a') # creates the file
# baconFile.write('Bacon is not a vegetable.')
# baconFile.close()
# send2trash.send2trash('bacon.txt')

#----------------------------------------------------------------------------------------
# örnek program; dosya adındaki amerikan style tarihi avrupa style a çevirme (MM-DD-YYYY>>DD-MM-YYYY)
# gün için belirtilen (0|1)?\d)>> tarih belirtirken 01,1,10 gibi 3 farklı şekilde yazılan
# gün tipini kabul etmek için
# ay için belirtilen (0|1|2|3)?\d)>> 01,2,31 gibi 3 farklı şekilde yazılan
# ay tipini kabul etmek için
# yıl için belirtilen (19|20)\d\d)>> 1991,2000 gibi 20 ve 21. yüzyıl ifadeleri için
# yıl tipini kabul etmek için. yıl için 1777 gibi 20 ve21. yy dışında yıl girersen hata alırsın
#Note: buradaki sorunlar 0-15-2000-02-31-2015 gibi yanlış tarihleri de doğru sayacaktır

# import shutil, os, re
# datePattern = re.compile(r"""^(.*?) ((0|1)?\d) - ((0|1|2|3)?\d) - ((19|20)\d\d) (.*?)$ """, re.VERBOSE)
# 
# for amerFilename in os.listdir('C:\\Users\Purgoufr\\Documents\\Eclipse Projects\\Python\\Fundamental_Codes\\test_folder'):
#     mo = datePattern.search(amerFilename)
#     
# # Skip files without a date.
#     if mo == None:
#         continue
# 
# # Get the different parts of the filename.
#     beforePart = mo.group(1)
#     monthPart  = mo.group(2)
#     dayPart    = mo.group(4)
#     yearPart   = mo.group(6)
#     afterPart  = mo.group(8)
# 
# # Form the European-style filename.
#     euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
# 
# # Get the full, absolute file paths.
#     absWorkingDir = os.path.abspath('C:\\Users\Purgoufr\\Documents\\Eclipse Projects\\Python\\Fundamental_Codes\\test_folder')
#     amerFilename = os.path.join(absWorkingDir, amerFilename)
#     euroFilename = os.path.join(absWorkingDir, euroFilename)
# 
# # Rename the files.
#     print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
#     shutil.move(amerFilename, euroFilename)   # uncomment after testing

#----------------------------------------------------------------------------------------
# #örnek program dosyanın içindeki metin içeriğini değiştirme
# #Bir üstteki örnek programdan farkı 
# #üstteki programda dosya adlarındaki tarihleri amerikan style dan europe style a çevirdi
# #Bu programda text içindeki tarhileri amerikan style dan europe style a çevirdi
# import shutil, os, re
# UgurTextFile2 = open('C:\\Users\\Purgoufr\\Documents\\Eclipse Projects\\Python\\Fundamental_Codes\\test_folder\\date_test_2_31-05-2016.txt', 'w')
# UgurTextFile = open('C:\\Users\\Purgoufr\\Documents\\Eclipse Projects\\Python\\Fundamental_Codes\\test_folder\\date_test31-05-2016.txt')
# datePattern = re.compile(r"""^(.*?) ((0|1)?\d) - ((0|1|2|3)?\d) - ((19|20)\d\d) (.*?)$ """, re.VERBOSE)
# for amerFilename in UgurTextFile:
#     mo = datePattern.search(amerFilename)
#     # Skip files without a date.    
#     if mo == None:
#         UgurTextFile2 = open('C:\\Users\\Purgoufr\\Documents\\Eclipse Projects\\Python\\Fundamental_Codes\\test_folder\\date_test_2_31-05-2016.txt', 'a')
#         UgurTextFile2.write(amerFilename)
#         continue
#     
#     # Get the different parts of the filename.
#     beforePart = mo.group(1)
#     monthPart  = mo.group(2)
#     dayPart    = mo.group(4)
#     yearPart   = mo.group(6)
#     afterPart  = mo.group(8)
#     
#     # Form the European-style filename.
#     euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
#     
#     UgurTextFile2 = open('C:\\Users\\Purgoufr\\Documents\\Eclipse Projects\\Python\\Fundamental_Codes\\test_folder\\date_test_2_31-05-2016.txt', 'a')
#     UgurTextFile2.write(euroFilename + '\n')
#     UgurTextFile2.close()
    
#----------------------------------------------------------------------------------------
# #örnek program debug, raise exception ile şekil oluştururken koşula uymayan sayılarda hata verdirdik
# def boxPrint(symbol, width, height):
#     if len(symbol) != 1:
#         raise Exception('Symbol must be a single character string.')
#     if width <= 2:
#         raise Exception('Width must be greater than 2.')
#     if height <= 2:
#         raise Exception('Height must be greater than 2.')
#     print(symbol * width)
#     for i in range(height - 2):
#         print(symbol + (' ' * (width - 2)) + symbol)
#     print(symbol * width)
#     
# for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
#     try:
#         boxPrint(sym, w, h)
#     except Exception as err:
#             print('An exception happened: ' + str(err))
        
#----------------------------------------------------------------------------------------






