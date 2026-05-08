#library for chatterbot 
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
#Loading Structured training data from files 
from chatterbot.trainers import JsonFileTrainer

chatbot = ChatBot("Chatpot")

trainer = JsonFileTrainer(chatbot)
trainer.train("./data/conversations.json")

#Training for chatbot
trainer = ListTrainer(chatbot)
trainer.train([
    "Hi",
    "Welcome, friend!",
])
trainer.train([
    "Are you a plant?",
    "No, I'm the pot below the plant!"
])

exit_conditions = (":q", "quit", "exit")
while True: 
    query = input("> ")
    if query in exit_conditions: 
        break
    else: 
        print(f"{chatbot.get_response(query)}")
