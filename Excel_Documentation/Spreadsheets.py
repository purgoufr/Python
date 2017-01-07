# -*- coding: utf-8 -*-
'''
Created on 26 Ara 2016

@author: Purgoufr
'''
# #Excel dosyasi acma
# import openpyxl, os
# print(os.getcwd())
# wb = openpyxl.load_workbook('ugur_test_excel.xlsx')
# print(type(wb))
# 
# #excel sayfalari(sheets) getirme
# print(wb.get_sheet_names())
# 
# #excel gecerli sayfayi secme
# sheet = wb.get_sheet_by_name('Sheet3')
# print(sheet)
# 
# #gecerli sayfanin adini getirme
# print(sheet.title)
# 
# #aktif olan sayfayi getir
# anotherSheet = wb.active
# print(anotherSheet)

#----------------------------------------------------------------------------------------
# #excel de hucre(cell) degerlerini ayri ayri getirme
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
# #satir ve sutun getirme
# print(sheet.cell(row=1, column=2))
# print(sheet.cell(row=1, column=2).value)
# 
# for i in range(1, 8, 2):
#         print(i, sheet.cell(row=i, column=2).value)

#----------------------------------------------------------------------------------------

# #maksimum kolon sayisi ve maksimum sutun sayisi
# import openpyxl
# wb = openpyxl.load_workbook('ugur_test_excel.xlsx')
# sheet = wb.get_sheet_by_name('Sheet1')
# print(sheet.max_row)
# print(sheet.max_column)

#----------------------------------------------------------------------------------------

# #sutun adlarini sayilara donusturme
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
# #satir ve sutun getirme ayrintili sekilde
# import openpyxl
# wb = openpyxl.load_workbook('ugur_test_excel.xlsx')
# sheet = wb.get_sheet_by_name('Sheet1')
# print(tuple(sheet['A1':'C3']))
# for rowOfCellObjects in sheet['A1':'C3']:
#     for cellObj in rowOfCellObjects:
#         print(cellObj.coordinate, cellObj.value)
#     print('--- END OF ROW ---')

#----------------------------------------------------------------------------------------
# #ornek program excel veri okuma(nufus sayimi ile ilgili tabloda(censuspopdata)
# #eyaletlerin ilcelerindeki sayim sayisi ve her sayimdaki nufuslarin toplami
# #Verileri Excel elektronik tablosundan okuma
# #Her ilcedeki nufus sayim yerlerinin sayisini sayma
# #Her ilcenin toplam nufusunu sayma
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
#     # increase the county pop by the pop in this census tract.
#     countyData[state][county]['pop'] += int(pop)
#     
# # Open a new text file and write the contents of countyData to it.
# print('Writing results...')
# resultFile = open('census2010.py', 'w')
# resultFile.write('allData = ' + pprint.pformat(countyData))
# resultFile.close()
# print('Done.')

# #bir onceki ornekte olusturulan tablodan veri alma
# import os
# os.chdir('C:\\Users\\Purgoufr\\Documents\\Eclipse Projects\\Python\\Excel_Documentation')
# import census2010
# census2010.allData['AK']['Anchorage']
# 
# anchoragePop = census2010.allData['AK']['Anchorage']['pop']
# print('The 2010 population of Anchorage was ' + str(anchoragePop))

#----------------------------------------------------------------------------------------
# #excel dosyasi olusturma
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
# #Yeni sheet(sayfa) olusturma
# wb.create_sheet()
# print(wb.get_sheet_names())
# 
# #Yeni olusturulan sheet in(sayfanin) adini degistirme(index=0 a olusturduk yani ilk sheet(sayfa))
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
# #cell e (hucreye) yazi yazma
# sheet = wb.get_sheet_by_name('Sheet')
# sheet['A1'] = 'Hello world!'
# print(sheet['A1'].value)

#----------------------------------------------------------------------------------------
# #Var olan exceli guncelleme
# import openpyxl
# 
# wb = openpyxl.load_workbook('update_example.xlsx')
# sheet = wb.get_sheet_by_name('Sheet1')
# 
# # The produce types and their updated prices
# PRiCE_UPDATES = {'Garlic': 3.07,
#                  'Celery': 1.19,
#                  'Lemon': 1.27}
# # TODO: Loop through the rows and update the prices.
# for rowNum in range(2, sheet.max_row):  # skip the first row
#     produceName = sheet.cell(row=rowNum, column=1).value
#     if produceName in PRiCE_UPDATES:
#         sheet.cell(row=rowNum, column=2).value = PRiCE_UPDATES[produceName]
# 
# wb.save('update_example.xlsx')

#----------------------------------------------------------------------------------------
# #excel dosya olusturma, yazi ekleme, yazi font degistirme
# import openpyxl
# 
# from openpyxl.styles import Font
# wb = openpyxl.Workbook()
# sheet = wb.get_sheet_by_name('Sheet')
# italic24Font = Font(size=24, italic=True)
# sheet['A1'].font = italic24Font
# sheet['A1'] = 'Hello world!'
# wb.save('styles.xlsx')

# #excel dosya olusturma, yazi ekleme, yazi font degistirme ornek 2
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
# sheet['B3'] = '24 pt italic'
#  
# wb.save('styles.xlsx')

#----------------------------------------------------------------------------------------
# #formul yazma
# import openpyxl
# wb = openpyxl.Workbook()
# sheet = wb.active
# sheet['C1'] = 200
# sheet['C2'] = 300
# sheet['C3'] = '=SUM(A1:A2)'
# wb.save('styles.xlsx')

#----------------------------------------------------------------------------------------
# #excel hucreleri boyutlandirma
# import openpyxl
# wb = openpyxl.Workbook()
# sheet = wb.active
# sheet['A1'] = 'Tall row'
# sheet['B2'] = 'Wide column'
# sheet.row_dimensions[1].height = 70
# sheet.column_dimensions['B'].width = 20
# wb.save('styles.xlsx')

#----------------------------------------------------------------------------------------
# #hucreleri birlestirme 
# import openpyxl
# wb = openpyxl.Workbook()
# sheet = wb.active
# sheet.merge_cells('A1:D3')
# sheet['A1'] = 'Twelve cells merged together.'
# sheet.merge_cells('C5:D5')
# sheet['C5'] = 'Two merged cells.'
# wb.save('styles.xlsx')

# #hucreleri ayirma
# import openpyxl
# wb = openpyxl.load_workbook('styles.xlsx')
# sheet = wb.active
# sheet.unmerge_cells('A1:D3')
# sheet.unmerge_cells('C5:D5')
# wb.save('styles.xlsx')

#----------------------------------------------------------------------------------------
# #Satir ve sutun ust bilgileri dondurma ya da sabitleme
# import openpyxl
# wb = openpyxl.load_workbook('update_example.xlsx')
# sheet = wb.active
# sheet.freeze_panes = 'A2'
# wb.save('freezeExample.xlsx')

#----------------------------------------------------------------------------------------
# #grafik (chart) olusturma hata veriyor ama calistiriyor
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















