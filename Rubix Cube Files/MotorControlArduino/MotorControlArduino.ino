
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

int StartClawA = 280;
int StartClawB = 280;
int StartClawC = 300;
int StartClawD = 260;

int LeftClawA = 120;
int LeftClawB = 490;
int LeftClawC = 115;
int LeftClawD = 490;

int RightClawA = 460;
int RightClawB = 100;
int RightClawC = 500;
int RightClawD = 95;


int MinA = 210;
int MinB = 130;
int MinC = 190;
int MinD = 220;

int half = 320;

int MAXA= 450;
int MAXB= 350;
int MAXC= 430;
int MAXD= 410;
void setup() {
  servos.begin();

  servos.setPWMFreq(60);
  
  // initialize the digital pin as an output.
  servos.setPWM(4,0,StartClawA);
  servos.setPWM(5,0,MAXA);

  servos.setPWM(6,0,StartClawB);
  servos.setPWM(7,0,MAXB);

  servos.setPWM(8,0,StartClawC);
  servos.setPWM(9,0,MAXC);

  servos.setPWM(10,0,StartClawD);
  servos.setPWM(11,0,MAXD);
  
  
  Serial.begin(9600);
  
}

void SlideIn(int motor) {
  servos.setPWM(motor,0,275);
}
void SlideOut(int motor) {
  if(motor == 5){
    servos.setPWM(motor,0,MAXA);
  }
  if(motor == 7){
    servos.setPWM(motor,0,MAXB);
  }
  if(motor == 9){
    servos.setPWM(motor,0,MAXC);
  }
  if(motor == 11){
    servos.setPWM(motor,0,MAXD);
  }
  
}
void Tighten(int motor,int Min){
  servos.setPWM(motor,0,Min); 
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
  Tighten(ServoA2,MinA);
  Tighten(ServoB2,MinB);
  Tighten(ServoC2,MinC);
  Tighten(ServoD2,MinD);  
  delay(500);
}
void RotateV(){
  servos.setPWM(ServoA1,0,StartClawA); 
  servos.setPWM(ServoB1,0,StartClawB); 
  servos.setPWM(ServoC1,0,StartClawC); 
  servos.setPWM(ServoD1,0,StartClawD); 
  Tighten(ServoA2,MinA);
  Tighten(ServoC2,MinC);
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
  Tighten(ServoB2,MinB);
  Tighten(ServoD2,MinD);
  delay(700);
}
void RotateH(){
  servos.setPWM(ServoA1,0,StartClawA); 
  servos.setPWM(ServoB1,0,StartClawB); 
  servos.setPWM(ServoC1,0,StartClawC); 
  servos.setPWM(ServoD1,0,StartClawD);
  delay(500); 
  Tighten(ServoB2,MinB);
  Tighten(ServoD2,MinD);
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
  Tighten(ServoA2,MinA);
  Tighten(ServoC2,MinC);
  delay(800);
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
    Serial.println(n);
    if(n == 1){
      Close();
      delay(300);
      ScanRotate();
      Close();

    }
    if(n == 2){
      n = Serial.parseInt();
      if(n == 0){
        Right(false);
      }
      else{
        Right(true);
      }
      Serial.println("done");
    }
    if(n == 3){
      n = Serial.parseInt();
      if(n == 0){
        Left(false);
      }
      else{
        Left(true);
      }
      Serial.println("done");
    }
    if(n == 4){
      n = Serial.parseInt();
      if(n == 0){
        Top(false);
      }
      else{
        Top(true);
      }
      Serial.println("done");
    }
    if(n == 5){
      n = Serial.parseInt();
      if(n == 0){
        Bottom(false);
      }
      else{
        Bottom(true);
      }
      Serial.println("done");
    }
    if(n == 6){
      n = Serial.parseInt();
      if(n == 0){
        Back(false);
      }
      else{
        Back(true);
      }
      Serial.println("done");
    }
    if(n == 7){
      n = Serial.parseInt();
      if(n == 0){
        Front(false);
      }
      else{
        Front(true);
      }
      Serial.println("done");
    }

  }

  // wait for a second
}

void Right(boolean reversed){
  Close();
  delay(500);
  if(reversed){
    servos.setPWM(ServoA1,0,LeftClawA);
  }
  else{
    servos.setPWM(ServoA1,0,RightClawA);
  }
  delay(500);

  SlideOut(ServoA2);
  delay(500);
  servos.setPWM(ServoA1,0,StartClawA);
  delay(500);

  Tighten(ServoA2,MinA);



}
void Left(boolean reversed){
  Close();
  delay(500);
  if(reversed){
    servos.setPWM(ServoC1,0,LeftClawC);
  }
  else{
    servos.setPWM(ServoC1,0,RightClawC);
  }
  delay(500);

  SlideOut(ServoC2);
  delay(500);
  servos.setPWM(ServoC1,0,StartClawC);
  delay(500);
  Tighten(ServoC2,MinC);
}

