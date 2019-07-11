# =============================================================================
# def remBalanceIter(balance, annualInterestRate, monthlyPaymentRate):
#     
#     i = 12
#     
#     while i > 0:
#         
#         minPayment = balance*monthlyPaymentRate
#         ub = balance - minPayment
#         interest = (annualInterestRate/12)*ub
#         
#         balance = ub + interest
#         i -= 1
#         
#     return print('Remaining balance: {}'.format(round(balance, 2)))
# 
# 
# def remBal(balance, annualInterestRate, monthlyPaymentRate):
#     balance *= ((1 - monthlyPaymentRate) * (1 + annualInterestRate/12))**12
#     return round(balance, 2)
# 
# 
# =============================================================================

balance = 320000
annualInterestRate = .2

init_balance = balance
monthlyInterestRate = annualInterestRate/12.0

lb = init_balance/12.0
ub = (init_balance * (1 + monthlyInterestRate)**12)/12.0
epsilon = 0.1

while True:
    guess = (lb+ub)/2
    for i in range(12):
        balance = (balance - guess) + (monthlyInterestRate*(balance - guess))
    if balance > epsilon:
        lb = guess
    elif balance < - epsilon:
        ub = guess
    else:
        break
    balance = init_balance
    
    
print('Lowest Payment: {}'.format(round(guess,2)))