import json
import urllib.request, urllib.parse, urllib.error
import xlsxwriter
import os.path

url = "https://api.covid19india.org/data.json"
url2 = "https://api.covid19india.org/v2/state_district_wise.json"
url3 = "https://api.covid19india.org/zones.json"
uh = urllib.request.urlopen(url)
data = uh.read().decode()
uh2 = urllib.request.urlopen(url2)
data2 = uh2.read().decode()
uh3 = urllib.request.urlopen(url3)
data3 = uh3.read().decode()
js3 = json.loads(data3)
print("Data Retrived")
js = json.loads(data)
js2 = json.loads(data2)
tdate = js["cases_time_series"]
state_data = js["statewise"]
tested_data = js["tested"]

row_worksheet1,col_worksheet1,row_worksheet2,col_worksheet2,row_worksheet3,col_worksheet3,row_worksheet4,col_worksheet4 = 1,0,1,0,1,0,1,0

def createdatabase():
    workbook = xlsxwriter.Workbook('Corona_DataBase.xlsx')
    worksheet1 = workbook.add_worksheet('Case Time Series')
    worksheet2 = workbook.add_worksheet('State Wise Cases')
    worksheet3 = workbook.add_worksheet('Tests')
    worksheet4 = workbook.add_worksheet('District Wise')
    bold = workbook.add_format({'bold': True})
    Red = workbook.add_format({'bg_color': '#FFC7CE'})
    Orange = workbook.add_format({'bg_color': '#FFEB9C'})
    Green = workbook.add_format({ 'bg_color': '#C6EFCE'})
    num_type = workbook.add_format({'num_format': '0'})

    worksheet1.write('A1', 'Date', bold)
    worksheet1.write('B1', 'Daily Confirmed', bold)
    worksheet1.write('C1', 'Dail Deceaced', bold)
    worksheet1.write('D1', 'Daily Recovered', bold)
    worksheet1.write('E1', 'Total Confirmed', bold)
    worksheet1.write('F1', 'Total Deceased', bold)
    worksheet1.write('G1', 'Total Recovered', bold)
    worksheet1.set_column('A:A', 15)
    worksheet1.set_column('B:G', 18)

    worksheet2.write('A1', 'Last Updated Time', bold)
    worksheet2.write('B1', 'State', bold)
    worksheet2.write('C1', 'State Code', bold)
    worksheet2.write('D1', 'Active', bold)
    worksheet2.write('E1', 'Confirmed', bold)
    worksheet2.write('F1', 'Deceaced', bold)
    worksheet2.write('G1', 'Recovered', bold)
    worksheet2.write('H1', 'Delta Confirmed', bold)
    worksheet2.write('I1', 'Delta Deceased', bold)
    worksheet2.write('J1', 'Delta Recovered', bold)
    worksheet2.set_column('A:A', 25)
    worksheet2.set_column('B:J', 18)

    worksheet3.write('A1', 'Update Time Stamp', bold)
    worksheet3.write('B1', 'Individuals tested per confirmed cases', bold)
    worksheet3.write('C1', 'Positive cases from samples reported', bold)
    worksheet3.write('D1', 'Sample reported today', bold)
    worksheet3.write('E1', 'Test positivity rate', bold)
    worksheet3.write('F1', 'Test conducted by private labs', bold)
    worksheet3.write('G1', 'Tests per Confirmed cases', bold)
    worksheet3.write('H1', 'Total individuals tested', bold)
    worksheet3.write('I1', 'Total positive cases', bold)
    worksheet3.write('J1', 'Total sample tested', bold)
    worksheet3.set_column('A:J', 30)
            
    worksheet4.write('A1','State',bold)
    worksheet4.write('B1','District',bold)
    worksheet4.write('C1','Confirmed',bold)
    worksheet4.write('D1','Active',bold)
    worksheet4.write('E1','Recovered',bold)
    worksheet4.write('F1','Deceased',bold)
    worksheet4.set_column('A:F',30)

    global row_worksheet1,col_worksheet1,row_worksheet2,col_worksheet2,row_worksheet3,col_worksheet3,row_worksheet4,col_worksheet4    

    std = ["lastupdatedtime","state","statecode","active","confirmed","deaths","recovered","deltaconfirmed","deltadeaths","deltarecovered"]
    for i in range(len(state_data)):
        for k in range(10):
            worksheet2.write(row_worksheet2, col_worksheet2 + k, js["statewise"][i][std[k]])
        row_worksheet2 = row_worksheet2 + 1
        col_worksheet2 = 0
    dist = []
    distdata = ["district","confirmed","active","recovered","deceased"]
    zonesss = ["Red","Orange","Green"]
    for m in range(735):
        dist.append(js3["zones"][m]["district"])
    for i in range(36):
        state = js2[i]["state"]
        for j in range(len(js2[i]["districtData"])):
            for k in range(5):
                try:
                    y = dist.index(js2[i]["districtData"][j]["district"])
                    x = zonesss.index(js3["zones"][y]["zone"])
                    if x == 0:
                        worksheet4.write(row_worksheet4, col_worksheet4,state,Red)
                        worksheet4.write(row_worksheet4, col_worksheet4 + k +1,js2[i]["districtData"][j][distdata[k]],Red)
                    elif x == 1:
                        worksheet4.write(row_worksheet4, col_worksheet4,state,Orange)
                        worksheet4.write(row_worksheet4, col_worksheet4 + k +1,js2[i]["districtData"][j][distdata[k]],Orange)
                    elif x == 2:
                        worksheet4.write(row_worksheet4, col_worksheet4,state,Green)
                        worksheet4.write(row_worksheet4, col_worksheet4 + k +1,js2[i]["districtData"][j][distdata[k]],Green)
                except:
                    worksheet4.write(row_worksheet4, col_worksheet4,state)
                    worksheet4.write(row_worksheet4, col_worksheet4 + k +1,js2[i]["districtData"][j][distdata[k]],)
            row_worksheet4 = row_worksheet4 + 1

            
    cts = ["date","dailyconfirmed","dailydeceased","dailyrecovered","totalconfirmed","totaldeceased","totalrecovered"]
    for i in range(len(tdate)):
        for k in range(7):
            worksheet1.write(row_worksheet1, col_worksheet1 + k, js["cases_time_series"][i][cts[k]])
        row_worksheet1 = row_worksheet1 + 1
                
            
    test = ["updatetimestamp","individualstestedperconfirmedcase","positivecasesfromsamplesreported","samplereportedtoday",
            "testpositivityrate","testsconductedbyprivatelabs","testsperconfirmedcase","totalindividualstested","totalpositivecases","totalsamplestested"]
    for i in range(len(tested_data)):
        for k in range(10):
            worksheet3.write(row_worksheet3, col_worksheet3 + k, js["tested"][i][test[k]])
        row_worksheet3 = row_worksheet3 + 1

    workbook.close()
