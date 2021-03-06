# -*- coding: utf-8 -*-
'''
Created on 2 Oca 2017

@author: Purgoufr
'''
#NOT: PYTHON 3 KULLAN!!!!!!!!!
#CSV File ozellikleri
# CSV files are simple, lacking many of the features of an Excel spreadsheet. For example, CSV files
# 
# Don’t have types for their values—everything is a string
# 
# Don’t have settings for font size or color
# 
# Don’t have multiple worksheets
# 
# Can’t specify cell widths and heights
# 
# Can’t have merged cells
# 
# Can’t have images or charts embedded in them

#----------------------------------------------------------------------------------------
# #CSV dosyasi acma , CSV data cekme(tablodan data cekme)
# import csv
# exampleFile = open('example.csv')
# exampleReader = csv.reader(exampleFile)
# exampleData = list(exampleReader)
# print(exampleData)
# print(exampleData[0][0])

#----------------------------------------------------------------------------------------
# #CSV dosyasini duzenli bir sekilde getirme(for loop kullanarak)
# import csv
# exampleFile = open('example.csv')
# exampleReader = csv.reader(exampleFile)
# for row in exampleReader:
#     print('Row #' + str(exampleReader.line_num) + ' ' + str(row))

#----------------------------------------------------------------------------------------
# import csv
# outputFile = open('output.csv', 'w', newline='')
# outputWriter = csv.writer(outputFile)
# 
# outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
# outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
# outputWriter.writerow([1, 2, 3.141592, 4])
# outputFile.close()

#----------------------------------------------------------------------------------------
# #Hucreleri virgul(comma) yerine sekme(tab) karakteriyle ayirmak  ve satirlarin cift araliklarla olmasi
# import csv
# csvFile = open('example.tsv', 'w', newline='')
# csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')
# csvWriter.writerow(['apples', 'oranges', 'grapes'])
# csvWriter.writerow(['eggs', 'bacon', 'ham'])
# csvWriter.writerow(['spam', 'spam', 'spam', 'spam', 'spam', 'spam'])
# csvFile.close()

#----------------------------------------------------------------------------------------
# #birden fazla CSV dosyasinin ilk satirini silme
# import csv, os
# os.makedirs('headerRemoved', exist_ok=True)
# # Loop through every file in the current working directory.
# for csvFilename in os.listdir('.'):
#     if not csvFilename.endswith('.csv'):
#         continue    # skip non-csv files
#     print('Removing header from ' + csvFilename + '...')
# 
# # Read the CSV file in (skipping first row).
# csvRows = []
# csvFileObj = open(csvFilename)
# readerObj = csv.reader(csvFileObj)
# for row in readerObj:
#     if readerObj.line_num == 1:
#         continue    # skip first row
#     csvRows.append(row)
# csvFileObj.close()
# 
# for csvFilename in os.listdir('.'):
#     if not csvFilename.endswith('.csv'):
#         continue    # skip non-CSV files
# 
#     # Write out the CSV file.
#     csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w', newline='')
#     csvWriter = csv.writer(csvFileObj)
#     for row in csvRows:
#         csvWriter.writerow(row)
#     csvFileObj.close()

#----------------------------------------------------------------------------------------
#                            JSON 
#----------------------------------------------------------------------------------------
# #JSON verilerini iceren bir dizgeyi bir Python degerine cevirmek icin onu json.loads() fonksiyonu kullandik
# #string i JSON a cevirme 
# stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineiQ": null}'
# import json
# jsonDataAsPythonValue = json.loads(stringOfJsonData)
# print(jsonDataAsPythonValue)

#----------------------------------------------------------------------------------------
# #Python value yu JSON a cevirme
# pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie','felineiQ': None}
# import json
# stringOfJsonData = json.dumps(pythonValue)
# print(stringOfJsonData)

#----------------------------------------------------------------------------------------
# #Siteden hava durumu verisi cekme
# 
# # Overall, the program does the following:
# # 
# # Reads the requested location from the command line.
# # Downloads JSON weather data from OpenWeatherMap.org.
# # Converts the string of JSON data to a Python data structure.
# # Prints the weather for today and the next two days.
# 
# # So the code will need to do the following:
# # 
# # Join strings in sys.argv to get the location.
# # Call requests.get() to download the weather data.
# # Call json.loads() to convert the JSON data to a Python data structure.
# # Print the weather forecast.
# 
# import json, requests, sys, pprint
# 
# # Compute location from command line arguments.
# if len(sys.argv) < 2:
#     print('Usage: csv_json_basic_codes.py location')
#     sys.exit()
# location = ' '.join(sys.argv[1:])
# 
# # Download the JSON data from OpenWeatherMap.org's APi.
# url ='http://api.openweathermap.org/data/2.5/weather?q=%s&appid=71c5acc8b7a96eece3a86c883bc423c1' % (location)
# response = requests.get(url)
# response.raise_for_status()
# 
# # Load JSON data into a Python variable.
# weatherData = json.loads(response.text)
# pp = pprint.PrettyPrinter(indent=0)
# 
# pp.pprint(weatherData['main']['temp']-273.15 )
# pp.pprint(weatherData['main']['humidity'])

