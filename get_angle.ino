#include <Servo.h>
#include<math.h>
Servo Shoulder_Joint;
Servo Elbow_Joint;
Servo Wrist_Joint;

float X2;
float Y2;
float point;

int i;
float CurrentAngle; 

float shoulder_length = 40.0;
float elbow_length = 20.0;
float wrist_length = 10.0;



int theta_one,theta_two,theta_three,theta_not;
int phi1,phi2,phi3;
float pi = 3.141569;

float Shoulder_angle, Elbow_angle, Wrist_angle; //Servo angles
#define PI 3.14159265
int data;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Shoulder_Joint.attach(11  );
  Elbow_Joint.attach(10);
  Wrist_Joint.attach(9);
  pinMode(13, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  
  if(Serial.available() > 3){
      data = Serial.read();
      if(data == 255)
      {
         Shoulder_angle = Serial.read();
         Elbow_angle = Serial.read();
         Wrist_angle = Serial.read();  
      }
        if (!isnan(Shoulder_angle)) 
     { //If Angle is a valid number.
    //Serial.println(Shoulder_angle);
    Shoulder_Joint.write(Shoulder_angle);
    delay(1000);
  }
  
 
    if (!isnan(Elbow_angle)) 
     { //If Angle is a valid number.
    //Serial.println(Shoulder_angle);
    Elbow_Joint.write(Elbow_angle);
    delay(1000);
  }
  if (!isnan(Wrist_angle)) 
     { //If Angle is a valid number.
    //Serial.println(Shoulder_angle);
    Wrist_Joint.write(Wrist_angle);
    delay(1000);
     }
  
  }      

   
   delay(4000);
}


/* if (!isnan(Elbow_angle)) { //If Angle is a valid number.

    CurrentAngle = Elbow_Joint.read();

    if (Elbow_angle > CurrentAngle) {
      Serial.println(Elbow_angle);
      for (i = CurrentAngle; i < Elbow_angle; i = i + 1) //if Elbow_angle > CurrentAngle.
      {

        Elbow_Joint.write(i);
        delay(5);
      }//end for CurrentAngle.
      
    }//end if Elbow_angle > CurrentAngle.

    else
    {
      //Serial.println(Elbow_angle);
      for (i = CurrentAngle; i > Elbow_angle; i = i - 1) //if Elbow_angle < CurrentAngle.
      {

        Elbow_Joint.write(i);
        delay(5);
      }//end for CurrentAngle.
    }//end else.

  }

  if (!isnan(Wrist_angle)) { //If Angle is a valid number.

    CurrentAngle = Wrist_Joint.read();

    if (Wrist_angle > CurrentAngle) {
      Serial.println(Wrist_angle);
      for (i = CurrentAngle; i < Wrist_angle; i = i + 1) //if Wrist_angle > CurrentAngle.
      {

        Wrist_Joint.write(i);
        delay(5);
      }//end for CurrentAngle.

    }//end if Wrist_angle > CurrentAngle.

    else
    {
      Serial.println(Wrist_angle);
      for (i = CurrentAngle; i > Wrist_angle; i = i - 1) //if Wrist_angle < CurrentAngle.
      {

        Wrist_Joint.write(i);
        delay(5);
      }//end for CurrentAngle.
    }//end else.*/

  
 

  
