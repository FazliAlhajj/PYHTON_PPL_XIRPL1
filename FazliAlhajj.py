class agama:
    def __init__(self, nama, kepercayaan):
        self.nama = nama 
        self.kepercayaan = kepercayaan
        
    def perkenalan(self):
        print (self.nama,"beragama",self.kepercayaan)
  
class islam(agama):
    def __init__(self, nama, kepercayaan, sholat):
        agama.__init__(self, nama, kepercayaan)
        self.sholat = sholat
        
class kristen(agama):
    def __init__(self, nama, kepercayaan, sembahyang):
        agama.__init__(self, nama, kepercayaan)
        self.sembahyang = sembahyang
        
        
        
Hisyam = islam('Hisyam','Islam','Sholat')
Hisyam.perkenalan()
print (f'{Hisyam.nama} beribadah dengan melakukan {Hisyam.sholat}\n')

Abraham = kristen('Abraham', 'Kristen', 'Sembahyang')
Abraham.perkenalan()
print (f'{Abraham.nama} beribadah dengan melakukan {Abraham.sembahyang}\n')


                
