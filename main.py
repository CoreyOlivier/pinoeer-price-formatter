import pandas as pd
import datetime

file = '~/Documents/pricelistTest.csv'
date = datetime.date.today()
strDate = datetime.date.strtime(date, "%m%d%y")
saveFile = '~/Documents/pricelist{}.csv'.format(strDate)

Qtys = ['Qty 1', 'Qty 2', 'Qty 3', 'Qty 4', 'Qty 5',
        'Qty 6', 'Qty 7', 'Qty 8', 'Qty 9', 'Qty 10']
prices = ['Amount 1', 'Amount 2', 'Amount 3', 'Amount 4', 'Amount 5',
          'Amount 6', 'Amount 7', 'Amount 8', 'Amount 9', 'Amount 10']


def upload(file=file):
    data = pd.read_csv(file)

    return data


def run(data):
    qtys = ['Qty 1', 'Qty 2', 'Qty 3', 'Qty 4', 'Qty 5',
            'Qty 6', 'Qty 7', 'Qty 8', 'Qty 9', 'Qty 10']
    prices = ['Amount 1', 'Amount 2', 'Amount 3', 'Amount 4', 'Amount 5',
              'Amount 6', 'Amount 7', 'Amount 8', 'Amount 9', 'Amount 10']

    data = data.drop_duplicates()
    data = data.dropna(subset=['NDC'])
    data = data.fillna(0)
    data.NDC = data.NDC.astype(str)
#    data.NDC = data.NDC.str[0:-2]
    data.NDC = data.NDC.str.zfill(11)

    for col in prices:
        data.loc[data[col] == 0, col] = 1000
        data[col] = data[col].map(lambda x: '{0:.2f}'.format(x))

    for col in qtys:
        data[col] = data[col].map(lambda x: '{0:.0f}'.format(x))

    data.UPC = ''
    data.Alternate = ''

    return data


def save(df, file=saveFile):
    df.to_csv(file, index=False, encoding='utf-8')
    print('Saved')
