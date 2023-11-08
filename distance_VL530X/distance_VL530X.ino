#include <Wire.h>
#include <Adafruit_VL53L0X.h>

Adafruit_VL53L0X vl53 = Adafruit_VL53L0X();

void setup() {
  Serial.begin(115200); // Initialise la communication série pour afficher les résultats
  Wire.begin(); // Initialise la liaison I2C
  
  if (!vl53.begin()) {
    Serial.println(F("Échec de l'initialisation du VL53L0X"));
    while (1);
  }
}

void loop() {
  VL53L0X_RangingMeasurementData_t measure; // initialise un struct pour stocker les données mesurées par notre capteur 
    
  if (vl53.getSingleRangingMeasurement(&measure)) { // Effectue une mesure unique de la distance retourne true si echec et false si réussi

    Serial.println(F("Échec de la mesure de distance")); 

  } else {
    Serial.print(F("Distance: "));
    Serial.print(measure.RangeMilliMeter); // récupère la mesure dans le struct en milimetre
    Serial.println(F(" mm"));
  }

  // Attendez un court délai entre les lectures (facultatif)
  delay(100);
}
