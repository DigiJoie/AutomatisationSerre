//Pin Digital
//0 et 1 RX TX pin mauvais voltage
//HUM pour humidite ou eau
//LUM pour lumiere
//LUM pour photoresistance ou luminosite
//Capteur VH400 pour l'humidite
const int PIN_D_CAPTEUR_HUM_A = 2;
const int PIN_D_CAPTEUR_HUM_B = 3;
const int PIN_D_CAPTEUR_HUM_C = 4;
const int PIN_D_CAPTEUR_HUM_D = 5;

//PhotoCell utilise comme capteur lumiere avec une resistance de 150ohm
const int PIN_D_CAPTEUR_LUM_A = 6;
const int PIN_D_CAPTEUR_LUM_B = 7;

//Relai Keyes Funduino 4 relais par board utilise
//relai humidite
const int PIN_D_RELAI_HUM_A = 8;
const int PIN_D_RELAI_HUM_B = 9;
const int PIN_D_RELAI_HUM_C = 10;
const int PIN_D_RELAI_HUM_D = 11;
//relai lumiere
const int PIN_D_RELAI_LUM_A = 12;
const int PIN_D_RELAI_LUM_B = 13;

//Pin Analogique
const int PIN_A_CAPTEUR_HUM_A = 0;
const int PIN_A_CAPTEUR_HUM_B = 1;
const int PIN_A_CAPTEUR_HUM_C = 2;
const int PIN_A_CAPTEUR_HUM_D = 3;
const int PIN_A_CAPTEUR_LUM_A = 4;
const int PIN_A_CAPTEUR_LUM_B = 5;

//pour communiquer avec RaspberryPi
const int BAUD_RATE = 9600;

//les etats
bool relaiValveA=false;
bool relaiValveB=false;
bool relaiValveC=false;
bool relaiValveD=false;
bool relaiLumA=false;
bool relaiLumB=false;

//les valeurs des capteur
int capteurHumA=0;
int capteurHumB=0;
int capteurHumC=0;
int capteurHumD=0;
int capteurLumA=0;
int capteurLumB=0;
bool stringComplete = false;
String commandePi;

void setup() 
{
  pinMode(PIN_D_CAPTEUR_HUM_A,OUTPUT);//2
  digitalWrite(PIN_D_CAPTEUR_HUM_A,LOW);
  pinMode(PIN_D_CAPTEUR_HUM_B,OUTPUT);//3
  digitalWrite(PIN_D_CAPTEUR_HUM_B,LOW);
  pinMode(PIN_D_CAPTEUR_HUM_C,OUTPUT);//4
  digitalWrite(PIN_D_CAPTEUR_HUM_C,LOW);
  pinMode(PIN_D_CAPTEUR_HUM_D,OUTPUT);//5
  digitalWrite(PIN_D_CAPTEUR_HUM_D,LOW);
  pinMode(PIN_D_CAPTEUR_LUM_A,OUTPUT);//6
  digitalWrite(PIN_D_CAPTEUR_LUM_A,LOW);
  pinMode(PIN_D_CAPTEUR_LUM_B,OUTPUT);//7
  digitalWrite(PIN_D_CAPTEUR_LUM_B,LOW);
  //les relais keyes funduino absorbe du courant alors high etain low allume.
  //On les etains tous
  pinMode(PIN_D_RELAI_HUM_A,OUTPUT);//8
  digitalWrite(PIN_D_RELAI_HUM_A,HIGH);
  pinMode(PIN_D_RELAI_HUM_B,OUTPUT);//9
  digitalWrite(PIN_D_RELAI_HUM_B,HIGH);
  pinMode(PIN_D_RELAI_HUM_C,OUTPUT);//10
  digitalWrite(PIN_D_RELAI_HUM_C,HIGH);
  pinMode(PIN_D_RELAI_HUM_D,OUTPUT);//11
  digitalWrite(PIN_D_RELAI_HUM_D,HIGH);
  pinMode(PIN_D_RELAI_LUM_A,OUTPUT);//12
  digitalWrite(PIN_D_RELAI_LUM_A,HIGH);
  pinMode(PIN_D_RELAI_LUM_B,OUTPUT);//13
  digitalWrite(PIN_D_RELAI_LUM_B,HIGH);
  
  //on initiale le portserie pour communiquer avec raspberry pi
  Serial.begin(BAUD_RATE);
  
  commandePi.reserve(15);
}

