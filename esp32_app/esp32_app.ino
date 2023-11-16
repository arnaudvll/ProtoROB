#include "esp_bt_main.h"
#include "esp_bt_device.h"
#include <BLEDevice.h>
#include <BLEUtils.h>
#include <BLEServer.h>
#include <Wire.h>
#include <Adafruit_VL53L0X.h>

#define SERVICE_UUID        "78f430b0-7ee3-11ee-b962-0242ac120002"
#define CHARACTERISTIC_UUID "7fd0727c-7ee3-11ee-b962-0242ac120002"

bool sensorMode = false;

class CharacteristicCallbacks: public BLECharacteristicCallbacks {
    void onWrite(BLECharacteristic *pCharacteristic) {
      std::string value = pCharacteristic->getValue();

      if (value.length() > 0) {
        for (int i = 0; i < value.length(); i++)
          Serial.print(value[i]);
        Serial.println();

        if (value == "sensor") {
          sensorMode = true;
        } else {
          sensorMode = false;
        }
      }
    }
};

class ServerCallbacks: public BLEServerCallbacks {
  void onConnect(BLEServer* pServer) {
    Serial.print("*** Device connected ***");
  }
  void onDisconnect(BLEServer* pServer) {
    Serial.print("*** Device disconnected ***");
    pServer->startAdvertising();
  }
};

Adafruit_VL53L0X vl53 = Adafruit_VL53L0X();


void setup() {
  Serial.begin(115200);

  Wire.begin(); // Initialize the I2C communication 

  if (!vl53.begin()) {
    Serial.println(F("VL53L0X Initialization Failed"));
    while (1);
  }

  Serial.println("Starting BLE work!");

  BLEDevice::init("ESP32BT_Porte");
  BLEServer *pServer = BLEDevice::createServer();
  BLEService *pService = pServer->createService(SERVICE_UUID);
  BLECharacteristic *pCharacteristic = pService->createCharacteristic(
                                         CHARACTERISTIC_UUID,
                                         BLECharacteristic::PROPERTY_READ |
                                         BLECharacteristic::PROPERTY_WRITE
                                       );


  pServer->setCallbacks(new ServerCallbacks());                      

  pCharacteristic->setCallbacks(new CharacteristicCallbacks());

  pService->start();
  //BLEAdvertising *pAdvertising = pServer->getAdvertising();  // this still is working for backward compatibility
  BLEAdvertising *pAdvertising = BLEDevice::getAdvertising();
  pAdvertising->addServiceUUID(SERVICE_UUID);
  //pAdvertising->setScanResponse(true);
  //pAdvertising->setMinPreferred(0x06);  // functions that help with iPhone connections issue
  //pAdvertising->setMinPreferred(0x12);
  //BLEDevice::startAdvertising();
  pAdvertising->start();
  //pServer->startAdvertising();
  Serial.println("Characteristic defined! Now you ccccan read it in your phone!");

}

void loop() {
  if (sensorMode == true) {
    VL53L0X_RangingMeasurementData_t measure; // Initialize a struct to store data measured by our sensor

    if (vl53.getSingleRangingMeasurement(&measure)) { // Perform a single distance measurement, returns true on failure, false on success

      Serial.println(F("Distance Measurement Failed"));

    } else {
      std::string value = std::to_string(measure.RangeMilliMeter);
      for (int i = 0; i < value.length(); i++)
          Serial.print(value[i]);
        Serial.println();
      //Serial.print(measure.RangeMilliMeter); // Retrieve the measurement from the struct in millimeters
    }



    // Wait for a short delay between readings (optional)
    delay(100);
  }
  
}