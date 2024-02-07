from brownie import network, config, accounts,MockV3Aggregator


DECIMALS = 8
STARTING_PRICE = 200000000000

LOCAL_BLOCKCHAIN_ENVIROMENTS= ["development", "ganache-local"]
FORKED_LOCAL_ENVIOREMENTS= ["mainnet-fork-dev","mainnet-fork"]

def get_account():
    if (network.show_active() in LOCAL_BLOCKCHAIN_ENVIROMENTS
        or network.show_active() in FORKED_LOCAL_ENVIOREMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])
    
def deploy_mock():
    print(f"La red activa es {network.show_active()}")
    print(f"Haciendo deploy de los mocks")
    MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from":get_account()})
    print(f"Los mocks ya están desplegados")