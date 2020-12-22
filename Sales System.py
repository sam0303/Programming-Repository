import numpy
while True:
    totalSale=0.00
    print ("""THIeve Sdn Bhd Sales System  
    ----Select Drink----
    [MT01] Signature Brown Sugar Milk Tea
    [WP01] Signature Blink Blink Pearl Tea
    [SM01] Smoothie with Pudding
    [CS01] ShakaLaka Berapi Coffee
    [Q]uit""")  #Printing as what stated in the question doct
    choice = input("Enter Choice [MT01/WP01/SM01/CS01/Q]:")  #Getting user input

    if (choice == "MT01"):
        name = "Signature Brown Sugar Milk Tea" #To be used later to display output to user
        numOfMonths = input("Enter number of months to record the sales : ") #number of months input
        numOfMonths = int(numOfMonths) #declaring variable as integer
        sales = [] #list to store the sales of each month
        for x in range(numOfMonths):    #for loop to store each month's sale and to find total sale. Each iteration is considered for a month
            print ("Enter number of cup sold for month ", x+1 , ":") #number of cups sold in the patricular month
            numOfCups = input () #getting input
            numOfCups = int(numOfCups) #declaring variable as int
            monSales = numOfCups * 6.50 #calculating sales for the months
            sales.append(monSales) #adding the value to the list
            totalSale = totalSale + monSales #adding up to totalsale

    elif (choice == "WP01"): #Refer to the comments in first 'if' condition...same rules applied to every other 'elif' conditions
        name = "Signature Blink Blink Pearl Tea"
        numOfMonths = input("Enter number of months to record the sales : ")
        numOfMonths = int(numOfMonths)
        sales = []
        for x in range(numOfMonths):
            print("Enter number of cup sold for month ", x + 1, ":")
            numOfCups = input()
            numOfCups = int(numOfCups)
            monSales = numOfCups * 7.05
            sales.append(monSales)
            totalSale = totalSale + monSales

    elif (choice == "SM01"): #Refer to the comments in first 'if' condition...same rules applied to every other 'elif' conditions
        name = "Smoothie with Pudding"
        numOfMonths = input("Enter number of months to record the sales : ")
        numOfMonths = int(numOfMonths)
        sales = []
        for x in range(numOfMonths):
            print("Enter number of cup sold for month ", x + 1, ":")
            numOfCups = input()
            numOfCups = int(numOfCups)
            monSales = numOfCups * 8.35
            sales.append(monSales)
            totalSale = totalSale + monSales

    elif (choice == "CS01"): #Refer to the comments in first 'if' condition...same rules applied to every other 'elif' conditions
        name = "ShakaLaka Berapi Coffee"
        numOfMonths = input("Enter number of months to record the sales : ")
        numOfMonths = int(numOfMonths)
        sales = []
        for x in range(numOfMonths):
            print("Enter number of cup sold for month ", x + 1, ":")
            numOfCups = input()
            numOfCups = int(numOfCups)
            monSales = numOfCups * 10.50
            sales.append(monSales)
            totalSale = totalSale + monSales

    elif (choice == "Q"): #in case Q was pressed, the total system exits
        exit()

    sales.sort() #once done with the for loop above, this command will sort the list in ascending order. Which means
    #the list's first index will be the smallest value and last index [-1] would be the largest.
    aveSales = totalSale/numOfMonths #finding average
    round(aveSales, 2) #rounding off average to two decimal points
    print("The biggest sales is RM ", round(sales[-1], 2)) #printing biggest value
    print("The smallest sales is RM ", round(sales[0], 2)) #printing smallest value
    print("Average sales from ", name, ", in " , numOfMonths , " months is: RM" , aveSales) #printing average value
    sales.clear() #clearing the elements in the list make it recycable.
    if input('If you wish to exit, Press Q. Or else press any other letter \n') == 'Q': #if user press any other key than Q, then
        #the system will repeat due to while loop command in line 1.
        break