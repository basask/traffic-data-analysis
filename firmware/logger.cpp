#include <Wire.h>
#include <VL53L0X.h>

VL53L0X sensor;

unsigned long currentMillis = 0;
int distance;

void setup() {
  Serial.begin(9600);
  Wire.begin();
  sensor.init();
  sensor.setTimeout(500);
  sensor.setMeasurementTimingBudget(20000);
}

void loop() {
  currentMillis = millis();
  distance = sensor.readRangeSingleMillimeters();
  if(distance < 8189){
      Serial.print(currentMillis);
      Serial.print(',');
      Serial.println(distance);
  }
}