#include <ros.h>
#include <std_msgs/Bool.h>

#define ON 1
#define OFF 0

int state = ON;

void toggleState(const std_msgs::Bool& msg) {
  if (msg.data) {
    state = ON;
  } else {
    state = OFF;
  }
}

ros::NodeHandle nh;
ros::Subscriber<std_msgs::Bool> sub("turn_on", &toggleState);


void setup() {
  pinMode(9, OUTPUT);
  nh.initNode();
  nh.subscribe(sub);
}

void loop() {
  nh.spinOnce();
  digitalWrite(9, state);
}
