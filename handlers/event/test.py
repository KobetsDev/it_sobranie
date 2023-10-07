from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat bot named Charlie
chatbot = ChatBot('Charlie')

trainer = ListTrainer(chatbot)

trainer.train([
    'Привет!',
    'Давно тебя не видел, как ты?',
    'Давай поговорим'
])

# Get a response to the input text 'I would like to book a flight.'
response = chatbot.get_response('Давно тебя не видел, как ты?')

print(response)
