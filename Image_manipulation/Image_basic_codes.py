# -*- coding: utf-8 -*-
'''
Created on 9 Oca 2017

@author: Purgoufr
'''
# 
# #Renklerin Standart rgba degeri, Standard Color Names and Their RGBA Values
# 
# from PiL import imageColor
# print(imageColor.getcolor('red', 'RGBA'))
# print(imageColor.getcolor('RED', 'RGBA'))
# print(imageColor.getcolor('Black', 'RGBA'))
# print(imageColor.getcolor('chocolate', 'RGBA'))
# print(imageColor.getcolor('CornflowerBlue', 'RGBA'))

#----------------------------------------------------------------------------------------
# #Resim dosyasi acma
# from PiL import image
# catim = image.open('zophie.png')
# print(catim.size)
# 
# #Resim boyutunu getir
# width, height = catim.size
# print(width)
# print(height)
# 
# #Resim adini getir
# print(catim.filename)
# 
# #Resim formatini getir
# print(catim.format)
# print(catim.format_description)
# 
# #Resim formatini degistirme 
# catim.save('zophie.jpg')

#----------------------------------------------------------------------------------------
# # Resim dosyasi olusturma
# from PiL import image
# im = image.new('RGBA', (100, 200), 'purple')
# im.save('purpleimage.png')
# im2 = image.new('RGBA', (20, 20))
# im2.save('transparentimage.png')

#----------------------------------------------------------------------------------------
# # Resimin bir parca kesme 
# from PiL import image
# catim = image.open('zophie.png')
# print(catim.size)
# croppedim = catim.crop((335, 345, 565, 560))
# croppedim.save('cropped.png')

#----------------------------------------------------------------------------------------
# #Resim kopyalama     
# from PiL import image
# catim = image.open('zophie.png')
# catCopyim = catim.copy()
# 
# #Resimi kes
# faceim = catim.crop((335, 345, 565, 560))
# print(faceim.size)
# 
# #Resim yapistirma
# catCopyim.paste(faceim, (0, 0))
# #Resim yapistirma 
# catCopyim.paste(faceim, (400, 500))
# catCopyim.save('pasted.png')

#----------------------------------------------------------------------------------------
# #Resimden bir parca kopyalayip resimin tamamina yapistirma
# from PiL import image
# catim = image.open('zophie.png')
# catimWidth, catimHeight = catim.size
# 
# faceim = catim.crop((335, 345, 565, 560))
# 
# faceimWidth, faceimHeight = faceim.size
# catCopyTwo = catim.copy()
# 
# for left in range(0, catimWidth, faceimWidth):
#     for top in range(0, catimHeight, faceimHeight):
#         print(left, top)
#         catCopyTwo.paste(faceim, (left, top))
# catCopyTwo.save('tiled.png')

#----------------------------------------------------------------------------------------
# #Resimin boyutlarini degistirme
# 
# from PiL import image
# #Orijinal resim boyutu
# catim = image.open('zophie.png')
# width, height = catim.size
# 
# #yuksekligi ve genisligi 2 ye bolduk
# quartersizedim = catim.resize((int(width / 2), int(height / 2)))
# quartersizedim.save('quartersized.png')
# 
# #yukseklige ve genislige 500 ekledik
# svelteim = catim.resize((width+500, height + 500))
# svelteim.save('svelte.png')

#----------------------------------------------------------------------------------------
# #Resimi dondurme
# from PiL import image
# 
# catim = image.open('zophie.png')
# catim.rotate(90).save('rotated90.png')
# catim.rotate(180).save('rotated180.png')
# 
# # Rotate() yonteminde, dondurulen yeni goruntunun tumune uyacak sekilde olmasi icin True anahtarini kullan
# 
# catim.rotate(6).save('rotated6.png')
# catim.rotate(6, expand=True).save('rotated6_expanded.png')
# 
# #Ayna (mirror) yontemiyle saga sola yukari assagi dondurme
# catim.transpose(image.FLiP_LEFT_RiGHT).save('horizontal_flip.png')
# catim.transpose(image.FLiP_TOP_BOTTOM).save('vertical_flip.png')

#----------------------------------------------------------------------------------------
# # Piksellerle resim olusturma (getpixel() ve putpixel() Kullanimi) 

