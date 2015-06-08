import serial
import datetime
from tkinter import *
from tkinter import ttk

#texte pour le protocole de communication avec arduino
#R pour relai V pour valve
TexteRelaiValveA="RV_A"
TexteRelaiValveB="RV_B"
TexteRelaiValveC="RV_C"
TexteRelaiValveD="RV_D"

#L pour lumiere
TexteRelaiLumiereA="RL_A"
TexteRelaiLumiereB="RL_B"

#C pour capteur H pour Humidite
TexteCapteurHumiditeA="CH_A"
TexteCapteurHumiditeB="CH_B"
TexteCapteurHumiditeC="CH_C"
TexteCapteurHumiditeD="CH_D"

#L pour lumiere
TexteCapteurLumiereA="CL_A"
TexteCapteurLumiereB="CL_B"

#0 off | 1 on
EtatRelaiValveA=0
EtatRelaiValveB=0
EtatRelaiValveC=0
EtatRelaiValveD=0
EtatRelaiLumiereA=0
EtatRelaiLumiereB=0

#Doit envoyer commande de changement d'etat au arduino
ChangementEtatRelaiValveA=False
ChangementEtatRelaiValveB=False
ChangementEtatRelaiValveC=False
ChangementEtatRelaiValveD=False
ChangementEtatRelaiLumiereA=False
ChangementEtatRelaiLumiereB=False

#valeur des capteur
#humidite en volumetric water content
ValeurCapteurHumiditeA=0.0
ValeurCapteurHumiditeB=0.0
ValeurCapteurHumiditeC=0.0
ValeurCapteurHumiditeD=0.0

#lumiere en %
ValeurCapteurLumiereA=0.0
ValeurCapteurLumiereB=0.0

#bac 1
ValeurVoulueLumiereA=0.0
#nord
ValeurVoulueHumiditeA=0.0
#sud
ValeurVoulueHumiditeB=0.0


#bac2
ValeurVoulueLumiereB=0.0
#nord
ValeurVoulueHumiditeC=0.0
#sud
ValeurVoulueHumiditeD=0.0

ModuleLumiereAEtat = False
ModuleLumiereBEtat = False
ModuleLumiereAMax = False
ModuleLumiereBMax = False


#CommandeAllumeLampes ="s LAMP.manual 100%"
#CommandeEteintLampes ="s LAMP.manual 0%"
CommandeModuleLumiere ="s LAMP.manual "

ValeurModuleLumiereA = 0
ValeurModuleLumiereB = 0

#pour faire la moyenne des valeurs de lumière puisqu'il change trop souvent
CompteurMoyenneLumiere = 0
CumulMoyenneLumiereA = 0
CumulMoyenneLumiereB = 0
ValeurMoyenneLumiereA= 0
ValeurMoyenneLumiereB= 0
NombreDePasseLumieres=20


CalibrationLampeAB = False
CalibrationLampeBC = False

ArduinoSerie = serial.Serial("/dev/ttyACM0",timeout =0.01,writeTimeout = None)
LampeA = serial.Serial("/dev/ttyACM1",timeout =0.01,writeTimeout = None)
LampeB = serial.Serial("/dev/ttyACM2",timeout =0.01,writeTimeout = None)
LampeC = serial.Serial("/dev/ttyACM3",timeout =0.01,writeTimeout = None)
LampeD = serial.Serial("/dev/ttyACM4",timeout =0.01,writeTimeout = None)

