import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe



publish.single("/garden/test", "payload", hostname="localhost")


msg = subscribe.simple("piscina/luz", hostname="localhost")
print("%s %s" % (msg.topic, msg.payload))

while (1):
    msg = subscribe.simple("piscina/luz", hostname="localhost")
    print("%s %s" % (msg.topic, msg.payload))
     