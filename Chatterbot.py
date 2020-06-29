from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat bot named Charlie
chatbot = ChatBot('FreeBirdsBot')

trainer = ListTrainer(chatbot)

trainer.train(['Hi','Hello','How are you?','I am fine and You?','Greate','What are you Doing?','nothing just roaming around.'])

while True:
	input_data = input("You- ")
	response = chatbot.get_response(input_data)
	print("FreeBirdsBot- ",response)

