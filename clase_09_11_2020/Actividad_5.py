'''
Created on 13-nov-2020

@author: maxus
'''
class Persona:
    def  __init__ (self, nombre, edad, lugarresidencia):
        self.__nombre = nombre
        self.__edad = edad
        self.__lugarresidencia = lugarresidencia
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre=nombre
        
    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, edad):
        self.__edad=edad
    
    @property
    def lugarresidencia(self):
        return self.__lugarresidencia
    
    @lugarresidencia.setter
    def lugarresidencia(self, lugarresidencia):
        self.__lugarresidencia=lugarresidencia
    
    def descripcion(self):
        cadena="Persona: "+self.nombre+", Edad: "+str(self.edad)+", Lugar de residencia: "+self.lugarresidencia
        return cadena

class Empleado(Persona):
     
    def __init__ (self, nombre, edad, lugarresidencia,salario,antiguedad):
        super().__init__(nombre, edad, lugarresidencia)
        self.__salario = salario
        self.__antiguedad = antiguedad
         
    @property
    def salario(self):
        return self.__salario
     
    @salario.setter
    def salario(self,salario):
        self.__salario = salario
         
     
    @property
    def antiguedad(self):
        return self.__antiguedad
      
    @antiguedad.setter
    def antiguedad(self,antiguedad):
        self.__antiguedad = antiguedad
        
    def descripcionempleado(self):
#        super.descripcion() 
#       cadena2 = ""
#        cadena2 = "Persona: "+ super.__nombre+",\nEdad:"+str(super.__edad)+ ",\nLugar de Residencia: "+super.__lugarresidencia+ ",\nSalario: "+self.__salario+ ",\nantiguedad: "+self.__antiguedad+" anyos"
        cadena3 = super().descripcion()+ ",\nSalario: "+str(self.__salario)+ ",\nantiguedad: "+str(self.antiguedad)
        return cadena3
    

pers = Empleado('Rogelio', 23, 'Sevilla', 32500, 8)
print(pers.descripcionempleado())
persona = Persona("Clara", 12, "Mairena")
print(persona.descripcion())