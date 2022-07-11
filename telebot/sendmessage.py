import requests
from .models import TeleSettings

def sendTelegram(tg_name, tg_phone):
	settings = TeleSettings.objects.get()
	token = str(settings.tg_token)
	chat_id = str(settings.tg_chat_id)
	text = str(settings.tg_message)
	api = 'https://api.telegram.org/bot'
	method = api + token + '/sendMessage'

	a = text.find('{')
	b = text.find('}')
	c = text.rfind('{')
	d = text.rfind('}')

	part_one = text[0:a]
	part_two = text[b+1:c]
	part_three = text[d:-1]
	text_slice = part_one + tg_name + part_two + tg_phone + part_three

	req = requests.post(method, data={
		'chat_id': chat_id,
		'text': text_slice
		})
