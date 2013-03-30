/*
  Servidor web para monitorar temperatura e tensao da rede eletrica
  2013 - Cesar Augusto
*/

#include <SPI.h>
#include <Ethernet.h>
#include <Tensao.h>

// Pinos dos LEDs
const int ledVerde = 3;
const int ledVermelho = 4;

// Pinos Sensores
const int sensorPC = A1;
const int sensorRack = A0;
const int sensorHome = A2;
const int TensaoHome = A3;

// Enter a MAC address and IP address for your controller below.
// The IP address will be dependent on your local network:
byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };

IPAddress ip(192,168,3,70);
IPAddress gateway(192,168,3,1);
IPAddress subnet(255,255,255,0);

// Initialize the Ethernet server library
EthernetServer server(8090);

void setup(){
  // start the Ethernet connection and the server:
  Ethernet.begin(mac, ip, gateway, subnet);
  server.begin();
 
  //Serial.begin(9600);
}

void loop(){
  // Servidor De Monitoramento
  getServerWeb();
    
  // Teste da rede
  /*while (true){
    getConectRede();
    delay(60000);
  }*/
     
}

void getServerWeb(){

  EthernetClient client = server.available();
     
  if (client) {
    if (client.available()) {
        Tensao tensao(TensaoHome);
  
        client.println("HTTP/1.1 200 OK");
        client.println("Content-Type: application/json");
        client.println("charset: UTF-8");
        client.println();

        // output the value analog input pin
        client.print("{");
        client.print("'PC':'");
        client.print(calculaTemperatura(analogRead(sensorPC)));
        client.print("','Hack':'");
        client.print(calculaTemperatura(analogRead(sensorRack)));
        client.print("','Home':'");
        client.print(calculaTemperatura(analogRead(sensorHome)));
        client.print("','Voltagem':'");
        client.print(tensao.valor());
        client.print("'}");
        client.println();
    
    }
    // give the web browser time to receive the data
    delay(1);
    // close the connection
    client.stop();
  }
}

float calculaTemperatura(int val){
  float temperature = 0.0;
  
  temperature = (5.0 * val*100.0)/1023.0;
  return temperature;
}

void getConectRede(){
  
  IPAddress server(192,168,3,40); //HomeServer
  EthernetClient client;
  
  pinMode(ledVermelho,OUTPUT);
  pinMode(ledVerde,OUTPUT); 
  
  if (client.connect(server, 8080)) {
    digitalWrite(ledVerde,HIGH);
    digitalWrite(ledVermelho,LOW);
  } else {
    digitalWrite(ledVerde,LOW);
    digitalWrite(ledVermelho,HIGH);
  }
}
