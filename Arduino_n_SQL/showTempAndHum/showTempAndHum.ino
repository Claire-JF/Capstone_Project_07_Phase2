#include <DallasTemperature.h>
#define ONE_WIRE_BUS 4      //1-wire data bus connection at IO4
OneWire oneWire(ONE_WIRE_BUS);       //declaration
DallasTemperature sensors(&oneWire); //declaration
#include <dht11.h>       //Use the dht11 library
#define DHT11PIN 2   //Pin number of dht11 is defined as pin number 2
dht11 DHT11;      

void setup(void)
{
  Serial.begin(9600);
  Serial.println("");
  sensors.begin(); //initialization
  sensors.setWaitForConversion(false); //Set to non-blocking mode
  pinMode(DHT11PIN,OUTPUT); //Define the humidity module out pin
}

unsigned long previousMillis = 0; //Millisecond time recording
const long interval = 5000;       //Time interval
void loop(void)
{
  //The previous temperature is read every second and a new temperature conversion is initiated
  unsigned long currentMillis = millis();
  int chk = DHT11.read(DHT11PIN);
  int tem=(float)DHT11.temperature;//Obtain temperature
  int hum=(float)DHT11.humidity;//Obtain humidity
  if (currentMillis - previousMillis >= interval)//If the previous time is greater than or equal to the time interval
  {
    previousMillis = currentMillis;//Update time record

    float tempC = sensors.getTempCByIndex(0); 
    if (tempC != DEVICE_DISCONNECTED_C)//Data legalization
    {
      Serial.print("Temperature:");
      Serial.print(tempC);
      Serial.print("℃");
      Serial.print(",");
    }
    sensors.requestTemperatures();//Initiate a new temperature transition
    Serial.print("Humidity:");
    Serial.print(hum);
    Serial.println("%");
  }
  delay(3600000);//Update for each hour
}
