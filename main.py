from kivy.app import App
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner,SpinnerOption
from kivy.uix.popup import Popup
from kivy.core.text import LabelBase
from random import random
from plyer import accelerometer
from time import sleep,time
from os import walk


layout=RelativeLayout()
LabelBase.register(name='院审',fn_regular='font.ttf')
sllh=30
amns=0
tran=('杉森雅和 - 成歩堂龍一 ～異議あり  2001',
'杉森雅和 - 追求 ～追いつめられて／バリエーション',
'杉森雅和 - 追求 ～追いつめられて',
'岩垂徳行 - 成歩堂龍一 ～異議あり  2004',
'木村明美 - 追求 ～問いつめたくて',
'岩垂徳行 - 追求 ～とっつかまえて／バリエーション',
'山田靖子 - 追究 ～つきつめたくて',
'Objection-Funk',
'英国法廷組曲 追求 ~追いつめられて',
'北川保昌 - 追求 ~大逆転のとき')

class app(App):
	def build(self):
		accelerometer.enable()
		self.amns=Image(source='objection.png',pos_hint={'x':0,'center_y':0.5},size_hint_y=1,allow_stretch=True,keep_ratio=True)
		self.cnm=SoundLoader.load('objection.ogg')
		self.cnm.bind(on_stop=self.a)
		self.bgms={'None':None,**{x:None for x in tran}}
		self.bgm=None
		self.choose_bgm=Spinner(text='None',values=self.bgms.keys(),font_name='院审',size_hint=(1,0.1),pos_hint={'y':0.9},option_cls=O)
		self.choose_bgm.bind(text=self.choose)
		Window.rotation=-90
		Window.allow_screensaver=False
		Clock.schedule_interval(self.update,1/30)
		a=Button(text='把思维逆转过来!',font_size=layout.size[1],background_color=(0,0,0),font_name='院审')
		a.bind(on_press=self.objection)
		layout.add_widget(a)
		self.b=TextInput(hint_text='请输入灵敏度',text='30',size_hint=(0.28,0.1),pos_hint={'center_x':0.34,'y':0.3},font_size=a.font_size/2,font_name='院审')
		layout.add_widget(self.b)
		h=Button(text='?',size_hint=(0.05,0.1),pos_hint={'x':0.43,'y':0.3},background_color=(0,0,0,0.2),color=(0,0,0),font_name='院审',font_size=a.font_size/2)
		p=Popup(title='参数参考',title_font='院审',content=Label(font_name='院审',text='10:置于桌上,拍案激活\n30~50:手持甩动激活'),size_hint=(0.4,0.4))
		h.bind(on_press=lambda i:p.open())
		layout.add_widget(h)
		self.c=TextInput(hint_text='请输入延时',size_hint=(0.28,0.1),pos_hint={'center_x':0.66,'y':0.3},font_size=a.font_size/2,font_name='院审')
		layout.add_widget(self.c)
		layout.add_widget(self.choose_bgm)
		self.st=0
		return layout
	def objection(self,a):
		Window.rotation*=-1
	def a(self,instance):
		layout.remove_widget(self.amns)
		if self.bgm:
			if self.bgm.state!='play':
				self.bgm.play()
	def update(self,dt):
		try:
			sllh=int(self.b.text)
		except:
			sllh=10
			if not self.b.focus:
				self.b.text=''
		try:
			amns=float(self.c.text)
		except:
			amns=0
			if not self.c.focus:
				self.c.text=''
		a=accelerometer.acceleration
		if self.cnm.state=='play':
			t=max(1-2*(time()-self.st)/self.cnm.length,0)
			self.amns.pos_hint={'center_x':0.49+random()*0.02*t,'center_y':0.49+random()*0.02*t}
		elif any((abs(x) if x else 0)>sllh for x in a):
			if amns:
				sleep(amns)
			layout.add_widget(self.amns)
			self.cnm.play()
			self.st=time()
	def choose(self,i,x):
		if self.bgm:
			if self.bgm.state=='play':
				self.bgm.stop()
		if x!='None' and not self.bgms[x]:
			self.bgms[x]=SoundLoader.load(f'bgm/{tran.index(x)}.mp3')
		self.bgm=self.bgms[x]

class O(SpinnerOption):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		self.font_name='院审'

app().run()