import requests, random
from user_agent import generate_user_agent
from keep_alive import  keep_alive
keep_alive()
tok = '7076927531:AAGR-mKglzPScwJbDnMuKTQEtMcBEWvtAtA'
id = '-1002144143134'
while True:
	rq = '0123456789'
	aa = 'qwertyuiopasdfghjklzxcvbnm'
	a = random.choice(aa)
	b = random.choice(aa)
	c = random.choice(aa)
	d = random.choice(rq)
	e = random.choice(rq)
	
	li = f'{a}{a}{b}{b}{c}'
	lii = f'{a}{b}{b}{c}{c}'
	liii = f'{a}{a}{b}{c}{c}'
	iiii = f'{a}{a}{b}{b}{c}'
	lu = f'{a}{a}{a}{c}{d}'
	luu = f'{a}{b}{c}{c}{c}'
	lui = [li,lii,lii,liii,iiii,lu,luu]
	h = random.choice(lui)
	#liii = f'{a}{a}{b}{b}{c}'
	#liiii = f'{a}{a}{b}{b}{c}'
	
	req = requests.post('https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/',headers ={'Host':'www.instagram.com',
'content-length':'85',
'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"',
'x-ig-app-id':'936619743392459',
'x-ig-www-claim':'0',
'sec-ch-ua-mobile':'?0',
'x-instagram-ajax':'81f3a3c9dfe2',
'content-type':'application/x-www-form-urlencoded',
'accept':'*/*',
'x-requested-with':'XMLHttpRequest',
'x-asbd-id':'198387',
'user-agent':generate_user_agent(),
'x-csrftoken':'jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv',
'sec-ch-ua-platform':'"Linux"',
'origin':'https://www.instagram.com',
'sec-fetch-site':'same-origin',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://www.instagram.com/accounts/emailsignup/',
'accept-encoding':'gzip, deflate, br',
'accept-language':'en-IQ,en;q=0.9',
'cookie':'csrftoken=jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv',
'cookie':'mid=YtsQ1gABAAEszHB5wT9VqccwQIUL',
'cookie':'ig_did=227CCCC2-3675-4A04-8DA5-BA3195B46425',
'cookie':'ig_nrcb=1'},data=f'email=aakmnnsjskksmsnsn%40gmail.com&username={h}&first_name=&opt_into_one_tap=false')
	if '{"message":"feedback_required","spam":true,"feedback_title":"Try Again Later","feedback_message":"We limit how often you can do certain things on Instagram to protect our community. Tell us if you think we made a mistake.","feedback_url":"repute/report_problem/scraping/","feedback_appeal_label":"Tell us","feedback_ignore_label":"OK","feedback_action":"report_problem","status":"fail"}' in req.text:
	        print('⛔ USER IS BAND : '+h)
	elif  '"errors": {"username":' in req.text or  '"code": "username_is_taken"' in req.text:
	        print('❌ USER IS UNVALID : '+h)
	        requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={id}&text=❌ USER IS UNVALID : {h}')
	else:
             print('✅ USER IS VALID : '+h)
             dmj = f'"= = = = = = = = = = = = = = = = = = = =\n ㅤ\n يوزر من عمك علاوي 😂 : @{h}\n ㅤ\n= = = = = = = = = = = = = = = = = = = =\n@rKKuu / @AboMlakk .'
             
             requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={id}&text=				تم صيد يوزر جديد : @{h} \n@j_tja | @AboMlakk ,')
