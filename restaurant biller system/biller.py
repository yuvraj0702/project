from menu import menu
from converter import csv_to_pdf
total = 0
choices = ["yes,no,y,n"]
def main():
    name = input("Enter custumer name:") 
    name2 = name +".pdf"
    
    name = (name + "_bill.csv").lower()

    if(name=='_bill.csv'):
        name = "bill.csv"
        name2 = "bill.pdf"
    
    name = name.capitalize()
    name2 = name2.capitalize()
  
    prices = []
    

    running = True
    with open(name,"w") as file:
        while running:
            try:
                item = input("Item:").upper()
                if(item == ''):
                    running = False
                    break
                price = menu[item]
                prices.append(price)
                file.write(item+','+str(price)+'\n')
            except:
                print("Invalid input")
        while True:
            try:
                percent = int(input("Discount percent:"))
                if(percent>100):
                    print("Enter valid percent number")
                else:
                    break
            except (TypeError,ValueError):
                print("Enter discount in number")

        total = sum(prices)
        total = round(discount(total,percent))
        file.write(f"\nDISCOUNT,{percent}%")

        file.write(f"\nTOTAL,{total}")

    csv_to_pdf(name,name2)
            
##finding total sum
def sum(prices):
    sum = 0
    for price in prices:
        sum = sum + price
    return sum

def discount(amount,percent):
    return amount * ((100-percent)/100)
    
main()




