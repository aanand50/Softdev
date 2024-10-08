"""Aditya Anand
CAD
SoftDev
K04: Random Selection of Devos
2024-09-13
time spent: .7 hour"""

import random

krewes = {
       	4: [
    	'DUA','TAWAB','EVA','JACK','VICTOR','EVAN','JASON','COLYI','IVAN','TANZEEM',
    	'TAHMIM','STANLEY','LEON','NAOMI','NIA','ANASTASIA','JADY','BRIAN','JACOB',
    	'ALEX','CHONGTIAN','DANNY','MARCO','ABIDUR','ANKITA','ANDY','ETHAN','AMANDA',
    	'AIDAN','LINDA','QIANJUN','JIAYING','KISHI'
    	],
       	5: [
            	'ADITYA','MARGIE','RACHEL','ALEXANDER','ZIYAD','DANNY','ENDRIT','CADEN',
            	'VEDANT','SUHANA','KYLE','KEVIN','RAYMOND','CHRISTOPHER','JONATHAN','SASHA',
            	'NAFIYU','TIM','WILL','DANIEL','BENJAMIN','CLAIRE','CHLOE','STELLA','TRACY',
            	'JESSICA','JACKIE','WEN YUAN','YINWEI','TIFFANY','JAYDEN DANIEL','PRINCEDEN'
          	]
     	}

def randDevo():
	pd = random.randint(4,5)
	List = krewes[pd]
	devo = random.randint(0, len(List)-1)
	return List[devo]

print(randDevo())
