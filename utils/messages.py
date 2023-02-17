''' messages
      - EMG message utilities
'''

# the JSON structure of the messages returned by the service bus can be found here, organized by type
#    https://developer.equinix.com/docs/emg/getting-started

#   https://developer.equinix.com/docs/emg/overview

import asyncio
import json
import sys

from utils.servicebus import servicebus_queue_receiver

'''
   message handlers by resource type
'''

def BreakFix (msg):
    #print("> BreakFix")
    pass
    
def Shipping (msg):
    #print("> Shipping")
    pass
    
def WorkVisit (msg):
    #print("> WorkVisit")
    pass
    
def SmartHands (msg):
    #print("> SmartHands")
    pass
   
def CrossConnect (msg):
    #print("> CrossConnect")
    pass

def DataCenter_Network_VirtualConnection (msg):
    print("> Fabric VC")
    print(str(msg))
    #name = msg["Body"]["data"]["name"]
    #status = msg["Body"]["data"]["operation"]["operationalStatus"]
    #description = msg["Body"]["description"]
    #print("\tname: %s\n\tstatus: %s\n\tdescription: %s" % ( name, status, description ))
    #pass
    
def DataCenter_Network_Port (msg):
    print("> Fabric Port")
    print(str(msg))
    #name = msg["Body"]["data"]["name"]
    #status = msg["Body"]["data"]["operation"]["operationalStatus"]
    #description = msg["Body"]["description"]
    #print("\tname: %s\n\tstatus: %s\n\tdescription: %s" % ( name, status, description ))
    #pass

def DataCenter_Maintenance (msg):
    #print("> DataCenter Maintenance")
    pass
    
def DataCenter_Advisory (msg):
    #print("> DataCenter Advisory")
    pass

def DataCenter_Incident (msg):
    #print("> DataCenter Incident")
    pass

def DataCenter_SecurityIncident (msg):
    #print("> DataCenter Security Incident")
    pass

def Network_Maintenance (msg):
    #print("> Network Maintenance")
    pass
    
def Network_Incident (msg):
    #print("> Network Incident")
    pass


'''
   dispatch table of resource types to message handlers
'''

resource_handlers = { 
#   resource value                            message handlers
#   --------------------------------------    -------------------------------------
    'BreakFix'                              : BreakFix,
    'Shipping'                              : Shipping,
    'WorkVisit'                             : WorkVisit,
    'SmartHands'                            : SmartHands, 
    'CrossConnect'                          : CrossConnect,
    'DataCenter.Network.VirtualConnection'  : DataCenter_Network_VirtualConnection,
    'DataCenter.Network.Port'               : DataCenter_Network_Port,
    'DataCenter.Maintenance'                : DataCenter_Maintenance,
    'DataCenter.Advisory'                   : DataCenter_Advisory,
    'DataCenter.Incident'                   : DataCenter_Incident, 
    'DataCenter.SecurityIncident'           : DataCenter_SecurityIncident,
    'Network.Maintenance'                   : Network_Maintenance,
    'Network.Incident'                      : Network_Incident
    }

def dispatchResource (msg):
    try:
        (resource_handlers[msg['Resource']])( msg )
        
    except KeyError:
        print("warning: unhandled Resource type encountered, dumping JSON.")
        print(str(msg))
        pass
        

''' 
   billing handlers 
'''        

def Billing_CrossConnect (msg):
    #print("> Billing (CrossConnect)")
    pass
    
def Billing_Accessory (msg):
    #print("> Billing (Accessory)")
    pass
    
def Billing_ColoOrder (msg):
    #print("> Billing (ColoOrder)")
    pass
    
def Billing_SmartHands (msg):
    #print("> Billing (SmartHands)")
    pass
    
def Billing_BreakFix (msg):
    #print("> Billing (BreakFix)")
    pass
    
def Billing_Shipping (msg):
    #print("> Billing (Shipping)")
    pass

def Billing_IbxSmartView (msg):
    #print("> Billing (IBX SmartView)")
    pass

def Billing_NetworkProduct (msg):
    #print("> Billing (NetworkProduct)")
    pass

def Billing_WorkVisit (msg):
    #print("> Billing (WorkVisit)")
    pass

'''
   dispatch table of resource types to billing handlers
   note: billing messages are defined by the existence of LineItems in the Body
'''

billing_handlers = {
#   resource value      billing handlers
#   -----------------   ----------------------
    'CrossConnect'    : Billing_CrossConnect,
    'Accessory'       : Billing_Accessory,
    'ColoOrder'       : Billing_ColoOrder,
    'SmartHands'      : Billing_SmartHands,
    'BreakFix'        : Billing_BreakFix,
    'Shipping'        : Billing_Shipping,
    'IbxSmartView'    : Billing_IbxSmartView,
    'NetworkProduct'  : Billing_NetworkProduct,
    'WorkVisit'       : Billing_WorkVisit
    }    

def dispatchBilling (msg):
    try:
        billing_handlers[msg['Resource']]( msg )                # known Billing types
        
    #except KeyError:
    except:
        print('in dispatchBilling('+msg['Resource']+')')
        print("warning: unhandled Billing type encountered, dumping JSON.")
        print(str(msg))       

 
'''
   service bus receiver loop
'''
   
async def receive_messages ():
    messages = []
    receiver = servicebus_queue_receiver()
    
    with receiver:
        received_msgs = receiver.receive_messages ( max_message_count=25, max_wait_time=30 )
        
        for message in received_msgs:
            temp = json.loads(str(message))
            msg = json.loads(temp["Task"])

            # filter messages here
            messages.append(msg)

        # end of for loop    
        #print(receiver.status)    
        receiver.close()
        
        return messages
