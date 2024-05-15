int inches = 0;
int cm = 0;
int PinoDoSensor = 9; 
int EchoPin = 10;
int DistanciaPadrao = 100;
int PinoAlarme = 8;
char input;
long duration;
int distance;
char inputPermanente = 'd';

void sirene(byte pino, byte repeticoes) {
  for (int i = 0; i < repeticoes; i++) {
    for (int i = 100; i < 1500; i += 5) {
      tone(pino, i);
      delay(1);
    }
    for (int i = 1500; i > 100; i -= 5) {
      tone(pino, i);
      delay(1);
    }
    noTone(pino);
    delay(100);
  }
}

void portaAberta(byte pino) {
    tone(pino, 600);
    delay(100);
    noTone(pino);
    delay(100);
}

int readUltrasonicDistance(int trigPin, int echoPin)
{
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  // Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);
  // Calculating the distance
  distance = duration * 0.034 / 2;
  // Prints the distance on the Serial Monitor
  return distance;
}

void setup()
{
  
  pinMode(PinoAlarme, OUTPUT);
  pinMode(PinoDoSensor, OUTPUT); 
  pinMode(EchoPin, INPUT); 
  Serial.begin(9600);
}

void loop()
{
  cm = readUltrasonicDistance(PinoDoSensor, EchoPin) + 2;
  input = Serial.read();
  if(inputPermanente == 'l' || input == 'l')
  {
    inputPermanente = 'l';
    if(cm > DistanciaPadrao )
    {
        sirene(PinoAlarme, 5);
    }
  }
  if(inputPermanente == 'd' || input == 'd')
  {
    inputPermanente ='d';
	  if(cm > DistanciaPadrao)
    {    	
        portaAberta(PinoAlarme);
        
    }
  }
  
  Serial.print(cm);
  Serial.println("cm");
 }