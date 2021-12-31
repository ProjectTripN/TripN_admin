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
from django.db.models import Sum
from ledger.models import Ledger


class ReportProcess:
    def make_report(self):
        sales = Ledger.objects.filter(date__year=2021, category='매출액').aggregate(Sum('price'))['sales_sum']
        print(sales)
        cost_of_sales = Ledger.objects.filter(date__year=2021, category='매출원가').aggregate(Sum('price'))['cost_of_sales']
        print(cost_of_sales)
        gross_profit = Ledger.objects.filter(date__year=2021, category='매출총이익').aggregate(Sum('price'))['gross_profit']
        print(gross_profit)
        selling_expenses = Ledger.objects.filter(date__year=2021, category='판매비와관리비').aggregate(Sum('price'))['selling_expenses']
        print(selling_expenses)
        fees = Ledger.objects.filter(date__year=2021, category='지급수수료').aggregate(Sum('price'))['fees']
        print(fees)
        operating_income = Ledger.objects.filter(date__year=2021, category='영업이익').aggregate(Sum('price'))['operating_income']
        print(operating_income)
        other_income = Ledger.objects.filter(date__year=2021, category='기타수익').aggregate(Sum('price'))['other_income']
        print(other_income)
        other_loss = Ledger.objects.filter(date__year=2021, category='기타비용').aggregate(Sum('price'))['other_loss']
        print(other_loss)
        financial_income = Ledger.objects.filter(date__year=2021, category='금융수익').aggregate(Sum('price'))['financial_income']
        print(financial_income)
        financial_loss = Ledger.objects.filter(date__year=2021, category='금융비용').aggregate(Sum('price'))['financial_loss']
        print(financial_loss)
        # net_income = operating_income['operating_income'] + other_income[''] - other_loss[''] + financial_income[''] - financial_loss['']
        # print(net_income)
