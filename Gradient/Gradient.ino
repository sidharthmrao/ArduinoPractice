#define ON 1
#define OFF 0

int timeInterval = 100;

void setup() {
  pinMode(11, OUTPUT);
  pinMode(10, OUTPUT);
}

void loop() {
  int i = 0;
  while (i < 255) {
    analogWrite(11, i);
    analogWrite(10, 255 - i);
    delay(10);
    i += 5;
  }
  i = 0;
  while (i < 255) {
    analogWrite(11, 255 - i);
    analogWrite(10, i);
    delay(10);
    i += 5;
  }

}
