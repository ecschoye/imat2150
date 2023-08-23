import numpy as np

def nest(c,x):
    #Evaluer polynomet med koeffisienter c[] i x vha horners metode
    #Du kan se på matlabfunksjonen nest i Sauer for inspirasjon

    # Initialize result
    result = c[0]

    # Evaluate value of polynomial
    # using Horner's method
    for i in range(1, len(c)):
        result = result * x + c[i]

    return result


#Denne funksjonen skal printe ut feilen du får når du bruker funksjonen "funk(c,x)"
#til å evaluere polynomet fra oppgaveteksten ved å sammenligne det med det ekvivalente uttrykket
def test_feil(funk):
    c = np.ones(51) #sjekk ut numpy funksjonen ones :)
    x = 1.00001
    Px = (x**51-1)/(x-1)  #Ekvivalent uttrykk for polynom fra oppgavetekst, evaluert i x=1.00001
    return "{:.11e}".format(abs(Px - funk(c, x))) #returnerer absoluttverdien av differansen mellom Px og polynomet evaluert i x, med 11 desimaler




