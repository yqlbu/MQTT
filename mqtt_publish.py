# MQTT Publish Demo
# Publish two messages, to two different topics

import paho.mqtt.publish as publish

publish.single("CoreElectronics/test", "Hello", hostname="localhost")
publish.single("CoreElectronics/topic", "World!", hostname="localhost")
print("Done")
