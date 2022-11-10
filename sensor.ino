
#include<dht.h>
dht DHT;
#define DHT11_PIN 8

void setup(){

  Serial.begin(9600);
}

void loop(){
  DHT.read11(DHT11_PIN);
  //Serial.print(" ");
  Serial.print(DHT.temperature);
  //Serial.println(" Celsius");
  //Serial.print("  ");
  Serial.print(DHT.humidity);
  //Serial.println(" %");
  delay(2000);

  Serial.println();
}
