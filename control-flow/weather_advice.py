# Ask the user for the weather
weather = input("What's the weather like today? (sunny/rainy/cold): ")

# Check the weather and give advice
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a jacket and warm clothes.")
else:
    print("Sorry, I don't understand that weather type.")
