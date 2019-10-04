#ifndef MODULEMQTT_H
#define MODULEMQTT_H

#include "module.h"

#include <WiFi.h>
#include <PubSubClient.h>

//#define BOARD_NAME "M1"
#define BOARD_NAME "Controller"

#define MY_MQTT_HOST "10.25.249.104"
#define MY_MQTT_HOST_PORT 1883
#define MY_MQTT_USERNAME ""
#define MY_MQTT_PASSWORD ""

const char* MQTT_SERVER_IP = MY_MQTT_HOST;
const int MQTT_SERVER_PORT = MY_MQTT_HOST_PORT;

const char* MQTT_USER = MY_MQTT_USERNAME;
const char* MQTT_PASSWORD = MY_MQTT_PASSWORD;
const char* MQTT_CLIENT_NAME = BOARD_NAME;

class ModuleMqtt : public ModuleWifi {

private:

	WiFiClient _wifiClient;
	PubSubClient _mqttClient;

	//MQTT IN MODULE
	void _callback(char* top, uint8_t* payload, unsigned int length) {

		char msg[MQTT_PAYLOAD_MAX];
		String topic = String(top);

		//message
		for (int i = 0; i < MQTT_PAYLOAD_MAX; i++) {
			char c = '\0';
			if (i < (int)length) c = (char)payload[i];
			msg[i] = c;
		}

		String message = String(msg);
		message.remove(length);


		log_log(F("MQTT: ["));
		log_log(top);
		log_log(F("] - "));
		for (int i = 0; i < (int)length; i++) {
			log_log((char)payload[i]);
		}
		if (length > MQTT_PAYLOAD_MAX) {
			log_log(F("!!! payload too big"));
		}
	}

public:

	ModuleMqtt() : ModuleWifi() {

	}

	void begin() {
		log_logln(F("Setting up MQTT"));

		connect(true);

		log_logln(F("MQTT setup done"));
	}

	void subscribe(String topic) {
		_mqttClient.subscribe(topic.c_str());
	}


	void publish(String topic, String payload) {
		_mqttClient.publish(topic.c_str(), payload.c_str());
	}

	bool loop() {
		if (!_mqttClient.connected()) {
			connect(true);
			return false;
		}
		else {
			_mqttClient.loop();
			return true;
		}
	}

	//WTFFFFFFFFFFFFFFF
	std::function<void(char*, uint8_t*, unsigned int)> callback = [=](char* topic, uint8_t* payload, unsigned int length) {
		this->_callback(topic, payload, length);
	};


	void connect(bool sub) {

		_mqttClient.setClient(_wifiClient);
		_mqttClient.setServer(MQTT_SERVER_IP, MQTT_SERVER_PORT);
		_mqttClient.setCallback(callback);

		if (!_mqttClient.connected()) {
			log_logln(F("Connecting to MQTT..."));
			if (_mqttClient.connect(MQTT_CLIENT_NAME, MQTT_USER, MQTT_PASSWORD)) {
				log_logln(F("   connected"));
		/*		if (sub) {
					subscribe();
				}*/
			}
			else {
				log_log(F("   failed with state "));
				log_logln(_mqttClient.state());
				delay(50);
			}
		}
	}
};

#endif // MQTT_ENABLE