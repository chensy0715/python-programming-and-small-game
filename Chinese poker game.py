#!/usr/bin/python

#get the refer from other website

class Card:
	def __init__(self, suit_id, rank_id):
		self.rank_id = rank_id#rank是牌的符号，如“J”
		self.suit_id = suit_id#suit是牌的花色，如“红桃”
		 
		if self.rank_id == 1:                               
			self.rank = "A"                              
			self.value1 = 1#value是牌的值，比大小用的                                  
		elif self.rank_id == 2:                            
			self.rank = "4"                             
			self.value1 = 3                                
		elif self.rank_id == 3:                            
			self.rank = "6"                            
			self.value1 = 5                                
		elif self.rank_id == 4:                            
			self.rank = "8"                             
			self.value1 = 7                                
		elif self.rank_id == 5:                       
			self.rank = "9"               
			self.value1 = 9
		elif self.rank_id == 6:
			self.rank = "10"
			self.value1 = 11
		elif self.rank_id == 7:
			self.rank = "11"
			self.value1 = 13
		elif self.rank_id == 8:
			self.rank = "12"
			self.value1 = 15
		elif self.rank_id == 9:
			self.rank = "13"
			self.value1 = 17
		elif self.rank_id == 10:
			self.rank = "3"
			self.value1 = 19
		elif self.rank_id == 11:
			self.rank = "5"
			self.value1 = 21
		elif self.rank_id == 12:
			self.rank = "2"
			self.value1 = 23
		elif self.rank_id == 14:
			self.rank = "g"#g表示鬼，七鬼二五三的“鬼”
			self.value1 = 25
		elif self.rank_id == 13:
			self.rank = "7"
			self.value1 = 27
		else:
			self.rank = "RankError"                        
			self.value1 = -1                                
 
		if self.suit_id == 1:
			self.suit = "H"#H是黑桃——这是为了方便输入，将花色用拼音的首字母代替
			self.value2 = 0#颜色为黑色的value2都为0
		elif self.suit_id == 2:                            
			self.suit = "h"#h是红桃
			self.value2 = 1#颜色为红色的value2都为1
		elif self.suit_id == 3:                             
			self.suit = "m"#m是梅花
			self.value2 = 0
		elif self.suit_id == 4:                             
			self.suit = "f"#f是方片，以上普通牌的花色
			self.value2 = 1
		elif self.suit_id == 5:
			self.suit = "b"#b是黑色
			self.value2 = 0
		elif self.suit_id == 6:
			self.suit = "r"#r是红色，这两个是区分大小王的
			self.value2 = 1
		else:                                               
			self.suit = "SuitError"
			self.value2 = -1
						
		self.value = self.value1 + self.value2#牌的值=value1+value2，这也解释了为何我设定的value1都是奇数
		self.name = self.suit + self.rank#牌的称呼是花色加符号，如红桃K显示为“hK”


import random
from cards import Card
############################################################################################################################################
#函数：初始化
############################################################################################################################################
def init_cards():
	global deck, p_hand, c_hand, up_card, nc_kou, np_kou, c_kou, p_kou
	deck = []#此为待揭的牌
	nc_kou=np_kou=0#电脑和玩家的扣牌数
	c_kou=[]#电脑扣的牌
	p_kou=[]#玩家扣的牌
	for pear in range(2):#pear是“副”的意思，这里要用2副牌
		for suit in range(1, 5):#suit是“花色”的意思，扑克牌共有4种花色
			for rank in range(1, 14):#rank指牌的符号如“A”、“9”等
				next = Card(suit, rank)
				deck.append(next)
	deck.append(Card(5,14))
	deck.append(Card(6,14))#这两行是初始化比较特殊的大王和小王
 
	p_hand = []#此为玩家手中的牌
	for cards in range(0, 5):
		card = random.choice(deck)
		p_hand.append(card)
		deck.remove(card)
	 
	c_hand = []#此为电脑手中的牌    
	for cards in range(0, 5):
		card = random.choice(deck)
		c_hand.append(card)
		deck.remove(card)

