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
        sales = Ledger.objects.filter(date__year=2021, category='매출액').aggregate(Sum('price'))['price__sum']
        print({'sales': sales})
        cost_of_sales = Ledger.objects.filter(date__year=2021, category='매출원가').aggregate(Sum('price'))['price__sum']
        print({'cost_of_sales': cost_of_sales})
        gross_profit = Ledger.objects.filter(date__year=2021, category='매출총이익').aggregate(Sum('price'))['price__sum']
        print({'gross_profit': gross_profit})
        selling_expenses = Ledger.objects.filter(date__year=2021, category='판매비와관리비').aggregate(Sum('price'))['price__sum']
        print({'selling_expenses': selling_expenses})
        fees = Ledger.objects.filter(date__year=2021, category='지급수수료').aggregate(Sum('price'))['price__sum']
        print({'fees': fees})
        operating_income = Ledger.objects.filter(date__year=2021, category='영업이익').aggregate(Sum('price'))['price__sum']
        print({'operating_income': operating_income})
        other_income = Ledger.objects.filter(date__year=2021, category='기타수익').aggregate(Sum('price'))['price__sum']
        print({'other_income': other_income})
        other_loss = Ledger.objects.filter(date__year=2021, category='기타비용').aggregate(Sum('price'))['price__sum']
        print({'other_loss': other_loss})
        financial_income = Ledger.objects.filter(date__year=2021, category='금융수익').aggregate(Sum('price'))['price__sum']
        print({'financial_income': financial_income})
        financial_loss = Ledger.objects.filter(date__year=2021, category='금융비용').aggregate(Sum('price'))['price__sum']
        print({'financial_loss': financial_loss})

        # net_income = operating_income['price__sum'] + other_income['price__sum'] - other_loss['price__sum'] + financial_income['price__sum'] - financial_loss['price__sum']
        # print(net_income)