def LitValeurArduino():
                ligneArduino = str(ArduinoSerie.readline())
                #print(ligneArduino)
                if(ligneArduino!=-1):
                        mots = ligneArduino.split(" ")
                        for mot in mots:
                                var = mot.split(":")
                                if len(var)==2:
                                        try :
                                                if(var[0] == TexteRelaiValveA):
                                                        global EtatRelaiValveA
                                                        EtatRelaiValveA = int(var[1])
                                                        
                                                if(var[0] == TexteRelaiValveB):
                                                        global EtatRelaiValveB
                                                        EtatRelaiValveB = int(var[1])
                                                        
                                                if(var[0] == TexteRelaiValveC):
                                                        global EtatRelaiValveC
                                                        EtatRelaiValveC = int(var[1])
                                                        
                                                if(var[0] == TexteRelaiValveD):
                                                        global EtatRelaiValveD
                                                        EtatRelaiValveD = int(var[1])
                                                        
                                                if(var[0] == TexteRelaiLumiereA):
                                                        global EtatRelaiLumiereA
                                                        EtatRelaiLumiereA = int(var[1])
                                                        
                                                if(var[0] == TexteRelaiLumiereB):
                                                        global EtatRelaiLumiereB
                                                        EtatRelaiLumiereB = int(var[1])
                                                        
                                                if(var[0] == TexteCapteurHumiditeA):
                                                        global ValeurCapteurHumiditeA
                                                        ValeurCapteurHumiditeA = int(var[1])
                                                        
                                                if(var[0] == TexteCapteurHumiditeB):
                                                        global ValeurCapteurHumiditeB
                                                        ValeurCapteurHumiditeB = int(var[1])
                                                        
                                                if(var[0] == TexteCapteurHumiditeC):
                                                        global ValeurCapteurHumiditeC
                                                        ValeurCapteurHumiditeC = int(var[1])
                                                        
                                                if(var[0] == TexteCapteurHumiditeD):
                                                        global ValeurCapteurHumiditeD
                                                        ValeurCapteurHumiditeD = int(var[1])
                                                        
                                                if(var[0] == TexteCapteurLumiereA):
                                                        global ValeurCapteurLumiereA
                                                        ValeurCapteurLumiereA = int(var[1])
                                                        
                                                if(var[0] == TexteCapteurLumiereB):
                                                        global ValeurCapteurLumiereB
                                                        ValeurCapteurLumiereB = int(var[1])
                                        except:
                                                pass
def EnvoiCommande():
    #i=10
    #n=61
    i=4
    n=i*6+1
    j=0
    
    while(j !=n):
        try:
            LitValeurArduino()
            if(j==i*1):
                ArduinoSerie.write(("A"+str(1)+'\n').encode("ASCII"))
            if(j==i*2):
                ArduinoSerie.write(("B"+str(1)+'\n').encode("ASCII"))
            if(j==i*3):
                ArduinoSerie.write(("C"+str(1)+'\n').encode("ASCII"))
            if(j==i*4):
                ArduinoSerie.write(("D"+str(1)+'\n').encode("ASCII"))
            if(j==i*5):
                ArduinoSerie.write(("E"+str(1)+'\n').encode("ASCII"))
            if(j==i*6):
                ArduinoSerie.write(("F"+str(1)+'\n').encode("ASCII"))
            j+=1
        except:
            ArduinoSerie.close()
            ArduinoSerie.open()
    ArduinoSerie.flushInput()

