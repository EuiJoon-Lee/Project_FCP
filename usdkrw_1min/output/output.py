import csv

price_data = []
price_set = []
file_name1 = 'USDKRW_'
file_name2 = '_output'
edited_name = []
USDKRW_deviations = []
deviation = list()
i = 2014

while i <= 2019:
    price_data = []
    price_set = []
    edited_name = file_name1 + str(i) + file_name2
    print(edited_name)
    i += 1

    f = open(edited_name+'.csv', 'rt', encoding='utf-8')
    data = csv.reader(f)

    for row in data :
        try:
            price = row
            price_set.append(price[6])
            if not data: break
        except:
            print()
      
    for line in price_set:
        try:
            if not price_set: break
            deviation.append((float(line)))
            USDKRW_deviations.append(deviation)
            deviation = []
        except:
            print()
    f.close()


with open('USDKRW_deviation.csv', "w", newline="") as g:
    writer = csv.writer(g)
    writer.writerows(USDKRW_deviations)
