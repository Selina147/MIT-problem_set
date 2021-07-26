#ps_1b
annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percentage of your salary to save, as a dicimal: '))
total_cost = float(input('Enter the cost of your dream house: '))
semi_annual_raise = float(input('Enter the semi raise, as a dicimal: '))
current_savings = 0
portion_down_payment = 0.25
r = 0.04
months = 0
#存款大于等于首付时买房
while current_savings < total_cost *portion_down_payment:
    if (months-1)>0 and (months-1) % 6 == 0:
        annual_salary *= (1+semi_annual_raise)
    current_savings += annual_salary/12 * portion_saved + current_savings*r/12 
    months +=1 
print('Number of months: ',months)