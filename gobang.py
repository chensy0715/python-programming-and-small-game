#!/usr/bin/python

from Tkinter import *
from tkMessageBox import *
class Game:
	def __init__(self):
		self.A=[]
		self.B=[]
		self.record=set()
		self.recor=set()
		self.rec=self.record|self.recor
		self.root=Tk()
		self.root.geometry("180x250")
		self.root.title("Wu Zi Qi Game")
		self.r=Canvas(self.root,width=180,height=210,bg="purple")
		pic=PhotoImage(file="beijing.gif")
		self.r.create_image(90,100,image=pic)
		self.r.place(x=0,y=15)
		Label(self.root,text="***Wu Zi Qi Game***",fg="red").place(x=20,y=0)
		Button(self.root,text="start",command=self.start).place(x=30,y=230)
		Button(self.root,text="quit ",command=self.root.destroy).place(x=100,y=230)
		self.r.mainloop()

	def start(self):
		self.root.destroy()
		self.top=Tk()
		self.top.title("Game Start")
		self.c=Canvas(self.top,width=480,height=480,bg="white")
		self.c.pack()
		self.c.create_rectangle(25,25,455,455,fill="gray")
		for i in range(30,451,30):
			for j in range(30,451,30):
				self.c.create_oval(i-2,j-2,i+2,j+2,fill="blue")
		for i in range(1,16):
			self.c.create_line(30,30*i,450,30*i)
			self.c.create_line(30*i,30,30*i,450)
		self.c.create_oval(234,234,246,246,fill="black")
		self.c.create_oval(115,115,125,125,fill="black")
		self.c.create_oval(355,115,365,125,fill="black")
		self.c.create_oval(115,355,125,365,fill="black")
		self.c.create_oval(355,355,365,365,fill="black")
		self.c.bind("<Button-1>",self.callback1)
		self.c.bind("<Button-3>",self.callback2)
		self.c.mainloop()     
	
	def callback1(self,event):
		u,v=event.x,event.y
		
		s=u/15
		if s%2==1:
			self.x=(s+1)/2
		else:
			self.x=s/2

		l=v/15
		if l%2==1:
			self.y=(l+1)/2
		else:
			self.y=l/2
		g=(self.y-1)*15+self.x
		while g not in self.rec:
			self.c.create_oval(self.x*30-12,self.y*30-12,self.x*30+12,self.y*30+12,fill="black")
			self.A.append(g)
			self.record=set(self.A)
			self.rec=self.record|self.recor
			judge=panduan(g,self.record)
			if judge==1:
				answer=showinfo("Game over","Black wins!")
				self.top.destroy()
				
	def callback2(self,event):
		u,v=event.x,event.y
		
		s=u/15
		if s%2==1:
			self.m=(s+1)/2
		else:
			self.m=s/2

		l=v/15
		if l%2==1:
			self.n=(l+1)/2
		else:
			self.n=l/2
		
		k=(self.n-1)*15+self.m
		while k not in self.rec:
			self.c.create_oval(self.m*30-12,self.n*30-12,self.m*30+12,self.n*30+12,fill="white")
			self.B.append(k)
			self.recor=set(self.B)
			self.rec=self.record|self.recor
			judge=panduan(k,self.recor)
			if judge==1:
				answer=showinfo("Game over","White wins!")
				self.top.destroy()
				
		   
def panduan(g,record):
	#判断横排是否出现赢的情况
	if {g-4,g-3,g-2,g-1}<=record:
		return 1
	elif {g-3,g-2,g-1,g+1}<=record:
		return 1
	elif {g-2,g-1,g+1,g+2}<=record:
		return 1        
	elif {g-1,g+1,g+2,g+3}<=record:
		return 1        
	elif {g+1,g+2,g+3,g+4}<=record:
		return 1       
	#判断竖列是否出现赢的情况
	elif {g-60,g-45,g-30,g-15}<=record:
		return 1        
	elif {g-45,g-30,g-15,g+15}<=record:
		return 1        
	elif {g-30,g-15,g+15,g+30}<=record:
		return 1        
	elif {g-15,g+15,g+30,g+45}<=record:
		return 1        
	elif {g+15,g+30,g+45,g+60}<=record:
		return 1
	#判断\列是否出现赢的情况
	elif {g-16,g-32,g-48,g-64}<=record:
		return 1        
	elif {g-48,g-32,g-16,g+16}<=record:
		return 1        
	elif {g-32,g-16,g+16,g+32}<=record:
		return 1                
	elif {g-16,g+16,g+32,g+48}<=record:
		return 1        
	elif {g+16,g+32,g+48,g+60}<=record:
		return 1
	#判断/列是否出现赢的情况
	elif {g-14,g-28,g-42,g-56}<=record:
		return 1        
	elif {g-14,g-28,g-42,g+14}<=record:
		return 1
	elif {g-14,g-28,g+14,g+28}<=record:
		return 1
	elif {g-14,g+14,g+28,g+42}<=record:
		return 1
	elif {g+14,g+28,g+42,g+56}<=record:
		return 1
	else:
		return 0
	  
def main():
	print "欢迎来到五子棋战场！黑方用左键，白方用右键，谁先下都可以，落子无悔，不要在棋盘周围空地点击。Are you ready?"
	game=Game()
main()

