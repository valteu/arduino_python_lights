String data;
String var;
String num_led;
String brightness;
int SATURATION;
#include <FastLED.h>

#define NUM_LEDS 12      /* The amount of pixels/leds you have */
#define DATA_PIN 3       /* The pin your data line is connected to */
#define LED_TYPE WS2812B /* I assume you have WS2812B leds, if not just change it to whatever you have */
#define BRIGHTNESS 255    /*Control the brightness of your leds */
/*#define SATURATION 255  Control the saturation of your leds */

CRGB leds[NUM_LEDS];

void setup() { 
  FastLED.clear();
  Serial.begin(9600); //initialize serial COM at 9600 baudrate
  pinMode(LED_BUILTIN, OUTPUT); //make the LED pin (13) as output
  FastLED.addLeds<LED_TYPE, DATA_PIN>(leds, NUM_LEDS);
  Serial.println("Hi!, I am Arduino");
}
 
void loop() {
while (Serial.available()){
  for (int i = 0; i < 3; i++)
  {
    data = Serial.read();
    if (i == 0)
    {
      var = data.toInt();
    }
    else if (i == 1){
      num_led = data;
    }
    else if (i == 2)
    {
      brightness = data.toInt();
    }
  }
  Serial.println(var);
  Serial.println(num_led);
  Serial.println(brightness);
  data = Serial.read();

  var = data[0];
  num_led = data[1];
  /*NUM_LEDS = num_led;*/
   SATURATION = brightness.toInt();
   Serial.println(SATURATION);

  }

  if (var == '1')
    for (int j = 0; j < 255; j++) {
      for (int i = 0; i < NUM_LEDS; i++) {
        leds[i] = CHSV(i - (j * 2), BRIGHTNESS, SATURATION); /* The higher the value 4 the less fade there is and vice versa */ 
      }
      FastLED.show();
      delay(25); /* Change this to your hearts desire, the lower the value the faster your colors move (and vice versa) */
    }
  if (var == '0') /* pause led*/
    FastLED.clear();
  }