def CommunicationModulesLampe():

    global ModuleLumiereAEtat
    global ModuleLumiereBEtat
    global ModuleLumiereAMax
    global ModuleLumiereBMax

    global ValeurModuleLumiereA
    global ValeurModuleLumiereB

    global LaNuit

    ModuleAEtatChange=False
    ModuleBEtatChange=False
    
    global ValeurMoyenneLumiereA
    global ValeurMoyenneLumiereB
    global EtatLumiereA
    global EtatLumiereB
    if (ArretEclairage is True):
        EtatLumiereAVoulue = False
        EtatLumiereBVoulue = False
        ModuleLumiereAEtat = False
        ModuleLumiereAMax = False
        
        if(ValeurModuleLumiereA !=0) and (ValeurModuleLumiereB!=0):            
            try:
                LampeA.write((CommandeModuleLumiere+str(ValeurModuleLumiereA)+'%' +'\n').encode("ASCII"))
                LampeB.write((CommandeModuleLumiere+str(ValeurModuleLumiereA)+'%' +'\n').encode("ASCII"))
                LampeC.write((CommandeModuleLumiere+str(ValeurModuleLumiereB)+'%' +'\n').encode("ASCII"))
                LampeD.write((CommandeModuleLumiere+str(ValeurModuleLumiereB)+'%' +'\n').encode("ASCII"))
            except:
                LampeA.close()
                LampeA.open()
                LampeB.close()
                LampeB.open()
                LampeC.close()
                LampeC.open()
                LampeD.close()
                LampeD.open()
    else:        
        #Un à La fois pour à cause de l'interférence de lux entre les lampes et les capteurs
        if (LumiereVoulueA < ValeurMoyenneLumiereA) and (ValeurModuleLumiereA < 100):
            ValeurModuleLumiereA+=1
            ModuleAEtatChange =True

        elif (LumiereVoulueA >ValeurMoyenneLumiereA) and (ValeurModuleLumiereA > 0):
            ValeurModuleLumiereA-=1
            ModuleAEtatChange =True
        
        elif (LumiereVoulueB <ValeurMoyenneLumiereB) and (ValeurModuleLumiereB < 100):
            ValeurModuleLumiereB+=1
            ModuleBEtatChange =True

        elif (LumiereVoulueB >ValeurMoyenneLumiereB) and (ValeurModuleLumiereB > 0):
            ValeurModuleLumiereB-=1
            ModuleBEtatChange =True

        if ValeurModuleLumiereA <=0:
            ModuleLumiereAEtat = False
            ModuleLumiereAMax = False
            
        if ValeurModuleLumiereA >=100:
            ModuleLumiereAEtat = True
            ModuleLumiereAMax = True

        if ValeurModuleLumiereB <=0:
            ModuleLumiereBEtat = False
            ModuleLumiereBMax = False
            
        if ValeurModuleLumiereB >=100:
            ModuleLumiereBEtat = True
            ModuleLumiereBMax = True
        
        try:
            if (ModuleAEtatChange is True):
                LampeA.write((CommandeModuleLumiere+str(ValeurModuleLumiereA)+'%' +'\n').encode("ASCII"))
                LampeB.write((CommandeModuleLumiere+str(ValeurModuleLumiereA)+'%' +'\n').encode("ASCII"))
            else:
                if (LumiereVoulueA > ValeurMoyenneLumiereA):
                    EtatLumiereAVoulue = True
                elif (LumiereVoulueA < ValeurMoyenneLumiereA):
                    EtatLumiereAVoulue = False
                    
            if (ModuleAEtatChange is True):
                LampeC.write((CommandeModuleLumiere+str(ValeurModuleLumiereB)+'%' +'\n').encode("ASCII"))
                LampeD.write((CommandeModuleLumiere+str(ValeurModuleLumiereB)+'%' +'\n').encode("ASCII"))
            else:
                if (LumiereVoulueB > ValeurMoyenneLumiereB):
                    EtatLumiereBVoulue = True
                elif (LumiereVoulueB < ValeurMoyenneLumiereB):
                    EtatLumiereBVoulue = False
        
        except:
            LampeA.close()
            LampeA.open()
            LampeB.close()
            LampeB.open()
            LampeC.close()
            LampeC.open()
            LampeD.close()
            LampeD.open()           
    LampeA.flushInput()
    LampeB.flushInput()
    LampeC.flushInput()
    LampeD.flushInput()

def CommunicationArduino():
    global ChangementEtatRelaiValveA
    global ChangementEtatRelaiValveB
    global ChangementEtatRelaiValveC
    global ChangementEtatRelaiValveD
    global ChangementEtatRelaiLumiereA
    global ChangementEtatRelaiLumiereB

    try:
        #lit 5 fois pour avoir les bonnes donnees
        for x in range(0,5): 
            LitValeurArduino()
        #envoi une seule commande a la fois pour le arduino pour ne pas le submerger de data
        if(ChangementEtatRelaiValveA is True):
            if EtatValveAVoulue is True:
                ArduinoSerie.write(("A"+str(1)+'\n').encode("ASCII"))
            if EtatValveAVoulue is False:
                ArduinoSerie.write(("A"+str(0)+'\n').encode("ASCII"))
            ChangementEtatRelaiValveA = False
                
        elif(ChangementEtatRelaiValveB is True):
            if EtatValveBVoulue is True:
                ArduinoSerie.write(("B"+str(1)+'\n').encode("ASCII"))
            if EtatValveBVoulue is False:
                ArduinoSerie.write(("B"+str(0)+'\n').encode("ASCII"))
            ChangementEtatRelaiValveB = False
            
        elif(ChangementEtatRelaiValveC is True):
            if EtatValveCVoulue is True:
                ArduinoSerie.write(("C"+str(1)+'\n').encode("ASCII"))
            if EtatValveCVoulue is False:
                 ArduinoSerie.write(("C"+str(0)+'\n').encode("ASCII"))
            ChangementEtatRelaiValveC = False
                
                
        elif(ChangementEtatRelaiValveD is True):
            if EtatValveDVoulue is True:
                ArduinoSerie.write(("D"+str(1)+'\n').encode("ASCII"))
            if EtatValveDVoulue is False:
                ArduinoSerie.write(("D"+str(0)+'\n').encode("ASCII"))
            ChangementEtatRelaiValveD= False
            
        elif(ChangementEtatRelaiLumiereA is True):
            if EtatLumiereAVoulue is True:
                ArduinoSerie.write(("E"+str(1)+'\n').encode("ASCII"))
            if EtatLumiereAVoulue is False:
                ArduinoSerie.write(("E"+str(0)+'\n').encode("ASCII"))
            ChangementEtatRelaiLumiereA = False
            
        elif(ChangementEtatRelaiLumiereB is True):
            if EtatLumiereBVoulue is True:
                ArduinoSerie.write(("F"+str(1)+'\n').encode("ASCII"))
            if EtatLumiereBVoulue is False:
                ArduinoSerie.write(("F"+str(0)+'\n').encode("ASCII"))
            ChangementEtatRelaiLumiereB = False
                
    except:
        ArduinoSerie.close()
        ArduinoSerie.open()
    ArduinoSerie.flushInput()
    
