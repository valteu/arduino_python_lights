#include <Adafruit_NeoPixel.h>

String data;
String mode;
int current_strip = 100;
double green;
double red;
double blue;
int brightness;

 
// Pattern types supported:
enum  pattern { NONE, RAINBOW_CYCLE, THEATER_CHASE, COLOR_WIPE, SCANNER, FADE , COMPASS, DOUBLESCANNER, FOLLOWER, HALFUPDOWN, TWINKLE, RUNNING, RUNNINGRAINBOW, OFF, STATIC };
// Patern directions supported:
enum  direction { FORWARD, REVERSE };
 
// NeoPattern Class - derived from the Adafruit_NeoPixel class
class NeoPatterns : public Adafruit_NeoPixel
{
    public:
 
    // Member Variables:  
    pattern  ActivePattern;  // which pattern is running
    direction Direction;     // direction to run the pattern
    
    unsigned long Interval;   // milliseconds between updates
    unsigned long lastUpdate; // last update of position
    
    uint32_t Color1, Color2;  // What colors are in use
    uint16_t TotalSteps;  // total number of steps in the pattern
    uint16_t Index;  // current step within the pattern
    
    void (*OnComplete)();  // Callback on completion of pattern
    
    // Constructor - calls base-class constructor to initialize strip
    NeoPatterns(uint16_t pixels, uint8_t pin, uint8_t type, void (*callback)())
    :Adafruit_NeoPixel(pixels, pin, type)
    {
        OnComplete = callback;
    }
    
    // Update the pattern
    void Update()
    {
        if((millis() - lastUpdate) > Interval) // time to update
        {
            lastUpdate = millis();
            switch(ActivePattern)
            {
                case RAINBOW_CYCLE:
                    RainbowCycleUpdate();
                    break;
                case THEATER_CHASE:
                    TheaterChaseUpdate();
                    break;
                case COLOR_WIPE:
                    ColorWipeUpdate();
                    break;
                case SCANNER:
                    ScannerUpdate();
                    break;
                case FADE:
                    FadeUpdate();
                    break;
                case OFF:
                    OffUpdate(); 
                    break;
                case STATIC:  // Custom animation for candle
                    StaticUpdate(); 
                    break;
                default:
                    break;
            }
        }
    }
  
    // Increment the Index and reset at the end
    void Increment()
    {
        if (Direction == FORWARD)
        {
           Index++;
           if (Index >= TotalSteps)
            {
                Index = 0;
                if (OnComplete != NULL)
                {
                    OnComplete(); // call the comlpetion callback
                }
            }
        }
        else // Direction == REVERSE
        {
            --Index;
            if (Index <= 0)
            {
                Index = TotalSteps-1;
                if (OnComplete != NULL)
                {
                    OnComplete(); // call the comlpetion callback
                }
            }
        }
    }
    
    // Reverse pattern direction
    void Reverse()
    {
        if (Direction == FORWARD)
        {
            Direction = REVERSE;
            Index = TotalSteps-1;
        }
        else
        {
            Direction = FORWARD;
            Index = 0;
        }
    }
    
    // Initialize for a RainbowCycle
    void RainbowCycle(uint8_t interval, direction dir = FORWARD)
    {
        ActivePattern = RAINBOW_CYCLE;
        Interval = interval;
        TotalSteps = 255;
        Index = 0;
        Direction = dir;
    }
    
    // Update the Rainbow Cycle Pattern
    void RainbowCycleUpdate()
    {
        for(int i=0; i< numPixels(); i++)
        {
            setPixelColor(i, Wheel(((i * 256 / numPixels()) + Index) & 255));
        }
        show();
        Increment();
    }
 
    // Initialize for a Theater Chase
    void TheaterChase(uint32_t color1, uint32_t color2, uint8_t interval, direction dir = FORWARD)
    {
        ActivePattern = THEATER_CHASE;
        Interval = interval;
        TotalSteps = numPixels();
        Color1 = color1;
        Color2 = color2;
        Index = 0;
        Direction = dir;
   }
    
    // Update the Theater Chase Pattern
    void TheaterChaseUpdate()
    {
        for(int i=0; i< numPixels(); i++)
        {
            if ((i + Index) % 3 == 0)
            {
                setPixelColor(i, Color1);
            }
            else
            {
                setPixelColor(i, Color2);
            }
        }
        show();
        Increment();
    }
 
    // Initialize for a ColorWipe
    void ColorWipe(uint32_t color, uint8_t interval, direction dir = FORWARD)
    {
        ActivePattern = COLOR_WIPE;
        Interval = interval;
        TotalSteps = numPixels();
        Color1 = color;
        Index = 0;
        Direction = dir;
    }
    
    // Update the Color Wipe Pattern
    void ColorWipeUpdate()
    {
        setPixelColor(Index, Color1);
        show();
        Increment();
    }
    
    // Initialize for a SCANNNER
    void Scanner(uint32_t color1, uint8_t interval)
    {
        ActivePattern = SCANNER;
        Interval = interval;
        TotalSteps = (numPixels() - 1) * 2;
        Color1 = color1;
        Index = 0;
    }
 
