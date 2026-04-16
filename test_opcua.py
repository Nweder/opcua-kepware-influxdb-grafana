#testing connaction to Kepware OPC UA server and reading a single value

from opcua import Client

url = "opc.tcp://REMOVED_HOST:56000"
client = Client(url)

try:
    client.connect()
    print("Connected to Laser2  ")

    node = client.get_node("ns=2;s=MachineStates.ProcessActive")
    value= node.get_value()
    print("processActive",value)
    client.disconnect()

except Exception as e:
    print("error , No conncation", e)