#interface            

def humA():
   global HumiditeVoulueA
   HumiditeVoulueA = float(HumA.get())
   valeur = str(HumiditeVoulueA)
   selection = "Nord_teneur en eau voulue:" + valeur +'%'
   LHumA.config(text = selection, font =FonteTexte)
def humB():
   global HumiditeVoulueB
   HumiditeVoulueB = float(HumB.get())
   valeur = str(HumiditeVoulueB)
   selection = "Sud_teneur en eau voulue:" + valeur +'%'
   LHumB.config(text = selection, font =FonteTexte)
def humC():
   global HumiditeVoulueC
   HumiditeVoulueC = float(HumC.get())
   valeur = str(HumiditeVoulueC)  
   selection = "Nord_teneur en eau voulue:" + valeur +'%'
   LHumC.config(text = selection, font =FonteTexte)
def humD():
   global HumiditeVoulueD
   HumiditeVoulueD = float(HumD.get())
   valeur = str(HumiditeVoulueD)
   selection = "Sud_teneur en eau voulue:" + valeur +'%'
   LHumD.config(text = selection, font =FonteTexte)
def lumA():
   global LumiereVoulueA
   LumiereVoulueA = int(LumA.get())
   valeur = str(LumiereVoulueA)   
   selection = "Lumière Voulue:" + valeur +'%'
   LLumA.config(text = selection, font =FonteTexte)
def lumB():
   global LumiereVoulueB
   LumiereVoulueB = int(LumB.get())
   valeur = str(LumiereVoulueB)   
   selection = "Lumière Voulue:" + valeur +'%'
   LLumB.config(text = selection, font =FonteTexte)

def OnOFF(var):
   if var == 0:
      return "OFF"
   else:
      return "ON"

def MiseAJourHeureActuelle():
   LeTemps = str(datetime.datetime.time(datetime.datetime.now()))
   LeTempsSepare=LeTemps.split(":")
   Heure= LeTempsSepare[0]
   global HeureActuelle
   HeureActuelle =int(Heure)
   VerifieHeure()

global ArretEclairage
#Temps d'éclairage pour le repos des plantes la nuit
def VerifieHeure():
   global ArretEclairage
   if (HeureActuelle<6) or (HeureActuelle>24):      
      ArretEclairage = True
   else:
      ArretEclairage = False
def MiseAJourEtatEtValeurReel():
   global VRHumA
   global VRHumB
   global VRHumC
   global VRHumD
   global VRLumA
   global VRLumB
   global EtatValveA
   global EtatValveB
   global EtatValveC
   global EtatValveD
   global EtatLumiereA
   global EtatLumiereB
   global EtatValveAVoulue
   global EtatValveBVoulue
   global EtatValveCVoulue
   global EtatValveDVoulue
   global EtatLumiereAVoulue
   global EtatLumiereBVoulue
   global HumiditeVoulueA
   global HumiditeVoulueB
   global HumiditeVoulueC
   global HumiditeVoulueD
   global LumiereVoulueA
   global LumiereVoulueB

   
   MiseAJourHeureActuelle()
   ChangeEtat()
   if (HumiditeVoulueA > VRHumA):
      EtatValveAVoulue = True;
   else:
      EtatValveAVoulue = False;
      
   if (HumiditeVoulueB > VRHumB):
      EtatValveBVoulue = True;
   else:
      EtatValveBVoulue = False;
      
   if (HumiditeVoulueC > VRHumC):
      EtatValveCVoulue = True;
   else:
      EtatValveCVoulue = False;
      
   if (HumiditeVoulueD > VRHumD):
      EtatValveDVoulue = True;
   else:
      EtatValveDVoulue = False;

   

