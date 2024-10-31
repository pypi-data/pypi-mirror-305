from .util import *
from .config import *
from .contract import *

class Cast():
    def __init__(self):
        pass

    @call_check_setup
    def call(self, contract_address, function_signature, *args):
        contract = Contract(contract_address)
        return contract.call(function_signature, *args)
    
    @call_check_setup
    def send(self, contract_address, function_signature, *args, value=0):
        contract = Contract(contract_address)
        return contract.send(function_signature, *args, value=value)