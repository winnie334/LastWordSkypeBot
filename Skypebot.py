from cleverwrap import CleverWrap
from skpy import Skype
import time, datetime


def checkfornewmessages(sk_instance, id, last_msg):
	new_msg, new_last_msg = None, None
	messages = sk_instance.chats[id].getMsgs()
	for message in messages:
		if message.userId != sk_instance.userId and message.time > last_msg:
			new_msg = message.content
			new_last_msg = message.time
	return new_msg, new_last_msg

if __name__ == '__main__':
	"""
	The general workflow of the program:
	-check every x seconds for new messages with skpy
	-if there are any, pass them to cleverbot
	-send the answer back
	"""

	timeout = 10		# time to wait between every message request
	contact = "cornelis.bleijenberg1"		# skype contact who thinks he can last-word you
	cleverbot = CleverWrap("CC3c4wQUshfBgb6iLEEjFe1xWhw")

	sk = Skype('winnie33_', input('password? '))
	id = sk.contacts[contact].chat.id
	last_msg = sk.chats[id].getMsgs()[0].time
	print('last messsage was ', last_msg)

	while True:
		new_message, newtime = checkfornewmessages(sk, id, last_msg)
		if new_message is not None:
			answer = cleverbot.say(new_message)
			sk.chats[id].sendMsg(answer)
			print('New message received! Answer: ' + answer)
			last_msg = newtime
		time.sleep(timeout)

