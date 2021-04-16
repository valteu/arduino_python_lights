String data;
int mode;
int green;
int red;
int blue;
int num_led;
int brightness;
byte gHue; 
bool gReverseDirection = false;
int current_strip;
int current_led_strip;

int device_1_values[6] = {0, 0, 0, 0, 0, 0};
int device_2_values[6] = {0, 0, 0, 0, 0, 0};
int device_3_values[6] = {0, 0, 0, 0, 0, 0};

bool device_1_active = true;
bool device_2_active = false;
bool device_3_active = false;

bool data_achieved = false;


#include <FastLED.h>

#define DATA_PIN 3       /* The pin your data line is connected to */
#define LED_TYPE WS2812B /* I assume you have WS2812B leds, if not just change it to whatever you have */
#define COLOR_ORDER GRB
#define COOLING  55
#define SPARKING 120
#define NUM_STRIPS 3
#define NUM_LEDS 36


CRGB leds[NUM_LEDS];
CLEDController *controllers[NUM_STRIPS];

void setup() { 
  FastLED.clear();
  Serial.begin(9600); //initialize serial COM at 9600 baudrate
  pinMode(LED_BUILTIN, OUTPUT); //make the LED pin (13) as output
  FastLED.addLeds<LED_TYPE, 3, COLOR_ORDER>(leds, NUM_LEDS).setCorrection( TypicalLEDStrip );
  FastLED.addLeds<LED_TYPE, 5, COLOR_ORDER>(leds, NUM_LEDS).setCorrection( TypicalLEDStrip );
  FastLED.addLeds<LED_TYPE, 6, COLOR_ORDER>(leds, NUM_LEDS).setCorrection( TypicalLEDStrip );
  Serial.println("Hi!, I am Arduino");
}
 
void loop() {
  if (Serial.available()){
    for (int i = 0; i < 6; i++)
    {
      data = Serial.read();
      if (i == 0)
      {
        mode = data.toInt();
      }
      else if (i == 1){
        green = data.toInt();
      }
      else if (i == 2)
      {
        red = data.toInt();
      }
      else if (i == 3)
      {
        blue = data.toInt();
      }
      else if (i == 4)
      {
        current_led_strip = data.toInt();
         Serial.println("strip:");
         Serial.println(current_led_strip);
      }
      else if (i == 5)
      {
        brightness = data.toInt();
      }
      
      if (current_led_strip == 0)
      {
      for (int a = 0; a < 6; a++)
        {
          device_1_values[0] = mode;
          device_1_values[1] = green;
          device_1_values[2] = red;
          device_1_values[3] = blue;
          device_1_values[4] = brightness;
          device_1_values[5] = current_led_strip;
          Serial.println("device_1:");
          Serial.println(device_1_values[0]);
          Serial.println(device_1_values[1]);
          Serial.println(device_1_values[2]);
          Serial.println(device_1_values[3]);
          Serial.println(device_1_values[4]);
          Serial.println(device_1_values[5]);
        }
      }
      else if (current_led_strip == 1)
      {
      for (int a = 0; a < 6; a++)
        {
          device_2_values[0] = mode;
          device_2_values[1] = green;
          device_2_values[2] = red;
          device_2_values[3] = blue;
          device_2_values[4] = brightness;
          device_2_values[5] = current_strip;
        }
      }
      else if (current_led_strip == 2)
      {
      for (int a = 0; a < 6; a++)
        {
          device_3_values[0] = mode;
          device_3_values[1] = green;
          device_3_values[2] = red;
          device_3_values[3] = blue;
          device_3_values[4] = brightness;
          device_3_values[5] = current_strip;
        }
      }
    }
    data_achieved = true;
  }
  if (data_achieved == true)
  {
    if (device_1_active == true)
    {
      Serial.println("device_1:");
      Serial.println(device_1_values[0]);
      Serial.println(device_1_values[1]);
      Serial.println(device_1_values[2]);
      Serial.println(device_1_values[3]);
      Serial.println(device_1_values[4]);
      Serial.println(device_1_values[5]);
      device_1_active = false;
      device_2_active = true;
      modes(device_1_values);
    }
    else if (device_2_active == true)
    {
      Serial.println("device_2:");
      Serial.println(device_2_values[0]);
      Serial.println(device_2_values[1]);
      Serial.println(device_2_values[2]);
      Serial.println(device_2_values[3]);
      Serial.println(device_2_values[4]);
      Serial.println(device_2_values[5]);
      device_2_active = false;
      device_3_active = true;
      modes(device_2_values);  
    }
    else if (device_3_active == true)
    {
      device_3_active = false;
      device_1_active = true;
      modes(device_3_values);  
    }
  }
}


String modes(int device_values[6]){
  mode = device_values[0];
  green = (device_values[1] / 100);
  red = (device_values[2] / 100);
  blue = (device_values[3] / 100);
  brightness = device_values[4];
  current_strip = device_values[5];
  
  if (mode == 0){
    while (mode == 0){
      fill_solid(leds, NUM_LEDS, CRGB::Black);
      FastLED[current_strip].showLeds(brightness);/* green, red, blue */
      if (Serial.available() > 0){
          loop();
        }
      else{
        ;
       }
    }
  }
  if (mode == 1){
    Serial.println("enterd mode 1");
    FastLED.clear();
    while (mode == 1){
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
      FastLED[current_strip].showLeds();
        if (current_strip == 1)
        {
          for (int a = 0; a < 6; a++)
          {
            device_1_values[0] = mode;
            device_1_values[1] = (green * 100);
            device_1_values[2] = (red * 100);
            device_1_values[3] = (blue * 100);
            device_1_values[4] = brightness;
            device_1_values[5] = current_strip;
          }
        }
        else if (current_strip == 2)
        {
        for (int a = 0; a < 6; a++)
          {
            device_2_values[0] = mode;
            device_2_values[1] = (green * 100);
            device_2_values[2] = (red * 100);
            device_2_values[3] = (blue * 100);
            device_2_values[4] = brightness;
            device_2_values[5] = current_strip;
          }
        }
        else if (current_strip == 3)
        {
          for (int a = 0; a < 6; a++)
          {
            device_3_values[0] = mode;
            device_3_values[1] = (green * 100);
            device_3_values[2] = (red * 100);
            device_3_values[3] = (blue * 100);
            device_3_values[4] = brightness;
            device_3_values[5] = current_strip;
          }
        }     
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
