from pyntelope import (
    types, 
    Action, 
    Authorization, 
    WaxMainnet, 
    WaxTestnet, 
    Data, 
    Transaction
)



class Waxtion:
    def __init__(self, account: types.Name, key: str, test: bool = True):
        self.account = account
        self.key = key
        self.auth = Authorization(actor=account, permission="active")
        
        if test:
            self.network = WaxTestnet()
        else:
            self.network = WaxMainnet()

    def get_table(self, table_info: dict, bound: types.Name = ""):
        
        if bound:
            table_info["lower_bound"] = bound
            table_info["upper_bound"] = bound

        table = self.network.get_table_rows(
            **table_info
        ) 
        print(table)
        return table
    
    def transfer_tokens(self, 
        _from: types.Name, 
        _to: types.Name, 
        asset: types.Asset, 
        memo: types.String, 
        contract: types.Name,
        simple: bool = False
    ):
        """Transfer tokens and outputs txn data or txn hash.

        Args:
            _from (types.Name): Sender
            _to (types.Name): Receiver
            asset (types.Asset): Eg. '1.00000000 WAX'
            memo (types.String): String
            contract (types.Name): EOSIO Name
            simple (bool, optional): If true, outputs only txn hash else, full txn. Defaults to False.

        Returns:
            dict or string: Outputs txn data or txn hash.
        """
        
        data = self.structure_token_transfer_data(_from, _to, asset, memo)
        action = self.structure_action(contract, "transfer", data)
        resp = self.send_action([action])
        return resp if not simple or not resp else resp["transaction_id"]
    
    def structure_token_transfer_data(self, 
        _from: types.Name, 
        _to: types.Name,
        asset: types.Asset, 
        memo: types.String
    ):
        """Transforms params into eosio compatible data types.

        Args:
            _from (types.Name): Sender
            _to (types.Name): Receiver
            asset (types.Asset): Asset (1.00000000 WAX)
            memo (types.String): String

        Returns:
            _type_: List of Data Types to add to action payload.
        """
        data = [
            Data(name="from", value=types.Name(_from)),
            Data(name="to", value=types.Name(_to)),
            Data(
                name="quantity", # Selects the 'quantity' field in this action, must be a valid field in the action
                value=types.Asset(asset), # Asset type must be specified as 'quantity' requires the amount and currency type, which Asset includes
            ),
            Data(
                name="memo", # Selects the 'memo' field in this action, just an extra message with the transfer
                value=types.String(memo), # String type is used for memo
            ),
        ]
        return data
        
    
    def structure_action(self, 
        contract: types.String, 
        name: types.String, 
        data: list
    ):
        """Structures all the data into an EOSIO Action.

        Args:
            contract (types.String): EOSIO Name
            name (types.String): Action Name
            data (list): List of Data Objects

        Returns:
            Action: Action that can be signed into a transaction
        """
        action = Action(
            account=contract,
            name=name,
            data=data,
            authorization=[self.auth],
        )
        
        return action
        

    def send_action(self, 
        action: Action
    ):  
        """Signs the Action and sends it to the blockchain

        Args:
            action (Action): Action received from class flow

        Returns:
            Response: Response from the Post Action into API
        """
        raw_transaction = Transaction(actions=action)

    
        linked_transaction = raw_transaction.link(net=self.network)


        signed_transaction = linked_transaction.sign(key=self.key)

        resp = signed_transaction.send()

        return resp

    def struct_single_scope_table_data(self, niche, bound: str = ""):
        data = {"code": self.contract, "table": niche, "scope": self.contract}
        if bound:
            data["lower_bound"] = bound
            data["upper_bound"] = bound
        return data
    
    def struct_multi_scope_table_data(self, niche, scope, bound: str = ""):
        data = {"code": self.contract, "table": niche, "scope": scope}
        if bound:
            data["lower_bound"] = bound
            data["upper_bound"] = bound
        return data
    
    def result_analysis(self, result):
        if "transaction_id" in result.keys():
            return True
        return False