def ChangeEtat():
   global EtatValveA
   global EtatValveB
   global EtatValveC
   global EtatValveD
   global EtatLumiereA
   global EtatLumiereB
   global EtatValveAVoulue
   global EtatValveBVoulue
   global EtatValveCVoulue
   global EtatValveDVoulue
   global EtatLumiereAVoulue
   global EtatLumiereBVoulue
   global EtatRelaiValveA
   global EtatRelaiValveB
   global EtatRelaiValveC
   global EtatRelaiValveD
   global EtatRelaiLumiereA
   global EtatRelaiLumiereB
   global ChangementEtatRelaiValveA
   global ChangementEtatRelaiValveB
   global ChangementEtatRelaiValveC
   global ChangementEtatRelaiValveD
   global ChangementEtatRelaiLumiereA
   global ChangementEtatRelaiLumiereB
   
   if(EtatRelaiValveA==0):
       EtatValveA=False
   if(EtatRelaiValveA==1):
       EtatValveA=True
   if(EtatRelaiValveB==0):
       EtatValveB=False
   if(EtatRelaiValveB==1):
       EtatValveB=True
   if(EtatRelaiValveC==0):
       EtatValveC=False
   if(EtatRelaiValveC==1):
       EtatValveC=True
   if(EtatRelaiValveD==0):
       EtatValveD=False
   if(EtatRelaiValveD==1):
       EtatValveD=True    
   if(EtatRelaiLumiereA==0):
       EtatLumiereA=False
   if(EtatRelaiLumiereA==1):
       EtatLumiereA=True    
   if(EtatRelaiLumiereB==0):
       EtatLumiereB=False
   if(EtatRelaiLumiereB==1):
       EtatLumiereB=True
       
   if(EtatValveA!=EtatValveAVoulue):
       ChangementEtatRelaiValveA =True  
   if(EtatValveB!=EtatValveBVoulue):
       ChangementEtatRelaiValveB =True 
   if(EtatValveC!=EtatValveCVoulue):
       ChangementEtatRelaiValveC =True 
   if(EtatValveD!=EtatValveDVoulue):
       ChangementEtatRelaiValveD =True 
   if(EtatLumiereA!=EtatLumiereAVoulue):
       ChangementEtatRelaiLumiereA =True 
   if(EtatLumiereB!=EtatLumiereBVoulue):
       ChangementEtatRelaiLumiereB =True 

