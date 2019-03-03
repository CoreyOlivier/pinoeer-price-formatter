import datetime
import pandas as pd

file = '~/Documents/pricelistTest.csv'
date = datetime.date.today()
strDate = datetime.date.strftime(date, "%m%d%y")
saveFile = '~/Documents/pricelist{}.csv'.format(strDate)

qtys = ['Qty 1', 'Qty 2', 'Qty 3', 'Qty 4', 'Qty 5',
        'Qty 6', 'Qty 7', 'Qty 8', 'Qty 9', 'Qty 10']
prices = ['Amount 1', 'Amount 2', 'Amount 3', 'Amount 4', 'Amount 5',
          'Amount 6', 'Amount 7', 'Amount 8', 'Amount 9', 'Amount 10']


def upload(file=file):
    data = pd.read_csv(file)

    return data


def format_data(data):
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

def last_prices(df):
    for i in range(0, len(df)):
        last = False
        counter = 10
        while last is False:
            if counter == 0:
                break
            if pd.notnull(df.loc[i, 'Qty {}'.format(counter)]) is True:
                replace_cell(df, i, counter)
                last = True
            counter = counter - 1
    return df


def replace_cell(df, row, counter):
    qty = df.loc[row, 'Qty {}'.format(counter)]
    amount = df.loc[row, 'Amount {}'.format(counter)]
    if counter == 10:
        counter = 9
    df.loc[row, 'Qty {}'.format(counter+1)] = qty*10
    df.loc[row, 'Amount {}'.format(counter+1)] = amount*10


def save(df, file=saveFile):
    df.to_csv(file, index=False, encoding='utf-8')
    print('Saved')


if __name__ == '__main__':
    save(format_data(last_prices(upload())))
