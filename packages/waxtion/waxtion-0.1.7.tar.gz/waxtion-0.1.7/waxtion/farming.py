from .waxtion import *
from .cals_coins import *

class Farming(CalCoin):
    def __init__(self, account, key, test):
        super().__init__(account, key, test)
        self.materials = "farmmaterial"
        self.veggies = "userveggies"
        self.stats = "farmstats"
        self.multi_scope = [self.veggies]
        
    def get_farm_materials(self, bound: str = ""):
        data = self.struct_single_scope_table_data("farmmaterial", bound)
        table = self.get_table(data)
        return table[0] if bound and table else table
    

    def get_farm_stats(self, bound: str = ""):
        data = self.struct_cal_or_coin_table_data("farmstats", bound)
        table = self.get_table(data)
        return table[0] if bound and table else table
    
    def get_user_veggies(self, account, bound: str = ""):
        data = self.struct_multi_scope_table_data("userveggies", account, bound)
        table = self.get_table(data)
        return table[0] if bound and table else table
    
    
    
    def farm_deposit(self, account, seed, water, compost):
        action_name = "farmdeposit"
        data = self.basic_action_data(account)
        data.append(Data(name="seed", value=types.Uint64(seed)))
        data.append(Data(name="water", value=types.Uint64(water)))
        data.append(Data(name="compost", value=types.Uint64(compost)))
        
        actions = self.structure_action(self.contract, action_name, data)
        return self.send_action([actions])

    def fertilize(self, account, amount):
        action_name = "farmdeposit"
        data = self.basic_action_data(account)
        data.append(Data(name="amount", value=types.Uint64(amount)))
        actions = self.structure_action(self.contract, action_name, data)
        return self.send_action([actions])
    
    def farm_spend(self, account, seed, water, compost):
        action_name = "farmspend"
        data = self.basic_action_data(account)
        data.append(Data(name="seed", value=types.Uint64(seed)))
        data.append(Data(name="water", value=types.Uint64(water)))
        data.append(Data(name="compost", value=types.Uint64(compost)))
        
        actions = self.structure_action(self.contract, action_name, data)
        return self.send_action([actions])
    
    def grass_create(self, account, amount, grass):
        action_name = "grasscreate"
        data = self.basic_action_data(account)
        data.append(Data(name="amount", value=types.Uint64(amount)))
        data.append(Data(name="grass", value=types.Uint64(grass)))
        
        actions = self.structure_action(self.contract, action_name, data)
        return self.send_action([actions])
    
    
    def harvest(self, account, amount,):
        action_name = "harvest"
        data = self.basic_action_data(account)
        data.append(Data(name="amount", value=types.Uint64(amount)))
        actions = self.structure_action(self.contract, action_name, data)
        return self.send_action([actions])
    
    def veggy_consume(self, account, template_id, amount):
        action_name = "veggyconsume"
        data = self.basic_action_data(account)
        data.append(Data(name="template_id", value=types.Uint64(template_id)))
        data.append(Data(name="amount", value=types.Uint64(amount)))
        
        actions = self.structure_action(self.contract, action_name, data)
        return self.send_action([actions])
    
    def veggy_sale(self, account, template_id, amount):
        action_name = "veggysale"
        data = self.basic_action_data(account)
        data.append(Data(name="template_id", value=types.Uint64(template_id)))
        data.append(Data(name="amount", value=types.Uint64(amount)))
        
        actions = self.structure_action(self.contract, action_name, data)
        return self.send_action([actions])
    
    
    def weeded(self, account, amount):
        action_name = "weeded"
        data = self.basic_action_data(account)
        data.append(Data(name="amount", value=types.Uint64(amount)))
        
        actions = self.structure_action(self.contract, action_name, data)
        return self.send_action([actions])
    
    
    
    
