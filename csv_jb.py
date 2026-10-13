import csv

with open('sensor_raw.csv','r',encoding='GBK',newline='') as f:
    reader=csv.DictReader(f)
    groups={}
    for x in reader:
        try:
            v=float(x['电压'])
        except (ValueError,TypeError):
            continue
        groups.setdefault(x['日期'],[]).append(v)
# for date,value in groups.items():
#     avg=sum(value)/len(value)
#     print(f'{date:<10}: 平均电压 {avg:<5.5}')
with open('sensor_raw.csv','w',encoding='utf-8-sig',newline='') as f:
    writer=csv.writer(f)
    writer.writerow(['日期','平均电压','有效值数量'])
    for date,value in groups.items():
        avg=sum(value)/len(value)
        writer.writerow([date,avg,len(value)])


