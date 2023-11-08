/*
  ----------------------------------------------------------------------------
  File:       VL53L0X_Distance_Sensor.ino
  Description: This Arduino sketch interfaces with the VL53L0X Time-of-Flight
               distance sensor using the Adafruit VL53L0X library. It measures
               distances and displays them over a serial communication interface.
  ----------------------------------------------------------------------------
  Author:     Clément Poirié
  Date:       08/11/2000
  Version:    1.0
  ----------------------------------------------------------------------------
  Usage:
  - Ensure that the required Adafruit_VL53L0X library is installed in your Arduino IDE.
  - Connect the VL53L0X sensor to your Arduino board according to the wiring instructions.
  - Upload this sketch to your Arduino.
  - Open the serial monitor to view distance measurements in millimeters.
  ----------------------------------------------------------------------------
*/

#include <Wire.h>
#include <Adafruit_VL53L0X.h>

Adafruit_VL53L0X vl53 = Adafruit_VL53L0X();

void setup() {
  Serial.begin(115200); // Initialize serial communication to display results
  Wire.begin(); // Initialize the I2C communication

  if (!vl53.begin()) {
    Serial.println(F("VL53L0X Initialization Failed"));
    while (1);
  }
}

void loop() {
  VL53L0X_RangingMeasurementData_t measure; // Initialize a struct to store data measured by our sensor

  if (vl53.getSingleRangingMeasurement(&measure)) { // Perform a single distance measurement, returns true on failure, false on success

    Serial.println(F("Distance Measurement Failed"));

  } else {
    Serial.print(F("Distance: "));
    Serial.print(measure.RangeMilliMeter); // Retrieve the measurement from the struct in millimeters
    Serial.println(F(" mm"));
  }

  // Wait for a short delay between readings (optional)
  delay(100);
}





// #include <Wire.h>
// #include <Adafruit_VL53L0X.h>

// Adafruit_VL53L0X vl53 = Adafruit_VL53L0X();

// void setup() {
//   Serial.begin(115200); // Initialise la communication série pour afficher les résultats
//   Wire.begin(); // Initialise la liaison I2C
  
//   if (!vl53.begin()) {
//     Serial.println(F("Échec de l'initialisation du VL53L0X"));
//     while (1);
//   }
// }

// void loop() {
//   VL53L0X_RangingMeasurementData_t measure; // initialise un struct pour stocker les données mesurées par notre capteur 
    
//   if (vl53.getSingleRangingMeasurement(&measure)) { // Effectue une mesure unique de la distance retourne true si echec et false si réussi

//     Serial.println(F("Échec de la mesure de distance")); 

//   } else {
//     Serial.print(F("Distance: "));
//     Serial.print(measure.RangeMilliMeter); // récupère la mesure dans le struct en milimetre
//     Serial.println(F(" mm"));
//   }

//   // Attendez un court délai entre les lectures (facultatif)
//   delay(100);
// }