print("1.Total Cases")
print("2.Total Recovered")
print("3.Total Active Cases")
print("4.Total Dead")
print("5.Total Overview")
print("6.State Data")
print("7.New Cases in India")
print("8.Cases on date")
print("9.Create DataBase")
print("10.Exit")
while True:
    op = input("what you want to do >>")

    if op == "1":
        y = js["statewise"][0]["confirmed"]
        print("Total Cases >>", y)
    elif op == "2":
        m = js["statewise"][0]["recovered"]
        print("Total Recovered >>", m)
    elif op == "3":
        k = js["statewise"][0]["active"]
        print("Total Active >>", k)
    elif op == "4":
        l = js["statewise"][0]["deaths"]
        print("Total Deaths >>", l)
    elif op == "5":
        confirm = js["statewise"][0]["confirmed"]
        re = js["statewise"][0]["recovered"]
        acti = js["statewise"][0]["active"]
        dead = js["statewise"][0]["deaths"]
        print("Total Confirmed >>", confirm)
        print("Total Recovered >>", re)
        print("Total Active >>", acti)
        print("Total Dead >>", dead)

    elif op == "6":
        name = input("Enter the name of the state code>>")
        for i in range(38):
            state = js["statewise"][i]["statecode"]
            if (state == name):
                confirm = js["statewise"][i]["confirmed"]
                re = js["statewise"][i]["recovered"]
                acti = js["statewise"][i]["active"]
                dead = js["statewise"][i]["deaths"]
                print(state)
                print("Total Confirmed >>", confirm)
                print("Total Recovered >>", re)
                print("Total Active >>", acti)
                print("Total Dead >>", dead)
                print("........................................")
                print("........................................")
    elif op == "7":
        confirm = js["statewise"][0]["deltaconfirmed"]
        re = js["statewise"][0]["deltarecovered"]
        dead = js["statewise"][0]["deltadeaths"]
        lastup = js["statewise"][0]["lastupdatedtime"]
        print("New Confirmed >>", confirm)
        print("New Recovered >>", re)
        print("New Deaths >>", dead)
        print("Last updated at>>", lastup)
        print("........................................")
        print("........................................")
    elif op == "8":
        input_date = input("Enter the date in format DD MMMM>> ")
        for i in range(len(tdate)):
            odate = js["cases_time_series"][i]["date"]
            odate = odate.rstrip()
            if input_date == odate:
                dconfirm = js["cases_time_series"][i]["dailyconfirmed"]
                tconfirm = js["cases_time_series"][i]["totalconfirmed"]
                dre = js["cases_time_series"][i]["dailyrecovered"]
                tre = js["cases_time_series"][i]["totalrecovered"]
                ddead = js["cases_time_series"][i]["dailydeceased"]
                tdead = js["cases_time_series"][i]["totaldeceased"]
                print(odate)
                print("Confirmed on that day>>", dconfirm)
                print("Recovered on that day>>", dre)
                print("Deaths on that day>>", ddead)
                print("Total Confirmed >>", tconfirm)
                print("Total Recovered >>", tre)
                print("Total Deaths >>", tdead)
                print("........................................")
                print("........................................")
    elif op == "9":

        if os.path.exists('Corona_DataBase.xlsx') == True:
            print("DataBase already exists")
            check = input("Do you want to update Database")
            if check == "yes":
                createdatabase()
                print("Database updated")
        else:
            createdatabase()
            print("Database Created")
    elif op == "10":
        print("Thank You!!")
        break
    else:
        print("PLease give proper operation!")
