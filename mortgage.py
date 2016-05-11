from __future__ import with_statement
import datetime
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def get_monthly_payment(bal,months,coupon):
    ratio = (1+coupon) ** months
    return bal*coupon*ratio/(ratio-1)
bal = 420000
base = 10000# monthly base salary
total_30  = get_monthly_payment(bal,360,0.0375/12) * 360
total_15 = get_monthly_payment(bal,180,0.0315/12) * 180
total = 0
month_pay = get_monthly_payment(bal,360,0.0375/12)
remaining_balance_30 = []
remaining_balance_15 = []
for i in range(360):
    interest = bal * 0.0375/12
    p = month_pay - interest
    bal = bal - p
    if (i+1) %12 ==0:
        remaining_balance_30.append(bal)
bal = 420000
month_pay = get_monthly_payment(bal,180,0.0315/12)
for i in range(180):
    interest = bal * 0.0315/12
    p = month_pay - interest
    bal = bal - p
    if (i+1) %12 ==0:
        remaining_balance_15.append(bal)
for i in range(15):
    remaining_balance_15.append(-month_pay*(i+1)*12)
fvs = []
market_gain  = []
figure= plt.figure()
ax = figure.add_subplot(111)
print '------',remaining_balance_30[15]
for index,rate in enumerate([0.02,0.03,0.04,0.05,0.06]):
    fvs = []
    market_gain =[]
    for i in range(1,16):
        total = 0
        for j in range(1,i+1):
            fv = 13000 * (1+rate)**j
            total += fv
#        print i,total,remaining_balance_30[i-1] -(remaining_balance_15[i-1] if i < 15 else 0)
        fvs.append(total)
        market_gain.append(remaining_balance_30[i-1] -(remaining_balance_15[i-1] ))
    new_fvs = []
    for i in range(16,30):
        total -= 1945 * 12
        total = (1+rate) * total if total >0 else total
        print total,i
        new_fvs.append(total+560000-remaining_balance_30[i-1])
        market_gain.append(560000)
    print new_fvs
    ax.plot(range(16,30),new_fvs,color=['red','blue','black','yellow','pink'][index],label='hold money %s'%rate)
ax.plot(range(1,30),market_gain,color='green',label='house money')
#ax.plot(range(1,31),remaining_balance_30,color='green',label='30 re bal')
#ax.plot(range(1,16),remaining_balance_15,color='green',label='15 re bal')

ax.legend(loc=2)
plt.savefig('/h/wjiang/public_html/mortgage.png')