#函数：轮到玩家

def player_turn():
	global deck, p_hand, p_blocked, up_card, over, p_kou, np_kou, card1, p_hand1, pkou,cpou, c_hand, nc_kou, p_first_play,win
	valid_play1 = False
	print "你手中的牌:",
	p_hand1 = p_hand[:]
	p_hand_sorted = []#这两行将玩家的牌按从大到小的顺序排序
 
	if Blocked:#Blocked为真则牌已被揭完，这种情况下玩家手中的牌会小于5张，因此排序时应特殊处理
		for i in range(1,6-p_blocked):
			card1 = p_hand1[0]
			for card in p_hand1:
				if card1.value < card.value:
					card1 = card
			p_hand_sorted.append(card1)
			p_hand1.remove(card1)
	else:    
		for i in range(1,6):
			card1 = p_hand1[0]
			for card in p_hand1:
				if card1.value < card.value:
					card1 = card
			p_hand_sorted.append(card1)
			p_hand1.remove(card1)
			 
	for card in p_hand_sorted:
		print card.name,#打印出玩家手中的牌
	if (p_hand_sorted[0].value==27 and p_hand_sorted[1].value==25 and p_hand_sorted[2].value==23 and p_hand_sorted[3].value==21 and p_hand_sorted[4].value==19)or(p_hand_sorted[0].value==28 and p_hand_sorted[1].value==26 and p_hand_sorted[2].value==24 and p_hand_sorted[3].value==22 and p_hand_sorted[4].value==20):
		over+=1
		win=1#判断是否为同颜色的七鬼二五三，若为真则本局结束，玩家获胜
	else:
		print "\n你想要做什么？",
		response1 = raw_input ("出牌还是扣牌？" )
		while not valid_play1:#valid是“合法”的意思，用while语句判断玩家的每次输入是否合法，若不合法则让玩家重新输入
			if response1=="出牌":
				pkou=False
				valid_play1=True
				response2=raw_input("请输入你要出的牌:")
				valid_play2=False
				while not valid_play2:
					selected_card1 = None
					while selected_card1 == None:
						for card in p_hand:
							if response2==card.name:
								selected_card1=card
						if selected_card1 == None:
							response2=raw_input("对不起，你手中没有这张牌，请重新输入:")
					if p_first_play==True:#若本局玩家第一个出牌，则不用和明牌比大小
						p_first_play=False
						valid_play2=True
						p_hand.remove(selected_card1)
						up_card=selected_card1
						print"你出了一张",selected_card1.name
						if len(deck)>0:
							card=random.choice(deck)
							p_hand.append(card)
							deck.remove(card)
							print"你揭到一张",card.name
						else:
							p_blocked+=1#p_blocked是牌揭完后轮到玩家的次数，通过这个可以知道玩家手中的牌数，是为了给玩家手中的牌排序用的
							if len(p_hand)==0:#玩家的牌出完了但电脑的牌还没出完，电脑只能将手中的牌全部扣掉
								for card in c_hand:
									c_kou.append(card)
									nc_kou=nc_kou+1
								over+=1
					else:#否则，玩家选择的牌必须大于明牌up_card（也就是电脑刚出的牌），才能出出去
						if ckou==True:#如果刚才电脑没有出牌而是扣了一张牌，则将明牌的值设为0
							up_card.value=0
						if selected_card1.value>up_card.value:
							valid_play2=True
							p_hand.remove(selected_card1)
							up_card=selected_card1
							print"你出了一张",selected_card1.name
							if len(deck)>0:#牌没被揭完
								card=random.choice(deck)
								p_hand.append(card)
								deck.remove(card)
								print"你揭到一张",card.name
							else:#牌已被揭完
								p_blocked+=1#此处与上面一样
								if len(p_hand)==0:
									for card in c_hand:
										c_kou.append(card)
										nc_kou=nc_kou+1
									over+=1
					if not valid_play2:
						response2=raw_input("对不起，你输入的牌没有对方出的牌大，请重新你输入:")
			elif response1=="扣牌":
				valid_play1=True
				pkou=True
				response3=raw_input("请输入要扣的牌:")
				valid_play3=False
				while not valid_play3:
					selected_card2=None
					while selected_card2==None:
						for card in p_hand:
							if response3==card.name:
								selected_card2=card
								valid_play3=True
						if selected_card2==None:
							response3=raw_input("对不起，你手中没有这张牌，请重新输入:")         
					p_hand.remove(selected_card2)
					np_kou=np_kou+1
					p_kou.append(selected_card2)
					print"你扣了一张",selected_card2.name
					if len(deck)>0:
						card=random.choice(deck)
						p_hand.append(card)
						deck.remove(card)
						print"你揭到一张",card.name
					else:
						p_blocked+=1
						if len(p_hand)==0:
							over+=1
					if not valid_play3:
						response3=raw_input("对不起，你的输入不合法，请重新你输入:")
			if not valid_play1:
				response1=raw_input("对不起，你的输入不合法，请重新你输入:")
			 

