# -*- coding: utf-8 -*-
'''
Created on 7 Oca 2017

@author: Purgoufr
'''

# ---Provider---                   ---SMTP server domain name---
#                                     Genel SMTP portu=587
# Gmail                               smtp.gmail.com
# 
# Outlook.com/Hotmail.com             smtp-mail.outlook.com
# 
# Yahoo Mail                          smtp.mail.yahoo.com
# 
# AT&T                                smpt.mail.att.net (port 465)
# 
# Comcast                             smtp.comcast.net
# 
# Verizon                             smtp.verizon.net (port 465)

#----------------------------------------------------------------------------------------
## Mail gönderme
# import smtplib
# smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
# smtpObj.ehlo()
# smtpObj.starttls()
# smtpObj.login(' your_mail@gmail.com ', ' Password ')
# smtpObj.sendmail(' your_mail@gmail.com ', ' receiver_mail@example.com ', 'Subject: So long.\nDear Alice, so long and thanks for all the fish. Sincerely, Bob')
# smtpObj.quit()

#----------------------------------------------------------------------------------------
# 
# #Ornek program
# #Uye ucretleri hatirlatici E-postasi Gondermek
# import openpyxl, smtplib
#  
# # Open the spreadsheet and get the latest dues status.
# wb = openpyxl.load_workbook('Email_send.xlsx')
# sheet = wb.get_sheet_by_name('Sheet1')
#  
# lastCol = sheet.get_highest_column()
# latestMonth = sheet.cell(row=1, column=lastCol).value
#  
# # Check each member's payment status.
# unpaidMembers = {}
# for r in range(2, sheet.get_highest_row() + 1):
#     payment = sheet.cell(row=r, column=lastCol).value
#     if payment != 'paid':
#         name = sheet.cell(row=r, column=1).value
#         email = sheet.cell(row=r, column=2).value
#         unpaidMembers[name] = email
#          
# # Log in to email account.
# smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
# smtpObj.ehlo()
# smtpObj.starttls()
# #smtpObj.login(' ugurkebir@gmail.com ', sys.argv[1])
#  
#      
# smtpObj.login(' purgoufr@gmail.com ', ' mehmet123 ')
#  
# # Send out reminder emails.
# for name, email in unpaidMembers.items():
#     body = "Subject: %s dues unpaid.\nDear %s,\nRecords show that you have not paid dues for %s. Please make this payment as soon as possible. Thank you!'" %  (latestMonth, name, latestMonth)
#     print('Sending email to %s...' % email)
#     sendmailStatus = smtpObj.sendmail('purgoufr@gmail.com', email, body)
#      
#     if sendmailStatus != {}:
#         print('There was a problem sending email to %s: %s' % (email,sendmailStatus))
# smtpObj.quit()

#----------------------------------------------------------------------------------------


