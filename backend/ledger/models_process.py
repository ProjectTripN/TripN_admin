# 여행업 알선 수입＝여행자로부터 받는 관광요금－원가
import csv
import random
import pandas as pd
from django.db.models import Sum
from ledger.models import Ledger
from common.models import ValueObject, Reader, Printer
from reservation.models import Reservation


class Processing:
    def __init__(self):
        vo = ValueObject()
        reader = Reader()
        self.printer = Printer()
        vo.context = 'ledger/data/'
        vo.fname = 'sales.csv'
        self.csvfile = reader.new_file(vo)

    def report_process(self):
        with open('ledger/data/2020_PL_3.csv', newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                # if not FinReports.objects.filter(category=row['항목명']).exists():
                report = Ledger.objects.create(year=2020,
                                               date='2020-12-31',
                                               category=row['항목명'],
                                               price=int(float(row['전기'])),
                                               )
                print(f'1 >>>> {report}')
        print('USER DATA UPLOADED SUCCESSFULLY!')

    def pre_sales(self):
        arr = []
        for t in range(1, 43):
            t = Reservation.objects.get(pk=t)
            total = t.total_price - t.tax
            price = t.price
            date = t.reg_date
            profit = total - price
            arr.append(date)
            arr.append('매출액')
            arr.append(total)
            arr.append(date)
            arr.append('매출원가')
            arr.append(price)
            arr.append(date)
            arr.append('매출총이익')
            arr.append(profit)
        n = 3
        result = [arr[i * n:(i + 1) * n] for i in range((len(arr) + n - 1) // n)]
        df = pd.DataFrame(result, columns=['date', 'category', 'price'])
        print(df)
        df.to_csv(self.csvfile)

    def sales_process(self, s):
        arr = []
        t = Reservation.objects.get(pk=s)
        total = t.total_price - t.tax  # 매출액
        price = t.price                # 매출원가
        date = t.reg_date              #
        profit = total - price
        arr.append(date)
        arr.append('매출액')
        arr.append(total)
        arr.append(date)
        arr.append('매출원가')
        arr.append(price)
        arr.append(date)
        arr.append('매출총이익')
        arr.append(profit)
        # arr.append(date)
        # arr.append('영업이익')
        # arr.append(total)
        n = 3
        result = [arr[i * n:(i + 1) * n] for i in range((len(arr) + n - 1) // n)]
        df = pd.DataFrame(result, columns=['date', 'category', 'price'])
        print(df)
        df.to_csv('ledger/data/get_sales.csv')

    def pre_cost(self):
        arr = []

        def create_price():
            return random.randint(10000, 1000000)

        def create_month():
            month = random.randint(1, 12)
            if month < 10:
                month = f'0{month}'
            return month

        def create_day():
            day = random.randint(1, 28)
            if day < 10:
                day = f'0{day}'
            return day

        def create_date():
            return f'2021-{create_month()}-{create_day()}'

        for i in range(100):
            arr.append(create_date())
            arr.append('판매비와관리비')
            arr.append(create_price())
            arr.append(create_date())
            arr.append('지급수수료')
            arr.append(create_price())
            arr.append(create_date())
            arr.append('기타비용')
            arr.append(create_price())
            arr.append(create_date())
            arr.append('금융비용')
            arr.append(create_price())
            arr.append(create_date())
            arr.append('기타수익')
            arr.append(create_price())
            arr.append(create_date())
            arr.append('금융수익')
            arr.append(create_price())
        n = 3
        result = [arr[i * n:(i + 1) * n] for i in range((len(arr) + n - 1) // n)]
        df = pd.DataFrame(result, columns=['date', 'category', 'price'])
        print(df)
        df.to_csv('ledger/data/cost.csv')

    def insert_sales(self):
        with open('ledger/data/sales.csv', newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                # if not Ledger.objects.filter(category=row['category'], date=row['date']).exists():
                    ledger = Ledger.objects.create(date=row['date'],
                                                   year=2021,
                                                   category=row['category'],
                                                   price=row['price'])
                    print(f'2 >>>> {ledger}')
            print('DATA UPLOADED SUCCESSFULLY!')

    def insert_cost(self):
        with open('ledger/data/cost.csv', newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                ledger = Ledger.objects.create(date=row['date'],
                                               year=2021,
                                               category=row['category'],
                                               price=row['price'])
                print(f'2 >>>> {ledger}')
            print('DATA UPLOADED SUCCESSFULLY!')

    def show_cost(self):
        cost = [{f'월': f'{p}',
                 f'매출원가': Ledger.objects.filter(date__year=2021, date__month=p, category='매출원가').aggregate(Sum('price'))['price__sum'],
                 f'판매비와관리비': Ledger.objects.filter(date__year=2021, date__month=p, category='판매비와관리비').aggregate(Sum('price'))['price__sum'],
                 f'지급수수료': Ledger.objects.filter(date__year=2021, date__month=p, category='지급수수료').aggregate(Sum('price'))['price__sum'],
                 f'기타비용': Ledger.objects.filter(date__year=2021, date__month=p, category='기타비용').aggregate(Sum('price'))['price__sum'],
                 f'금융비용': Ledger.objects.filter(date__year=2021, date__month=p, category='금융비용').aggregate(Sum('price'))['price__sum']} for p in range(1, 13)]
        return cost

    def year_profit(self):
        profit = [{f'월': f'{p}',
                   f'매출총이익': Ledger.objects.filter(date__year=2021, date__month=p, category='매출총이익').aggregate(Sum('price'))['price__sum'],
                   f'영업이익': (Ledger.objects.filter(date__year=2021, date__month=p, category='매출총이익').aggregate(Sum('price'))['price__sum']
                             - Ledger.objects.filter(date__year=2021, date__month=p, category='판매비와관리비').aggregate(Sum('price'))['price__sum']
                             - Ledger.objects.filter(date__year=2021, date__month=p, category='지급수수료').aggregate(Sum('price'))['price__sum']),
                   f'기타수익': Ledger.objects.filter(date__year=2021, date__month=p, category='기타수익').aggregate(Sum('price'))['price__sum'],
                   f'금융수익': Ledger.objects.filter(date__year=2021, date__month=p, category='금융수익').aggregate(Sum('price'))['price__sum'],
                   f'당기순이익': Ledger.objects.filter(date__year=2021, date__month=p, category='당기순이익').aggregate(Sum('price'))['price__sum']} for p in range(1, 13)]
        return profit

# - Ledger.objects.filter(date__year=2021, date__month=p, category='판매비와관리비').aggregate(Sum('price'))['price__sum']
#                               - Ledger.objects.filter(date__year=2021, date__month=p, category='지급수수료').aggregate(Sum('price'))['price__sum']
#                               + Ledger.objects.filter(date__year=2021, date__month=p, category='기타수익').aggregate(Sum('price'))['price__sum']
#                               - Ledger.objects.filter(date__year=2021, date__month=p, category='기타비용').aggregate(Sum('price'))['price__sum']
#                               + Ledger.objects.filter(date__year=2021, date__month=p, category='금융수익').aggregate(Sum('price'))['price__sum']
#                               - Ledger.objects.filter(date__year=2021, date__month=p, category='금융비용').aggregate(Sum('price'))['price__sum']
