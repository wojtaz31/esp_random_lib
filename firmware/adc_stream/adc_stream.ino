#define NOISE_PIN 5

void setup(){
  Serial.begin(115200);
  pinMode(NOISE_PIN, INPUT);
}

void loop(){
  byte randomByte = 0;

  for(int i=0; i<8; ++i) {
    int analogNoise = analogRead(NOISE_PIN);
    byte lsb = (analogNoise & 0x01);
    
    // bitwise adding lsb on i-th position of byte
    randomByte |= (lsb << i);
    delayMicroseconds(50);
  }

  Serial.write(randomByte);
}