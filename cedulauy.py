#!/usr/bin/env python

import random

def crear_cedula( ):
    cedula    = []
    for n in range(0,7):
        cedula.append( random.randint(0,9) )
    dv = digito_verificador( cedula )
    ci = ''.join(map(str,cedula)) + '-' + str(dv)
    return ci

def digito_verificador( cedula ):
    factores  = [2,9,8,7,6,3,4]
    sumatoria = 0
    digverif  = 0
    for d in range(0,7):
         sumatoria += cedula[d] * factores[d]
    digverif = 10 - (sumatoria % 10)
    return digverif
