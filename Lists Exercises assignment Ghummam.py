Fruits=("Orange","Watermelon","Mango","Banana","Avacado")
print(Fruits)
colours=["red","blue","green","yellow","purple"]
print(colours[0])
print(colours[2])
print(colours[-1])
numbers=[10,20,30,40,50]
numbers[1]=25
numbers.append(60)
print(numbers)
names=["Alice","Bob","Charlie","David","Emma"]
subset=names[:3]
print(subset)
num=2
for i in range(1,11):
    print(i**num)
shopping_cart=[]
shopping_cart.append("milk")
shopping_cart.append("bread")
shopping_cart.append("egg")
shopping_cart.extend(["butter","cheese"])
print(shopping_cart)
numbers=[45,22,88,56,92,33]
max_value=max(numbers)
min_value=min(numbers)
print("maximum value:",max_value)
print("minimum value:",min_value)
letters=["a","b","a","c","b","a","d"]
count_a=letters.count("a")
print("the letter 'a' appears",count_a,"times." )
square_of_evens=[x**2 for x in range(11)if x%2==0]
print(square_of_evens)
numbers=[1,2,2,3,4,4,5,6,6,7]
unique_numbers=list(set(numbers))
print(unique_numbers)