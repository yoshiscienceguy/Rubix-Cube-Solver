
#include <Servo.h>

Servo ServoA1;
Servo ServoA2;
Servo ServoB1;
Servo ServoB2;
Servo ServoC1;
Servo ServoC2;
Servo ServoD1;
Servo ServoD2;
//2s are Claws
//1s are pinions
int sliderStart = 150;
int sliderEnd = 40;
int gripperStart = 92;
int StartClawA = 80;
int StartClawB = 85;
int StartClawC = 85;
int StartClawD = 90;

int LeftClawA = 10;
int LeftClawB = 180;
int LeftClawC = 0;
int LeftClawD = 175;

int RightClawA = 165;
int RightClawB = 0;
int RightClawC = 180;
int RightClawD = 0;
void setup() {
  // initialize the digital pin as an output.
  ServoA1.attach(4);
  ServoA2.attach(5);
  ServoB1.attach(6);
  ServoB2.attach(7);
  ServoC1.attach(8);
  ServoC2.attach(9);
  ServoD1.attach(10);
  ServoD2.attach(11);
  
  ServoA1.write(StartClawA);
  ServoA2.write(sliderStart);
  
  ServoB1.write(StartClawB);
  ServoB2.write(sliderStart);
  
  ServoC1.write(StartClawC);
  ServoC2.write(sliderStart);
  
  ServoD1.write(StartClawD);
  ServoD2.write(sliderStart);

  Serial.begin(9600);
}

void SlideIn(Servo motor) {
  motor.write(70);
}
void SlideOut(Servo motor) {
  motor.write(160);
}
void Tighten(Servo motor){
  motor.write(50);  
}
void RESET() {
  SlideOut(ServoA2);
  SlideOut(ServoB2);
  SlideOut(ServoC2);
  SlideOut(ServoD2);

  ServoA1.write(85);
  ServoB1.write(100);
  ServoC1.write(80);
  ServoD1.write(90);
}

void Close(){
   Tighten(ServoA2);
   Tighten(ServoB2);
   Tighten(ServoC2);
   Tighten(ServoD2);  
   delay(500);
}
void PeekV(){
   SlideOut(ServoB2);
   SlideOut(ServoD2);
   Tighten(ServoA2);
   Tighten(ServoC2);
   delay(1000);
   Tighten(ServoA2);
   Tighten(ServoC2);
   Tighten(ServoB2);
   Tighten(ServoD2);
   delay(1000);
}

void PeekH(){
   SlideOut(ServoA2);
   SlideOut(ServoC2);
   Tighten(ServoB2);
   Tighten(ServoD2);
   delay(1000);
   Tighten(ServoB2);
   Tighten(ServoD2);
   Tighten(ServoA2);
   Tighten(ServoC2);
   delay(1000);  
}
void RotateV(){
  ServoA1.write(StartClawA);
  ServoC1.write(StartClawC);
  ServoB1.write(StartClawB);
  ServoD1.write(StartClawD);
  Tighten(ServoA2);
  Tighten(ServoC2);
  SlideOut(ServoB2);
  SlideOut(ServoD2);
  delay(500);
  ServoA1.write(RightClawA);
  ServoC1.write(LeftClawC);
  ServoB1.write(StartClawB);
  ServoD1.write(StartClawD);
  delay(500);
  Tighten(ServoB2);
  Tighten(ServoD2);
  delay(700);
  SlideOut(ServoA2);
  SlideOut(ServoC2);
  delay(700);
  ServoA1.write(StartClawA);
  ServoC1.write(StartClawC);
  ServoB1.write(StartClawB);
  ServoD1.write(StartClawD);
  delay(700);
  Tighten(ServoB2);
  Tighten(ServoD2);
  Tighten(ServoA2);
  Tighten(ServoC2);
  delay(700);
}
void RotateH(){
  ServoA1.write(StartClawA);
  ServoC1.write(StartClawC);
  ServoB1.write(StartClawB);
  ServoD1.write(StartClawD);
  Tighten(ServoB2);
  Tighten(ServoD2);
  SlideOut(ServoA2);
  SlideOut(ServoC2);
  delay(500);
  ServoA1.write(StartClawA);
  ServoC1.write(StartClawC);
  ServoB1.write(RightClawB);
  ServoD1.write(LeftClawD);
  delay(500);
  Tighten(ServoA2);
  Tighten(ServoC2);
  delay(700);
  SlideOut(ServoB2);
  SlideOut(ServoD2);
  delay(700);
  ServoA1.write(StartClawA);
  ServoC1.write(StartClawC);
  ServoB1.write(StartClawB);
  ServoD1.write(StartClawD);
  delay(700);
  Tighten(ServoB2);
  Tighten(ServoD2);
  Tighten(ServoA2);
  Tighten(ServoC2);
  delay(700);
}
void ScanRotate() {
  for(int i = 0; i < 4; i++){
    Close();
    RotateV();
    PeekH();
    PeekV();

  }
  for(int i = 0; i < 4; i++){
    Close();
    RotateH();
    PeekV();
    PeekH();

  }

}
int n = 1;
// the loop routine runs over and over again forever:
void loop() {
  if (Serial.available() > 0) {
    n = Serial.parseInt();
    delay(1000);
    ScanRotate();
    Close();
    
//    LM();
//    LMi();
//    RM();
//    RMi();
//    UM();
//    UMi();
//    DM();
//    DMi();
//    FM();
    delay(1000);
    RESET();


  }

  // wait for a second
}


