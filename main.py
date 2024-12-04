import argparse
import csv
from datetime import datetime
import calendar
date = datetime.now().date()
parser = argparse.ArgumentParser(description='Expense Tracker')
parser.add_argument('action', choices=['add', 'list', 'summary', 'delete', 'update'])
parser.add_argument('--description', help='what are you adding', required=False)
parser.add_argument('--amount', type=float, help='the cost', required=False)

parser.add_argument('--id', type=int,required=False)
parser.add_argument('--month', type=int)
args = parser.parse_args()


def add():
    global date
    if args.amount is not None and args.description is not None:
        if args.amount >= 0:
            try:
                with open('data.csv', 'r') as f:
                    reader = csv.DictReader(f)
                    id_ = len(list(reader))+1
            except FileNotFoundError:
                id_ = 1
                with open('data.csv', 'a+', newline='') as f:
                    writer = csv.DictWriter(f, ['ID', 'Date', 'Description', 'Amount'])
                    writer.writeheader()
                    writer.writerow({'ID': id_, 'Date': datetime.now().date(), 'Description': args.description, 'Amount': f'${args.amount}'})
            else:
                with open('data.csv', 'a+', newline='') as f:
                    writer = csv.DictWriter(f, ['ID', 'Date', 'Description', 'Amount'])
                    if id_ == 1:
                        writer.writeheader()
                    writer.writerow({'ID': id_, 'Date': date, 'Description': args.description, 'Amount': f'${args.amount}'})
            print(f'Added {args.description} for {args.amount}')
        else:
            print('Error! \nEnter an amount and description when adding an expense')
    else:
        print('Error Invalid Input')
def delete(id_):

    with open('data.csv', 'r') as f:
        reader = csv.DictReader(f)
        rows = [row for row in reader if row['ID'] != f'{id_}']



    with open('data.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        for row in rows:
            writer.writerow(row)





def view(type):
    if type == 'list':
        with open('data.csv', 'r') as f:
            reader = csv.DictReader(f)
            heads = reader.fieldnames
            print(f"{heads[0]:<5} {heads[1]:<12} {heads[2]:<12} {heads[3]:<5}")
            # print(heads)
            for row in reader:
                print(f"{row['ID']:<5} {row['Date']:<12} {row['Description']:<12} {row['Amount']:>5}")
    elif type == 'summary':

        with open('data.csv', 'r') as f:
            reader = csv.DictReader(f)
            amount = sum([float(((row['Amount']).split('$'))[1]) for row in reader])
            try:
                month = args.month
                with open('data.csv', 'r') as f:
                    reader = csv.DictReader(f)
                    rows = sum([float(((row['Amount']).split('$'))[1]) for row in reader if
                                ((row['Date']).split('-'))[1] == str(month)])

                date_month = calendar.month_name[month]
                if len(date_month) == 0:
                    print(f'No expenses found for {date_month}')
                else:
                    print(f'Total expenses for {date_month} is ${rows}')

            except:
                print(f'Total expenses: ${amount}')


    # print(f"This is the {type}")


if args.action == 'add':
    add()
elif args.action == 'list':
    view(args.action)
elif args.action == 'summary':
    view(args.action)
elif args.action == 'delete':
    delete(args.id)
elif args.action == 'update':
    update()

