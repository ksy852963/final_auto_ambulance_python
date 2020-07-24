from mqtt.campublisher import ImageMqttPublisher

imageMqttPublisher = ImageMqttPublisher("192.168.3.231", 1883, "/camerapub")
imageMqttPublisher.start()
