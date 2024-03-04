from decimal import Decimal
from datetime import datetime
import sqlite3

#####################################################################################################
#   Program Definition Segment
#####################################################################################################


def CountRunTimeRead():

    with open('run_count.txt', 'r') as file:
        run_count = file.read()

    run_count = int(run_count) + 1

    return run_count

def CountRunTimeWrite(run_count):
    with open('run_count.txt', 'w') as file:
        file.write(str(run_count))

# Here we define a class object for current price information. Since it's clear and scalable
class PriceObj:
    def __init__(self,
                 exchangeName=None,
                 currName1=None,
                 currName2=None,

                 volume1=None,
                 volume1USD=None,
                 volume2=None,
                 volume2USD=None,
                 thisSwapVolumeUSD=None,

                 totalSwapVolumeUSD=None,
                 reserve1 = None,
                 reserve2 = None,
                 reserveUSD=None,
                 liquidity=None,



                 direction=None,
                 priceNumber=None,
                 rev_priceNumber=None,
                 arbWithList2Step=None,
                 # arbWithList3Step=None,
                 creation_time=None,
                 run_count=None,
                 serial_number=None):

        self.exchangeName = exchangeName
        self.currName1 = str(currName1) if currName1 else None
        self.currName2 = str(currName2) if currName2 else None

        self.volume1 = volume1
        self.volume1USD = volume1USD
        self.volume2 = volume2
        self.volume2USD = volume2USD
        self.thisSwapVolumeUSD = thisSwapVolumeUSD
        if volume1USD != None and volume2USD != None and totalSwapVolumeUSD == None:
            self.thisSwapVolumeUSD = volume1USD + volume2USD
        self.totalSwapVolumeUSD = totalSwapVolumeUSD

        self.reserve1 = reserve1
        self.reserve2 = reserve2
        self.reserveUSD = reserveUSD
        self.liquidity = liquidity

        self.direction = direction
        # Caution! Direction is a string, not a boolean. That's for better readability.
        # It should only have two values: "curr1_to_curr2" or "curr2_to_curr1"

        self.priceNumber = priceNumber if isinstance(priceNumber, Decimal) else Decimal(priceNumber)

        if isinstance(rev_priceNumber, Decimal):
            self.rev_priceNumber = rev_priceNumber
        elif rev_priceNumber is not None:
            self.rev_priceNumber = Decimal(rev_priceNumber)
        elif priceNumber is not None:
            self.rev_priceNumber = Decimal(1 / self.priceNumber)


        self.arbWithList2Step = arbWithList2Step if arbWithList2Step else []
        # self.arbWithList3Step = arbWithList3Step if arbWithList3Step else []

        if isinstance(creation_time, str) and creation_time.isdigit():
            creation_time = int(creation_time)

        if isinstance(creation_time, (int, float)):  # if creation_time is a timestamp
            self.creation_time = datetime.fromtimestamp(creation_time)
        else:
            self.creation_time = creation_time if creation_time else datetime.fromtimestamp(
                0)  # Use the provided datetime or 1970-01-01 00:00:00
        self.run_count = run_count
        self.serial_number = serial_number

        #
        # # If creation_time is a string representing a datetime
        # elif isinstance(creation_time, str):
        #     try:
        #         self.creation_time = datetime.strptime(creation_time, '%Y-%m-%d %H:%M:%S')
        #     except ValueError:
        #         print(f"Invalid datetime format for creation_time: {creation_time}")
        #         self.creation_time = None

    #Temporary abandoned since not all exchanges provide the same information
    # def set_direction(self, direction):
    #     if direction not in ["curr1_to_curr2", "curr2_to_curr1"]:
    #         raise ValueError("Invalid direction. It must be either 'curr1_to_curr2' or 'curr2_to_curr1'.")
    #     self.direction = direction

#### Unused code
# symbol_Tulip = (
#     "BTC",  # 0
#     "ETH",  # 1
#     "USDT"  # 2
# )
