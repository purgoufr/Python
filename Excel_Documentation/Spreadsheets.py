# -*- coding: utf-8 -*-
'''
Created on 26 Ara 2016

@author: Purgoufr
'''
# #Excel dosyası açma
# import openpyxl, os
# print(os.getcwd())
# wb = openpyxl.load_workbook('ugur_test_excel.xlsx')
# print(type(wb))
# 
# #excel sayfaları(sheets) getirme
# print(wb.get_sheet_names())
# 
# #excel geçerli sayfayı seçme
# sheet = wb.get_sheet_by_name('Sheet3')
# print(sheet)
# 
# #geçerli sayfanın adını getirme
# print(sheet.title)
# 
# #aktif olan sayfayı getir
# anotherSheet = wb.active
# print(anotherSheet)

#----------------------------------------------------------------------------------------
# #excel de hücre(cell) değerlerini ayrı ayrı getirme
# import openpyxl
# wb = openpyxl.load_workbook('ugur_test_excel.xlsx')
# sheet = wb.get_sheet_by_name('Sheet1')
# print(sheet['A1'])
# print(sheet['A1'].value)
# 
# c = sheet['B1']
# print(c.value)
# 
# print('Row ' + str(c.row) + ', Column ' + c.column + ' is ' + c.value)
# print('Cell ' + c.coordinate + ' is ' + c.value)
# print(sheet['C1'].value)
# 
# #satır ve sütun getirme
# print(sheet.cell(row=1, column=2))
# print(sheet.cell(row=1, column=2).value)
# 
# for i in range(1, 8, 2):
#         print(i, sheet.cell(row=i, column=2).value)

#----------------------------------------------------------------------------------------

# #maksimum kolon sayısı ve maksimum sutün sayısı
# import openpyxl
# wb = openpyxl.load_workbook('ugur_test_excel.xlsx')
# sheet = wb.get_sheet_by_name('Sheet1')
# print(sheet.max_row)
# print(sheet.max_column)

#----------------------------------------------------------------------------------------

# #sütun adlarını sayılara dönüştürme
# import openpyxl
# from openpyxl.utils import get_column_letter,  column_index_from_string
# print(get_column_letter(1))
# 
# print(get_column_letter(2))
# 
# print(get_column_letter(27))
# 
# print(get_column_letter(900))
# 
# wb = openpyxl.load_workbook('ugur_test_excel.xlsx')
# sheet = wb.get_sheet_by_name('Sheet1')
# print(get_column_letter(sheet.max_column))
# 
# print(column_index_from_string('A'))
# 
# print(column_index_from_string('AA'))

#----------------------------------------------------------------------------------------
# #satır ve sütün getirme ayrıntılı şekilde
# import openpyxl
# wb = openpyxl.load_workbook('ugur_test_excel.xlsx')
# sheet = wb.get_sheet_by_name('Sheet1')
# print(tuple(sheet['A1':'C3']))
# for rowOfCellObjects in sheet['A1':'C3']:
#     for cellObj in rowOfCellObjects:
#         print(cellObj.coordinate, cellObj.value)
#     print('--- END OF ROW ---')

#----------------------------------------------------------------------------------------
# #örnek program excel veri okuma(nufus sayımı ile ilgili tabloda(censuspopdata)
# #eyaletlerin ilçelerindeki sayım sayısı ve her sayımdaki nufusların toplamı
# #Verileri Excel elektronik tablosundan okuma
# #Her ilçedeki nüfus sayım yerlerinin sayısını sayma
# #Her ilçenin toplam nüfusunu sayma
# 
# import openpyxl, pprint
# print('Opening workbook...')
# wb = openpyxl.load_workbook('censuspopdata.xlsx')
# sheet = wb.get_sheet_by_name('Population by Census Tract')
# countyData = {}
# 
# # TODO: Fill in countyData with each county's population and tracts.
# print('Reading rows...')
# 
# for row in range(2, sheet.max_row + 1):
#     # Each row in the spreadsheet has data for one census tract.
#     state  = sheet['B' + str(row)].value
#     county = sheet['C' + str(row)].value
#     pop    = sheet['D' + str(row)].value
#     
#     # Make sure the key for this state exists.
#     countyData.setdefault(state, {})
#     
#     # Make sure the key for this county in this state exists.
#     countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})
#     
#     # Each row represents one census tract, so increment by one.
#     countyData[state][county]['tracts'] += 1
#     
#     # Increase the county pop by the pop in this census tract.
#     countyData[state][county]['pop'] += int(pop)
#     
# # Open a new text file and write the contents of countyData to it.
# print('Writing results...')
# resultFile = open('census2010.py', 'w')
# resultFile.write('allData = ' + pprint.pformat(countyData))
# resultFile.close()
# print('Done.')

# #bir önceki örnekte oluşturulan tablodan veri alma
# import os
# os.chdir('C:\\Users\\Purgoufr\\Documents\\Eclipse Projects\\Python\\Excel_Documentation')
# import census2010
# census2010.allData['AK']['Anchorage']
# 
# anchoragePop = census2010.allData['AK']['Anchorage']['pop']
# print('The 2010 population of Anchorage was ' + str(anchoragePop))

