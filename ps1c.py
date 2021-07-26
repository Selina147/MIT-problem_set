#ps_1c
annual_salary = int(input('Enter the starting salary: '))

def result(annual_salary,portion_saved):
    total_cost = 1000000
    portion_down_payment = 0.25
    down_payment = total_cost * portion_down_payment  #首付
    semi_annual_raise = 0.07
    r = 0.04
    current_savings = 0
    months = 0
    while months < 36:
        months += 1
        current_savings += annual_salary/12 * portion_saved + current_savings*r/12 
        if months % 6 == 0:
             annual_salary *= (1+semi_annual_raise)
        if current_savings >= down_payment - 100:
            return True
    return False

high = 10000
low = 0
mid = (high+low)/2
guess = 0
if result(annual_salary,high/10000) == False:
    print("It is not possible to pay the down payment in three years.")
else:
    while high - low > 1:
        guess += 1
        if result(annual_salary,mid/10000):
            high = mid 
        else:
            low = mid
    print("Best savings rate:%.4f" %(mid/10000))
    print("Steps in bisection search:",guess)
