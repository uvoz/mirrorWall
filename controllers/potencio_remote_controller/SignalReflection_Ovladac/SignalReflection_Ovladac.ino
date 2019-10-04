// Visual Micro is in vMicro>General>Tutorial Mode
// 
/*
	Name:       SignalReflection_Ovladac.ino
	Created:	1.10.2019 10:02:34
	Author:     MATES-PC\Mates
*/

// Define User Types below here or use a .h file
//


// Define Function Prototypes that use User Types below here or use a .h file
//


// Define Functions below here or use other .ino or cpp files
//

// The setup() function runs once each time the micro-controller starts



#include <WiFi.h>
#include <PubSubClient.h>
#include <math.h>
#include <FastLED.h>


#include "module.h"
#include "wifi_module.h"
#include "mqtt_module.h"


#define LED_PIN     4
#define NUM_LEDS    24
#define BRIGHTNESS  64
#define LED_TYPE    WS2812B
#define COLOR_ORDER GRB

#define SERIAL_BAUD 115200

#define POT1_PIN 34
#define POT2_PIN 39
#define POT3_PIN 35

#define FPS 50
#define MAX_LAG_SECONDS 2

CRGB leds[NUM_LEDS];

ModuleWifi wifi;
ModuleMqtt mqtt;

int movementsX[FPS * MAX_LAG_SECONDS];
int movementsY[FPS * MAX_LAG_SECONDS];




void setup()
{
	FastLED.addLeds<LED_TYPE, LED_PIN, COLOR_ORDER>(leds, NUM_LEDS).setCorrection(TypicalLEDStrip);
	FastLED.setBrightness(BRIGHTNESS);

	pinMode(POT1_PIN, INPUT);
	pinMode(POT2_PIN, INPUT);
	pinMode(POT3_PIN, INPUT);

	Serial.begin(SERIAL_BAUD);

	wifi.begin();
	mqtt.begin();


	/*mqtt.publish("movemirror", "{\"mirror\":42,\"ud\":-20,\"lr\":-20}");
	delay(1000);
	mqtt.publish("movemirror", "{\"mirror\":42,\"ud\":20,\"lr\":20}");
	delay(1000);*/
}



// Add the main program code into the continuous loop() function
void loop()
{
	static unsigned long millis_last = 0;

	if (millis() - millis_last >= 1000 / FPS) {
		millis_last = millis();

		int angleX = map(analogRead(POT1_PIN), 0, 4095, 140, 1440);
		int angleY = map(analogRead(POT2_PIN), 0, 4095, 140, 1440);
		int lag = map(analogRead(POT3_PIN), 0, 4095, 0, FPS * MAX_LAG_SECONDS);

		int led_count = map(lag, 0, FPS * MAX_LAG_SECONDS, 0, NUM_LEDS);
		
		for (int i = 0; i < NUM_LEDS; i++)
			leds[i] = CRGB::Black;

		for (int i = 0; i < led_count; i++)
			leds[i] = CRGB::White;

		FastLED.show();

		//Serial.println(angle);

		for (int i = FPS * MAX_LAG_SECONDS - 1; i >= 1; i--)
		{
			movementsX[i] = movementsX[i - 1];
			movementsY[i] = movementsY[i - 1];
		}
		movementsX[0] = angleX;
		movementsY[0] = angleY;
		//Serial.println(angle);


		for (size_t i = 0; i < 16; i+=2)
		{
			int j = map(i, 0, 16, 0, lag);

			float x = movementsX[j] / 10.0;
			float y = movementsY[j] / 10.0;

			String msgX = "{\"bonnet\":0,\"servo\":" + String(i) + ",\"angle\":" + String(x) + "}";
			String msgY = "{\"bonnet\":0,\"servo\":" + String(i+1) + ",\"angle\":" + String(y) + "}";
			//Serial.println(msg);

			mqtt.publish("hub1/pinlevelapi", msgX);
			mqtt.publish("hub1/pinlevelapi", msgY);
		}

	}

	delayMicroseconds(500);
}
