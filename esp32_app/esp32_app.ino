#include <Wire.h>
#include <Adafruit_VL53L0X.h>


Adafruit_VL53L0X vl53 = Adafruit_VL53L0X();



void setup() {
  Serial.begin(115200); // Initialise la communication série pour afficher les résultats
  Wire.begin(21, 22); // Initialise la communication I2C avec les broches SDA sur 21 et SCL sur 22 (à adapter selon votre configuration)
  

  if (!vl53.begin()) {
    Serial.println(F("Échec de l'initialisation du capteur VL53L0X"));
    while (1);
  }
}

void loop() {
  VL53L0X_RangingMeasurementData_t measure; // Initialise une structure pour stocker les données mesurées par le capteur

  if (vl53.getSingleRangingMeasurement(&measure)) { // Effectue une mesure de distance unique, renvoie true en cas d'échec, false en cas de succès

    Serial.println(F("Échec de la mesure de distance"));

  } else {
    Serial.print(F("Distance : "));
    Serial.print(measure.RangeMilliMeter); // Récupère la mesure de la structure en millimètres
    Serial.println(F(" mm"));
  }

  // Attendre un court délai entre les lectures (facultatif)
  delay(100);
}