    // Update the Scanner Pattern
    void ScannerUpdate()
    { 
        for (int i = 0; i < numPixels(); i++)
        {
            if (i == Index)  // Scan Pixel to the right
            {
                 setPixelColor(i, Color1);
            }
            else if (i == TotalSteps - Index) // Scan Pixel to the left
            {
                 setPixelColor(i, Color1);
            }
            else // Fading tail
            {
                 setPixelColor(i, DimColor(getPixelColor(i)));
            }
        }
        show();
        Increment();
    }
    
    // Initialize for a Fade
    void Fade(uint32_t color1, uint32_t color2, uint16_t steps, uint8_t interval, direction dir = FORWARD)
    {
        ActivePattern = FADE;
        Interval = interval;
        TotalSteps = steps;
        Color1 = color1;
        Color2 = color2;
        Index = 0;
        Direction = dir;
    }
    
    // Update the Fade Pattern
    void FadeUpdate()
    {
        // Calculate linear interpolation between Color1 and Color2
        // Optimise order of operations to minimize truncation error
        uint8_t red = ((Red(Color1) * (TotalSteps - Index)) + (Red(Color2) * Index)) / TotalSteps;
        uint8_t green = ((Green(Color1) * (TotalSteps - Index)) + (Green(Color2) * Index)) / TotalSteps;
        uint8_t blue = ((Blue(Color1) * (TotalSteps - Index)) + (Blue(Color2) * Index)) / TotalSteps;
        
        ColorSet(Color(red, green, blue));
        show();
        Increment();
    }
    void Off(uint32_t color1, uint32_t color2, uint16_t steps, uint8_t interval, direction dir = FORWARD)
    {
      ActivePattern = OFF;
      Interval = interval;
      TotalSteps = steps;
      Index = 0;
      Direction = dir;
    }
    
    // Initialize for a OFF
    void OffUpdate()
    {

      ColorSet(Color(0, 0, 0));
      show();
      Increment();
    }
    void Static(uint16_t steps, uint8_t interval, direction dir = FORWARD)
    {
      ActivePattern = OFF;
      Interval = interval;
      TotalSteps = numPixels();
      Index = 0;
      Direction = dir;
    }
    
    // Initialize for a OFF
    void StaticUpdate()
    {

      for (int i = 0; i < numPixels(); i++)
        {
          ColorSet(Color(red, green, blue));
        }
        show();
        Increment();
    }
    // Calculate 50% dimmed version of a color (used by ScannerUpdate)
    uint32_t DimColor(uint32_t color)
    {
        // Shift R, G and B components one bit to the right
        uint32_t dimColor = Color(Red(color) >> 1, Green(color) >> 1, Blue(color) >> 1);
        return dimColor;
    }
 
    // Set all pixels to a color (synchronously)
    void ColorSet(uint32_t color)
    {
        for (int i = 0; i < numPixels(); i++)
        {
            setPixelColor(i, color);
        }
        show();
    }
 
    // Returns the Red component of a 32-bit color
    uint8_t Red(uint32_t color)
    {
        return (color >> 16) & 0xFF;
    }
 
    // Returns the Green component of a 32-bit color
    uint8_t Green(uint32_t color)
    {
        return (color >> 8) & 0xFF;
    }
 
    // Returns the Blue component of a 32-bit color
    uint8_t Blue(uint32_t color)
    {
        return color & 0xFF;
    }
    
    // Input a value 0 to 255 to get a color value.
    // The colours are a transition r - g - b - back to r.
    uint32_t Wheel(byte WheelPos)
    {
        WheelPos = 255 - WheelPos;
        if(WheelPos < 85)
        {
            return Color(255 - WheelPos * 3, 0, WheelPos * 3);
        }
        else if(WheelPos < 170)
        {
            WheelPos -= 85;
            return Color(0, WheelPos * 3, 255 - WheelPos * 3);
        }
        else
        {
            WheelPos -= 170;
            return Color(WheelPos * 3, 255 - WheelPos * 3, 0);
        }
    }
};
 
void Strip2Complete();
void Strip3Complete();
void Strip1Complete();
 
// Define some NeoPatterns for the two rings and the Strip1
//  as well as some completion routines
NeoPatterns Strip2(9, 5, NEO_GRB + NEO_KHZ800, &Strip2Complete);
NeoPatterns Strip3(9, 6, NEO_GRB + NEO_KHZ800, &Strip3Complete);
NeoPatterns Strip1(24, 3, NEO_GRB + NEO_KHZ800, &Strip1Complete);
 
// Initialize everything and prepare to start
void setup()
{
  Serial.begin(9600);
  
  // Initialize all the pixelStrips
  Strip2.begin();
  Strip3.begin();
  Strip1.begin();
  
  // Kick off a pattern
  Strip2.TheaterChase(Strip2.Color(255,255,0), Strip2.Color(0,0,50), 100);
  Strip3.RainbowCycle(3);
  Strip3.Color1 = Strip2.Color1;
  Strip1.Scanner(Strip2.Color(255,0,0), 55);
  Serial.println("Hi!, I am Arduino");
}
 
