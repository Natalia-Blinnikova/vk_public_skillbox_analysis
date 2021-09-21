
#coding:utf8
import requests 
import json 
import os
import os.path
import openpyxl
import time
from datetime import datetime
os.chdir("C:/Users/...") 
wfile = open('databaseVK.csv', 'w', encoding='utf8')    
wfile.write("date;text;comments;likes;reposts;views;attach_count;attach_types")

TOKEN='78fd4...' #токен скрыт
V = '5.131'
n = 0

for offsetik in list(range(0, 2100, 100)): #офсет позволяет смещать начало выборки записей и начинать не с нулевой, а на 100 записей старее

    params ={'owner_id': '-66669811', 'offset' : offsetik, 'count' : 100, 'owners_only' : 1, 'access_token' : TOKEN, 'v' : V} 
    response = requests.get('https://api.vk.com/method/wall.get', params)

    rjson = response.json()
    items1 = rjson['response']['items']
    #print(items1)

    for dictionary in items1:
        lstToCSV = []
        listKeys = ["['date']", "['text']", "['comments']['count']", "['likes']['count']", "['reposts']['count']", "['views']['count']"]
        for key in listKeys: 
            try:
                var = eval(str(dictionary) + key)
                lstToCSV.append(var) #и создаю список, в котором все значения для одной вакансии для 1ой строки в эксель. 
            except BaseException: 
                lstToCSV.append(None)
        text = lstToCSV[1]
        characters = ['\n', ';'] #эти символы удалить, чтобы они не засчитывались как перенос строки или сдвиг на колонку
        for char in characters:
            text = text.replace(char, '')

        lstToCSV[1] = text

        timestamp = lstToCSV[0]
        date_time = datetime.fromtimestamp(timestamp)

        lstToCSV[0] = date_time
        try: 
            attaches = dictionary['attachments'] #а тут еще у поста есть приложения. Их может быть несколько - каждое приложение - это отдельный список
            lstToCSV.append(len(attaches))       #Поэтому можно посчитать, а сколько этих приложений
            list_types = []
            for an_attach in attaches:           #и затем для каждого приложения посмотреть тип. Их записать в список, и если там много значений, собрать их в строку
                typic = an_attach['type']
                if typic not in list_types: 
                    list_types.append(typic)
            string_types = ''
            for attach_type in list_types: 
                string_types += str(attach_type)

            lstToCSV.append(string_types)        #и затем аппенднуть это к списку, который записывается в строчку csv

        except BaseException:
            lstToCSV.append(0)
            lstToCSV.append('NoAttach')     

        #print(lstToCSV)

        wfile.write('\n')
        wfile.write('{};{};{};{};{};{};{};{}'.format(*lstToCSV))  
        
    time.sleep(10)
wfile.close()

