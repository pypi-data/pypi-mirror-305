import solcx
from web3 import Web3, HTTPProvider
from eth_abi import encode as encode_abi

is_warned = False

class Config():
    def __init__(self) -> None:
        self.rpc_url = None
        self.privkey = None
        self.w3 = None
        self.wallet = None
        self.is_setup = False

        latest_solc_version = solcx.get_installed_solc_versions()
        if latest_solc_version == []:
            print("solcx's solc not found, installing solc")
            solcx.install_solc()
            latest_solc_version = solcx.get_installed_solc_versions()

        solcx.set_solc_version(latest_solc_version[-1])
        self.solc_version = latest_solc_version[-1]

    def setup(self, rpc_url, privkey):
        self.is_setup = True
        self.rpc_url = rpc_url
        self.privkey = privkey
        self.w3 = Web3(HTTPProvider(rpc_url))
        self.wallet = self.w3.eth.account.from_key(privkey)
        self.w3.eth.default_account = self.wallet.address

def check_setup():
    global is_warned
    if not config.is_setup:
        if not is_warned:
            print("Warning: Configuration not set up, this may cause unexpected behavior")
            print("please run config.setup(rpc_url, privkey) first")
            is_warned = True
        return False
    return True

def call_check_setup(func):
    def wrapper(*args, **kwargs):
        check_setup()
        return func(*args, **kwargs)
    return wrapper

def check_setup_on_create(cls):
    original_init = cls.__init__
    def new_init(self, *args, **kwargs):
        check_setup() 
        original_init(self, *args, **kwargs)
    cls.__init__ = new_init
    return cls

config = Config()