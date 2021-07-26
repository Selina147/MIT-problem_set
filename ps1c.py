#ps_1c
annual_salary = float(input('Enter the starting salary: '))
total_cost = 1000000
portion_down_payment = 0.25
semi_annual_raise = 0.07
r = 0.04
current_savings = 0
months = 0
high = 10000
low = 0
mid = 5000
for portion_saved in range(low,high+1):
    while current_savings < total_cost *portion_down_payment and months < 36:
        if (months-1)>0 and (months-1) % 6 == 0:
            annual_salary *= (1+semi_annual_raise)
        months +=1 
        current_savings += annual_salary/12 * portion_saved + current_savings*r/12 