#函数：轮到电脑

def computer_turn():#与player_turn类似，只是不用判断输入是否合法，默认出比明牌大的最小的牌，扣最小的牌
	global c_hand, deck, up_card, over, c_blocked, c_kou, nc_kou, pkou,ckou, p_hand, np_kou,c_first_play
	suit_cards=[]
	ckou=False
	c_hand1 = c_hand[:]
	c_hand_sorted = []
 
	if Blocked:
		for i in range(1,6-c_blocked):
			card1 = c_hand1[0]
			for card in c_hand1:
				if card1.value < card.value:
					card1 = card
			c_hand_sorted.append(card1)
			c_hand1.remove(card1)
	else:    
		for i in range(1,6):
			card1 = c_hand1[0]
			for card in c_hand1:
				if card1.value < card.value:
					card1 = card
			c_hand_sorted.append(card1)
			c_hand1.remove(card1)
 
	if (c_hand_sorted[0].value==27 and c_hand_sorted[1].value==25 and c_hand_sorted[2].value==23 and c_hand_sorted[3].value==21 and c_hand_sorted[4].value==19)or(c_hand_sorted[0].value==28 and c_hand_sorted[1].value==26 and c_hand_sorted[2].value==24 and c_hand_sorted[3].value==22 and c_hand_sorted[4].value==20):
		over+=1
		win=2
	else:    
		if pkou==True or c_first_play==True:
			best_play = c_hand[0]
			for card in c_hand:
				if card.value < best_play.value:
					best_play = card
			c_hand.remove(best_play)
			up_card = best_play
			print "电脑出了一张", best_play.name
			if Blocked==True:
				nc_hand=0
				for card in c_hand:
					nc_hand=nc_hand+1
				print"电脑还剩下%i张牌"%nc_hand
			if len(deck) >0:
				next_card = random.choice(deck)
				c_hand.append(next_card)
				deck.remove(next_card)
			else:
				c_blocked+=1
				if len(c_hand)==0:
					for card in p_hand:
						p_kou.append(card)
						np_kou=np_kou+1
					over+=1
		else:     
			for card in c_hand:
				if card.value>up_card.value:
					suit_cards.append(card)
			if len(suit_cards) > 0:
				best_play = suit_cards[0]
				for card in suit_cards:
					if card.value < best_play.value:
						best_play = card
				c_hand.remove(best_play)
				up_card = best_play
				print "电脑出了一张", best_play.name
				if len(deck) >0:
					next_card = random.choice(deck)
					c_hand.append(next_card)
					deck.remove(next_card)
				else:
					c_blocked+=1
					if len(c_hand)==0:
						over+=1
			else:
				if len(c_hand)>0:
					selected_card=c_hand[0]
					for card in c_hand:
						if card.value<selected_card.value:
							selected_card=card
					c_hand.remove(selected_card)
					nc_kou=nc_kou+1
					c_kou.append(selected_card)
					print"电脑扣了一张牌"
					ckou=True
					if len(deck) >0:
						next_card = random.choice(deck)
						c_hand.append(next_card)
						deck.remove(next_card)
					else:
						c_blocked+=1
				else:
					print"电脑的牌出完了"
					over+=1
