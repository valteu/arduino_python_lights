String data;
String var;
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

  if (var == "0"){  /* off */
    for (int i = 0; i < NUM_LEDS; i++) {
      leds[i].setRGB(0, 0, 0);/* green, red, blue */
    }
  }
  else if (var == "1"){ /* green */
    for (int i = 0; i < NUM_LEDS; i++) {
      leds[i].setRGB((2.5 * brightness), (0 * brightness), (0 * brightness));
    }
  }
  else if (var == "2"){ /* yellow */
    for (int i = 0; i < NUM_LEDS; i++) {
      leds[i].setRGB((2.5 * brightness), (2.5 * brightness), (0 * brightness));
    }
  }
  else if (var == "3"){ /* red */
    for (int i = 0; i < NUM_LEDS; i++) {
      leds[i].setRGB((0 * brightness), (2.5 * brightness), (0 * brightness));
    }
  }
  else if (var == "4"){ /* pink */
    for (int i = 0; i < NUM_LEDS; i++) {
      leds[i].setRGB((0 * brightness), (2.5 * brightness), (2.5 * brightness));
    }
  }
  else if (var == "5"){ /* tortoise */
    for (int i = 0; i < NUM_LEDS; i++) {
      leds[i].setRGB((2.5 * brightness), (0 * brightness), (2.5 * brightness));
    }
  }
  else if (var == "6"){ /* blue */
    for (int i = 0; i < NUM_LEDS; i++) {
      leds[i].setRGB((0 * brightness), (0 * brightness), (2.5 * brightness));
    }
  }
  else if (var == "7"){ /* blue */
    for (int i = 0; i < NUM_LEDS; i++) {
      leds[i].setRGB((2.5 * brightness), (2.5 * brightness), (2.5 * brightness));
    }
  }
  FastLED.show();

  }
}
