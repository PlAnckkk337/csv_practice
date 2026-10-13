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
for date,value in groups.items():
    avg=sum(value)/len(value)
    print(f'{date:<10}: 平均电压 {avg:<5.5}')

