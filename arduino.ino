// Rueda izquierda
int PinIN1 = 2;
int PinIN2 = 3;
// Rueda derecha
int PinIN3 = 4;
int PinIN4 = 5;

void setup() {
  // inicializar la comunicación serial a 9600 bits por segundo:
  Serial.begin(9600);
  // configuramos los pines como salida
  pinMode(PinIN1, OUTPUT);
  pinMode(PinIN2, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    String comando = Serial.readStringUntil('\n');
    // Recibir <comando|texto>, dividirlos e imprimir texto
    if (comando == "a") {
      Avanzar();
      Serial.println("Avanzando");
    } else if (comando == "r") {
      Retroceder();
      Serial.println("Retrocediendo");
    } else if (comando == "di") {
      Serial.println("Doblando a izquierda");
    } else if (comando == "dd") {
      Serial.println("Doblando a derecha");
    }
  }
}

void Avanzar()
{
  digitalWrite (PinIN1, HIGH);
  digitalWrite (PinIN2, LOW);
  digitalWrite (PinIN3, HIGH);
  digitalWrite (PinIN4, LOW);
  Frenar();
}

void Retroceder()
{
  digitalWrite (PinIN1, LOW);
  digitalWrite (PinIN2, HIGH);
  digitalWrite (PinIN3, LOW);
  digitalWrite (PinIN4, HIGH);
  Frenar();
}

void DoblarIzquierda()
{
  digitalWrite (PinIN1, HIGH);
  digitalWrite (PinIN2, LOW);
  digitalWrite (PinIN3, LOW);
  digitalWrite (PinIN4, LOW);
  Frenar();
}

void DoblarDerecha()
{
  digitalWrite (PinIN1, LOW);
  digitalWrite (PinIN2, LOW);
  digitalWrite (PinIN3, HIGH);
  digitalWrite (PinIN4, LOW);
  Frenar();
}

void Frenar()
{
  digitalWrite (PinIN1, LOW);
  digitalWrite (PinIN2, LOW);
  digitalWrite (PinIN3, LOW);
  digitalWrite (PinIN4, LOW);
}
