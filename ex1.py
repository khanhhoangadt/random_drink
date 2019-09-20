import random
questions = {
"strong": "Do ye like yer drinks strong?",
"salty": "Do ye like it with a salty tang?",
"bitter": "Are ye a lubber who likes it bitter?",
"sweet": "Would ye like a bit of sweetness with yer poison?",
"fruity": "Are ye one for a fruity finish?",
}
ingredients = {
"strong": ["glug of rum", "slug of whisky", "splash of gin"],
"salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
"bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
"sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
"fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

def random_drink():
    n = 0
    while(n == 0):
        print("Enter the taste :", questions.keys())

        input_taste = raw_input()

        if input_taste in ingredients:
            tastes = ingredients[input_taste]
            random_taste = random.randint(0,len(tastes))
            n += 1
            return(tastes[random_taste])
print(random_drink())