#include <dht11.h>
dht11 DHT11;
#define DHT11PIN 2
void setup(){
  Serial.begin(9600);
}

void loop(){
  int chk = DHT11.read(DHT11PIN);
  Serial.print("Temperature: ");
  Serial.print((float)DHT11.temperature, 2);
  Serial.print("℃");
  Serial.print(",");
  Serial.print("Humidity: ");
  Serial.print((float)DHT11.humidity, 2);
  Serial.println("%");


  delay(3600000);//Updated every hour
}
