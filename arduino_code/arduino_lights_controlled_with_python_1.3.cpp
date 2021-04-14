String data;
String mode;
double green;
double red;
double blue;
String num_led;
int brightness;
byte gHue; 
bool gReverseDirection = false;
int current_strip;

#include <FastLED.h>

#define DATA_PIN 3       /* The pin your data line is connected to */
#define LED_TYPE WS2812B /* I assume you have WS2812B leds, if not just change it to whatever you have */
#define COLOR_ORDER GRB
#define COOLING  55
#define SPARKING 120
#define NUM_STRIPS 3


CRGB leds[NUM_LEDS];
CLEDController *controllers[NUM_STRIPS];

void setup() { 
  FastLED.clear();
  Serial.begin(9600); //initialize serial COM at 9600 baudrate
  pinMode(LED_BUILTIN, OUTPUT); //make the LED pin (13) as output
  controllers[0] = &FastLED.addLeds<LED_TYPE, 3, COLOR_ORDER>(leds, NUM_LEDS).setCorrection( TypicalLEDStrip );
  controllers[1] = &FastLED.addLeds<LED_TYPE, 5, COLOR_ORDER>(leds, NUM_LEDS).setCorrection( TypicalLEDStrip );
  controllers[2] = &FastLED.addLeds<LED_TYPE, 6, COLOR_ORDER>(leds, NUM_LEDS).setCorrection( TypicalLEDStrip );
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
        current_strip = data.toInt();
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
  modes(mode, green/100, red/100, blue/100, brightness, current_strip);
  }
}


String modes(String mode, double green, double red, double blue, int brightness, int current_strip){

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
        leds[i].setRGB((red * brightness), (green * brightness), (blue * brightness));
      }
      if (Serial.available() > 0){
          loop();
        }
      else{
        ;
       }
    }
  }                  /* light effects */
  else if (mode == "2"){ /* rainbow */
    FastLED.clear();
    while (mode == "2"){
      for (int j = 0; j < 255; j++) {
        for (int i = 0; i < NUM_LEDS; i++) {
           leds[i] = CHSV(i - (j * 2), 255, brightness);
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
  else if (mode == "3"){
    FastLED.clear();
    while (mode == "3"){
    for(int j = 0; j < 256; j++) {
      for(int i = 0; i < NUM_LEDS; i++) {
        CRGB color (0,0,0);
        if(((i * 256 / NUM_LEDS + j) % 256) < 85) {
          color.g = 0;
          color.r = ((float)((i * 256 / NUM_LEDS + j) % 256) / 85.0f) * 255.0f;
          color.b = 255 - color.r;
        } else if(((i * 256 / NUM_LEDS + j) % 256) < 170) {
          color.g = ((float)(((i * 256 / NUM_LEDS + j) % 256) - 85) / 85.0f) * 255.0f;
          color.r = 255 - color.g;
          color.b = 0;
        } else if(((i * 256 / NUM_LEDS + j) % 256) < 256) {
          color.b = ((float)(((i * 256 / NUM_LEDS + j) % 256) - 170) / 85.0f) * 255.0f;
          color.g = ((i * 256 / NUM_LEDS + j) % 256) - color.b;
          color.r = 1;
        }
        leds[i] = color;  
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
}
  else if (mode == "4"){ /* ball */
    FastLED.clear();
    while (mode == "4"){
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
  else if (mode == "5"){ /* fade */
  FastLED.clear();
  while (mode == "5"){
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
  else if (mode == "6"){ /* rainbow */
    FastLED.clear();
    while (mode == "6"){
      for (int j = 0; j < 255; j++) {
        for (int i = 0; i < NUM_LEDS; i++) {
          fill_rainbow( leds, NUM_LEDS, gHue, 7);
          EVERY_N_MILLISECONDS( 20 ) { gHue++; }
           if (Serial.available() > 0){
            loop();
            }
            else{
              ;
             }
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
  else if (mode == "7"){ /* juggle */
    FastLED.clear();
    while (mode == "7"){
      for (int j = 0; j < 255; j++) {
        for (int i = 0; i < NUM_LEDS; i++) {
          fadeToBlackBy( leds, NUM_LEDS, 20);
          byte dothue = 0;
          for( int i = 0; i < 8; i++) {
            leds[beatsin16( i+7, 0, NUM_LEDS-1 )] |= CHSV(dothue, 200, 255);
            dothue += 32;
            if (Serial.available() > 0){
            loop();
            }
            else{
              ;
             }
          }
        }
        FastLED.show();
        delay(25); /* Change this to your hearts desire, the lower the value the faster your colors move (and vice versa) */
        }
     }
  }
  else if (mode == "8"){  /* off */
    FastLED.clear();
    Serial.println(mode);
    while (mode == "8"){
      static byte heat[NUM_LEDS];
      for( int i = 0; i < NUM_LEDS; i++) {
        heat[i] = qsub8( heat[i],  random8(0, ((COOLING * 10) / NUM_LEDS) + 2));
      }
      for( int k= NUM_LEDS - 1; k >= 2; k--) {
      heat[k] = (heat[k - 1] + heat[k - 2] + heat[k - 2] ) / 3;
      }
      if( random8() < SPARKING ) {
      int y = random8(7);
      heat[y] = qadd8( heat[y], random8(160,255) );
      }
      for( int j = 0; j < NUM_LEDS; j++) {
      CRGB color = HeatColor( heat[j]);
      int pixelnumber;
      if( gReverseDirection ) {
        pixelnumber = (NUM_LEDS-1) - j;
      } else {
        pixelnumber = j;
      }
      leds[pixelnumber] = color;
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
  else if (mode == "9"){ /* green */
    FastLED.clear();
    while (mode == "9"){
      for (int i = 0; i < NUM_LEDS; i++) {
        fadeToBlackBy( leds, NUM_LEDS, 20);
        int pos = beatsin16( 13, 0, NUM_LEDS-1 );
        leds[pos] += CHSV( gHue, 255, 192);
        Serial.println(gHue);
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
}