void loop() 
{
  if(stringComplete)
  {
    miseAJourEtat();
    stringComplete=false;
  }
  miseAJourCapteur();
  envoiEtat();
  delay(10);
  envoiValeurCapteur();
  delay(10);
}

void  miseAJourEtat()
{
    String relai = commandePi.substring(0,1);
    String valeur =  commandePi.substring(1);
    int iValeur=-1;
    if(valeur!="")
    {
      iValeur = valeur.toInt();
    }
     //relai valve
     if(relai == "A")
     {
       if(iValeur==1)
       {
         activeRelai(PIN_D_RELAI_HUM_A);
         relaiValveA = true;
       }
       else if(iValeur==0)
       {
         etainRelai(PIN_D_RELAI_HUM_A); 
         relaiValveA = false;
       } 
     }
     else if(relai == "B")
      {
       if(iValeur==1)
       {
         activeRelai(PIN_D_RELAI_HUM_B);
         relaiValveB = true;
       }
       else if(iValeur==0)
       {
         etainRelai(PIN_D_RELAI_HUM_B); 
         relaiValveB = false;
       }
      }
     else if(relai == "C")
     {
       if(iValeur==1)
       {
         activeRelai(PIN_D_RELAI_HUM_C);
         relaiValveC = true;
       }       
       else if(iValeur==0)
       {
         etainRelai(PIN_D_RELAI_HUM_C);
         relaiValveC = false; 
       } 
     }
       else if(relai == "D")
       {
         if(iValeur==1)
         {
           activeRelai(PIN_D_RELAI_HUM_D);
           relaiValveD = true;
         }
         else if(iValeur==0)
         {
           etainRelai(PIN_D_RELAI_HUM_D);
           relaiValveD = false; 
         }  
       }
       //relai lumiere  
       else if(relai == "E")
       {
         if(iValeur==1)
         {
           activeRelai(PIN_D_RELAI_LUM_A);
           relaiLumA = true;
         }
         else if(iValeur==0)
         {
           etainRelai(PIN_D_RELAI_LUM_A);
           relaiLumA = false; 
         }
       }
       else if(relai == "F")
       {
         if(iValeur==1)
         {
           activeRelai(PIN_D_RELAI_LUM_B);
           relaiLumB = true;
         }
         else if(iValeur==0)
         {
           etainRelai(PIN_D_RELAI_LUM_B);
           relaiLumB = false; 
         } 
       }     
    commandePi ="";
}

void envoiEtat()
{
  //RV = Relai Valve
  //RL = RelaiLumiere
  Serial.print(" RV_A:"+String(relaiValveA)+' ');
  Serial.print("RV_B:"+String(relaiValveB)+' ');
  Serial.print("RV_C:"+String(relaiValveC)+' ');
  Serial.print("RV_D:"+String(relaiValveD)+' ');
  Serial.print("RL_A:"+String(relaiLumA)+' ');
  Serial.println("RL_B:"+String(relaiLumB)+' ');
}


void envoiValeurCapteur()
{
  //Capteur Humidite ==CH 
  //Capteur Lumiere ==CL
  Serial.print(" CH_A:"+ String(capteurHumA)+' ');
  Serial.print("CH_B:"+ String(capteurHumB)+' ');
  Serial.print("CH_C:"+ String(capteurHumC)+' ');
  Serial.print("CH_D:"+ String(capteurHumD)+' ');
  Serial.print("CL_A:"+ String(capteurLumA)+' ');
  Serial.println("CL_B:"+ String(capteurLumB)+' ');
}
 void miseAJourCapteur()
 {
   capteurHumA = litValeurHumidite(PIN_D_CAPTEUR_HUM_A,PIN_A_CAPTEUR_HUM_A);
   capteurHumB = litValeurHumidite(PIN_D_CAPTEUR_HUM_B,PIN_A_CAPTEUR_HUM_B);
   capteurHumC = litValeurHumidite(PIN_D_CAPTEUR_HUM_C,PIN_A_CAPTEUR_HUM_C);
   capteurHumD = litValeurHumidite(PIN_D_CAPTEUR_HUM_D,PIN_A_CAPTEUR_HUM_D);
   capteurLumA = litValeurCapteurLumiere(PIN_D_CAPTEUR_LUM_A,PIN_A_CAPTEUR_LUM_A);
   capteurLumB = litValeurCapteurLumiere(PIN_D_CAPTEUR_LUM_B,PIN_A_CAPTEUR_LUM_B);
 }


