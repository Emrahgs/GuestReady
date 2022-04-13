import datetime

def get_commission(date_str):
    date = '%Y-%m-%d'
    commission = 10
    try:
        months = datetime.datetime.strptime(input, date).month
        if 6<=months<=9:
            commission = 15
    except ValueError:
        return ValueError('Please, enter a valid date')    
    return float(commission)
    
input = ('2022-6-13')
print(get_commission(input))