#----------------------------------------------------------------------------------------
# #excel dosyası oluşturma
# import openpyxl
# wb = openpyxl.Workbook()
# print(wb.get_sheet_names())
# 
# sheet = wb.active
# print(sheet.title)
# 
# sheet.title = 'Ugur Test Sheet'
# print(wb.get_sheet_names())
# 
# #Yeni sheet(sayfa) oluşturma
# wb.create_sheet()
# print(wb.get_sheet_names())
# 
# #Yeni oluşturulan sheet in(sayfanın) adını değiştirme(index=0 a oluşturduk yani ilk sheet(sayfa))
# wb.create_sheet(index=0, title='First Sheet')
# print(wb.get_sheet_names())
# 
# wb.create_sheet(index=2, title='Middle Sheet')
# print(wb.get_sheet_names())
# 
# #sheet(sayfa) silme    
# wb.remove_sheet(wb.get_sheet_by_name('Middle Sheet'))
# print(wb.get_sheet_names())
# 
# #cell e (hücreye) yazı yazma
# sheet = wb.get_sheet_by_name('Sheet')
# sheet['A1'] = 'Hello world!'
# print(sheet['A1'].value)

#----------------------------------------------------------------------------------------
# #Var olan exceli güncelleme
# import openpyxl
# 
# wb = openpyxl.load_workbook('update_example.xlsx')
# sheet = wb.get_sheet_by_name('Sheet1')
# 
# # The produce types and their updated prices
# PRICE_UPDATES = {'Garlic': 3.07,
#                  'Celery': 1.19,
#                  'Lemon': 1.27}
# # TODO: Loop through the rows and update the prices.
# for rowNum in range(2, sheet.max_row):  # skip the first row
#     produceName = sheet.cell(row=rowNum, column=1).value
#     if produceName in PRICE_UPDATES:
#         sheet.cell(row=rowNum, column=2).value = PRICE_UPDATES[produceName]
# 
# wb.save('update_example.xlsx')

#----------------------------------------------------------------------------------------
# #excel dosya oluşturma, yazı ekleme, yazı font değiştirme
# import openpyxl
# 
# from openpyxl.styles import Font
# wb = openpyxl.Workbook()
# sheet = wb.get_sheet_by_name('Sheet')
# italic24Font = Font(size=24, italic=True)
# sheet['A1'].font = italic24Font
# sheet['A1'] = 'Hello world!'
# wb.save('styles.xlsx')

# #excel dosya oluşturma, yazı ekleme, yazı font değiştirme örnek 2
# import openpyxl
# from openpyxl.styles import Font
# wb = openpyxl.Workbook()
# sheet = wb.get_sheet_by_name('Sheet')
#  
# fontObj1 = Font(name='Times New Roman', bold=True)
# sheet['A1'].font = fontObj1
# sheet['A1'] = 'Bold Times New Roman'
#  
# fontObj2 = Font(size=24, italic=True)
# sheet['B3'].font = fontObj2
# sheet['B3'] = '24 pt Italic'
#  
# wb.save('styles.xlsx')

#----------------------------------------------------------------------------------------
# #formül yazma
# import openpyxl
# wb = openpyxl.Workbook()
# sheet = wb.active
# sheet['C1'] = 200
# sheet['C2'] = 300
# sheet['C3'] = '=SUM(A1:A2)'
# wb.save('styles.xlsx')

#----------------------------------------------------------------------------------------
# #excel hücreleri boyutlandırma
# import openpyxl
# wb = openpyxl.Workbook()
# sheet = wb.active
# sheet['A1'] = 'Tall row'
# sheet['B2'] = 'Wide column'
# sheet.row_dimensions[1].height = 70
# sheet.column_dimensions['B'].width = 20
# wb.save('styles.xlsx')

#----------------------------------------------------------------------------------------
# #hücreleri birleştirme 
# import openpyxl
# wb = openpyxl.Workbook()
# sheet = wb.active
# sheet.merge_cells('A1:D3')
# sheet['A1'] = 'Twelve cells merged together.'
# sheet.merge_cells('C5:D5')
# sheet['C5'] = 'Two merged cells.'
# wb.save('styles.xlsx')

# #hücreleri ayırma
# import openpyxl
# wb = openpyxl.load_workbook('styles.xlsx')
# sheet = wb.active
# sheet.unmerge_cells('A1:D3')
# sheet.unmerge_cells('C5:D5')
# wb.save('styles.xlsx')

#----------------------------------------------------------------------------------------
# #Satır ve sutun üst bilgileri dondurma ya da sabitleme
# import openpyxl
# wb = openpyxl.load_workbook('update_example.xlsx')
# sheet = wb.active
# sheet.freeze_panes = 'A2'
# wb.save('freezeExample.xlsx')

#----------------------------------------------------------------------------------------
# #grafik (chart) oluşturma hata veriyor ama çalıştırıyor
# import openpyxl
# 
# wb = openpyxl.Workbook()
# sheet = wb.active
# for i in range(1, 11):         # create some data in column A
#     sheet['A' + str(i)] = i
# 
# refObj = openpyxl.chart.Reference(sheet, min_col=1, min_row=1, max_col=1, max_row=10)
# 
# seriesObj = openpyxl.chart.Series(refObj, title='First series')
# 
# chartObj = openpyxl.chart.BarChart()
# chartObj.title = 'My Chart'
# chartObj.append(seriesObj)
# sheet.add_chart(chartObj, 'C5')
# wb.save('sampleChart.xlsx')

#----------------------------------------------------------------------------------------














