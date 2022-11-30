import os
from termcolor import colored, cprint

class Dispenser():
    
    def __init__(self, password = 'azerty'):
        self.stock = 100
        self.cash = 11.5
        self.item_1 = 1.5
        self.password = password
        
        
    def stock_down(self,quantity):
        self.stock = self.stock - quantity
        return self.stock
    
    
    def stock_up(self,quantity):
        self.stock = self.stock + quantity
        return self.stock
    
    
    def cash_down(self, coin, technicien = False):
        if technicien:
            self.cash_down_technicien(coin)
        else:
            self.cash = self.cash - coin
        return self.cash


    def cash_up(self,coin):
        self.cash = self.cash + coin
        return self.cash


    def cash_back(self,coin):
        self.cash_down(coin - self.item_1)
        return coin - self.item_1

    
    def bad_amount(self,coin):
        return coin < self.item_1

    
    def bad_stock(self,quantity):
        return quantity > self.stock
              
    
    def buy(self,quantity,coin):
        if (self.bad_amount(coin) or self.bad_stock(quantity)):
            return f"{self.build_sentence(quantity)}"
        else: 
            self.stock_down(quantity)
            self.cash_up(coin)
            
            return Dispenser.error_or_valid_message(sentence=f"Rendu monnaie 💰: {self.cash_back(coin)} €", error=False)
        
    
    def display_menu(self):
        coin = input("Mets ta pièce\n")
        coin = float(coin)
        #quantity = float(input("Combien de cannette ?  > "))
        self.buy(1,coin)
        return None
            

    def check(self):
        if self.verify_password():
            for variable_instance, value in Dispenser.__dict__.items():
                    print(f"{variable_instance} : {value}")
        else:
            return Dispenser.error_or_valid_message(sentence='Mot de passe invalide')
        
    
    def cash_down_technicien(self,coin):
        
        if self.verify_password():
            if self.cash > coin:
                self.cash = self.cash - coin
                return self.cash
            else:
                return Dispenser.error_or_valid_message(sentence=f"Erreur : Vous demandez {coin} € alors qu'il y a {self.cash} € en trésorie ! ")
        else:
            return Dispenser.error_or_valid_message(sentence='Mot de passe invalide')
        
    
    def verify_password(self):
        input_password = input("Entrez un mot de passe > ")
        return self.password == input_password
    
    
    def build_sentence(self,quantity):
        if self.bad_stock(quantity):
            Dispenser.error_or_valid_message(sentence=f"Arsouille ! Tu as trop picolé ! Il n'y a plus de stock !")
            return None
        else:
            #Pour mac : 
            #return f"Rentre chez toi, voyou {os.system('say VOYOU !')}"
            Dispenser.error_or_valid_message(sentence=f"Pas assez d'argent. Rentre chez toi, VOYOU !")
            return None
    
        
    @classmethod
    def error_or_valid_message(cls,sentence='', error=True):
        if error:
            color = 'red'
        else:
            color = 'green'
        cprint(sentence, color, attrs=["reverse", "blink"])
        