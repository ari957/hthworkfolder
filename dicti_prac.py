
# the_of_is_(the grocery price of chicken is 1.99)
grocery_list = {
  "chicken": 1.59, 
  "beef": 1.99,
  "cheese": 1,
  "milk": 2.5,
}
 

family_pet_names = {"Nebula": 2, "Snowy": 7, "Zuko": 1, "Canelo": 1}
 
shoe_names = {"Jordan 13": 1,"Yeezy": 8, "Foamposite": 10, "Air Max": 5, "SB Dunk": 20}

def total_price ( item1, item2 ):
  price1 = grocery_list[item1]
  price2 = grocery_list[item2]
  total = price1 +price2

  return total

def price_difference( item1, item2 ):
  price1 = grocery_list[item1]
  price2 = grocery_list[item2]
  price_difference = abs(price1 - price2)

  return price_difference

print( price_difference ( "beef", "cheese") )








