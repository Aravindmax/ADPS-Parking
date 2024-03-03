#Pathilib to find file path
import pathlib

#For working with excel files :
import pandas as pd
from openpyxl import Workbook



def creating_excel():
    
    user_file=pathlib.Path('user_log.xlsx')

    if user_file.exists():
            pass
    else :
            user_file=Workbook()
            sheet=user_file.active
            headers = ['DATE', 'ENTRY TIME', 'SLOT NO', 'MOBILE NO', 'VEHICLE NO', 'OTP SENT','EXIT TIME']
            sheet.append(headers)

            user_file.save('user_log.xlsx')


    parking_file=pathlib.Path('parking_details.xlsx')

    if parking_file.exists():
            pass
    else :
            print('PARKING EXCEL FILE NOT FOUND...PLEASE CREATE A EXCEL FILE LIKE MENTIONED IN THE \'Readme.txt\' ON THE INSTALLED LOCATION.')
            parking_file=Workbook()
            sheet=parking_file.active
            headers = ['SLOT NO', 'STATUS', 'LOCATION', 'OTP', 'VEHICLE NO']
            sheet.append(headers)

            parking_file.save('parking_details.xlsx')