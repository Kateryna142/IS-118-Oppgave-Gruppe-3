# Kateryna Lykhatska
# Gruppeinnlevering 2 - IS-118
# Interaktiv historie: Erling og prosjektteamet i storming-fasen
#
# ---------- Variabler ----------
valg1 = ""   # Beslutning 1: "plenum" eller "individuelle samtaler"
valg2 = ""   # Beslutning 2: "felles møte" eller "avvente"
valg3 = ""   # Beslutning 3: "relasjonsbygging" eller "fremdrift"
poeng = 0    # 0 eller 1 poeng per beslutning, maks 3
print()
print("    Velkommen til den interaktive historien")
print()
print("===Erling og prosjektteamet i storming-fasen!===")
print()
print("Det har gått seks uker siden Erling samlet teamet som skal utvikle kommunens nye digitale medborgerportal.")
print("Oppstarten var full av energi, men nå begynner samarbeidet å knirke. Teamet er i storming-fasen: stemningen")
print("er spent og kommunikasjonen hakkete.")
print()
print("Silje (UX-designer) og Elias (IT-rådgiver) er uenige om teknologivalg og design, og diskusjonene har blitt mer personlige.")
print("Samtidig vokser spenningen mellom Hamdi (kulturavdelingen) og Hallgeir (innbyggerforeningen) om hvordan innbyggerne skal")
print("delta i digitale folkemøter. Første prototype skal være klar om tre uker.")
print()
print("Du er Erling, og valgene dine avgjør om teamet går videre mot norming, eller blir stående fast i stormen.")
print()
input("Trykk Enter for å starte... ")
print()
print("===Beslutning 1: Silje og Elias===")
print("Du har to alternativer for å håndtere konflikten mellom Silje og Elias:")
print("A. Ta det opp i plenum for å skape åpenhet")
print("B. Ta individuelle samtaler for å dempe temperaturen")

while valg1 == "":
    svar = input("Hva velger du? (A/B): ").strip().upper()
    if svar == "A":
        valg1 = "plenum"
    elif svar == "B":
        valg1 = "individuelle samtaler"
        poeng += 1
    else:
        print("Ugyldig valg. Vennligst velg A eller B.")

if valg1 == "plenum":
    print("Alle får høre begge sider, og teamet ser at du tar ansvar. Men Silje og Elias føler")
    print("at de må forsvare seg foran de andre, og diskusjonen dreier seg mer om personlige")
    print("motsetninger enn om selve teknologivalget.")
elif valg1 == "individuelle samtaler":
    print("Silje og Elias får si hva de mener uten press fra resten av teamet, og temperaturen")
    print("går ned. Men de vet ikke om du tok noens parti, og resten av teamet kan begynne å")
    print("spekulere. Uenigheten om teknologivalget er heller ikke løst.")
print()
input("Trykk Enter hvis du er klar til å fortsette... ")
print()
print("Litt senere...")
print()
if valg1 == "plenum":
    print("Plenumsmøtet har satt spor. Teamet har delt seg i to leirer, og Hamdi og Hallgeir")
    print("har havnet på hver sin side. Uenigheten om folkemøtene er ikke lenger skjult,")
    print("og det er for sent å forebygge. Nå må du håndtere en konflikt som allerede")
    print("har kommet til overflaten.")
else:
    print("Det er roligere i teamet, og resten av gruppen tror konflikten er løst.")
    print("Hamdi og Hallgeir er fortsatt uenige, men ingen har tatt side.")
    print("Uenigheten ulmer, og du har fortsatt mulighet til å forebygge.")
print()
print("===Beslutning 2: Hamdi og Hallgeir===")
print("Du har to alternativer for å håndtere konflikten mellom Hamdi og Hallgeir:")
print("A. Å avvente og la dem løse konflikten selv")
print("B. Organisere et felles møte for å diskutere uenigheten")

while valg2 == "":
    svar = input("Hva velger du? (A/B): ").strip().upper()
    if svar == "A":
        valg2 = "avvente"
    elif svar == "B":
        valg2 = "felles møte"
        poeng += 1
    else:
        print("Ugyldig valg. Vennligst velg A eller B.")

if valg2 == "avvente":
    print("Du får mer tid til å sikre fremdriften, og Hamdi og Hallgeir får ta ansvar for")
    print("samarbeidet selv. Men uenigheten fortsetter å utvikle seg, og frustrasjonen")
    print("vokser i det stille.")
elif valg2 == "felles møte":
    print("Hamdi og Hallgeir får presentere synspunktene sine og finner et kompromiss mellom")
    print("kontroll og åpenhet. Møtet tok likevel tid fra arbeidet med prototypen.")
print()
print("Litt senere... Fristen for prototypen nærmer seg.")
print()
if valg1 == "individuelle samtaler" and valg2 == "felles møte":
    print("Begge konfliktene er dempet, og ingen har tatt side. Teamet har et godt")
    print("utgangspunkt, men tilliten etter seks uker med uro er ikke helt på topp.")
elif valg1 == "individuelle samtaler":
    print("Konflikten mellom Silje og Elias har roet seg, og teamet er fortsatt samlet.")
    print("Men uenigheten mellom Hamdi og Hallgeir har vokst i det stille og er i ferd")
    print("med å blusse opp.")
elif valg2 == "felles møte":
    print("Hamdi og Hallgeir har funnet et kompromiss, men teamet bærer fortsatt preg")
    print("av splittelsen etter plenumsmøtet.")
else:
    print("Teamet er delt i to leirer, og uenigheten mellom Hamdi og Hallgeir har blusset")
    print("opp og blitt en del av splittelsen. Teamet er preget av mistillit, og det blir")
    print("vanskelig å skape et godt samarbeidsmiljø. Arbeidet står i fare.")
print()
input("Trykk Enter hvis du er klar til å fortsette... ")
print()
print("===Beslutning 3: Motivasjon===")
print("Du har to alternativer for å motivere teamet:")
print("A. Fokusere på relasjonsbygging og teamets trivsel")
print("B. Fokusere på fremdrift og leveranser")

while valg3 == "":
    svar = input("Hva velger du? (A/B): ").strip().upper()
    if svar == "A":
        valg3 = "relasjonsbygging"
        poeng += 1
    elif svar == "B":
        valg3 = "fremdrift"
    else:
        print("Ugyldig valg. Vennligst velg A eller B.")
if valg3 == "relasjonsbygging":
    print("Teamet blir bedre kjent, og tilliten og kommunikasjonen blir åpnere. Men en sosial")
    print("aktivitet løser ikke konfliktene automatisk, og den tar tid fra prototypen.")
elif valg3 == "fremdrift":
    print("Konkrete mål og synlige resultater gir teamet mestringsfølelse. Men problemene")
    print("kan bli liggende, og mistilliten består.")
print()
input("Trykk på Enter for å se resultatet...")
print()
print("===Utfall===")
if poeng == 3:
    print("Teamet går over i norming-fasen. Både konfliktene og samarbeidet er håndtert,")
    print("og tilliten er styrket. Alle uenigheter er ikke borte, men teamet har et bedre")
    print("grunnlag for å håndtere dem sammen.")
elif poeng == 2:
    print("Konflikten er delvis løst. Teamet gjør fremgang, men relasjonene er fortsatt")
    print("sårbare. Du bør følge opp kommunikasjonen, slik at konfliktene ikke blusser opp igjen.")
else:
    print("Teamet står fast i storming-fasen. Flere konflikter er uløst, motivasjonen og")
    print("samarbeidet svekkes, og prosjektet blir forsinket.")
print()
print(f"Poengsum {poeng} av 3.")
print()