from youtubesearchpython import VideosSearch
import paho.mqtt.client as mqtt
from paho.mqtt.client import Client

Broker = "address_mqtt"
search="test/search" # topic for text to search
topic = "test/link" # topic for address video youtube


client = Client(client_id = search)
client = mqtt.Client()
client.connect(Broker, 1883, 60)
def on_connect(client, userdata, flags, rc):
    print("connect")

def on_message(client, userdata, message):
    link(message.payload.decode())



def link(download):
    videosSearch = VideosSearch(download, limit=1)
    link = str(videosSearch.result())
    link = link.find('/watch?v=')
    link = link[link:link+ 20]
    link=link[9:]
    client.publish(topic, mqtt)
while True:
    client.on_connect = on_connect
    client.on_message = on_message
