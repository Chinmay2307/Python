import json
import urllib.request, urllib.parse, urllib.error
import xlsxwriter

url = "https://api.covid19india.org/data.json"
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print("Data Retrived")
js = json.loads(data)
tdate = js["cases_time_series"]
state_data = js["statewise"]
tested_data = js["tested"]

check = 0
row_worksheet1=1
col_worksheet1=0        

row_worksheet2=1
col_worksheet2=0        

row_worksheet3=1
col_worksheet3=0

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
        print("Total Cases >>",y)
    elif op == "2":
        m = js["statewise"][0]["recovered"]
        print("Total Recovered >>",m)
    elif op == "3":
        k = js["statewise"][0]["active"]
        print("Total Active >>",k)
    elif op == "4":
       l = js["statewise"][0]["deaths"]
       print("Total Deaths >>",l)
    elif op == "5":
        confirm = js["statewise"][0]["confirmed"]
        re = js["statewise"][0]["recovered"]
        acti = js["statewise"][0]["active"]
        dead = js["statewise"][0]["deaths"]
        print("Total Confirmed >>",confirm)
        print("Total Recovered >>",re)
        print("Total Active >>",acti)
        print("Total Dead >>",dead)

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
        print("Last updated at>>",lastup)
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
        
        if check == 0:
            workbook=xlsxwriter.Workbook('Corona_DataBase.xlsx')
            worksheet1=workbook.add_worksheet('Case Time Series')
            worksheet2=workbook.add_worksheet('State Wise Cases')
            worksheet3=workbook.add_worksheet('Tests')
            bold=workbook.add_format({'bold' : True })
            num_type=workbook.add_format({'num_format': '0'})
            

            worksheet1.write('A1','Date',bold)
            worksheet1.write('B1','Daily Confirmed',bold)
            worksheet1.write('C1','Dail Deceaced',bold)
            worksheet1.write('D1','Daily Recovered',bold)
            worksheet1.write('E1','Total Confirmed',bold)
            worksheet1.write('F1','Total Deceased',bold)
            worksheet1.write('G1','Total Recovered',bold)
            worksheet1.set_column('A:A',15)
            worksheet1.set_column('B:G',18)
            
            worksheet2.write('A1','Last Updated Time',bold)
            worksheet2.write('B1','State',bold)
            worksheet2.write('C1','State Code',bold)
            worksheet2.write('D1','Active',bold)
            worksheet2.write('E1','Confirmed',bold)
            worksheet2.write('F1','Deceaced',bold)
            worksheet2.write('G1','Recovered',bold)
            worksheet2.write('H1','Delta Confirmed',bold)
            worksheet2.write('I1','Delta Deceased',bold)
            worksheet2.write('J1','Delta Recovered',bold)
            worksheet2.set_column('A:A',25)
            worksheet2.set_column('B:J',18)

            worksheet3.write('A1','Update Time Stamp',bold)
            worksheet3.write('B1','Individuals tested per confirmed cases',bold)
            worksheet3.write('C1','Positive cases from samples reported',bold)
            worksheet3.write('D1','Sample reported today',bold)
            worksheet3.write('E1','Test positivity rate',bold)
            worksheet3.write('F1','Test conducted by private labs',bold)
            worksheet3.write('G1','Tests per Confirmed cases',bold)
            worksheet3.write('H1','Total individuals tested',bold)
            worksheet3.write('I1','Total positive cases',bold)
            worksheet3.write('J1','Total sample tested',bold)
            worksheet3.set_column('A:A',25)
            worksheet3.set_column('B:B',35)
            worksheet3.set_column('C:C',35)
            worksheet3.set_column('D:D',25)
            worksheet3.set_column('E:E',23)
            worksheet3.set_column('F:F',30)
            worksheet3.set_column('G:G',23)
            worksheet3.set_column('H:H',23)
            worksheet3.set_column('I:I',22)
            worksheet3.set_column('J:J',22)

            for i in range(len(state_data)):
                
                worksheet2.write(row_worksheet2,col_worksheet2,js["statewise"][i]["lastupdatedtime"])
                worksheet2.write(row_worksheet2,col_worksheet2+1,js["statewise"][i]["state"],num_type)
                worksheet2.write(row_worksheet2,col_worksheet2+2,js["statewise"][i]["statecode"],num_type)
                worksheet2.write(row_worksheet2,col_worksheet2+3,js["statewise"][i]["active"],num_type)
                worksheet2.write(row_worksheet2,col_worksheet2+4,js["statewise"][i]["confirmed"],num_type)
                worksheet2.write(row_worksheet2,col_worksheet2+5,js["statewise"][i]["deaths"],num_type)
                worksheet2.write(row_worksheet2,col_worksheet2+6,js["statewise"][i]["recovered"],num_type)
                worksheet2.write(row_worksheet2,col_worksheet2+7,js["statewise"][i]["deltaconfirmed"],num_type)
                worksheet2.write(row_worksheet2,col_worksheet2+8,js["statewise"][i]["deltadeaths"],num_type)
                worksheet2.write(row_worksheet2,col_worksheet2+9,js["statewise"][i]["deltarecovered"],num_type)


                row_worksheet2=row_worksheet2+1
                col_worksheet2=0

            

            for i in range(len(tdate)):
                
                worksheet1.write(row_worksheet1,col_worksheet1,js["cases_time_series"][i]["date"])
                worksheet1.write(row_worksheet1,col_worksheet1+1,js["cases_time_series"][i]["dailyconfirmed"],num_type)
                worksheet1.write(row_worksheet1,col_worksheet1+2,js["cases_time_series"][i]["dailydeceased"],num_type)
                worksheet1.write(row_worksheet1,col_worksheet1+3,js["cases_time_series"][i]["dailyrecovered"],num_type)
                worksheet1.write(row_worksheet1,col_worksheet1+4,js["cases_time_series"][i]["totalconfirmed"],num_type)
                worksheet1.write(row_worksheet1,col_worksheet1+5,js["cases_time_series"][i]["totaldeceased"],num_type)
                worksheet1.write(row_worksheet1,col_worksheet1+6,js["cases_time_series"][i]["totalrecovered"],num_type)
                
                row_worksheet1=row_worksheet1+1
                col_worksheet1=0



            for i in range(len(tested_data)):
                
                worksheet3.write(row_worksheet3,col_worksheet3,js["tested"][i]["updatetimestamp"],num_type)
                worksheet3.write(row_worksheet3,col_worksheet3+1,js["tested"][i]["individualstestedperconfirmedcase"],num_type)
                worksheet3.write(row_worksheet3,col_worksheet3+2,js["tested"][i]["positivecasesfromsamplesreported"],num_type)
                worksheet3.write(row_worksheet3,col_worksheet3+3,js["tested"][i]["samplereportedtoday"],num_type)
                worksheet3.write(row_worksheet3,col_worksheet3+4,js["tested"][i]["testpositivityrate"],num_type)
                worksheet3.write(row_worksheet3,col_worksheet3+5,js["tested"][i]["testsconductedbyprivatelabs"],num_type)
                worksheet3.write(row_worksheet3,col_worksheet3+6,js["tested"][i]["testsperconfirmedcase"],num_type)
                worksheet3.write(row_worksheet3,col_worksheet3+7,js["tested"][i]["totalindividualstested"],num_type)
                worksheet3.write(row_worksheet3,col_worksheet3+8,js["tested"][i]["totalpositivecases"],num_type)
                worksheet3.write(row_worksheet3,col_worksheet3+9,js["tested"][i]["totalsamplestested"],num_type)
                 

                row_worksheet3=row_worksheet3+1
                col_worksheet3=0

            workbook.close()
            check=1
            print("DataBase Created")
        else:
            print("DataBase is already created")
    elif op == "10":
        print("Thank You!!")
        break
    else:
        print("PLease give proper operation!")
