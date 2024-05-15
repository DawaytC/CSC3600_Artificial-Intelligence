#213748
#DWIGHT CUTAD

# Define the rules using lambda functions
rules = [
    # Rule 1: If the user likes action and adventure movies,
    # recommend a superhero movie
    {'condition': lambda facts: facts['likes action'] and facts['likes adventure'],
     'recommendation': 'Superhero movie'},

    # Rule 2: If the user likes drama and romance movies,
    # recommend a romantic drama movie
    {'condition': lambda facts: facts['likes drama'] and facts['likes romance'],
     'recommendation': 'Romantic drama movie'},

    # Rule 3: If the user likes comedy and animation movies,
    # recommend an animated comedy movie
    {'condition': lambda facts: facts['likes comedy'] and facts['likes animation'],
     'recommendation': 'Animated comedy movie'},

    # Rule 4: If the user likes scary and drama movies,
    # recommend a horror movie
    {'condition': lambda facts: facts['likes scary'] and facts['likes drama'],
     'recommendation': 'Horror movie'},

    # Rule 5: If the user likes crime and suspense movies,
    # recommend a thriller movie
    {'condition': lambda facts: facts['likes crime'] and facts['likes suspense'],
     'recommendation': 'Thriller movie'},
]

# Define the initial facts
facts = {
    'likes action': True,
    'likes adventure': False,
    'likes drama': True,
    'likes romance': True,
    'likes comedy': False,
    'likes animation': True,
    'likes scary': True,
    'likes crime': True,
    'likes suspense': False,
}

# Apply the rules to the facts
recommendations = [rule['recommendation'] for rule in rules if rule['condition'](facts)]

# Print the recommendations
if recommendations:
    print("Recommendations based on your preferences:")
    for index, item in enumerate(recommendations, start=1):
        print(f"{index}. {item}")
else:
    print("No recommendations available based on your preferences.")