""" 
    emg_listener
"""

import signal
import sys
import asyncio
from dotenv import load_dotenv
from os.path import exists

from utils.messages import receive_messages, dispatchResource, dispatchBilling
#import utils.messages
    
    
def sigint_handler(sig, frame):
    print('exiting..')
    sys.exit(0)
        
    
async def main():
    if not exists(".env"):
        print("error: .env file not found. exiting.")
        sys.exit(1)
    
    try:
        load_dotenv()
    except AttributeError:
        print("error: unable to import .env file. exiting.")
        sys.exit(1)

    print('launching listener.. ctrl+C to exit.')
    
    while (True):
        for msg in await receive_messages():
            # call the event handler based on the resource type
            dispatchResource(msg)
                
            # if billing details are present, call the billing handler for that resource type  
            try:
                if "LineDetails" in msg["Body"].keys():
                    dispatchBilling(msg)
            except KeyError:
                pass


if __name__ == "__main__":
    signal.signal( signal.SIGINT, sigint_handler )
    asyncio.run( main() ) 