#!/bin/bash

docker run \
--rm -it \
--device=/dev/gpiochip0:/dev/gpiochip0 --device=/dev/gpiochip1:/dev/gpiochip1 --device=/dev/gpiochip2:/dev/gpiochip2 \
--device=/dev/ttyTHS0:/dev/ttyTHS0 \
-v sensorlog:/work/log \
-e MQTT_BROKER_HOST=192.168.1.21 \
-e MQTT_BROKER_PORT=1883 \
-e MQTT_SENSOR_DATA_TOPIC=/demo \
-e MQTT_LOG_INFORMATION_TOPIC=/demo \
-e SENSOR_DATA_FILE=/work/log/sensor_data.json \
-e LOG_INFORMATION_FILE=/work/log/log_information.json \
sensor-app
