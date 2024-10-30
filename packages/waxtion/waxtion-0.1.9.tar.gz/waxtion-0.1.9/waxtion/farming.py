from .waxtion import *
from .cals_coins import *

class Farming(CalCoin):
    def __init__(self, account, key, test):
        super().__init__(account, key, test)
        self.materials = "farmmaterial"
        self.veggies = "userveggies"
        self.stats = "farmstats"
        self.multi_scope = [self.veggies]
    
    def get_orders(self, account, bound: str = ""):
        data = self.struct_multi_scope_table_data("orders", account, bound)
        table = self.get_table(data)
        return table
        
    def get_farm_materials(self, bound: str = ""):
        data = self.struct_single_scope_table_data("farmmaterial", bound)
        table = self.get_table(data)
        return table[0] if bound and table else table
    

    def get_farm_stats(self, bound: str = ""):
        data = self.struct_single_scope_table_data("farmstats", bound)
        table = self.get_table(data)
        return table[0] if bound and table else table
    
    def get_user_veggies(self, account, bound: str = ""):
        data = self.struct_multi_scope_table_data("userveggies", account, bound)
        table = self.get_table(data)
        return table[0] if bound and table else table
    
    def create_orders(self, account, orders):
        action_name = "farmorder"
        actions = []
        for order in orders:
            data = self.basic_action_data(account)
            data.append(Data(name="asset_id", value=types.Uint64(order.asset_id)))
            data.append(Data(name="amount", value=types.Uint64(order.amount)))
            data.append(Data(name="fertilized", value=types.Bool(order.fertilized)))
            data.append(Data(name="ready_at1", value=types.Bool(order.ready_at1)))
            data.append(Data(name="ready_at2", value=types.Bool(order.ready_at)))
            action = self.structure_action(self.contract, action_name, data)
            actions.append(action)
        return self.send_action(actions)
    
    def delete_orders(self, account, orders):
        action_name = "delorder"
        actions = []
        for order in orders:
            data = self.basic_action_data(account)
            data.append(Data(name="asset_id", value=types.Uint64(order.asset_id)))
            action = self.structure_action(self.contract, action_name, data)
            actions.append(action)
        return self.send_action(actions)
        
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
    
    
    def veggy_deposit(self, account, veg_data):
        action_name = "veggydeposit"
        actions = []
        for veg in veg_data:
            data = self.basic_action_data(account)
            data.append(Data(name="template_id", value=types.Uint64(veg[1])))
            data.append(Data(name="amount", value=types.Uint64(veg[0])))
            action = self.structure_action(self.contract, action_name, data)
            actions.append(action)
            
        return self.send_action(actions)
    
    def veggy_consume(self, account, template_id, amount):
        action_name = "veggyconsume"
        data = self.basic_action_data(account)
        data.append(Data(name="template_id", value=types.Uint64(template_id)))
        data.append(Data(name="amount", value=types.Uint64(amount)))
        
        actions = self.structure_action(self.contract, action_name, data)
        return self.send_action([actions])
    
        
    def subveggy(self, account, template_id, amount):
        action_name = "subveggy"
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
    
    
    def create_farming_order(self, account, asset_id, amount, fertilized, ready_at):
        action_name = "farmorder"
        data = self.basic_action_data(account)
        data.append(Data(name="asset_id", value=types.Uint64(asset_id)))
        data.append(Data(name="amount", value=types.Uint64(amount)))
        data.append(Data(name="fertilized", value=types.Bool(fertilized)))
        data.append(Data(name="ready_at", value=types.Uint64(ready_at)))
        actions = self.structure_action(self.contract, action_name, data)
        return self.send_action([actions])
    
    
