from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import requests
app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
	msg = request.form.get('Body')
	headers = {
	'Connection': 'keep-alive',
	'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://www.tutorialspoint.com',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www.tutorialspoint.com/execute_python_online.php',
    'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8',
	}
	data = {
	'lang': 'python',
	'device': '',
	'code': msg,
	'stdinput': '',
	'ext': 'py',
	'compile': '0',
	'execute': 'python main.py',
	'mainfile': 'main.py',
	'uid': '8734933'
	}
	r = requests.post('https://tpcg.tutorialspoint.com/tpcg.php', headers=headers, data=data)
	txt = r.text
	resp = MessagingResponse()
	resp.message(txt)
	return str(resp)

if __name__ == "__main__":
    app.run(debug=True)




