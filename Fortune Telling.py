import random


Fortune = ["You will find wild success as a musician", "You're gonna need a bigger boat", "Welcome to Jurassic Park", "PIZZA!", "I like penguins", "It's Morphin Time!", "Tyrannosaurus", "Cynthia", "Roy's our boy!", "Dragons are cool", "Pony", "Every villain is lemons", "Barnacles to the customer", "Bankai"," Marth", "Play Fire Emblem!", "Cherish your Waifus"]
Question = 'What is your question? '

def prompt_question(Question):
    response = raw_input(Question)
    print random.choice(Fortune)


prompt_question(Question)

