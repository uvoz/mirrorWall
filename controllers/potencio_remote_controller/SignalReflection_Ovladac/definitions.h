
#include <arduino.h>

#define DEBUG_ENABLE
#define LOG_ENABLE

/*Board services*/
#define WIFI_ENABLE
//#define OTA_ENABLE
#define MQTT_ENABLE



/*Service settings*/

#define MQTT_PAYLOAD_MAX 64

#define MQTT_TOPIC_ROOT BOARD_NAME

#define MQTT_TOPIC_STATE MQTT_TOPIC_ROOT "/STA"

#define MQTT_TOPIC_OPERATOR MQTT_TOPIC_ROOT "/OPE"
#define MQTT_TOPIC_OPERATOR_CARDID MQTT_TOPIC_OPERATOR "/CID"
//#define MQTT_TOPIC_OPERATOR_CARDDATA MQTT_TOPIC_OPERATOR "/CDA"

#define MQTT_TOPIC_TRACKING MQTT_TOPIC_ROOT "/TRA"

#define MQTT_TOPIC_RUN MQTT_TOPIC_ROOT "/RUN"

#define MQTT_TOPIC_ACESS MQTT_TOPIC_ROOT "/ACE"

#define NO_MESSAGE ""

//==============================================================

#ifdef DEBUG_ENABLE

#define log_debugln(x); Serial.println(x);
#define log_debug(x); Serial.print(x);
#define log_debugf(a,b); Serial.printf(a,b);

#else

#define log_debugln(x); 
#define log_debug(x); 
#define log_debugf(a,b);  

#endif

#ifdef LOG_ENABLE

#define log_logln(x); Serial.println(x);
#define log_log(x); Serial.print(x);
#define log_logf(a,b); Serial.printf(a,b);

#else

#define log_logln(x);
#define log_log(x);
#define log_logf(a,b);  

#endif

