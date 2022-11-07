tall1 = 8
tall2 = 6

print(tall1 * tall2)

print(6*8)

def arealkalkulator():
    bredde = 8
    lengde = 6

    areal = bredde * lengde
    print(f"Arealet til rektangelen er {areal}" + ".")
    #Her brukte jeg en f-streng

arealkalkulator()

def VolumTilEnKubeKalkulator():
    Lengde = 10
    Bredde = 5
    Høyde = 8
    GrunnFlate = Lengde * Bredde
    Volum = GrunnFlate * Høyde
    print(Volum)

VolumTilEnKubeKalkulator()

def SporsmalOmNavn():
    navn = input("Hva heter du?")
    print("Hyggelig å møtte deg " + navn + "!")

SporsmalOmNavn()

def MultiplikasjonAv2Helltall():
    heltall1 = int(input("Velg et heltall: "))
    heltall2 = int(input("Velg et annet heltall: "))
    print("Produktet blir: " + str(heltall1 * heltall2))

MultiplikasjonAv2Helltall()