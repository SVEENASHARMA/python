pies = 'p'

print("Welcome to the House of Pies! Here are our pies:")

List_of_pies= ["Pecan","Apple Crisp","Bean","Banoffee","Black Bun","Blueberry","Buko","Burek","Tamale","Steak",]

purchased_pies = [0,0,0,0,0,0,0,0,0,0]

while pies == "p":

    
    print("---------------------------------------------------------------------")
    print("(1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee, (5) Black Bun, (6) Blueberry, (7) Buko, (8) Burek, (9) Tamale, (10) Steak ")

    order = input("Which pie would you like? ")

    purchased_pies[int(order)-1] = purchased_pies[int(order)-1]+1
    
    print("---------------------------------------------------------------------")
    
    print("Great! We will have that " + List_of_pies[int(order)-1] + " right out for you! ")
    
    pies = input("Would you like to make another purchase: (y)es or (n)o? ")

    print("---------------------------------------------------------------------")

print("Thank you for shopping with us today! You purchased: ")

for pie_index in range(len(List_of_pies)):
    
    print(str(purchased_pies[pie_index]) + " " + str(List_of_pies[pie_index]))
    
    