import csv
from common.models import ValueObject, Reader, Printer
from user.models import User


class Processing:
    def __init__(self):
        vo = ValueObject()
        reader = Reader()
        self.printer = Printer()
        vo.context = 'user/data/'
        vo.fname = 'user2.csv'
        self.csvfile = reader.new_file(vo)

    def insert_data(self):
        self.insert_users()

    def insert_users(self):
        with open('user/data/user2.csv', newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                # if not FinReports.objects.filter(category=row['항목명']).exists():
                users = User.objects.create(user_id=row['user_id'],
                                            address=row['address'],
                                            birth=row['birth'],
                                            card_company=row['card_company'],
                                            card_number=row['card_number'],
                                            email=row['email'],
                                            first_name=row['first_name'],
                                            gender=row['gender'],
                                            last_name=row['last_name'],
                                            mbti=row['mbti'],
                                            mbti_list=row['mbti_list'],
                                            name=row['name'],
                                            passport=row['passport'],
                                            password=row['password'],
                                            phone_number=row['phone_number'],
                                            reg_date=row['reg_date'],
                                            username=row['username'])
                print(f'1 >>>> {users}')
        print('USER DATA UPLOADED SUCCESSFULLY!')