def MiseAjourInterface():
   MiseAJourEtatEtValeurReel()
   
   global VRHumA
   global VRHumB
   global VRHumC
   global VRHumD
   global VRLumA
   global VRLumB
   global EtatValveA
   global EtatValveB
   global EtatValveC
   global EtatValveD
   global EtatLumiereA
   global EtatLumiereB
   global CompteurMoyenneLumiere
   global CumulMoyenneLumiereA
   global CumulMoyenneLumiereB 
   VRHumA=ValeurCapteurHumiditeA/100
   VRHumB=ValeurCapteurHumiditeB/100
   VRHumC=ValeurCapteurHumiditeC/100
   VRHumD=ValeurCapteurHumiditeD/100
   VRLumA=100-(ValeurCapteurLumiereA/134)
   VRLumB=100-(ValeurCapteurLumiereB/134)

   if(VRLumA>100):
       VRLumA=100
   if(VRLumB>100):
       VRLumB=100
       
   VRLumA=round(VRLumA,2)    
   VRLumB=round(VRLumB,2)
   
   
   if CompteurMoyenneLumiere!=NombreDePasseLumieres:
       CumulMoyenneLumiereA+=VRLumA
       CumulMoyenneLumiereB+=VRLumB
       CompteurMoyenneLumiere +=1
       
    
   else:
       CompteurMoyenneLumiere = 0
       ValeurMoyenneLumiereA=CumulMoyenneLumiereA/NombreDePasseLumieres
       ValeurMoyenneLumiereB=CumulMoyenneLumiereB/NombreDePasseLumieres
              


   #les états
   texte = 'Valve nord:'+ str(OnOFF(EtatValveA))
   if(EtatValveA is False):     
      LEtatValveA.configure(text = texte,background="red",relief ="raised")
   else:
      LEtatValveA.configure(text = texte,background="green",relief ="raised")
      
   texte = 'Valve sud:'+ str(OnOFF(EtatValveB))
   if(EtatValveB is False):
      LEtatValveB.configure(text = texte,background="red",relief ="raised")
   else:
      LEtatValveB.configure(text = texte,background="green",relief ="raised")
      
   texte = 'Valve nord:'+ str(OnOFF(EtatValveC))     
   if(EtatValveC is False):
      LEtatValveC.configure(text = texte,background="red",relief ="raised")
   else:
      LEtatValveC.configure(text = texte,background="green",relief ="raised")
      
   texte = 'Valve sud:'+ str(OnOFF(EtatValveD))  
   if(EtatValveD is False):
      LEtatValveD.configure(text = texte,background="red",relief ="raised")
   else:
      LEtatValveD.configure(text = texte,background="green",relief ="raised")

   texte = 'Lumière:'+ str(OnOFF(EtatLumiereA))   
   if(EtatLumiereA is False) and (ModuleLumiereAEtat is False):
      LEtatLumiereA.configure(text = texte,background="red",relief ="raised")
   else:
      LEtatLumiereA.configure(text = texte,background="green",relief ="raised")
      
   texte = 'Lumière:'+ str(OnOFF(EtatLumiereB))   
   if(EtatLumiereB is False) and (ModuleLumiereBEtat is False):
      LEtatLumiereB.configure(text = texte,background="red",relief ="raised")
   else:
      LEtatLumiereB.configure(text = texte,background="green",relief ="raised")

   #les valeurs
   if VRHumA > 50:
       LVRHumA.configure(text='Nord_teneur en eau réelle:'+'Saturé'+'%', font =FonteTexte)
   else:
       LVRHumA.configure(text='Nord_teneur en eau réelle:'+str(VRHumA)+'%', font =FonteTexte)

   if VRHumB > 50:
       LVRHumB.configure(text='Sud_teneur en eau réelle:'+'Saturé'+'%', font =FonteTexte)
   else:
       LVRHumB.configure(text='Sud_teneur en eau réelle:'+str(VRHumB)+'%', font =FonteTexte)

   if VRHumC > 50:
       LVRHumC.configure(text='Nord_teneur en eau réelle:'+'Saturé'+'%', font =FonteTexte)
   else:
       LVRHumC.configure(text='Nord_teneur en eau réelle:'+str(VRHumC)+'%', font =FonteTexte)

   if VRHumD > 50:
       LVRHumD.configure(text='Sud_teneur en eau réelle:'+'Saturé'+'%', font =FonteTexte)
   else:
       LVRHumD.configure(text='Sud_teneur en eau réelle:'+str(VRHumD)+'%', font =FonteTexte)
       
   LVRLumA.configure(text ='Lumière Réelle:'+str(ValeurMoyenneLumiereA)+'%',font =FonteTexte)
   LVRLumB.configure(text='Lumière Réelle:'+str(ValeurMoyenneLumiereB)+'%',font =FonteTexte)
   
   CommunicationArduino()    
   root.after(2000,MiseAjourInterface)

global HeureActuelle
HeureActuelle =int(0)
global ArretEclairage
ArretEclairage = False

root = Tk()
root.title("Automatisation De Serre")
root.geometry("1200x600")
i=1
while i!=4:
   root.columnconfigure(i,weight=1)
   i+=1
i=1
while i!=13:
   root.rowconfigure(i,weight=1)
   i+=1

FonteTexte = "Arial 11 bold"

HumA = DoubleVar()
HumB = DoubleVar()
HumC = DoubleVar()
HumD = DoubleVar()
LumA = DoubleVar()
LumB = DoubleVar()



scaleA = Scale(root, from_=0.0, to=50.0, length=200,orient=HORIZONTAL,variable = HumA,resolution=0.1, font =FonteTexte)
scaleA.grid(column=1, row=2,ipady=20)

