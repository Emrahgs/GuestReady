import datetime

commission = 0

def get_commission(date_str):
    format = '%Y-%m-%d'
    months = datetime.datetime.strptime(input, format).month
    if 6<=months<=9:
        commission = 0.15
    else:
        commission = 0.1
    return float(commission)
    
input = ('2022-7-13')

print(get_commission(input))