# from PiL import image
# im = image.new('RGBA', (100, 100))
# im.getpixel((0, 0))
# 
# for x in range(100):
#     for y in range(50):
#         im.putpixel((x, y), (210, 210, 210))
#         
# from PiL import imageColor
# for x in range(100):
#     for y in range(50, 100):
#         im.putpixel((x, y), imageColor.getcolor('darkgray', 'RGBA'))
# im.getpixel((0, 0))
# im.getpixel((0, 50))
# im.save('putPixel.png')

#----------------------------------------------------------------------------------------
# #Resime logo ekleme
# import os
# from PiL import image
# 
# SQUARE_FiT_SiZE = 300
# LOGO_FiLENAME = 'logo.png'
# 
# logoim = image.open(LOGO_FiLENAME)
# logoWidth, logoHeight = logoim.size
# print(logoWidth)
# print(logoHeight)
# os.makedirs('withLogo', exist_ok=True)   #exist_ok=True bu dosya zaten var diye hata vermesini onler
# 
# # Loop over all files in the working directory. 
# #Eger calisma alaninda jpg,png veya senin tanimladigin isimde logo yoksa acmaz varsa im degiskenine atar
# 
# for filename in os.listdir('.'):
# #     if not (filename.endswith('.png') or filename.endswith('.jpg')) \
# #         or filename == LOGO_FiLENAME:   
#     if not (filename.endswith('.png') or filename.endswith('.jpg') or filename == LOGO_FiLENAME):
#         continue # skip non-image files and the logo file itself
# 
#     im = image.open(filename)
#     width, height = im.size
# 
# # Check if image needs to be resized.
# #Logo ekleyecegimiz resimin boyutunu 300x300 yapiyoruz
#     if width > SQUARE_FiT_SiZE and height > SQUARE_FiT_SiZE:
#         # Calculate the new width and height to resize to.
#         if width > height:
#             height = int((SQUARE_FiT_SiZE / width) * height)
#             width = SQUARE_FiT_SiZE
#         else:
#             width = int((SQUARE_FiT_SiZE / height) * width)
#             height = SQUARE_FiT_SiZE
#             
#         # Resize the image.
#         print('Resizing %s...' % (filename))
#         im = im.resize((width, height))
#         
#         # Resize the LOGo. LOGO nun boyutunu degistirdik
#         logoim=logoim.resize((75,100))
#         logoWidth, logoHeight = logoim.size
#         
#         print('Adding logo to %s...' % (filename))
#         im.paste(logoim, (width - logoWidth, height - logoHeight), logoim)
# 
#         # Save changes.
#         im.save(os.path.join('withLogo', filename))

#----------------------------------------------------------------------------------------
# #Geometrik sekillerle resim olusturma Draw function
# from PiL import image, imageDraw
# im = image.new('RGBA', (200, 200), 'white')
# draw = imageDraw.Draw(im)
# 
# #koordinat sisteminde dusun her parantez iki boyutu ifade eder (x,y)
# draw.line([(0, 0), (199, 0), (199, 199), (0, 199), (0, 0)], fill='black') #siyah cerceve
# 
# draw.rectangle((20, 30, 60, 60), fill='blue')
# 
# draw.ellipse((120, 30, 160, 60), fill='red')
# 
# draw.polygon(((57, 87), (79, 62), (94, 85), (120, 90), (103, 113)),fill='brown')
# 
# #For dongusu ile cizilmis bir yesil cizgi deseni
# for i in range(100, 200, 10):
#     draw.line([(i, 0), (200, i - 100)], fill='green')
# 
# im.save('drawing.png')

#----------------------------------------------------------------------------------------
# # text png olusturma. Yazi yazarak resim dosyasi olusturma
# from PiL import image, imageDraw, imageFont
# import os
# 
# im = image.new('RGBA', (200, 200), 'white')
# draw = imageDraw.Draw(im)
# 
# draw.text((20, 150), 'Hello', fill='purple')
# 
# fontsFolder = 'FONT_FOLDER' # e.g. 'Library/Fonts'
# arialFont = imageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 32)  #yazi fontu ve yazi boyutu belirleme
# 
# draw.text((100, 150), 'Howdy', fill='gray', font=arialFont)
# im.save('text.png')

#----------------------------------------------------------------------------------------





















    