labelblanc = ttk.Separator(root, orient=VERTICAL,)
labelblanc.grid(column=3, row=1,sticky="nsw", rowspan=12)
                    

buttonA = Button(root, text="Régler la teneur en eau nord", command=humA, font =FonteTexte)
buttonA.grid(column=1, row=3)

scaleB = Scale( root, from_=0.0, to=50.0, length=200,orient=HORIZONTAL,variable = HumB,resolution=0.1 , font =FonteTexte)
scaleB.grid(column=2, row=2,ipady=20)

buttonB = Button(root, text="Régler la teneur en eau sud", command=humB, font =FonteTexte)
buttonB.grid(column=2, row=3)

scaleC = Scale( root, from_=0, to=50,length=200,orient=HORIZONTAL, variable = HumC,resolution=0.1 , font =FonteTexte)
scaleC.grid(column=3, row=2,ipady=20)

buttonC = Button(root, text="Régler la teneur en eau nord", command=humC, font =FonteTexte)
buttonC.grid(column=3, row=3)

scaleD = Scale( root, from_=0, to=50,length=200,orient=HORIZONTAL,variable = HumD,resolution=0.1, font =FonteTexte )
scaleD.grid(column=4, row=2,padx=30,ipady=20)
            
buttonD = Button(root, text="Régler la teneur en eau sud", command=humD, font =FonteTexte)
buttonD.grid(column=4, row=3)

scaleE = Scale( root, from_=0, to=100,length=200,orient=HORIZONTAL,variable = LumA, font =FonteTexte )
scaleE.grid(column=1, row=8, columnspan =2,ipady=20)

buttonE = Button(root, text="Régler Lumière", command=lumA, font =FonteTexte)
buttonE.grid(column=1, row=9, columnspan =2)

scaleF = Scale( root, from_=0, to=100,length=200,orient=HORIZONTAL,variable = LumB, font =FonteTexte )
scaleF.grid(column=3, row=8, columnspan=2,ipady=20)

buttonF = Button(root, text="Régler Lumière", command=lumB, font =FonteTexte)
buttonF.grid(column=3, row=9,columnspan =2)


#VR Valeur Réel
global VRHumA
global VRHumB
global VRHumC
global VRHumD
global VRLumA
global VRLumB
VRHumA =0
VRHumB =0
VRHumC =0
VRHumD =0
VRLumA =0
VRLumB =0

#Etat Valve et Etat Lumière

global EtatValveA
global EtatValveB
global EtatValveC
global EtatValveD
global EtatLumiereA
global EtatLumiereB

EtatValveA=False
EtatValveB=False
EtatValveC=False
EtatValveD=False
EtatLumiereA=False
EtatLumiereB=False

#Valeur voulue
global HumiditeVoulueA
global HumiditeVoulueB
global HumiditeVoulueC
global HumiditeVoulueD
global LumiereVoulueA
global LumiereVoulueB
       
HumiditeVoulueA =0
HumiditeVoulueB =0
HumiditeVoulueC =0
HumiditeVoulueD =0
LumiereVoulueA =0
LumiereVoulueB =0

global EtatValveAVoulue
global EtatValveBVoulue
global EtatValveCVoulue
global EtatValveDVoulue
global EtatLumiereAVoulue
global EtatLumiereBVoulue

EtatValveAVoulue = False
EtatValveBVoulue = False
EtatValveCVoulue = False
EtatValveDVoulue = False
EtatLumiereAVoulue = False
EtatLumiereBVoulue = False

BacA =  Label(root, text='Bac 1:',font = "Arial 16 bold")
BacA.grid(column=1, row=1,columnspan=2)
BacA =  Label(root, text='Bac 2:',font = "Arial 16 bold")
BacA.grid(column=3, row=1,columnspan=2)

TVRHumA= str(VRHumA)
TVRHumB= str(VRHumB)
TVRHumC= str(VRHumC)
TVRHumD= str(VRHumD)

if VRHumA > 50:
   TVRHumA = "Saturé"
if VRHumB > 50:
   TVRHumB = "Saturé"
if VRHumC > 50:
   TVRHumC = "Saturé"
if VRHumD > 50:
   TVRHumD = "Saturé"


