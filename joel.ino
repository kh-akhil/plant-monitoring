#include "DHT.h"

// Define the pin and DHT sensor type
#define DHTPIN 3       // Digital pin connected to the DHT sensor
#define DHTTYPE DHT22  // DHT 22 (AM2302)
#define RELAYPIN 5

// Initialize the DHT sensor
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);  // Initialize Serial communication
  pinMode(RELAYPIN, OUTPUT); // Set relay pin as output
  digitalWrite(RELAYPIN, HIGH);
  dht.begin();         // Start the DHT sensor
}

void loop() {
  if(Serial.available()>0){
    int output = Serial.parseInt();
    if(output == 1){
      digitalWrite(RELAYPIN, LOW);
      delay(10000);
      digitalWrite(RELAYPIN, HIGH);
    }
  }
  int humidity = dht.readHumidity();        // Read humidity
  int temperature = dht.readTemperature(); // Read temperature in Celsius
  int fahrenheit = dht.readTemperature(true); // Read temperature in Fahrenheit
  int moisture = analogRead(A0);

  // Check if any readings failed
  if (isnan(humidity) || isnan(temperature) || isnan(fahrenheit)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  // Print the results
  Serial.print(temperature);
  Serial.print(",");
  Serial.print(humidity);
  Serial.print(",");
  Serial.println(moisture/10);
  delay(1000);
}
