#ifndef MODULEWIFI_H
#define MODULEWIFI_H

#include "module.h"

#include <WiFi.h>

#define MY_WIFI_SSID "Prusa Research Office1"
#define MY_WIFI_PASSWORD "prasopesMK3"

class ModuleWifi {

private:
	String _ssid = MY_WIFI_SSID;
	String _pass = MY_WIFI_PASSWORD;

protected:


public:
	ModuleWifi() {
		
	}

	ModuleWifi(String ssid, String pass) {
		_ssid = ssid;
		_pass = pass;
	}

	void begin()
	{
		log_logln();
		log_log(F("Connecting to "));
		log_logln(_ssid);

		int count = 0;

		WiFi.begin(_ssid.c_str(), _pass.c_str());
		while (WiFi.status() != WL_CONNECTED) {
			count++;
			if (count > 10) {
				log_logln("Reseting the ESP...");
				ESP.restart();
			}
			else {
				log_log(".");
			}
			delay(500);
		}

		//WiFi.hostname(WIFI_NAME);
		log_log(F("   IP address: "));
		log_logln(WiFi.localIP());
	}
};

#endif // WIFI_ENABLE