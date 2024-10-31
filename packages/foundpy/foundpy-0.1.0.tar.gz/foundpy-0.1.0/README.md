# foundpy

Foundpy is a Python implementation of a popular toolkit [Foundry](https://github.com/foundry-rs/foundry). It replicates Foundry's core functionality without needing Foundry's installation. Foundpy enables users to use Python's web3 module with similar command style as Foundry.

```py
from foundpy import *
config.setup(
    rpc_url="http://rpc.url/",
    privkey="0xdeadbeef"
)
setup_addr = "0xE162F3696944255cc2850eb73418D34023884D1E"
cast.send(setup_addr, "solve(bytes)", b"args123")
cast.call(setup_addr, "isSolved()")
```

## Installation

foundpy can be installed using pip:

```sh
pip install foundpy
```

## Usage

foundpy is best used with jupyter notebooks. But it can be used in a python script as well.

first initialize the configuration with the RPC and your private key:

```py
from foundpy import *
config.setup(
    rpc_url="http://rpc.url/",
    privkey="0xdeadbeef"
)
```

To interact with a contract, you can either use the `cast` object or instantiate a `Contract` object (source code required).

```py
setup_addr = "0xE162F3696944255cc2850eb73418D34023884D1E"
cast.send(setup_addr, "solve(bytes)", b"args123" value=0)
# or
setup = Contract(setup_addr, "Setup.Sol") # or "Setup.Sol:Setup" to specify the class
setup.send("solve", b"args123", value=0)
```

To deploy a contract, you can either use the `forge` object or use the `deploy_contract` function. Simply make sure that the contract's source code is in the same directory as the script. The constructor arguments can be passed by adding them to the function call after the filename.

```py
# This will return an address
attack = forge.create("Attack.sol:Attack", setup_addr, value=int(1*(10**18)))
# or
# This will return a Contract object, which you can interact with attack.call or attack.send
attack = deploy_contract("Attack.sol", setup.address, value=int(1*(10**18))) # or "Attack.Sol:Attack" to specify the class
```

You can check for more examples in the [example](./example/) directory.