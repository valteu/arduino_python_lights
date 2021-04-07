String data;
String mode;
double green;
double red;
double blue;
String num_led;
int brightness;
uint8_t gHue = 0;
int FRAMES_PER_SECOND = 120;
bool gReverseDirection = false;

#include <FastLED.h>

#define NUM_LEDS 60      /* The amount of pixels/leds you have */
#define DATA_PIN 3       /* The pin your data line is connected to */
#define LED_TYPE WS2812B /* I assume you have WS2812B leds, if not just change it to whatever you have */
#define SPARKING 120
#define COOLING  55

CRGB leds[NUM_LEDS];

void setup() { 
  FastLED.clear();
  Serial.begin(9600); //initialize serial COM at 9600 baudrate
  pinMode(LED_BUILTIN, OUTPUT); //make the LED pin (13) as output
  FastLED.addLeds<LED_TYPE, DATA_PIN, RGB>(leds, NUM_LEDS);
  Serial.println("Hi!, I am Arduino");
}

String mode0(String mode, double green, double red, double blue, int brightness){
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
String mode1(String mode, double green, double red, double blue, int brightness){
  FastLED.clear();
  while (mode == "1"){
      Serial.println("9.dsdsa");
    for (int i = 0; i < NUM_LEDS; i++) {
        Serial.println("8.dsdsa");

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
}
/* light effects */
String mode2(String mode, double green, double red, double blue, int brightness){
  FastLED.clear();
  while (mode == "2"){
    for (int j = 0; j < 255; j++) {
      if (Serial.available() > 0){
        loop();
      }
      else{
        ;
       }
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
String mode3(String mode, double green, double red, double blue, int brightness){
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

String mode4(String mode, double green, double red, double blue, int brightness){
  FastLED.clear();
  while (mode == "4"){
    for (int i = 0; i < NUM_LEDS; i++)
    {
      leds[i] = CRGB::Red;
      FastLED.show();
      delay(100);
      leds[i] = CRGB::Black;
      if (Serial.available() > 0){
        loop();
      }
      else{
        ;
       }
    }
    for (int i = NUM_LEDS - 1; i >= 0; i--)
    {
      leds[i] = CRGB::Red;
      FastLED.show();
      delay(100);
      leds[i] = CRGB::Black;
      if (Serial.available() > 0){
        loop();
      }
      else{
        ;
       }
    }
  }
}
String mode5(String mode, double green, double red, double blue, int brightness){
  FastLED.clear();
  while (mode == "5"){
  for( int colorStep=0; colorStep<256; colorStep++ ) {

      int r = colorStep;  // Redness starts at zero and goes up to full
      int b = 255-colorStep;  // Blue starts at full and goes down to zero
      int g = colorStep -255;  // No green needed to go from blue to red

      for(int x = 0; x < NUM_LEDS; x++){
          leds[x] = CRGB(g,r,b);
          if (Serial.available() > 0){
        loop();
      }
      else{
        ;
       }
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
String mode6(String mode, double green, double red, double blue, int brightness){
  FastLED.clear();
  while (mode == "5"){
    static byte heat[NUM_LEDS];

  // Step 1.  Cool down every cell a little
    for( int i = 0; i < NUM_LEDS; i++) {
      heat[i] = qsub8( heat[i],  random8(0, ((COOLING * 10) / NUM_LEDS) + 2));
    }
  
    // Step 2.  Heat from each cell drifts 'up' and diffuses a little
    for( int k= NUM_LEDS - 1; k >= 2; k--) {
      heat[k] = (heat[k - 1] + heat[k - 2] + heat[k - 2] ) / 3;
    }
    
    // Step 3.  Randomly ignite new 'sparks' of heat near the bottom
    if( random8() < SPARKING ) {
      int y = random8(7);
      heat[y] = qadd8( heat[y], random8(160,255) );
    }

    // Step 4.  Map from heat cells to LED colors
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
void loop() {
  FastLED.setBrightness( brightness );
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
        num_led = data;
      }
      else if (i == 5)
      {
        brightness = data.toInt();
      }
    }
    Serial.println(mode);
    Serial.println(num_led);
    Serial.println(brightness);
  if (mode =="0")
  {
    mode0(mode, green/100, red/100, blue/100, brightness);
  }
  else if (mode =="1")
  {
    mode1(mode, green/100, red/100, blue/100, brightness);
  }
  else if (mode =="2")
  {
    mode2(mode, green/100, red/100, blue/100, brightness);
  }
  else if (mode =="3")
  {
    mode3(mode, green/100, red/100, blue/100, brightness);
  }
  else if (mode =="4")
  {
    mode4(mode, green/100, red/100, blue/100, brightness);
  }
  else if (mode =="5")
  {
    mode5(mode, green/100, red/100, blue/100, brightness);
  }
  else if (mode =="6")
  {
    mode6(mode, green/100, red/100, blue/100, brightness);
  }
}
}
