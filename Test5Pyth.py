from FunctionAndDefinition import PriceObj
import asyncio
import logging

from pythclient.pythclient import PythClient
from pythclient.pythaccounts import PythPriceType
from pythclient.utils import get_key
from pythclient.solana import SOLANA_MAINNET_WS_ENDPOINT, MAINNET_ENDPOINT

solana_network="pythnet" #Todo: change to mainnet when it's ready
                        #Use "devnet" for testing purpose
use_program = True
serial_number = 0

first_mapping_account_key=get_key(solana_network, "mapping")
print("first_mapping_account_key")
print(first_mapping_account_key)
program_key=get_key(solana_network, "program")
print("program_key")
print(program_key)
run_count = 1


async def SolanaPythClientPriceFunction():
    solana_prices_obj = []
    async with PythClient(
        first_mapping_account_key=get_key(solana_network, "mapping"),
        program_key=get_key(solana_network, "program") if use_program else None,
        # solana_endpoint=MAINNET_ENDPOINT,
        # solana_ws_endpoint=SOLANA_MAINNET_WS_ENDPOINT

    ) as c:
        await c.refresh_all_prices()
        products = await c.get_products()
        for counter_pyth, item in enumerate(products):
            if item.attrs['asset_type'] == 'Crypto':
                pr = await item.get_prices()
                p =pr[PythPriceType.PRICE]
                if p.aggregate_price_info.price is not None:
                    if p.aggregate_price_info.price != 0:
                        curr_priceobj_1 = PriceObj(exchangeName="Solana",
                                                   currName1=item.attrs['base'],
                                                   currName2=item.attrs['quote_currency'],
                                                   priceNumber=p.aggregate_price_info.price,
                                                   creation_time=p.timestamp,
                                                   run_count = run_count,
                                                   serial_number = serial_number)
                        solana_prices_obj.append(curr_priceobj_1)
    return solana_prices_obj

# Python 3.7+
solana_prices_obj = asyncio.run(SolanaPythClientPriceFunction())
a = 1+2