import sys
import random

class Account:
    def __init__(self,holder):
        self.holder = holder
        self._balance = 0
        self.__account_number = random.randint(1000000,9999999)

    def deposit(self,summ):
        self._balance += summ

    def withdraw(self,summ):
        self._balance -= summ

    def get_bal(self):
        return f'Текущий баланс {self._balance}'
    
    def get_info(self):
        num_str = str(self.__account_number)
        return f'Имя счета: {self.holder}, Номер счета: ***{self.__account_number}'
    
    
        


class Bank:
    def __init__(self):
        self.accounts = []
    
    def find_account(self,holder_name):
        for acc in self.accounts:
            if holder_name == i:
                return 
        return False

    
    def transfer(self,sender_name,transfer_name,summ):
        sender = self.find_account(sender_name)
        transfer = self.find_account(transfer_name)

        if not sender or not transfer:
            return 'Один из счетов не найден'


        if summ > sender._balance:
            return 'Недостаточно средств для перевода'
        else:
            sender.withdraw(summ)
            transfer.deposit(summ)
            return 'перевод успешно выполнен!'

    def all_acc(self):
        return [acc.get_info() for acc in self.accounts]




bank1 = Bank()

while True:
    print('''Что вы хотите сделать? 
            1. создать новый счет 
            2. пополнить существующий счет  
            3. снять средства с существующего счета 
            4. перевести деньги на другой счет 
            5. посмотреть баланс счета
            6. посмотреть все имеющиеся счета
            0. выйти ''')
    choice_inp = input()

    if choice_inp.isdigit():
        choice = int(choice_inp)
    else:
        print('Введите число от 0 до 4')

    match choice:
        case 1:
            n = input('Введите имя счета ')
            new_acc = Account(n)
            bank1.accounts.append(new_acc)

        case 2:
            num = input('Введите имя счета ')
            acc = bank1.find_account(num)

            if acc:
                summ = int(input('Введите сумму для пополнения '))
                num.deposit(summ)
            else:
                print('Счета с таким именем не существует ')
            

        case 3:
            num = input('Введите имя счета ')
            if bank1.find_account(num):
                summ = int(input('Введите сумму для снятия '))
                if summ > num._balance:
                    print('Недостаточно средств для снятия ')
                else:
                    num.withdraw(summ)
            else:
                print('Счета с таким именем не существует')
        case 4:
            sender = input('Введите имя счета с которого будут отправлены деньги')
            transfer = input('Введите имя счета на который будут отправлены деньги')
            summ = int(input('Введите сколько денег вы хотите отправить'))

            bank1.transfer(sender,transfer,summ)
        case 5:
            num = input('Введите номер счета')
            if bank1.find_account(num):
                print(num.get_bal(num))
            else:
                print('счета с таким именем не существует')
        case 6:
            accounts = bank1.all_acc()
            for i in range(len(accounts)):
                print(accounts[i])
            
        case 0:
            sys.exit(0)

        
            
