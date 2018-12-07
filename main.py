import pandas as pd

file = input('File Path: ')

data = pd.read_csv(file)

Qtys = ['Qty 1', 'Qty 2', 'Qty 3', 'Qty 4', 'Qty 5',
        'Qty 6', 'Qty 7', 'Qty 8', 'Qty 9', 'Qty 10']
prices = ['Amount 1', 'Amount 2', 'Amount 3', 'Amount 4', 'Amount 5',
          'Amount 6', 'Amount 7', 'Amount 8', 'Amount 9', 'Amount 10']


def run(data):
    qtys = ['Qty 1', 'Qty 2', 'Qty 3', 'Qty 4', 'Qty 5',
            'Qty 6', 'Qty 7', 'Qty 8', 'Qty 9', 'Qty 10']
    prices = ['Amount 1', 'Amount 2', 'Amount 3', 'Amount 4', 'Amount 5',
              'Amount 6', 'Amount 7', 'Amount 8', 'Amount 9', 'Amount 10']

    data.NDC = data.NDC.astype(str)
    data.NDC = data.NDC.str[0:-2]
    data.NDC = data.NDC.str.zfill(11)

    print(Qtys)

    data[prices] = data[prices].fillna(0)

    for col in prices:
        data[col] = data[col].map(lambda x: '{0:.2f}'.format(x))

    for col in qtys:
        data[col] = data[col].map(lambda x: '{0:.0f}'.format(x))

        print(data)
