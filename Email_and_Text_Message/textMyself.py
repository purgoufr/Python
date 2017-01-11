'''
Created on 9 Oca 2017

@author: Purgoufr
'''
# #Ornek Program Twilio dan text mesaj atma icin 111-112. satiri uncomment yap
accountSID = 'AC7633c26c2c4ce5259c0dbfa0a8a12237'
authToken = '5109d299a835edb2b15d75c3075b9d34'
twilioNumber = '+16782563571'
myNumber = '+905398289835'

from twilio.rest import TwilioRestClient


def textmyself(message):
    twilioCli = TwilioRestClient(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)