// Main loop
void loop()
{
  Strip1.Update();
  Strip2.Update();
  Strip3.Update();
  if (Serial.available() > 0)
  {
    achievedata();
  }
  if (current_strip == 0)
    {
      if (mode == "0")
      {
        Strip1.ActivePattern = OFF;
      }
      else if (mode == "1"){
        Strip1.ActivePattern = STATIC;
        Strip1.TotalSteps = Strip1.numPixels();
        }
      else if (mode == "2"){
        Strip1.ActivePattern = RAINBOW_CYCLE;
        Strip1.TotalSteps = 255;
        Strip1.Interval = min(10, Strip1.Interval);
        }
      else if (mode == "3"){
        Strip1.ActivePattern = THEATER_CHASE;
        Strip1.Interval = 100;
        }
      else if (mode == "4"){
        Strip1.ActivePattern = COLOR_WIPE;
        Strip1.TotalSteps = Strip1.numPixels();
        }
      else if (mode == "5"){
        Strip1.ActivePattern = SCANNER;
        }
      else if (mode == "6"){
        Strip1.ActivePattern = FADE;
        Strip1.Interval = 20;
        }
      else if (mode == "7"){
          ;
        }
      Strip1.show();
    }
    else if (current_strip == 1)
    {
      if (mode == "0")
      {
        Strip2.ActivePattern = OFF;;
      }
      else if (mode == "1"){
        Strip2.ActivePattern = STATIC;
        Strip2.TotalSteps = Strip1.numPixels();
        }
      else if (mode == "2"){
        Strip2.ActivePattern = RAINBOW_CYCLE;
        Strip2.TotalSteps = 255;
        Strip2.Interval = min(10, Strip2.Interval);
        }
      else if (mode == "3"){
        Strip2.ActivePattern = THEATER_CHASE;
        Strip2.Interval = 100;
        }
      else if (mode == "4"){
        Strip2.ActivePattern = COLOR_WIPE;
        Strip2.TotalSteps = Strip2.numPixels();
        }
      else if (mode == "5"){
        Strip2.ActivePattern = SCANNER;
        }
      else if (mode == "6"){
        Strip2.ActivePattern = FADE;
        Strip2.Interval = 20;
        }
      else if (mode == "7"){
          ;
        }
      Strip2.show();
    }
    else if (current_strip == 2)
    {
      if (mode == "0")
      {
        Strip3.ActivePattern = OFF;
      }
      else if (mode == "1"){
        Strip3.ActivePattern = STATIC;
        Strip3.TotalSteps = Strip1.numPixels();
        }
      else if (mode == "2"){
        Strip3.ActivePattern = RAINBOW_CYCLE;
        Strip3.TotalSteps = 255;
        Strip3.Interval = min(10, Strip3.Interval);
        }
      else if (mode == "3"){
        Strip3.ActivePattern = THEATER_CHASE;
        Strip3.Interval = 100;
        }
      else if (mode == "4"){
        Strip3.ActivePattern = COLOR_WIPE;
        Strip3.TotalSteps = Strip3.numPixels();
        }
      else if (mode == "5"){
        Strip3.ActivePattern = SCANNER;
        }
      else if (mode == "6"){
        Strip3.ActivePattern = FADE;
        Strip3.Interval = 20;
        }
      else if (mode == "7"){
        ;
        }
      Strip3.show();
    }
  else // Back to normal operation
  {
    // Restore all pattern parameters to normal values
    Strip3.ActivePattern = THEATER_CHASE;
    Strip3.Interval = 100;
    Strip2.ActivePattern = RAINBOW_CYCLE;
    Strip2.TotalSteps = 255;
    Strip2.Interval = min(10, Strip3.Interval);
    Strip1.ActivePattern = OFF;
    Strip1.Interval = 200;
    Serial.println(Strip1.ActivePattern);
  }
}
 
//------------------------------------------------------------
//Completion Routines - get called on completion of a pattern
//------------------------------------------------------------
 
// Strip2 Completion Callback
void Strip2Complete()
{
    ;
}
 
// Ring 2 Completion Callback
void Strip3Complete()
{
    ;
}
 
// Strip1 Completion Callback
void Strip1Complete()
{
    ;
}

int achievedata()
{
  for (int i = 0; i < 6; i++)
  {
    data = Serial.read();
    if (i == 0)
    {
      mode = data;
      delay(10);
    }
    else if (i == 1)
    {
      green = data.toDouble();
      delay(10);
    }
    else if (i == 2)
    {
      red = data.toDouble();
      delay(10);
    }
    else if (i == 3)
    {
      blue = data.toDouble();
      delay(10);
    }
    else if (i == 4)
    {
      current_strip = data.toInt();
      delay(10);
    }
    else if (i == 5)
    {
      brightness = data.toInt();
      delay(10);
    }
  }
  Serial.println("data:");
  Serial.println(mode);
  Serial.println(green);
  Serial.println(red);
  Serial.println(blue);
  Serial.println(current_strip);
  Serial.println(brightness);
}
