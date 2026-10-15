# for:
#     读取：用标准库 csv 或 pandas 都行（建议先用 csv 标准库练手，贴合你已学的文件读写）。

#     清洗，规则如下：

#     去掉重复行（按订单号去重，保留第一次出现）

#     单价 转数字：去掉 ¥、去掉千位逗号、459.0 → 459

#     数量 转数字：空值填 1，3件 → 3，2.0 → 2

#     城市 空值填 未知

#     日期 统一成 YYYY-MM-DD（如 2024-01-06、2024-01-14）

#     商品 去掉首尾空格

#     新增一列 金额 = 单价 × 数量（数量为负表示退货，金额也相应为负，后面累加时直接带符号）。

#     输出 4 个文件（清洗后的数据）：

#     summary_by_category.csv：按「分类」汇总总金额，两列 分类,总金额

#     top5_products.csv：销售额最高的前 5 个「商品」，两列 商品,销售额，降序

#     orders_by_city.csv：按「城市」统计订单数，两列 城市,订单数

#     orders_2024_01.csv：2024 年 1 月的全部订单（清洗后的完整列）

#     打印到屏幕：去重后的总订单数、总销售额。

import csv

with open('sales_orders.csv','r',encoding='utf-8',newline='') as f:
    row=[]
    order_=[]
    row_=csv.DictReader(f)
    for x in row_:
        if not x['订单号'] in order_:
            order_.append(x['订单号'])
            row.append(x)
#去除重复订单号
# for x in row:
#     print(x)

#定向清洗数据
# row[1]['单价']='199'
# row[6]['单价']='459'
# row[13]['单价']='2999'

for x in row:
    x['单价']=x['单价'].replace('¥','')
    x['单价']=x['单价'].replace(',','')

# for x in row:
#     print(float(x['单价']))
for x in row:
    x['单价']=int(float(x['单价']))

# row.pop(19)#删掉数量小于0的数据

row[10]['数量']='3'

# l=[]
# for i in range(len(row)):
#     if row[i]['数量']!='' and float(row[i]['数量'])<0:
#         l.append(i)
# for i in range(len(l)-1,-1,-1):
#     row.pop(l[i])


for i in range(len(row)):
    if row[i]['数量']=='':
        row[i]['数量']=1
    row[i]['数量']=int(float(row[i]['数量']))

for x in row:
    if x['城市']=='':
        x['城市']='未知'

row[17]['日期']='2024-1-14'

for x in row:
    x['商品']=x['商品'].strip()

for x in row:
    x['金额']=x['数量']*x['单价']

groups={}
for x in row:
    groups.setdefault(x['分类'],0)
    groups[x['分类']]+=x['金额']
# print(groups)

with open('summary_by_category.csv','w',encoding='utf-8-sig',newline='') as f:
    writer=csv.writer(f)
    writer.writerow(['分类','金额'])
    for kind,sum_ in groups.items():
        writer.writerow([kind,sum_])

groups_sp={}
for x in row:
    groups_sp.setdefault(x['商品'],0)
    groups_sp[x['商品']]+=x['金额']
# print(groups_sp)

row_1=dict(sorted(groups_sp.items(),key=lambda ky:ky[1],reverse=True))
# print(row_1)
with open('top5_products.csv','w',encoding='utf-8-sig',newline='') as f:
    writer=csv.writer(f)
    writer.writerow(['商品','金额','排名'])
    n=5
    for key,value in row_1.items():
        writer.writerow([key,value,6-n])
        n-=1
        if n==0:
            break

groups_city={}
for x in row:
    groups_city.setdefault(x['城市'],0)
    groups_city[x['城市']]+=x['数量']

with open('orders_by_city.csv','w',encoding='utf-8-sig',newline='') as f:
    writer=csv.writer(f)
    writer.writerow(['城市','订单数'])
    for city,value in groups_city.items():
        writer.writerow([city,value])
gourps_time=[]
for x in row:
    if x['日期'][0:7]=='2024-01':
        gourps_time.append(x)
with open('orders_2024_01.csv','w',encoding='utf-8-sig',newline='') as f:
    writer=csv.writer(f)
    writer.writerow(['2024_01订单'])
    for x in gourps_time:
        writer.writerow([x])
sum_order=0
sum_money=0
for x in row:
    sum_order+=x['数量']
    sum_money+=x['金额']
print(sum_order)
print(sum_money)

# for x in row:
#     print(x)