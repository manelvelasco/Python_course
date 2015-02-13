# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 18:00:16 2013

@author: Manel velasco
"""

class foo:
    def __init__(self):
        pass
    def mi_funcion(self,*args,**kwargs):
        selector=""
        for index,item in enumerate(args):
            selector=selector+"_"+item.__class__.__name__
        try:
            return getattr(self,"mi_funcion"+selector)(*args,**kwargs)
        except:
            print "mi_funcion con parametros "+ repr(selector.split('_')[1:])+" no esta definida en la clase "+self.__class__.__name__
            
    def mi_funcion_str(self,cadena):
        print "sobrecarga con una cadena, la cadena es: " + cadena
    
    def mi_funcion_str_str(self, cadena1, cadena2):
        print "Sobrecarga con dos cadenas, las cadenas son: "+cadena1+", "+cadena2
    
    def mi_funcion_int(self, num):
        print "sobrecarga con un entero, el entero es: " + str(num)

a=foo()
a.mi_funcion("hola")
a.mi_funcion("hola","adios")
a.mi_funcion(3)
a.mi_funcion(3.)
