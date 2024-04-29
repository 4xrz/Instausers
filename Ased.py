import telebot
from telebot import *
from kvsqlite.sync import Client
from a4a import *
from time import sleep
from keep_alive import  keep_alive
keep_alive()

i = Client('oao.hex')
k = 'oao'
get = i.get(k)

bot = telebot.TeleBot('7076927531:AAGR-mKglzPScwJbDnMuKTQEtMcBEWvtAtA')


jk = types.InlineKeyboardMarkup(row_width=3)
ss = types.InlineKeyboardButton(text='بدأ الصيد ✓',callback_data='ss')
ob = types.InlineKeyboardButton(text='ايقاف البوت',callback_data='ob')

#hh = types.InlineKeyboardMarkup(row_width=3)
sb = types.InlineKeyboardButton(text='تشغيل البوت',callback_data='sb')
jk.add(sb)
jk.add(ob)
jk.add(ss)
#hh.add(sb)

@bot.message_handler(func=lambda m:m.text in ['ستارت'])
def start(m):
	print(get)
	bot.send_message(m.chat.id,'مرحبا بك عزيزي المالك، هذه الازرار و استخدمهن يروحي ،',reply_markup=jk)
		
@bot.callback_query_handler(func=lambda c:True)
def cl(c):
	data =c.data
	ci = c.message.chat.id
	if data == 'ss':
		print('done')
		iu = bot.send_message(c.message.chat.id,text='تم بدأ الصيد')
		bot.register_next_step_handler(iu,sts)
		
	if data=='ob':
			i.set(k,False)
			bot.send_message(ci,text='تم ايقاف البوت ')
			print('stop')
	if data =='sb':
			i.set(k,True)
			print(f'f {get}')
			bot.send_message(ci,'تم تشغيل البوت ✓ ،')
	
@bot.message_handler(func=lambda m:False)
def sts(m):
			
			#asi.add(oob)
			ii = bot.send_message(m.chat.id,text='انجب؟')
			while True:
				rq = '0123456789'
				aa = 'qwertyuiopasdfghjklzxcvbnm'
				aaa = '0123456789qwertyuiopasdfghjklzxcvbnm'
				a = random.choice(aa)
				b = random.choice(aa)
				c = random.choice(aa)
				d = random.choice(aa)
				e = random.choice(aaa)
				f = random.choice(aaa)
				g = random.choice(rq)
				h = random.choice(rq)
				i = random.choice(rq)
				j = random.choice(rq)
				li = f'{a}{a}{b}{b}{c}'
				lii = f'{a}{b}{b}{c}{c}'
				liii = f'{a}{a}{b}{c}{c}'
				liiii = f'{a}{a}{b}{b}{c}'
				lu = f'{a}{a}{a}{c}{d}'
				luu = f'{a}{b}{c}{c}{c}'
				lpp = f'{a}.{f}.{e}' 
				lppp = f'{a}.{f}_{e}'
				lpppp = f'{a}_{f}_{e}'  
				loi = f'{a}_{f}.{e}'
				lis = [li,lii,liii,liiii,lu,luu,lpp,lppp,lpppp,loi]
				kkl = random.choice(lis)
				h = check_insta_users(kkl)
				
				if h['Status'] =='available':
					h8 = f'''
				تم صيد يوزر جديد : `{kkl}` \n@j_tja | @AboMlakk ,
				'''
					bot.send_message(m.chat.id,text=f'				تم صيد يوزر جديد : @{kkl} \n@j_tja | @AboMlakk ,')
				else:
					fail = f'''
				غير متاح {kkl} ❌
				'''
				#h = bot.send_message(m.chat.id,text='انجب؟')
				asi = types.InlineKeyboardMarkup(row_width=3)
				oob = types.InlineKeyboardButton(text=f'غير متاح : {kkl} ❌',callback_data='uub')
				asi.add(oob)
				sleep(2)
				bot.edit_message_reply_markup(chat_id=ii.chat.id, message_id=ii.message_id,reply_markup=asi)
			
			'''
	if data =='sb' and get==True:
			bot.send_message(ci,'تم تشغيل البوت ✓ ،')
			i.delete(k)
			i.set(k,True)
			print(f'f {get}')'''
			#@j_tja 
bot.infinity_polling()		
