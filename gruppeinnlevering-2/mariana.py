print ("Velkommen til Erlings beslutningsspill!")
print ("Du er Erling, prosjektleder for kommunens nye digitale medborgerportal.")
print ("Du skal ta tre beslutninger som påvirker samarbeidet i prosjektgruppen.")
input ("Trykk enter for å starte spillet.")
poeng = 0
print ("Beslutning 1: Konflikten mellom Silje og Elias")
print ("Silje og Elias er uenige om hvordan medborgerportalen skal utvikles.")
print ("Erling må bestemme hvordan han skal håndtere konflikten.")
print ("A: Ta opp konflikten i plenum")
print ("B: Ha individuelle samtaler med Silje og Elias")
valg1 = input ("Velg A eller B: "). upper()
while valg1 != "A" and valg1 != "B":
    valg1 = input("Ugyldig valg! Velg A eller B: ").upper()
if valg1 == "A":
    print ("Erling tar opp konflikten foran hele teamet.")
    print ("Silje og Elias går i forsvar, og teamet blir mer splittet.")
elif valg1 == "B":
    print ("Erling snakker med Silje og Elias hver for seg.")
    print ("Konflikten roer seg, og teamet unngår en synlig splittelse.")
    poeng = poeng + 1
print ("Poengsum:", poeng)
print ()
if valg1 == "A":
    print ("Spittelsen i teamet gjør uenigheten mellom Hamdi og Hallgeir mer synlig.")
else: 
    print ("Stemningen i teamet er roligere, men Hamdi og Hallgeir er fortsatt uenige.")
print ("Beslutning 2: Konflikten mellom Hamdi og Hallgeir")
print ("Hamdi og Hallgeir har en konflikt som påvirker samarbeidet i teamet.")
print ("Erling må bestemme hvordan han skal håndtere situasjonen.")
print ("A: Ha et fellesmøte med Hamdi og Hallgeir")
print ("B: Vente og se om konflikten løser seg selv")
valg2 = input("Velg A eller B: "). upper()
while valg2 != "A" and valg2 != "B":
    valg2 = input("Ugyldig valg! Velg A eller B: ").upper()
if valg2 == "A": 
    print ("Erling arrangerer et fellesmøte mellom Hamdi og Hallgeir.")
    print ("Hamdi og Hallgeir får diskutert uenigheten og finner et kompromiss.")
    poeng = poeng + 1
elif valg2 == "B": 
    print ("Erling velger å vente og se om konflikten løser seg selv.")
    print ("Frustrasjonen mellom Hamdi og Hallgeir øker, og samarbeidet blir vanskeligere.")
print ("Total poengsum:", poeng)
print ()
if poeng == 2:
    print ("Begge konfliktene har roet seg, men teamet trenger fortsatt å styrke tilliten.")
elif poeng == 1:
    print ("En av konfliktene er håndtert, men det er fortsatt spenninger i teamet.") 
else:
    print ("Begge konfliktene er fortsatt uløst, og samarbeidet i teamet er vanskelig.")
print ("Beslutning 3: Motivasjonen i teamet")
print ("Prototypen skal være ferdig om tre uker.")
print ("Erling må bestemme hvordan han skal holde motivasjonen oppe i teamet.")
print ("A: Sette av tid til relasjonsbygging")
print ("B: Prioritere fremdrift og leveranser")
valg3 = input("Velg A eller B: "). upper()
while valg3 != "A" and valg3 != "B":
    valg3 = input("Ugyldig valg! Velg A eller B: ").upper()
if valg3 == "A":
    print ("Erling setter av tid til relasjonsbygging.")
    print ("Teamet blir bedre kjent, og tilliten og samarbeidet styrkes.")
    poeng = poeng + 1
elif valg3 == "B": 
    print ("Erling velger å prioritere fremdrift og leveranser")
    print ("Teamet jobber videre med prototypen, men konflikten kan påvirke samarbeidet.")
print ()
print ("Spillet er ferdig!")
print ("Din totale poengsum er:", poeng) 
if poeng == 3:
    print ("Teamet har klart å håndtere konfliktene og styrke samarbeidet.")
    print ("Teamet beveger seg fra storming-fasen til norming-fasen.")
elif poeng == 2: 
    print ("Teamet har løst noen av problemene, men samarbeidet er fortsatt sårbart.")
    print ("Erling må fortsette å jobbe med tilliten og kommunikasjonen i teamet.")
else: 
    print ("Flere konflikter i teamet er fortsatt uløst.")
    print ("Teamet blir værende i storming-fasen, og prosjektet kan bli forsinket.")