# import random

# customers = ['Jimmy', 'John', 'Stacie']

# winner = random.choice(customers)

# flavor = 'vanilla '

# print('Congratulations ' + winner + ' you have won an ice cream sundae.')

# prompt = ' Would you like a cherry on top? '
 
# wants_cherry = input(prompt)

# order = flavor + 'sundae'

# if (wants_cherry.lower() == 'yes'):
#     order = order + ' with cherry on top'

# print('One ' + order + ' for ' + winner  + ' coming right up... ')

#EXERCISE 2

#Let Python know we'll be using somne random functionality by importing the random module.
import random

#Make three lists one of verbs one of adjectives and one of nouns
verbs = ['Leverage', 'Sync', 'Target','Gamify', 'Offline', 'Crowd-sourced', '24/7', 'Lean-in', '30,000']

adjectives = ['A/B Tested', 'Freemium', 'Hyperlocal','Siloed', 'B-to-B', 'Oriented', 'Cloud Based', 'API based']

nouns = ['Early Adopter', 'Low hanging Fruit', 'Pipe-line', 'Splash Page', 'Productivity','Process', 'Tipping Point', 'Paradigm']

# Choose one verb, adjective and noun from each list
verb = random.choice(verbs)
adjective = random.choice(adjectives)
noun = random.choice(nouns)

# Now build out the phrase by adding the words together
phrase = verb + ' ' + adjective + ' ' + noun

# Output the phrasep
print('')
print(phrase)
print('')