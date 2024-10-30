from .waxtion import *


class CalCoin(Waxtion):
    def __init__(self, account, key, test):
        super().__init__(account, key, test)
        self.coins = "coins"
        self.calories = "calories"
        self.contract = "pixelstorage"
    
    
    
    def basic_action_data(self, account):
        return [
            Data(name="caller", value=types.Name(self.account)),
            Data(name="from", value=types.Name(account))
        ]
        
    def get_calories(self, bound: str = ""):
        data = self.struct_single_scope_table_data("calories", bound)
        table = self.get_table(data)
        return table[0] if bound and table else table

    def add_calories(self, account: str, amount: int):
        action_name = "addcalories"
        data = self.basic_action_data(account)
        data.append(Data(name="calories", value=types.Uint64(amount)))
        actions = self.structure_action(self.contract, action_name, data)
        return self.send_action([actions])

    def sub_calories(self, account: str, amount: int):
        action_name = "subcalories"
        data = self.basic_action_data(account)
        data.append(Data(name="calories", value=types.Uint64(amount)))
        actions = self.structure_action(self.contract, action_name, data)
        return self.send_action([actions])
        

    def get_coins(self, bound: str = ""):
        data = self.struct_single_scope_table_data("coins", bound)
        table = self.get_table(data)
        return table[0] if bound and table else table
    

    def farm_buy(self, account: str, amount: int):
        action_name = "farmbuy"
        data = self.basic_action_data(account)
        data.append(Data(name="amount", value=types.Uint64(amount)))
        
        actions = self.structure_action(self.contract, action_name, data)
        return self.send_action([actions])

    """
    def add_coins(self, account: str, amount: int):
        action_name = "addcoins"
        data = self.basic_action_data(account)
        data.append(Data(name="coins", value=types.Uint64(amount)))
        actions = self.structure_action(self.contract, action_name, data)
        return self.send_action([actions])

    def sub_coins(self, account: str, amount: int):
        action_name = "subcoins"
        data = self.basic_action_data(account)
        data.append(Data(name="coins", value=types.Uint64(amount)))
        actions = self.structure_action(self.contract, action_name, data)
        return self.send_action([actions])
    """