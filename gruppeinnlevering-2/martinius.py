# martinius.py
# IS-118 Gruppeoppgave 2 – interaktiv storyline
# Spilleren er prosjektleder Erling og tar tre valg som påvirker teamet.
# Hvert valg gir 0 eller 1 poeng, og poengsummen avgjør sluttutfallet.

# Introduksjon
print("Velkommen! Du er Erling, prosjektleder i kommunen.")
print("Du leder et team på 7-8 personer med ulike forventninger og verdier.")
print("Sammen skal dere utvikle en digital medborgerportal for kommunen, og dere har 15 måneder på dere.")
print("Prosjektet startet med høy energi, men etter seks uker har samarbeidet blitt vanskeligere.")
print(
    "Silje og Elias er i en konflikt som har blitt personlig, mens uenigheten mellom Hamdi og Hallgeir ulmer i bakgrunnen."
)
print("Lagånden i teamet synker, og du må ta tre valg som påvirker hvordan teamet og prosjektet utvikler seg videre.")
print("Du svarer ved å skrive 1 eller 2.")

# Poengsummen starter på 0 og øker når spilleren tar tak i konflikter eller styrker relasjonene
poeng = 0

# Beslutning 1: konflikten mellom Silje og Elias
print()
print("Det er tre uker til den første prototypen skal være ferdig.")
print("Silje og Elias er uenige om teknologivalget for portalen.")
print("Silje vil prioritere brukervennlighet, mens Elias legger vekt på sikkerhet og kostnader.")
print("Diskusjonene har blitt personlige, og begge har begynt å søke støtte hos andre i teamet.")
print("Hva gjør du?")
print("1: Ta opp konflikten i plenum med hele teamet")
print("2: Ha individuelle samtaler med Silje og Elias")

valg1 = input("Ditt valg (1 eller 2): ")

# Spør på nytt hvis svaret ikke er 1 eller 2
while valg1 != "1" and valg1 != "2":
    valg1 = input("Ugyldig valg. Skriv 1 eller 2: ")

if valg1 == "1":
    print("Du tar opp konflikten i plenum. Bakpraten stopper, og teamet ser at du tar tak i problemer.")
    print("Men Silje og Elias må forsvare seg foran alle, og de som støtter dem, blir dratt inn i konflikten.")
    print("Teamet deler seg, og Hamdi og Hallgeir havner på hver sin side.")
elif valg1 == "2":
    print("Du snakker med Silje og Elias hver for seg. De føler seg sett, og temperaturen i teamet går ned.")
    print("Resten av teamet antar at konflikten er løst, men Silje og Elias lurer på om du tok parti.")
    print("Hamdi og Hallgeir er fortsatt uenige, men ingen av dem har tatt side ennå.")
    poeng = poeng + 1

# Beslutning 2: uenigheten mellom Hamdi og Hallgeir
print()

# Situasjonen avhenger av hva spilleren valgte i beslutning 1
if valg1 == "1":
    print("Etter plenumsmøtet er uenigheten mellom Hamdi og Hallgeir ikke lenger skjult.")
    print("Det er for sent å forebygge, for konflikten har allerede kommet til overflaten.")
else:
    print("Det har roet seg i teamet etter samtalene med Silje og Elias.")
    print("Men uenigheten mellom Hamdi og Hallgeir ulmer i det stille, og en dag spør Hamdi om dere kan ta en prat.")

print("Hamdi vil at innbyggerne skal delta i digitale folkemøter gjennom kommunens egen, kontrollerte plattform.")
print("Hallgeir vil ha mer åpenhet og rom for spontane innspill fra innbyggerne.")
print("Hva gjør du?")
print("1: Kalle inn Hamdi og Hallgeir til et felles møte")
print("2: Avvente og la dem forsøke å løse det selv")

valg2 = input("Ditt valg (1 eller 2): ")

# Spør på nytt hvis svaret ikke er 1 eller 2
while valg2 != "1" and valg2 != "2":
    valg2 = input("Ugyldig valg. Skriv 1 eller 2: ")

if valg2 == "1":
    print("I møtet ser Hamdi og Hallgeir at de har et felles mål om at innbyggerne skal kunne delta.")
    print("De blir enige om et kompromiss: en kontrollert plattform med en åpen funksjon for innspill.")
    print("Men møtet tar tid, og prototypen skal snart leveres.")
    poeng = poeng + 1
elif valg2 == "2":
    print("Du får mer tid til fremdriften, og Hamdi og Hallgeir får ansvar for å finne en løsning selv.")
    print("Men uenigheten fortsetter, og frustrasjonen vokser og begynner å påvirke samarbeidet.")

# Beslutning 3: motivasjonen i teamet
print()

# Situasjonen avhenger av begge de forrige valgene
if valg1 == "2" and valg2 == "1":
    print("Begge konfliktene er dempet, og ingen har tatt side.")
    print("Teamet har et godt utgangspunkt, men tilliten etter seks uker med uro er ikke helt på topp.")
elif valg1 == "2" and valg2 == "2":
    print("Teamet er fortsatt samlet etter samtalene med Silje og Elias.")
    print("Men uenigheten mellom Hamdi og Hallgeir har vokst i det stille og er i ferd med å blusse opp.")
elif valg1 == "1" and valg2 == "1":
    print("Hamdi og Hallgeir har funnet et kompromiss.")
    print("Men teamet bærer fortsatt preg av splittelsen etter plenumsmøtet.")
else:
    print("Teamet er delt i to leirer, og uenigheten mellom Hamdi og Hallgeir har blitt en del av splittelsen.")
    print("Det er mye mistillit i teamet, og arbeidet med prototypen står i fare.")

print("Fristen for prototypen nærmer seg, og motivasjonen i teamet synker.")
print("Hva gjør du?")
print("1: Sette av tid til relasjonsbygging, for eksempel en uformell samling")
print("2: Prioritere fremdrift og la teamet fokusere på prototypen")

valg3 = input("Ditt valg (1 eller 2): ")

# Spør på nytt hvis svaret ikke er 1 eller 2
while valg3 != "1" and valg3 != "2":
    valg3 = input("Ugyldig valg. Skriv 1 eller 2: ")

if valg3 == "1":
    print("Teamet blir bedre kjent, og det blir lettere å forstå hverandre på tvers av fagområdene.")
    print("Men samlingen tar tid fra prototypen, og den løser ikke konfliktene av seg selv.")
    poeng = poeng + 1
elif valg3 == "2":
    print("Teamet får synlige resultater, og det gir en følelse av mestring.")
    print("Men problemene i teamet blir liggende, og de kan komme tilbake når nye beslutninger skal tas.")

# Sluttutfall basert på poengsummen
print()
print("Du fikk", poeng, "av 3 poeng.")

if poeng == 3:
    print("Teamet kommer seg ut av storming-fasen og går over i norming.")
    print("Uenighetene forsvinner ikke, men teamet har et godt grunnlag for å håndtere dem sammen.")
elif poeng == 2:
    print("Konfliktene er delvis løst, og teamet er på vei ut av storming-fasen.")
    print("Men relasjonene er sårbare, og du må følge med på at konfliktene ikke blusser opp igjen.")
else:
    print("Flere konflikter står uløst, og teamet blir stående fast i storming-fasen.")
    print("Motivasjonen er lav, samarbeidet er svakt, og prosjektet blir forsinket.")
