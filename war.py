class Card:
    suits=["spades","hearts","diamonds","clubs"]
    values=[None,None,"2","3","4","5","6","7",
            "8","9","10","Jack","Queen","King","Ace"]

    def __init__(self,v,s):
        """s(組み)もv(数値)も整数値です"""
        self.value=v
        self.suit=s
    def __lt__(self,c2):
        if self.value < c2.value :
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False
    def __gt__(self,c2):
        if self.value > c2.value :
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False
    def __repr__(self):
        return self.values[self.value]+" of "+\
               self.suits[self.suit]


from random import shuffle
class Deck:
    def __init__(self) -> None:
        self.cards=[]
        for i in range(2,15):
            for j in range(4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)
    def rm_card(self):
        if len(self.cards)==0:
            return
        return self.cards.pop()

class Player:
    def __init__(self,name):
        self.wins=0
        self.card=None
        self.name=name

class Game:
    def __init__(self):
        self.deck=Deck()
        name1=input("プレイヤー１を入力してください")
        name2=input("プレイヤー２を入力してください")
        self.p1=Player(name1)
        self.p2=Player(name2)
    def wins(self,winner):
        w="このラウンドは{}が勝ちました！"
        print(w.format(winner))
    def draw(self,p1,p2,c1,c2):
        d="{}は{}を引き、{}は{}を引きました！"
        d=d.format(p1,c1,p2,c2)
        print(d)
    def winner(self):
        if self.p1.wins > self.p2.wins:
            print(self.p1.wins,"対",self.p2.wins,"で",self.p1.name,"の勝ち！")
        elif self.p1.wins < self.p2.wins:
            print(self.p2.wins,"対",self.p1.wins,"で",self.p2.name,"の勝ち！")
        else:
            print(self.p2.wins,"対",self.p1.wins,"で引き分け！")

    def play_game(self):
        print("それでは戦争を始めます！")
        while len(self.deck.cards) >= 2 :
            m=input("qで終了、それ以外のキーで続行")
            if m == "q":
                break
            self.p1.card=self.deck.rm_card()
            self.p2.card=self.deck.rm_card()
            self.draw(self.p1.name,self.p2.name,self.p1.card,self.p2.card)
            if self.p1.card > self.p2.card :
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)
        self.winner()
            
game=Game()
game.play_game()
