#define ON 1
#define OFF 0

#define BLUE 11
#define RED 10

bool blue_on = false;
bool pressed = false;
int debounce_time_diff = 30;
int last_time = 0;

void setup() {
  Serial.begin(9600);
  pinMode(11, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(2, INPUT);
}

void loop() {
  if (digitalRead(2) == ON && !pressed && millis() - last_time > debounce_time_diff) {
    blue_on = !blue_on;
    last_time = millis();
    pressed = true;
    Serial.println("Button pressed");
  }

  if (digitalRead(2) == OFF) {
    pressed = false;
  }

  if (blue_on) {
    digitalWrite(BLUE, ON);
    digitalWrite(RED, OFF);
  } else {
    digitalWrite(BLUE, OFF);
    digitalWrite(RED, ON);
  }
}
