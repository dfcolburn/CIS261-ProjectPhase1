#def calculate_tax_and_netpay(total_hours, hourly_rate, tax_rate):
tax = float(total_hours) * float(hourly_rate) * (float(tax_rate) / 100)
net_pay = float(total_hours) * float(hourly_rate) - tax
'return tax', net_pay

def GetEmpName():
    empname = input("Enter employee name: ")
    return empname
#for the next three functions, you need to convert the input to a float, e.g., varname = float(input('descripion of input:  '))
#write the GetHoursWorked function
def get_total_hours():
    total_hours = float(input("Enter total hours: "))
    return total_hours

#write the GetHourlyRate function
def get_hourly_rate():
    hourly_rate = float(input("Enter hourly rate: "))
    return hourly_rate


# write the GetTaxRate function
def get_tax_rate():
    tax_rate = float(input("Enter tax rate (in %): "))
    return tax_rate



def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

def printinfo(empname, hours, hourlyrate,grosspay, taxrate, incometax, netpay):
    print("Name:  ", empname) 
    print("Hours Worked: ", f"{hours:,.2f}")
    # write the lines of code to display hourlyrate, grosspay, taxrate, incometax and netpay with correct formatting
    # taxrate needs to be formatted as percentage
    print('hourlyrate:', f'{hourly_rate:,.2f}')
    print("Total gross pay:", f'{total_gross_pay:,.2f}')
    print("Total tax rate:", f'{total_tax_rate (in %):,.2f}')
    print("Total income tax:", f'{total_income_tax:,.2f}')
    print("Total net pay:",f'{ total_net_pay;,.2f}')
    print()

def PrintTotals(TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay):    
    print()
    print(f"Total Number Of Employees: {TotEmployees}")
    print(f"Total Hours Worked: {TotHours:,.2f}")
    # write the code to print  TotGrossPay, TotTax, and TotNetpay with 2 decimal places
    print(f'Total tax:", {total_tax:,.2f}')
    print(f'Total gross pay:", {total_gross_pay:,.2f}')
    print('Total net pay:", {total_net_pay:,.2f}')
    print()

def main():

 if __name__ == "__main__":
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    while True:
        empname = GetEmpName()
        if (empname.upper() == "END"):
            break
        # write the code to assign to hours the return value from GetHoursWorked
hrsWrkd = GetHoursWorked()     
TotHours += hrsWrkd 
return_hrsWrkd
      # write the code to assign to hourlyrate the return value from GetHourlyRate
        # write the code to assign to taxrate the return value from GetTaxRate
hrlyRate = GetHourlyRate()
return_hourlyrate
taxRate = GetTaxRate()
return_TaxRate
grosspay, incometax, netpay = CalcTaxAndNetPay(hrsWrkd, hrlyRate, taxRate)
printinfo(empName, hrsWrkd, hrlyRate, grosspay, taxRate, incometax, netpay)
        
        # write the code to increment the other total variables with the appropriate values
def printinfo(empName, hrsWrkd, hrlyRate, grosspay, taxRate, incometax, netpay):
    print(empname, f"{hrsWrkd:,.2f}",  f"{hrlyRate:,.2f}", f"{grosspay:,.2f}",  f"{taxRate:,.1%}",  f"{incometax:,.2f}",  f"{netpay:,.2f}")
        # update total
total_employees += 1
total_hours += hours
total_tax += tax
total_gross_pay += gross_pay
total_net_pay += net_pay
    # display total counts
display_total_info(total_employees, total_hours, total_tax, total_gross_pay, total_net_pay)

# import guard

if __name__ == "__main__":
    main()

 
PrintTotals (TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay)
   
 
