import csv
import pandas as pd
from django.db.models import Sum
from fin_reports.models import FinReports
from ledger.models import Ledger


class ReportProcess:
    def make_report(self):
        sales = Ledger.objects.filter(date__year=2021, category='매출액').aggregate(Sum('price'))['price__sum']
        cost_of_sales = Ledger.objects.filter(date__year=2021, category='매출원가').aggregate(Sum('price'))['price__sum']
        gross_profit = Ledger.objects.filter(date__year=2021, category='매출총이익').aggregate(Sum('price'))['price__sum']
        selling_expenses = Ledger.objects.filter(date__year=2021, category='판매비와관리비').aggregate(Sum('price'))['price__sum']
        fees = Ledger.objects.filter(date__year=2021, category='지급수수료').aggregate(Sum('price'))['price__sum']
        operating_income = Ledger.objects.filter(date__year=2021, category='영업이익').aggregate(Sum('price'))['price__sum']
        other_income = Ledger.objects.filter(date__year=2021, category='기타수익').aggregate(Sum('price'))['price__sum']
        other_loss = Ledger.objects.filter(date__year=2021, category='기타비용').aggregate(Sum('price'))['price__sum']
        financial_income = Ledger.objects.filter(date__year=2021, category='금융수익').aggregate(Sum('price'))['price__sum']
        financial_loss = Ledger.objects.filter(date__year=2021, category='금융비용').aggregate(Sum('price'))['price__sum']
        df = pd.DataFrame((sales, cost_of_sales, gross_profit, selling_expenses, fees, operating_income, other_income,
                           other_loss, financial_income, financial_loss),
                          columns=['price'])
        i = FinReports.objects.filter(year=2021, category__in=['영업이익', '기타수익', '기타비용', '금융수익', '금융비용']).values()
        a = i.filter(category='영업이익')
        print(a)

    #     fin_reports = FinReports.objects.create(year=2021,
    #                                             category='금융비용',
    #                                             price=133654167
    #                                             )
    #     print(f'1 >>>> {fin_reports}')
    # print('USER DATA UPLOADED SUCCESSFULLY!')

# 	     매출액  Sales
# 	- 매출원가  Cost of sales
# ------------------------------
# 	  매출총이익  Gross profit
# 	- 판매비와관리비  Selling expenses
# 	- 지급수수료  Fees
# -------------------------------
# 	   영업이익  Operating income
# 	- 기타손익 및 금융손익 other income & financial loss
# 	  (기타수익 + 금융수익 - 기타비용 - 금융비용)
# -------------------------
# 	당기순이익  Net income
