


def GetEmpName():
    empname = input("Enter employee name: ")
    return empname
#for the next three functions, you need to convert the input to a float, e.g., varname = float(input('descripion of input:  '))
#write the GetHoursWorked 
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
    print(f"hourly Rate: ', {houly_rate},.2f")
    print(f"Total gross pay: {TotGrossPay},.2f")
    print(f"Total tax rate: {TotTaxRate},.2f") 
    print(f"Totalincome tax: {TotIncomeTax},.2f")
    print(f"Total net pay: {TotNetpay},.2f")
    print()
def PrintTotals(TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay):    
    print()
    print(f"Total Number Of Employees: {TotEmployees}")
    print(f"Total Hours Worked: {TotHours:,.2f}")
    # write the code to print  TotGrossPay, TotTax, and TotNetpay with 2 decimal places
    print("Total Gross pay:, {TotalGrossPay:,.2f}")
    print("Total tax:, {TotalTax:,.2f}")
    print("Total Net pay:, {TotNetPfay:,.2}")
    print()
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
         # write the code to assign to hourlyrate the return value from GetHourlyRate
        hours = GetHoursWorked()
        hourlyrate = Gethourlyrate()
       #write the code to assign to taxrate the return value from GetTaxRate
        taxrate = GetTaxRate()
        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        printinfo(empname,hours, hourlyrate, grosspay, taxrate, incometax, netpay)

        TotEmployees += 1
        TotHours += hours
        # write the code to increment the other total variables with the appropriate values
        HourlyRate += hourlyrate
        GrossPay += grosspay
        TaxRate += taxrate
        IncomeTax += incometax
        NetPay += netpay
        display_total_info(total_employees, total_hours, total_tax, total_gross_pay, total_net_pay)
        print()
 


PrintTotals (TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay)
print()



