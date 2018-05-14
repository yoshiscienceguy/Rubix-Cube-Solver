
#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>
Adafruit_PWMServoDriver servos = Adafruit_PWMServoDriver();
int ServoA2 = 5;
int ServoB2 = 7;
int ServoC2 = 9;
int ServoD2 = 11;

int ServoA1 = 4;
int ServoB1 = 6;
int ServoC1 = 8;
int ServoD1 = 10;


//2s are Claws
//1s are pinions

int StartClawA = 310;
int StartClawB = 340;
int StartClawC = 340;
int StartClawD = 345;
  
int LeftClawA = 125;
int LeftClawB = 540;
int LeftClawC = 125;
int LeftClawD = 550;

int RightClawA = 515;
int RightClawB = 120;
int RightClawC = 525;
int RightClawD = 135;


int MIN = 150;
int half = 320;
int MAX = 500;
void setup() {
  servos.begin();
  
  servos.setPWMFreq(60);
  // initialize the digital pin as an output.
  servos.setPWM(4,0,StartClawA);
  servos.setPWM(5,0,MAX);
  
  servos.setPWM(6,0,StartClawB);
  servos.setPWM(7,0,MAX);
  
  servos.setPWM(8,0,StartClawC);
  servos.setPWM(9,0,MAX);
  
  servos.setPWM(10,0,StartClawD);
  servos.setPWM(11,0,MAX);

  Serial.begin(9600);
}

void SlideIn(int motor) {
  servos.setPWM(motor,0,275);
}
void SlideOut(int motor) {
  servos.setPWM(motor,0,500);
}
void Tighten(int motor){
  servos.setPWM(motor,0,250); 
}

void RESET() {
  SlideOut(ServoA2);
  SlideOut(ServoB2);
  SlideOut(ServoC2);
  SlideOut(ServoD2);

  servos.setPWM(ServoA1,0,StartClawA); 
  servos.setPWM(ServoB1,0,StartClawB); 
  servos.setPWM(ServoC1,0,StartClawC); 
  servos.setPWM(ServoD1,0,StartClawD); 

}

void Close(){
   Tighten(ServoA2);
   Tighten(ServoB2);
   Tighten(ServoC2);
   Tighten(ServoD2);  
   delay(500);
}
void RotateV(){
  servos.setPWM(ServoA1,0,StartClawA); 
  servos.setPWM(ServoB1,0,StartClawB); 
  servos.setPWM(ServoC1,0,StartClawC); 
  servos.setPWM(ServoD1,0,StartClawD); 
  Tighten(ServoA2);
  Tighten(ServoC2);
  SlideOut(ServoB2);
  SlideOut(ServoD2);
  delay(500);
  
  servos.setPWM(ServoA1,0,RightClawA); 
  servos.setPWM(ServoB1,0,StartClawB); 
  servos.setPWM(ServoC1,0,LeftClawC); 
  servos.setPWM(ServoD1,0,StartClawD); 
  Serial.println("done");
  delay(2500);
  servos.setPWM(ServoA1,0,LeftClawA); 
  servos.setPWM(ServoB1,0,StartClawB); 
  servos.setPWM(ServoC1,0,RightClawC); 
  servos.setPWM(ServoD1,0,StartClawD); 

  Serial.println("done");
  delay(1500);
  
  servos.setPWM(ServoA1,0,StartClawA); 
  servos.setPWM(ServoB1,0,StartClawB); 
  servos.setPWM(ServoC1,0,StartClawC); 
  servos.setPWM(ServoD1,0,StartClawD); 
  delay(700);
  Tighten(ServoB2);
  Tighten(ServoD2);
  delay(700);
}
void RotateH(){
  servos.setPWM(ServoA1,0,StartClawA); 
  servos.setPWM(ServoB1,0,StartClawB); 
  servos.setPWM(ServoC1,0,StartClawC); 
  servos.setPWM(ServoD1,0,StartClawD);
  delay(500); 
  Tighten(ServoB2);
  Tighten(ServoD2);
  delay(500);
  SlideOut(ServoA2);
  SlideOut(ServoC2);
  delay(500);
  servos.setPWM(ServoA1,0,StartClawA); 
  servos.setPWM(ServoB1,0,RightClawB); 
  servos.setPWM(ServoC1,0,StartClawC); 
  servos.setPWM(ServoD1,0,LeftClawD); 
  Serial.println("done");
  delay(1500);
  Tighten(ServoA2);
  Tighten(ServoC2);
  delay(400);
  SlideOut(ServoB2);
  SlideOut(ServoD2);
  
  delay(500);
}
void ScanRotate() {
  for(int i = 0; i < 4; i++){
    //Close();
    
    RotateH();
    //PeekH();
    //PeekV();

  }

    //Close();
    RotateV();
    //PeekV();
    
    //PeekH();



}
int n = 1;
// the loop routine runs over and over again forever:
void loop() {
  if (Serial.available() > 0) {
    n = Serial.parseInt();
    Close();
    delay(300);
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


