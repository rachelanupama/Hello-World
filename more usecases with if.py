#bakery

'''cake =int( input('enter the cake price'))
if cake == 1200:
    print ("red velvet is available for 1200/-")
elif cake == 1000:
    print("almond cake is available for 1000/-")
elif cake == 800:
     print("butterscotch cake is available for 800/-")
else:
    print("not availabe")'''


#pizza house

print("""Welcome to pizza house! 
      1.  Crispy Chicken Pizza 
      2. Paneer Pizza
      3. Corn Pizza
      4. French Fries
      5. Chocolate cake and Ice cream""")
money = input("Enter the Item for the Price").lower()
if money == 'crispy chicken pizza' or money == 'crispy chicken':
    print("the cost of Crispy Chicken Pizza is 1000")
elif money == 'paneer pizza' or money == 'paneer':
    print("the cost of Paneer Pizza is 800")
elif money == 'corn pizza' or money == 'corn':
    print("the cost of Corn Pizza is 600")
elif money == 'french fries':
    print("the cost of French Fries is 300")
elif money == 'chocolate cake and ice cream':
    print("the cost of Chocolate cake and Ice cream is 200")
else:
    print("Not Available")









    
