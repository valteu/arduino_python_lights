String data;
String mode;
String num_led;
int brightness;

#include <FastLED.h>

#define NUM_LEDS 12      /* The amount of pixels/leds you have */
#define DATA_PIN 3       /* The pin your data line is connected to */
#define LED_TYPE WS2812B /* I assume you have WS2812B leds, if not just change it to whatever you have */


CRGB leds[NUM_LEDS];

void setup() { 
  FastLED.clear();
  Serial.begin(9600); //initialize serial COM at 9600 baudrate
  pinMode(LED_BUILTIN, OUTPUT); //make the LED pin (13) as output
  FastLED.addLeds<LED_TYPE, DATA_PIN, RGB>(leds, NUM_LEDS);
  Serial.println("Hi!, I am Arduino");
}
 
void loop() {
  if (Serial.available()){
    for (int i = 0; i < 3; i++)
    {
      data = Serial.read();
      if (i == 0)
      {
        mode = data;
      }
      else if (i == 1){
        num_led = data;
      }
      else if (i == 2)
      {
        brightness = data.toInt();
      }
    }
    Serial.println(mode);
    Serial.println(num_led);
    Serial.println(brightness);
      /* static light*/
  modes(mode);
  }
}


String modes(String mode){

  if (mode == "0"){  /* off */
    Serial.println(mode);
    while (mode == "0"){
      for (int i = 0; i < NUM_LEDS; i++) {
        leds[i].setRGB(0, 0, 0);/* green, red, blue */
        FastLED.show();
        if (Serial.available() > 0){
          loop();
        }
        else{
          ;
         }
      }
    }
  }
  else if (mode == "1"){ /* green */
    while (mode == "1"){
      for (int i = 0; i < NUM_LEDS; i++) {
        leds[i].setRGB((2.5 * brightness), (0 * brightness), (0 * brightness));
        FastLED.show();
        if (Serial.available() > 0){
          loop();
        }
        else{
          ;
         }
      }
    }
  }
  else if (mode == "2"){ /* yellow */
    while (mode == "2"){
      for (int i = 0; i < NUM_LEDS; i++) {
        leds[i].setRGB((2.5 * brightness), (2.5 * brightness), (0 * brightness));
        FastLED.show();
        if (Serial.available() > 0){
          loop();
        }
        else{
          ;
         }
      }
    }
  }
  else if (mode == "3"){ /* red */
    while (mode == "3"){
      for (int i = 0; i < NUM_LEDS; i++) {
        leds[i].setRGB((0 * brightness), (2.5 * brightness), (0 * brightness));
        FastLED.show();
        if (Serial.available() > 0){
          loop();
        }
        else{
          ;
         }
      }
    }
  }
  else if (mode == "4"){ /* pink */
    while (mode == "4"){
      for (int i = 0; i < NUM_LEDS; i++) {
        leds[i].setRGB((0 * brightness), (2.5 * brightness), (2.5 * brightness));
        FastLED.show();
        if (Serial.available() > 0){
          loop();
        }
        else{
          ;
         }
      }
    }
  }
  else if (mode == "5"){ /* tortoise */
    while (mode == "5"){
      for (int i = 0; i < NUM_LEDS; i++) {
        leds[i].setRGB((2.5 * brightness), (0 * brightness), (2.5 * brightness));
        FastLED.show();
        if (Serial.available() > 0){
          loop();
        }
        else{
          ;
         }
      }
    }
  }
  else if (mode == "6"){ /* blue */
    while (mode == "6"){
      for (int i = 0; i < NUM_LEDS; i++) {
        leds[i].setRGB((0 * brightness), (0 * brightness), (2.5 * brightness));
        FastLED.show();
        if (Serial.available() > 0){
          loop();
        }
        else{
          ;
         }
      }
    }
  }
  else if (mode == "7"){ /* white */
    while (mode == "7"){
      for (int i = 0; i < NUM_LEDS; i++) {
        leds[i].setRGB((2.5 * brightness), (2.5 * brightness), (2.5 * brightness));
        FastLED.show();
        if (Serial.available() > 0){
          loop();
        }
        else{
          ;
         }
      }
    }                     /* light effects */
  }
  else if (mode == "10"){ /* rainbow */
    while (mode == "10"){
      for (int j = 0; j < 255; j++) {
        for (int i = 0; i < NUM_LEDS; i++) {
          leds[i] = CHSV(i - (j * 2), brightness, 255); /* The higher the value 4 the less fade there is and vice versa */ 
        }
        FastLED.show();
        delay(25); /* Change this to your hearts desire, the lower the value the faster your colors move (and vice versa) */
        }
     if (Serial.available() > 0){
          loop();
        }
        else{
          ;
         }   
     }
    }
  }
