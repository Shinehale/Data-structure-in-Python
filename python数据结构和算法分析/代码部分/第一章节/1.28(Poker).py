"""
这个程序模拟的是我童年玩的一种游戏：
给每位游戏人员发牌，并且展示在桌面上
若桌面上的有牌跟本人一样所接牌面值一样，则从桌面上的牌到本人所接牌的数量加入到个人总分中
当手中所有的牌都接完了
统计分数，分数最高的胜利
你可以通过添加代码：
print(cards)
于UpdateCardList()中以打印游戏过程
"""
import os
import sys
import random
class Poker:
    def __init__(self,value):
        self.face=value%13
        self.suit=value%4

    def getFace(self):
        return self.face

    def getSuit(self):
        return self.suit

    def __repr__(self):
        return "face:"+str(self.face)+" suit:"+str(self.suit)


class Player:
    def __init__(self,name):
        self.num=0
        self.scores=0
        self.name=name
        self.cards=[]

    def getScores(self):
        return self.scores

    def getNum(self):
        return self.num

    def getName(self):
        return self.name

    def __repr__(self):
        return "playerName:"+str(self.name)+" Scores:"+str(self.scores)

    def setCard(self,cards):
        self.cards=cards
        self.num=len(self.cards)

    def delcard(self,pos):
        self.cards.pop(pos)
        self.num-=1

    def getOnecard(self,pos):
        return self.cards[pos]

    def addScore(self,value):
        self.scores+=value


class PokerAll:
    def __init__(self):
        self.used=[0]*52

    def checknew(self,value):
        if self.used[value]==0:
            self.used[value]=1
            return True
        else:
            return False


def getvalue():
    flag=True
    while flag:
        newvalue=random.randint(0,51)
        if PA.checknew(newvalue):
            return newvalue
        else:
            continue


def initGame():
    for i in range(N):
        Players.append(Player(chr(ord("A") + i)))
    for i in range(N):
        Players.append(Player(chr(ord("A") + i)))
    everyPlayercardNum=52//N
    for i in range(N):
        new_=[]
        for j in range(everyPlayercardNum):
            newvalue=getvalue()
            new_.append(Poker(newvalue))
        Players[i].setCard(new_)

def UpdateCardList():
    pos=-1
    global cards
    for i in range(len(cards)-1):
        if cards[i].getFace()==cards[len(cards)-1].getFace():
            pos=i
            break
    if pos==-1:return 0
    length=len(cards)-pos
    if pos==0:
        cards=[]
    else:
        cards=cards[0:pos]
    return length


def GoGame():
    which=0
    while True:
        flag=True
        R=Players[which].getNum()-1
        if R==0:
            oneCard=0
        elif R>=1:
            oneCard=random.randint(0,R)
        else:
            continue
        cards.append(Players[which].getOnecard(oneCard))
        add=UpdateCardList()
        Players[which].delcard(oneCard)
        Players[which].addScore(add)
        for i in range(N):
            if Players[i].getNum()!=0:flag=False
        if flag:break
        which=which+1
        which=which%N


def ReportGame():
    ans,pos=0,0
    for i in range(N):
        print(Players[i])
        if Players[i].getScores()>ans:
            pos=i
            ans=Players[i].getScores()
    print("The winner is %s" %(Players[pos].getName()))
    print("桌面上剩下的牌是：")
    print(cards)


N=int(input("请输入参加游戏的人数："))
Players=[]
cards=[]
PA=PokerAll()
initGame()
GoGame()
ReportGame()