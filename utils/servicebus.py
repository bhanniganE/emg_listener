''' servicebus
      - EMG servicebus access
'''
import sys
import os

#from config.prod import EQUINIX_OUTGOING_QUEUE, EQUINIX_OUTGOING_QUEUE_CONNECTION_STRING
from azure.servicebus import ServiceBusClient,ServiceBusReceiveMode

def servicebus_queue_receiver():
    try:
        conn_str = os.getenv("EQUINIX_OUTGOING_QUEUE_CONNECTION_STRING")
        queue_name = os.getenv("EQUINIX_OUTGOING_QUEUE")
    except Exception as e:
        print(str(e))
        sys.exit(1)
    
    try:
#        client = ServiceBusClient.from_connection_string(conn_str=EQUINIX_OUTGOING_QUEUE_CONNECTION_STRING)
#        queue_receiver = client.get_queue_receiver(queue_name=EQUINIX_OUTGOING_QUEUE, max_wait_time=5, recieve_mode=ServiceBusReceiveMode.RECEIVE_AND_DELETE )
        client = ServiceBusClient.from_connection_string(conn_str=conn_str)
        queue_receiver = client.get_queue_receiver(queue_name=queue_name, max_wait_time=5, recieve_mode=ServiceBusReceiveMode.RECEIVE_AND_DELETE )
        return queue_receiver
    except ValueError:
        print("error: unable to connect to servicebus. please confirm credentials.")
        sys.exit(1)