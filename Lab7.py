#Brett Zimmermann
#05/27/2012
#global
import re
import csv
data = []
#main
def main():
    #open file and convert to csv.reader
    dataset = open("NFL_Coaches_Career.csv", "r")
    records = csv.reader(dataset)
    #call sanitization
    sanitize(records)     
    #print menu
    print("*"*60)
    #call menu
    menu()
    #close the file
    dataset.close()
#sanitize the records function    
def sanitize(records):
    for record in records:
        if record[14] == " ":
             record[14] == 0
        if(record[0] != 'Rk'):
            if    record[0] == '': record[0] = 0
            else: record[0] =  int(record[0])
            record[1] = re.sub(r'[^a-zA-Z\ \' \.]','', record[1])
            if    record[2] == '': record[2] = 0
            else: record[2] =  int(record[2])
            record[3] = re.sub(r'[^0-9\-]','', record[3])
            if    record[4] == '': record[4] = 0
            else: record[4] =  int(record[4])
            if    record[5] == '': record[5] = 0
            else: record[5] =  int(record[5])
            if    record[6] == '': record[6] = 0
            else: record[6] =  int(record[6])
            if    record[7] == '': record[7] = 0
            else: record[7] =  int(record[7])
            if    record[8] == '':  record[8] = float(0)
            else: record[8] = float(record[8])
            if    record[9] == '': record[9] = 0
            else: record[9] =  int(record[9])
            if    record[10] == '': record[10] = 0
            else: record[10] =  int(record[10])
            if    record[11] == '': record[11] = 0
            else: record[11] =  int(record[11])
            if    record[12] == '': record[12] = 0
            else: record[12] =  int(record[12])
            if    record[13] == '': record[13] = 0
            else: record[13] =  int(record[13])
            if    record[14] == '':  record[14] = float(0)
            else: record[14] = float(record[14])
            if    record[15] == '':  record[15] = float(0)
            else: record[15] = float(record[15])
            if    record[16] == '': record[16] = 0
            else: record[16] =  int(record[16])
            if    record[17] == '': record[17] = 0
            else: record[17] =  int(record[17])
            if    record[18] == '': record[18] = 0
            else: record[18] =  int(record[18])
            if    record[19] == '': record[19] = 0
            else: record[19] =  int(record[19])
            if(record[4] != 0): record.append(((record[17]*4) + (record[12]*2))/ record[4])
            else: record.append(0)
            if(record[9] != 0): record.append(record[9]*record[2])
            else:record.append(0)
            data.append(record)
    print("{0} actual records in NFL_Coaches_Career.csv\n".format(len(data)))   
        
#menu
def menu():
    try:
        print("\n")
        print("The Best of the Best NFL Coaches of All Time",  "\n\n1.)Most Championships",\
                "\n2.)Most Super Bowl Appearances \n3.)Highest Winning Percentage", \
                "\n4.)Highest Playoff Winning Percentage \n5.)Best Coach", \
                "\n6.)Best Regular Season Coach \n0.) Exit")
        listnum = float(input("\nPlease Select a Menu Option: "))
        while listnum != 0:
                if listnum ==1:
                    return mostchamps()
                elif listnum ==2:
                    return mostsbappear()
                elif listnum == 3:
                    return highwinpercent()
                elif listnum == 4:
                    return highplayoffwin()
                elif listnum == 5:
                    return bestcoachps()
                elif listnum == 6:
                    return bestregcoach()
                else:
                    break
    except ValueError:
        print("You have entered in an invalid entry. Try again.")
        menu()
                
#most championships function        
def mostchamps():
    mylist = []
    counter = 0
    print('*'*10, 'Most Championships','*'*10)
    for record in sorted(data, key=lambda x: x[17], reverse=True):
        if record[17] >0:
            counter +=1
            print(record[1],  record[3], record[17])
            if counter == 20:
                return menu()
        
#most superbowl appearance function
def mostsbappear():
    mylist =[]
    counter = 0
    print('*'*10, 'Most SuperBowl Appearances','*'*10)
    for record in sorted(data, key=lambda x: x[18], reverse=True):
        if record[18] >0:
            counter +=1
            print(record[1],  record[3], record[18])
            if counter == 20:
                return menu()
            
#highest win percentage regular season function
def highwinpercent():
    mylist =[]
    counter = 0
    print('*'*10, 'Highest Regular Season Win Percentage','*'*10)
    for record in sorted(data, key=lambda x: x[8], reverse=True):
        if record[8] >0:
            counter +=1
            print(record[1],  record[3], format(record[8],'.2f'))
            if counter == 20:
                return menu()
            
#highest playoff win percentage function
def highplayoffwin():
    mylist =[]
    counter = 0
    print('*'*10, 'Highest Playoff Win Percentage','*'*10)
    for record in sorted(data, key=lambda x: x[14], reverse=True):
        if record[14] >0:
            counter +=1
            print(record[1], record[3], format(record[14],'.2f'))
            if counter == 20:
                return menu()
            
#best coach function
def bestcoachps():
   counter = 0
   print('*'*10, 'Best Coach','*'*10)
   for record in sorted(data, key = lambda x: x[20], reverse = True):
           counter+=1
           print(record[1], record[3], format(record[20],'.2f'))
           if counter == 20:
               return menu()
   
   
#best regular season coach function
def bestregcoach():
    counter = 0
    print('*'*10, 'Best Regular Season Coach','*'*10)
    for record in sorted(data, key = lambda x: x[21], reverse = True):
           counter+=1
           print(record[1], record[3], record[21])
           if counter == 20:
               return menu()

  
#call main
main()
