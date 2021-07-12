from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat bot named Charlie
train_data=['Hi','Hello','How are you?','I am fine and You?','Greate','What are you Doing?','nothing just roaming around.']
check_point=input('Do you want to add some more data to training dataset(yes\\no): ')
if check_point=='yes':
	take_data=True
	print('Enter stop in question to stop adding traning data')
	while take_data == True:
            q=input('Please Enter your Question : ')
            if q == 'stop':
                take_data=False
            else:
                a=input('Please Enter FreeBirdsBot reply of this question : ')
                train_data.append(q)
                train_data.append(a)


chatbot = ChatBot('FreeBirdsBot')
trainer = ListTrainer(chatbot)
trainer.train(train_data)

while True:
	input_data = input("You- ")
	if  'bye' in input_data :
		print('Bye Sir have a great day!')
		break
	else:
		response = chatbot.get_response(input_data)
		print("FreeBirdsBot- ",response)

