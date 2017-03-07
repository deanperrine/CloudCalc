
def main():
    print('========================================================')
    print('Cloud Storage Ramp-up Cost & Time-to-Transfer Calculator')
    print('========================================================')
    archive_total = float(input('Please enter the total storage to transfer (GB, e.g. "10000"): '))
    transfer_rate = float(input('Please enter the expected transfer rate (Gbps, e.g."1"): '))
    cloud_stor_cost = float(input('Please enter the destination cloud storage cost' \
                                  '\n(Do not include the "$" sign, e.g. enter: "0.007" for $0.007 per GB): '))
    days_to_transfer = ((((archive_total*8/transfer_rate)/60)/60)/24)
    months_to_transfer = days_to_transfer/30
    years_to_transfer = months_to_transfer/12
    print('Days to transfer: ', format(days_to_transfer, ',.2f'))
    print('Months to transfer: ', format(months_to_transfer, ',.2f'))
    print('Years to transfer: ', format(years_to_transfer, ',.2f'))
    xfer_per_day = archive_total/days_to_transfer
    day_cost = xfer_per_day * cloud_stor_cost / 30
    days = 365
    total_days = 0
    cost_sum = 0
    b = xfer_per_day * cloud_stor_cost / 30
    total_years = 1
    total_sum = 0.0
    while total_years < years_to_transfer + 1:
        b, total_cost = year_calc(day_cost, days, total_days,cost_sum,b,total_years)
        total_sum += total_cost
        total_years += 1
    print('Sum of years: $',format(total_sum, ',.2f'))
    print('Final Monthly Total $',format(archive_total * cloud_stor_cost, ',.2f'))
    print('Final Annual Total $',format(archive_total * cloud_stor_cost * 12, ',.2f'))
def year_calc(day_cost,days,total_days,cost_sum,b,total_years):
    while total_days < days -1:
        b += day_cost
        cost_sum += b
        total_days += 1
    total_cost = cost_sum + day_cost
    print('Year',total_years,'cost: $', format(cost_sum + day_cost, ',.2f'))
    return (b, total_cost)
main()