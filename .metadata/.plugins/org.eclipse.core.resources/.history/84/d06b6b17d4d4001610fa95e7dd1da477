# -*- coding: utf-8 -*-
'''
Created on 29 Ara 2016

@author: Purgoufr
'''

# #PDF dosyasının toplam sayfa sayısı
# import PyPDF2
# pdfFileObj = open('meetingminutes.pdf', 'rb')
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# print(pdfReader.numPages)
# 
# #sayfa içeriğini getirme
# pageObj = pdfReader.getPage(1)
# print(pageObj.extractText())

#----------------------------------------------------------------------------------------
# #PDF şifreli mi değil mi?
# import PyPDF2
# pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
# print(pdfReader.isEncrypted)
# 
# #PDF şifresini yaz
# print(pdfReader.decrypt('rosebud'))
# #numarası yazılan sayfayı getir
# pageObj = pdfReader.getPage(0)
# print(pageObj.extractText())

#----------------------------------------------------------------------------------------
# #PDF oluşturma-birden çok pdf i açıp içindekileri kopyalayıp yeni pdf oluşturabiliriz.
# #Burada iki tane pdf dosyası açtık ve ikisini yeni oluşturduğumuz tek bir PDF de birleştirdik
# 
# import PyPDF2
# pdf1File = open('meetingminutes.pdf', 'rb')
# pdf2File = open('meetingminutes2.pdf', 'rb')
# pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
# pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
# pdfWriter = PyPDF2.PdfFileWriter()
# 
# for pageNum in range(pdf1Reader.numPages):
#     pageObj = pdf1Reader.getPage(pageNum)
#     pdfWriter.addPage(pageObj)
# 
# for pageNum in range(pdf2Reader.numPages):
#     pageObj = pdf2Reader.getPage(pageNum)
#     pdfWriter.addPage(pageObj)
# 
# pdfOutputFile = open('combinedminutes.pdf', 'wb')
# pdfWriter.write(pdfOutputFile)
# pdfOutputFile.close()
# pdf1File.close()
# pdf2File.close()

#----------------------------------------------------------------------------------------
# #PDF sayfa yönü değiştirme(rotate)
# import PyPDF2
# minutesFile = open('meetingminutes.pdf', 'rb')
# pdfReader = PyPDF2.PdfFileReader(minutesFile)
# page = pdfReader.getPage(0)
# page.rotateClockwise(90)
# 
# pdfWriter = PyPDF2.PdfFileWriter()
# pdfWriter.addPage(page)
# resultPdfFile = open('rotatedPage.pdf', 'wb')
# pdfWriter.write(resultPdfFile)
# resultPdfFile.close()
# minutesFile.close()

#----------------------------------------------------------------------------------------
# #PDF e resim ikon ekleme(PDF e PDF ekleme)
# import PyPDF2
# minutesFile = open('meetingminutes.pdf', 'rb')
# pdfReader = PyPDF2.PdfFileReader(minutesFile)
# minutesFirstPage = pdfReader.getPage(0)
# pdfWatermarkReader = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))
# minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))
# pdfWriter = PyPDF2.PdfFileWriter()
# pdfWriter.addPage(minutesFirstPage)
# 
# for pageNum in range(1, pdfReader.numPages):
#     pageObj = pdfReader.getPage(pageNum)
#     pdfWriter.addPage(pageObj)
# resultPdfFile = open('watermarkedCover.pdf', 'wb')
# pdfWriter.write(resultPdfFile)
# minutesFile.close()
# resultPdfFile.close()

#----------------------------------------------------------------------------------------
# #PDF şifreleme(encrypt)
# import PyPDF2
# pdfFile = open('meetingminutes.pdf', 'rb')
# pdfReader = PyPDF2.PdfFileReader(pdfFile)
# pdfWriter = PyPDF2.PdfFileWriter()
# for pageNum in range(pdfReader.numPages):
#     pdfWriter.addPage(pdfReader.getPage(pageNum))
# 
# pdfWriter.encrypt('ugur')
# resultPdf = open('encryptedminutes.pdf', 'wb')
# pdfWriter.write(resultPdf)
# resultPdf.close()

#----------------------------------------------------------------------------------------
# #Geçerli çalışma dizinindeki tüm PDF'leri birleştirme
# import PyPDF2, os
# pdfFiles = []
# for filename in os.listdir('.'):
#     if filename.endswith('.pdf'):
#         pdfFiles.append(filename)
#             
# pdfFiles.sort(key=str.lower)                #Alfabetik sıralama
# pdfWriter = PyPDF2.PdfFileWriter()
# 
# #Loop through all the PDF files.
# for filename in pdfFiles:
#     pdfFileObj = open(filename, 'rb')
#     pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#     
# # Loop through all the pages (except the first) and add them.   
# for pageNum in range(1, pdfReader.numPages):
#     pageObj = pdfReader.getPage(pageNum)
#     pdfWriter.addPage(pageObj)
# 
# # Save the resulting PDF to a file.
# pdfOutput = open('allminutes.pdf', 'wb')
# pdfWriter.write(pdfOutput)
# pdfOutput.close()

#----------------------------------------------------------------------------------------



















