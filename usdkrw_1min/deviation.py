import csv

file_name = 'USDKRW_2014'
price_data = []
price_set = []
timeint1 = []
timeint2 = []
t1 = []
t2 = []
n = -1

f = open(file_name + '.csv', 'rt')
data = csv.reader(f)

for row in data:
    price_data = row[0:6]
    price_set.append(price_data)
    if not data: break
    
for line in price_set:
    if not price_set: break
    try:
        time1=price_set[n-1]
        time2=price_set[n]
        timestr1 = time1[1].split(':')
        timestr2 = time2[1].split(':')
        t1 = timestr1[0] + timestr1[1] + timestr1[2]
        t2 = timestr2[0] + timestr2[1] + timestr2[2]
        if int(t1) - int(t2) == 100:
            if abs(((float(price_set[n-1][4])-float(price_set[n][3]))/float(price_set[n][3])*100)) > abs(((float(price_set[n-1][3])-float(price_set[n][4]))/float(price_set[n][4])*100)):
                price_set[n-1].append(float((float(price_set[n-1][4])-float(price_set[n][3]))/float(price_set[n][3])*100))
                n-=1
            else:
                price_set[n-1].append(float((float(price_set[n-1][3])-float(price_set[n][4]))/float(price_set[n][4])*100))
                n-=1
        else: 
            price_set[n-1].append('')
            n-=1
    except IndexError:
        print('')
    f.close()

with open(file_name + '_output.csv', "w", newline="") as g:
    writer = csv.writer(g)
    writer.writerows(price_set)