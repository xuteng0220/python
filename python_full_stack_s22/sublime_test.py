import random

class Poker:
    card = [i + j for i in ['Spade', 'Heart', 'Diamond', 'Club'] for j in [str(i) for i in range(2, 10)] + list('JQKA')]

    def __init__(self, name):
        self.name = name

    def shuffle_card(self):
        self.card = random.shuffle(self.card) 
        print(self.card)


    def random_select(self):
        print(f"{self.name}您随机抽取的牌为：{random.sample(self.card, 1)}")


    def specific_select(self):
        self.num = int(print('请输入序号(1~52):'))
        if 0 < self.num < 53:
            print(self.card[self.num-1])
        else:
            print(f"{self.num}超出范围了")

    def order_card(self):
        pass


    def quit(self):
        print('qiut the game')

p = Poker('ryan')
print(p.card)
p.shuffle_card()
p.random_select()
p.specific_select()



-----------------------------------------------------------------

class Goods:

    def __init__(self, name, price, discount):
        self.name = name
        self.__price = price
        self.__discount = discount

    @property
    def price(self):
        return self.__price * self.__discount

    @price.setter
    def price(self, new_price):
        self.__price = new_price


    @s

    @deleter


