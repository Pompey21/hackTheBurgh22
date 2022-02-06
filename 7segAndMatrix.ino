#include "Timer.h" //include timer library
#include "LedControl.h"

LedControl lc=LedControl(14,15,16,1);
/* we always wait a bit between updates of the display */
unsigned long delaytime1=500;
unsigned long delaytime2=50;

long count = 0;
Timer t; // craete a timer object
long number = 0; //declear the variables
int first_digit = 0;
int second_digit = 0;
int third_digit = 0;
int fourth_digit = 0;
int timer_event = 0;
int CA_1 = 12;
int CA_2 = 11;
int CA_3 = 10;
int CA_4 = 9;
int clk = 6;
int latch = 5;
int data = 4;
int digits[4] ;
int CAS[4] = {12, 11, 10, 9};
byte numbers[21] {B11111100, B01100000, B11011010, B11110010, B01100110, B10110110, B10111110, B11100000, B11111110, B11110110,
                  B11111101, B01100001, B11011011, B11110011, B01100111, B10110111, B10111111, B11100001, B11111111, B11110111,
                  B00000000};

int slidecounter = 0;
long updateInterval = 100000;
int currentPol = 150;
int currentImg = 0;

int randomBias = 10;
//byte combinations for each number 0-9
void setup() {
  Serial.begin(9600); //serial start and pin config
  pinMode(CA_1, OUTPUT);
  pinMode(CA_2, OUTPUT);
  pinMode(CA_3, OUTPUT);
  pinMode(CA_4, OUTPUT);
  pinMode(clk, OUTPUT);
  pinMode(latch, OUTPUT);
  pinMode(data, OUTPUT);
  digitalWrite(CA_1, HIGH);
  digitalWrite(CA_2, HIGH);
  digitalWrite(CA_3, HIGH);
  digitalWrite(CA_4, HIGH);

  lc.shutdown(0,false);
  /* Set the brightness to a medium values */
  lc.setIntensity(0,2);
  /* and clear the display */
  lc.clearDisplay(0);
  
  break_number(1234, 0);
  timer_event = t.every(1, display_number);
  Serial.println("please Enter a number from 0 to 9999");
}

void loop() {
  slidecounter = slidecounter + 1;
  t.update(); //timer update
  if (Serial.available()) { // read from serial
    t.stop(timer_event); //stop timer if anythign to read
    cathode_high(); // blank the screen
    String s = Serial.readString(); //read the serail value
    // Decimal place stuff
    int dpIndex = s.indexOf(".");
    s.remove(dpIndex,1);
    number = (long)s.toInt(); //convert it to int
    if (number > 9999) { //check the number is 0-9999
      Serial.println("Please Enter Number Between 0 - 9999");
    } else {
      break_number(number, dpIndex);
      timer_event = t.every(1, display_number); // start timer again
    }
  }

  if (slidecounter % updateInterval == 0) {
    
    writeArduinoOnMatrix((int)((slidecounter / updateInterval)% (6 * updateInterval)));
    
  }
  if (slidecounter % (updateInterval/4) == 0) {
      currentPol += random(-10,10 + randomBias);
  if (currentPol < 20) {
    currentPol += 100;
  }
  if (currentPol > 300) {
    randomBias = 0;
  }
  break_number(currentPol, 3); 
  }
}

void break_number(long num, int dpIndex) { // seperate the input number into 4 single digits

  first_digit = num / 1000;
  if (dpIndex == 1) {
    digits[0] = first_digit + 10;
  } else {
    if (first_digit != 0) {
          digits[0] = first_digit;  
    } else {
      digits[0] = 20;
    }
  }

  int first_left = num - (first_digit * 1000);
  second_digit = first_left / 100;
  if (dpIndex == 2) {
    digits[1] = second_digit + 10;
  } else {
    digits[1] = second_digit;
  }
  int second_left = first_left - (second_digit * 100);
  third_digit = second_left / 10;
  if (dpIndex == 3) {
    digits[2] = third_digit + 10;
  } else {
    digits[2] = third_digit;
  }
  fourth_digit = second_left - (third_digit * 10);
  digits[3] = fourth_digit;
  if (dpIndex == 4) {
    digits[3] = fourth_digit + 10;
  } else {
    digits[3] = fourth_digit;
  }
}

void display_number() { //scanning

  cathode_high(); //black screen
  digitalWrite(latch, LOW); //put the shift register to read
  shiftOut(data, clk, LSBFIRST, numbers[digits[count]]); //send the data
  digitalWrite(CAS[count], LOW); //turn on the relevent digit
  digitalWrite(latch, HIGH); //put the shift register to write mode
  count++; //count up the digit
  if (count == 4) { // keep the count between 0-3
    count = 0;
  }
}

void cathode_high() { //turn off all 4 digits
  digitalWrite(CA_1, HIGH);
  digitalWrite(CA_2, HIGH);
  digitalWrite(CA_3, HIGH);
  digitalWrite(CA_4, HIGH);
}




/*
 This method will display the characters for the
 word "Arduino" one after the other on the matrix. 
 (you need at least 5x7 leds to see the whole chars)
 */
void writeArduinoOnMatrix(int imgNumber) {
  /* here is the data for the characters */
  byte house[8] =  {B00011000,B00111100,B01111110,B11111111,B01011010,B01111110,B01101110,B01101110};
  byte tick[8] =  {B00000000,B00000000,B00000001,B00000010,B01000100,B00101000,B00010000,B00000000};
  byte smile[8] = {B00000000,B00000000,B00100100,B00100100,B00000000,B01000010,B00111100,B00000000};
  byte sad[8] = {B00000000,B00000000,B01100110,B00100100,B00000000,B01111110,B01000010,B00000000};
  byte cross[8] =  {B00000000,B01000010,B00100100,B00011000,B00011000,B00100100,B01000010,B00000000};
  byte man[8] = {B00000111,B00000011,B00100001,B11111001,B00100001,B00100001,B01010001,B10001001};
  byte image[8];

  currentImg += 1;

  if (currentPol < 250) {
      if (currentImg % 3 == 0) { memcpy(image, smile, sizeof(smile[0])*8);}
      else if (currentImg % 3 == 1) { memcpy(image, tick, sizeof(tick[0])*8);}
      else if (currentImg % 3 == 2) { memcpy(image, man, sizeof(man[0])*8);}
  } else {
    if (currentImg % 3 == 0) { memcpy(image, house, sizeof(house[0])*8);}
    else if (currentImg % 3 == 1) { memcpy(image, sad, sizeof(sad[0])*8);}
    else if (currentImg % 3 == 2) { memcpy(image, cross, sizeof(cross[0])*8);} 
  }

 

  /* now display them one by one with a small delay */
  lc.setRow(0,0,image[0]);
  lc.setRow(0,1,image[1]);
  lc.setRow(0,2,image[2]);
  lc.setRow(0,3,image[3]);
  lc.setRow(0,4,image[4]);
  lc.setRow(0,5,image[5]);
  lc.setRow(0,6,image[6]);
  lc.setRow(0,7,image[7]);
}
