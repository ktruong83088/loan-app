debt1 = [7350.03,6.990,209.43]
debt2 = [20000,6,300]
debt3 = [30000,7,300]

debts = [debt1,debt2,debt3]

extra = int(input('Extra amt: '))

def interest(bal, interest):
    x = ((interest/100)*bal)/12
    return x

def new_balance(bal, interest):
    return bal + interest

def next_balance(x, y):
    return x - y
	
def project(x, y=0):
    balance = x[0]
    rate = x[1]
    min_payment = x[2] + y
    month = 0
    total_loss = 0
    while balance > 0:
        if balance - min_payment > 0:
            add = interest(balance, rate)
            new = new_balance(balance, add)
            after_pay = next_balance(new, min_payment)
            month += 1
            total_loss += add
            balance = after_pay
        elif balance - min_payment < 0:
            add = interest(balance, rate)
            new = new_balance(balance, add)
            total_loss += add
            balance = 0
        else:
            print('something went wrong')
    final = [new, total_loss, month]
    return final


def output(x):
    print('Final Balance: ' + str(x[0]))
    print('Interest lost: ' + str(x[1]))
    print('Months to until done: ' + str(x[2]))


def run_project(x, extra):
    out = []
    out_extra = []
    y = extra
    x = debts
    for debt in debts:
        out = project(debt)
        output(out)
    for debt in debts:
        out_extra = project(debt, y)
        output(out_extra)

run_project(debts, extra)

def comparison(x, y):
    interest_saved = x[1] - y[1]
    months_saved = x[2] - y[2]
    print('Interested saved: ' + str(interest_saved))
    print('Months saved: ' + str(months_saved))



    