LVRHumA = Label(root, text='Nord_teneur en eau réelle:'+TVRHumA+'%', font =FonteTexte)
LVRHumA.grid(column=1, row=5)
LVRHumB = Label(root, text='Sud_teneur en eau réelle:'+TVRHumB+'%', font =FonteTexte)
LVRHumB.grid(column=2, row=5)
LVRHumC= Label(root, text='Nord_teneur en eau réelle:'+TVRHumC+'%', font =FonteTexte)
LVRHumC.grid(column=3, row=5)
LVRHumD = Label(root, text='Sud_teneur en eau réelle:'+TVRHumD+'%', font =FonteTexte)
LVRHumD.grid(column=4, row=5)
LVRLumA = Label(root, text='Lumière Réelle:'+str(VRLumA)+'%',font =FonteTexte)
LVRLumA.grid(column=1, row=10,columnspan =2)
LVRLumB = Label(root, text='Lumière Réelle:'+str(VRLumB)+'%',font =FonteTexte)
LVRLumB.grid(column=3, row=10,columnspan =2)

LHumA = Label(root)
LHumB = Label(root)
LHumC = Label(root)
LHumD = Label(root)
LLumA = Label(root)
LLumB = Label(root)


LHumA = Label(root, text='Nord_teneur en eau voulue:'+'0'+'%',font =FonteTexte)
LHumA.grid(column=1, row=6)
LHumB = Label(root, text='Sud_teneur en eau voulue:'+'0'+'%',font =FonteTexte)
LHumB.grid(column=2, row=6)
LHumC = Label(root, text='Nord_teneur en eau voulue:'+'0'+'%',font =FonteTexte)
LHumC.grid(column=3, row=6)
LHumD = Label(root, text='Sud_teneur en eau Voulue:'+'0'+'%',font =FonteTexte)
LHumD.grid(column=4, row=6)
LLumA = Label(root, text='Lumière Voulue:'+'0'+'%',font =FonteTexte)
LLumA.grid(column=1, row=11,columnspan =2)
LLumB = Label(root, text='Lumière Voulue:'+'0'+'%',font =FonteTexte)
LLumB.grid(column=3, row=11,columnspan =2)



LEtatValveA = Label(root, text='ValveA:'+str(OnOFF(EtatValveA)),font =FonteTexte)
if(EtatValveA == 0):
   LEtatValveA.configure(background="red",relief ="raised")
else:
   LEtatValveA.configure(background="green",relief ="raised")   
LEtatValveA.grid(column=1, row=7,ipady=10)

LEtatValveB = Label(root, text='ValveB:'+str(OnOFF(EtatValveB)),font =FonteTexte)
if(EtatValveB == 0):
   LEtatValveB.configure(background="red",relief ="raised")
else:
   LEtatValveB.configure(background="green",relief ="raised") 
LEtatValveB.grid(column=2, row=7,ipady=10)

LEtatValveC= Label(root, text='ValveC:'+str(OnOFF(EtatValveC)),font =FonteTexte)
if(EtatValveC == 0):
   LEtatValveC.configure(background="red",relief ="raised")
else:
   LEtatValveC.configure(background="green",relief ="raised") 
LEtatValveC.grid(column=3, row=7,ipady=10)

LEtatValveD = Label(root, text='ValveD:'+str(OnOFF(EtatValveD)),font =FonteTexte)
if(EtatValveD == 0):
   LEtatValveD.configure(background="red",relief ="raised")
else:
   LEtatValveD.configure(background="green",relief ="raised") 
LEtatValveD.grid(column=4, row=7,ipady=10)

LEtatLumiereA = Label(root, text='LumiereA:'+str(OnOFF(EtatLumiereA)),font =FonteTexte)
if(EtatLumiereA == 0):
   LEtatLumiereA.configure(background="red",relief ="raised")
else:
   LEtatLumiereA.configure(background="green",relief ="raised") 
LEtatLumiereA.grid(column=1, row=12,columnspan =2,ipady=10)

LEtatLumiereB = Label(root, text='LumiereB:'+str(OnOFF(EtatLumiereB)),font =FonteTexte)
if(EtatLumiereB == 0):
   LEtatLumiereB.configure(background="red",relief ="raised")
else:
   LEtatLumiereB.configure(background="green",relief ="raised") 
LEtatLumiereB.grid(column=3, row=12, columnspan =2,ipady=10)

MiseAjourInterface()

root.mainloop()



        