//appelle a chaque fin de loop
void serialEvent() 
{
  while (Serial.available()) 
  {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    commandePi += inChar;
    // if the incoming character is a newline, set a flag
    // so the main loop can do something about it:
    if (inChar == '\n') 
    {
      stringComplete = true;
    }
  }
}

int FloatAIntEtArondie(float valeur)
{
  int iTemp=(int)valeur;
  float fTemp=valeur-iTemp;
  if(fTemp>0.5)
  {
    return (int)(valeur+1);
  }
  return (int)valeur;
}

//retourne la valeur du capteur de 0 a 1024 
int litValeurCapteur(const int PIN_ECRITURE,const int PIN_LECTURE,const int NOMBRE_DE_LECTURE)
{
  const int ATTENTE_LECTURE_MS = 100;
  int valeur = 0;
  
  //fait une moyenne
  for(int i=0;i!=NOMBRE_DE_LECTURE;i++)
  {
    digitalWrite(PIN_ECRITURE,HIGH);
    delay(ATTENTE_LECTURE_MS);
    valeur += analogRead(PIN_LECTURE);
    digitalWrite(PIN_ECRITURE,LOW);  
  }
  return valeur/NOMBRE_DE_LECTURE;
}
//retourne la valeur du capteur voltage
float litValeurCapteurVoltage(const int PIN_ECRITURE,const int PIN_LECTURE,const int NOMBRE_DE_LECTURE)
{
  return litValeurCapteur(PIN_ECRITURE,PIN_LECTURE,NOMBRE_DE_LECTURE)*(5.0/1023.0);
}

//retourn l'ohm du capteur photoresistif
int litValeurCapteurLumiere (const int PIN_ECRITURE,const int PIN_LECTURE)
{
  const int NOMBREDELECTURE = 4;
  const int VIN = 5; //Voltage d'arduino
  const float RESISTANCE_FIXE = 975; //vrai==975ohm(sur paquet 1000ohm) pour les 2!
  return FloatAIntEtArondie(RESISTANCE_FIXE/((VIN / litValeurCapteurVoltage(PIN_ECRITURE,PIN_LECTURE,NOMBREDELECTURE)) - 1));
  //return litValeurCapteur(PIN_ECRITURE,PIN_LECTURE,NOMBREDELECTURE);
}

//retourne la teneur en eau volumetrique(Volumetric Water Content) en %
int litValeurHumidite (const int PIN_ECRITURE,const int PIN_LECTURE)
{ 
  const int NOMBREDELECTURE = 4;
  float ValeurHumidite = 0.0;
  //pour retourner un int au lieu d'un float ou double
  const int NOMBREDECIMAL = 100;
  float valeurCapteurVoltage = litValeurCapteurVoltage(PIN_ECRITURE,PIN_LECTURE,NOMBREDELECTURE);
  if (valeurCapteurVoltage < 1.1)
    ValeurHumidite = 10.0*valeurCapteurVoltage-1.0;
  if(valeurCapteurVoltage < 1.3)
    ValeurHumidite = 25.0*valeurCapteurVoltage-17.5;
  if(valeurCapteurVoltage < 1.82)
    ValeurHumidite = 48.08*valeurCapteurVoltage-47.5;
  if(valeurCapteurVoltage < 2.2)
    ValeurHumidite = 26.32*valeurCapteurVoltage-7.89; 
  // si valeur en haut de 50 sature (valeur pu bonne) 
  if(valeurCapteurVoltage >= 2.2)
    ValeurHumidite = 26.32*valeurCapteurVoltage-7.89; 
    
    return ValeurHumidite*NOMBREDECIMAL;
 }

void activeRelai(const int PIN_ECRITURE)
{
  delay(25);
  digitalWrite(PIN_ECRITURE,LOW); 
}

void etainRelai(const int PIN_ECRITURE)
{
  delay(25);
  digitalWrite(PIN_ECRITURE,HIGH);
}