void Top(boolean reversed){
  Close();
  delay(500);
  if(reversed){
    servos.setPWM(ServoB1,0,RightClawB);
  }
  else{
    servos.setPWM(ServoB1,0,LeftClawB);
  }
  delay(500);

  SlideOut(ServoB2);
  delay(500);
  servos.setPWM(ServoB1,0,StartClawB);
  delay(500);
  Tighten(ServoB2,MinB);
}

void Bottom(boolean reversed){
  Close();
  delay(500);
  if(reversed){
    servos.setPWM(ServoD1,0,RightClawD);
  }
  else{
    servos.setPWM(ServoD1,0,LeftClawD);
  }
  delay(1500);

  SlideOut(ServoD2);
  delay(1000);
  servos.setPWM(ServoD1,0,StartClawD);
  delay(1500);
  Tighten(ServoD2,MinD);
}

void Back(boolean reversed){
  Close();
  delay(500);
  SlideOut(ServoA2);
  SlideOut(ServoC2);
  delay(500);
  servos.setPWM(ServoA1,0,StartClawA); 
  servos.setPWM(ServoB1,0,LeftClawB); 
  servos.setPWM(ServoC1,0,StartClawC); 
  servos.setPWM(ServoD1,0,RightClawD); 
  delay(700);
  Tighten(ServoA2,MinA);
  Tighten(ServoC2,MinC);
  delay(500);
  SlideOut(ServoB2);
  SlideOut(ServoD2);
  delay(500);
  servos.setPWM(ServoA1,0,StartClawA); 
  servos.setPWM(ServoB1,0,StartClawB); 
  servos.setPWM(ServoC1,0,StartClawC); 
  servos.setPWM(ServoD1,0,StartClawD); 
  delay(700);
  Right(reversed);
  delay(500);
  SlideOut(ServoB2);
  SlideOut(ServoD2);
  delay(500);
  servos.setPWM(ServoA1,0,StartClawA); 
  servos.setPWM(ServoB1,0,LeftClawB); 
  servos.setPWM(ServoC1,0,StartClawC); 
  servos.setPWM(ServoD1,0,RightClawD); 
  delay(700);
  Tighten(ServoB2,MinB);
  Tighten(ServoD2,MinD);
  delay(500);
  SlideOut(ServoA2);
  SlideOut(ServoC2);
  delay(500);
  servos.setPWM(ServoA1,0,StartClawA); 
  servos.setPWM(ServoB1,0,StartClawB); 
  servos.setPWM(ServoC1,0,StartClawC); 
  servos.setPWM(ServoD1,0,StartClawD);   
  delay(500);
  Close();
}
void Front(boolean reversed){
  Close();
  delay(500);
  SlideOut(ServoA2);
  SlideOut(ServoC2);
  delay(500);
  servos.setPWM(ServoA1,0,StartClawA); 
  servos.setPWM(ServoB1,0,LeftClawB); 
  servos.setPWM(ServoC1,0,StartClawC); 
  servos.setPWM(ServoD1,0,RightClawD); 
  delay(700);
  Tighten(ServoA2,MinA);
  Tighten(ServoC2,MinC);
  delay(500);
  SlideOut(ServoB2);
  SlideOut(ServoD2);
  delay(500);
  servos.setPWM(ServoA1,0,StartClawA); 
  servos.setPWM(ServoB1,0,StartClawB); 
  servos.setPWM(ServoC1,0,StartClawC); 
  servos.setPWM(ServoD1,0,StartClawD); 
  delay(700);
  Left(reversed);
  delay(500);
  SlideOut(ServoB2);
  SlideOut(ServoD2);
  delay(500);
  servos.setPWM(ServoA1,0,StartClawA); 
  servos.setPWM(ServoB1,0,LeftClawB); 
  servos.setPWM(ServoC1,0,StartClawC); 
  servos.setPWM(ServoD1,0,RightClawD); 
  delay(700);
  Tighten(ServoB2,MinB);
  Tighten(ServoD2,MinD);
  delay(500);
  SlideOut(ServoA2);
  SlideOut(ServoC2);
  delay(500);
  servos.setPWM(ServoA1,0,StartClawA); 
  servos.setPWM(ServoB1,0,StartClawB); 
  servos.setPWM(ServoC1,0,StartClawC); 
  servos.setPWM(ServoD1,0,StartClawD);   
  delay(500);
  Close();
}



