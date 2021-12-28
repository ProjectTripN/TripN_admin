import csv
import pandas as pd

import ledger
from common.models import ValueObject, Printer, Reader
from fin_reports.models import FinReports
from ledger.models import Ledger
from ledger.serializer import LedgerSerializer


class DbUploader:
    def __init__(self):
        vo = ValueObject()
        reader = Reader()
        self.printer = Printer()
        vo.context = 'fin_reports/data/'
        vo.fname='2020_PL_3.csv'
        self.csvfile = reader.new_file(vo)

    def insert_data(self):
        self.insert_fin_report()

    def pre_process(self):
        df = pd.read_csv(self.csvfile, encoding='UTF-8', thousands=',')
        df = df.fillna(0)
        df.to_csv(self.csvfile + '2020_PL_2.csv')

    def insert_fin_report(self):
        ledger = Ledger.objects.all()
        ledger = LedgerSerializer(ledger, many=True).data
        for row in ledger:
            print(row)
            fin_reports = FinReports.objects.create(year=row['year'],
                                                    category=row['category'],
                                                    price=row['price'],
                                                    ledger_id=row['id']
                                                    )
            print(f'1 >>>> {fin_reports}')
        print('USER DATA UPLOADED SUCCESSFULLY!')
