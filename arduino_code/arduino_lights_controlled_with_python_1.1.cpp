String data;
String mode;
double green;
double red;
double blue;
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
  Serial.println("1.dsdsa");
  if (Serial.available()){
    Serial.println("2.dsdsa");
    for (int i = 0; i < 6; i++)
    {
      Serial.println("3.dsdsa");
      data = Serial.read();
      if (i == 0)
      {
        mode = data;
      }
      else if (i == 1){
        green = data.toDouble();
      }
      else if (i == 2)
      {
        red = data.toDouble();
      }
      else if (i == 3)
      {
        blue = data.toDouble();
      }
      else if (i == 4)
      {
        num_led = data.toInt();
      }
      else if (i == 5)
      {
        brightness = data.toInt();
      }
    }
    Serial.println(mode);
    Serial.println(num_led);
    Serial.println(brightness);
      /* static light*/
  modes(mode, green/100, red/100, blue/100, brightness);
  }
}


String modes(String mode, double green, double red, double blue, int brightness){

  if (mode == "0"){  /* off */
    FastLED.clear();
    Serial.println(mode);
    while (mode == "0"){
      for (int i = 0; i < NUM_LEDS; i++) {
        leds[i].setRGB(0, 0, 0);/* green, red, blue */
        FastLED.show();
        
      }
      if (Serial.available() > 0){
          loop();
        }
      else{
        ;
       }
    }
  }
  else if (mode == "1"){ /* green */
    FastLED.clear();
    while (mode == "1"){
      for (int i = 0; i < NUM_LEDS; i++) {
        leds[i].setRGB((green * brightness), (red * brightness), (blue * brightness));
        FastLED.show();
      }
      if (Serial.available() > 0){
          loop();
        }
      else{
        ;
       }
    }
  }                  /* light effects */
  else if (mode == "10"){ /* rainbow */
    FastLED.clear();
    while (mode == "10"){
      for (int j = 0; j < 255; j++) {
        for (int i = 0; i < NUM_LEDS; i++) {
          leds[i] = CHSV(i - (j * 2), 255, brightness); /* The higher the value 4 the less fade there is and vice versa */ 
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
  else if (mode == "11"){ /* fade */
    FastLED.clear();
    while (mode == "11"){
    for( int colorStep=0; colorStep<256; colorStep++ ) {
  
        int r = colorStep;  // Redness starts at zero and goes up to full
        int b = 255-colorStep;  // Blue starts at full and goes down to zero
        int g = colorStep -255;  // No green needed to go from blue to red
  
        for(int x = 0; x < NUM_LEDS; x++){
            leds[x] = CRGB(r,g,b);
        }
        FastLED.show();
        delay(10);
      if (Serial.available() > 0){
          loop();
        }
        else{
          ;
         }
      }
    }
  }
  else if (mode == "12"){ /* ball */
    FastLED.clear();
    while (mode == "12"){
      for (int i = 0; i < NUM_LEDS; i++)
      {
        leds[i] = CRGB::Red;
        FastLED.show();
        delay(100);
        leds[i] = CRGB::Black;
      }
      for (int i = NUM_LEDS - 1; i >= 0; i--)
      {
        leds[i] = CRGB::Red;
        FastLED.show();
        delay(100);
        leds[i] = CRGB::Black;
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