############################################################################################################################################
#主循环
############################################################################################################################################
done=False#done指的是整个游戏结束，退出程序
p_total=c_total=0#玩家和电脑的大比分
game_time=1#游戏局数
while not done:
	game_done=False#game_done指的是本局游戏结束
	c_blocked=0#牌揭完后轮到电脑的次数
	p_blocked=0#牌揭完后轮到玩家的次数
	Blocked=False#牌被揭完
	over=0#over>0时game_done
	win=0#此为关于集齐同种颜色的七鬼二五三获胜的判断，win==1时玩家胜，win==2时电脑胜
	init_cards()#初始化扑克牌
	n=random.randint(0,2)#随机确定谁第一个出牌
	if n==0:
		p_first_play=True
		c_first_play=False
	else:
		p_first_play=False
		c_first_play=True
	pkou=False
	ckou=False
	print"第%i局"%game_time
	while not game_done:
		if n==0:#此为玩家第一个出牌
			player_turn()
			if c_blocked+p_blocked >= 1:#判断牌是否揭完
				Blocked=True
			if over>=1:#判断本局是否结束
				game_done=True
			if not game_done:
				computer_turn()
				if c_blocked+p_blocked >= 1:
					Blocked=True
				if over>=1:
					game_done=True
		else:#此为电脑第一个出牌
			computer_turn()
			if c_blocked+p_blocked >= 1:
				Blocked=True
			if over>=1:
				game_done=True
			if not game_done:
				player_turn()
				if c_blocked+p_blocked>=1:
					Blocked=True
				if over>=1:
					game_done=True
		if Blocked:
			print"牌已经被揭完了"
		if game_done:
			game_time+=1
			if win==1:
				print"你因集齐了同花色的七鬼二五三而赢得了本局的胜利！"
				print"你扣了%i张牌，而电脑扣了%i张牌"%(np_kou,nc_kou)
				p_total+=1
			elif win==2:
				print"你输了！电脑因集齐了同花色的七鬼二五三而赢得了本局的胜利！"
				print"你扣了%i张牌，而电脑扣了%i张牌"%(np_kou,nc_kou)
				c_total+=1
			else:
				if np_kou<nc_kou:
					print"你赢了!"
					print"你扣了%i张牌，而电脑扣了%i张牌"%(np_kou,nc_kou)
					p_total+=1
				elif np_kou>nc_kou:
					print"你输了!"
					print"你扣了%i张牌，而电脑扣了%i张牌"%(np_kou,nc_kou)
					c_total+=1
				else:
					c_kou_p=p_kou_p=0
					for card in c_kou:
						c_kou_p+=card_value
					for card in p_kou:
						p_kou_p+=card_value
					if c_kou_p>p_kou_p:
						print"你赢了!"
						print"你和电脑都扣了%i张牌，但你扣的牌价值更小，所以你赢了。"%np_kou
						p_total+=1
					elif c_kou_p<p_kou_p:
						print"你输了!"
						print"你和电脑都扣了%i张牌，但电脑扣的牌价值更小，所以电脑赢了。"%np_kou
						c_total+=1
					else:
						print"你和电脑战平了!"
						print"千年一遇啊!你和电脑都扣了%i张牌，而且所扣的牌的价值也相等!但由于该游戏的程序设计者偏心人类，所以这一局算你赢了！"%nc_kou
						p_total+=1
	play_again=raw_input("再玩一局(Y/N)？")
	if play_again.lower().startswith('y'):#这句让你无论是输入“Y”还是“y”,甚至是“yes”都等价于“y”
		done=False
		print"到目前为止，你和电脑的比分为%i:%i"%(p_total,c_total)
	else:
		done=True
print"最终比分："
print"你","\t","电脑"
print p_total,"\t",c_total
 
"""变量名命名规律：除扣牌的“扣”字用的是拼音“kou”外，其余变量皆用英文，如电脑简称“c”,玩家简称“p”"""
