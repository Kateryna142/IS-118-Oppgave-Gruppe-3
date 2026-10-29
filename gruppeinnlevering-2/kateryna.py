# kateryna.py
# Gruppeinnlevering 2 - IS-118
# Interaktiv historie: Erling og prosjektteamet i storming-fasen
BREDDE = 80  # bredde på overskrifter og linjer i terminalen
print()
print("=" * BREDDE)
print("Velkommen til den interaktive historien".center(BREDDE))
print("=" * BREDDE)
# Ytre løkke: hele spillet gjentas så lenge spilleren vil spille igjen
while True:
    # Variabler (nullstilles for hver runde)
    valg1 = ""   # Beslutning 1: "plenum" eller "individuelle samtaler"
    valg2 = ""   # Beslutning 2: "felles møte" eller "avvente"
    valg3 = ""   # Beslutning 3: "relasjonsbygging" eller "fremdrift"
    poeng = 0    # 0 eller 1 poeng per beslutning, maks 3
    print()
    print("Erling og prosjektteamet i storming-fasen!".center(BREDDE))
    print()
    # Introduksjon
    print("Du er Erling, prosjektleder for et tverrfaglig team som utvikler kommunens")
    print("nye digitale medborgerportal. Det har gått seks uker, og stemningen er blitt")
    print("spent og kommunikasjonen hakkete: teamet er i storming-fasen. Flere konflikter")
    print("må håndteres før prototypen skal være klar om tre uker. Valgene dine avgjør")
    print("om teamet går mot norming, eller blir stående fast.")
    print()
    input("Trykk Enter for å starte... ")
    print()
    print("Beslutning 1: Silje og Elias".center(BREDDE))
    print()
    print("Silje (UX-designer) og Elias (IT-rådgiver) er uenige om teknologivalg og design.")
    print("Silje vil ha best mulig brukeropplevelse og rom for innovasjon, mens Elias er")
    print("mest opptatt av sikkerhet og kostnader. Diskusjonene har blitt mer personlige,")
    print("og begge søker støtte hos andre i teamet.")
    print()
    print("Du har to alternativer for å håndtere konflikten mellom Silje og Elias:")
    print("A. Ta det opp i plenum for å skape åpenhet")
    print("B. Ta individuelle samtaler for å dempe temperaturen")
    # Beslutning 1: gjenta spørsmålet til spilleren gir et gyldig svar (A eller B)
    while valg1 == "":
        svar = input("Hva velger du? (A/B): ").strip().upper()
        if svar == "A":
            valg1 = "plenum"
        elif svar == "B":
            valg1 = "individuelle samtaler"
            poeng += 1
        else:
            print("Ugyldig valg. Vennligst velg A eller B.")
    print()
    # Konsekvens av valg 1
    if valg1 == "plenum":
        print("Alle hører begge sider, og teamet ser at du tar ansvar. Men Silje og Elias")
        print("må forsvare seg, og diskusjonen blir mer personlig enn faglig.")
    elif valg1 == "individuelle samtaler":
        print("Temperaturen går ned, men Silje og Elias vet ikke om du tok noens parti,")
        print("og uenigheten om teknologivalget er ikke løst.")
    print()
    input("Trykk Enter hvis du er klar til å fortsette... ")
    print()
    print("Beslutning 2: Hamdi og Hallgeir".center(BREDDE))
    print()
    print("Hamdi og Hallgeir er uenige om hvordan innbyggerne skal delta i digitale")
    print("folkemøter. Hamdi (kulturavdelingen) vil ha en kontrollert løsning på")
    print("kommunens plattform, mens Hallgeir (innbyggerforeningen) vil ha et åpnere")
    print("system. Frustrasjonen vokser.")
    print()
    # Situasjonen før beslutning 2 avhenger av valg 1
    if valg1 == "plenum":
        print("Etter plenumsmøtet har teamet delt seg i leirer, og Hamdi og Hallgeir")
        print("har havnet på hver sin side. Det er for sent å forebygge: uenigheten")
        print("er ikke lenger skjult.")
    else:
        print("Etter de individuelle samtalene er det roligere i teamet. Hamdi og")
        print("Hallgeir har ikke tatt side, og du kan fortsatt forebygge.")
    print()
    print("Du har to alternativer for å håndtere konflikten mellom Hamdi og Hallgeir:")
    print("A. Å avvente og la dem løse konflikten selv")
    print("B. Organisere et felles møte for å diskutere uenigheten")
    # Beslutning 2: gjenta spørsmålet til spilleren gir et gyldig svar (A eller B)
    while valg2 == "":
        svar = input("Hva velger du? (A/B): ").strip().upper()
        if svar == "A":
            valg2 = "avvente"
        elif svar == "B":
            valg2 = "felles møte"
            poeng += 1
        else:
            print("Ugyldig valg. Vennligst velg A eller B.")
    print()
    # Konsekvens av valg 2
    if valg2 == "avvente":
        print("Du får mer tid til fremdriften, men uenigheten vokser i det stille.")
    elif valg2 == "felles møte":
        print("Hamdi og Hallgeir finner et kompromiss mellom kontroll og åpenhet, men møtet")
        print("tok tid fra prototypen.")
    print()
    input("Trykk Enter hvis du er klar til å fortsette... ")
    print()
    print("Litt senere. Fristen for prototypen nærmer seg.")
    print()
    # Situasjonen før beslutning 3 avhenger av valg 1 og valg 2:
    # Betingelsene sjekkes i rekkefølge, så hver elif forutsetter at de forrige ikke traff.
    if valg1 == "individuelle samtaler" and valg2 == "felles møte":
        # Begge konfliktene er håndtert
        print("Begge konfliktene er dempet, men tilliten etter seks uker med")
        print("uro er ikke helt på topp.")
    elif valg1 == "individuelle samtaler":
        # Her er valg 1 individuelle samtaler, men ikke begge håndtert, så valg 2 er "avvente".
        # Bare Silje og Elias er håndtert
        print("Silje og Elias har roet seg, men uenigheten mellom Hamdi og Hallgeir er i ferd")
        print("med å blusse opp.")
    elif valg2 == "felles møte":
        # Valg 1 er ikke individuelle samtaler, ellers hadde forrige gren truffet, så det er "plenum".
        # Bare Hamdi og Hallgeir er håndtert
        print("Hamdi og Hallgeir har funnet et kompromiss, men teamet bærer fortsatt preg")
        print("av splittelsen etter plenumsmøtet.")
    else:
        # Det eneste som gjenstår: valg 1 er "plenum" og valg 2 er "avvente".
        # Ingen av konfliktene er håndtert
        print("Teamet er delt i to leirer og preget av mistillit, og arbeidet står i fare.")
    print()
    print("Beslutning 3: Motivasjon".center(BREDDE))
    print()
    print("Du har to alternativer for å motivere teamet:")
    print("A. Fokusere på relasjonsbygging og teamets trivsel")
    print("B. Fokusere på fremdrift og leveranser")
    # Beslutning 3: gjenta spørsmålet til spilleren gir et gyldig svar (A eller B)
    while valg3 == "":
        svar = input("Hva velger du? (A/B): ").strip().upper()
        if svar == "A":
            valg3 = "relasjonsbygging"
            poeng += 1
        elif svar == "B":
            valg3 = "fremdrift"
        else:
            print("Ugyldig valg. Vennligst velg A eller B.")
    print()
    # Konsekvens av valg 3
    if valg3 == "relasjonsbygging":
        print("Teamet blir bedre kjent og tilliten øker, men det tar tid fra prototypen")
        print("og løser ikke konfliktene automatisk.")
    elif valg3 == "fremdrift":
        print("Synlige resultater gir mestringsfølelse, men mistilliten består.")
    print()
    input("Trykk Enter hvis du er klar til å fortsette... ")
    print()
    print("Utfall".center(BREDDE))
    print()
    # Utfall basert på poengsummen: 3 = norming, 2 = delvis løst, 0-1 = forsinket, fast i storming
    if poeng == 3:
        print("Teamet går over i norming-fasen. Tilliten er styrket, og teamet har et")
        print("bedre grunnlag for å håndtere uenigheter sammen.")
    elif poeng == 2:
        print("Konfliktene er delvis løst. Teamet gjør fremgang, men relasjonene er fortsatt")
        print("sårbare. Du bør følge opp kommunikasjonen, slik at konfliktene")
        print("ikke blusser opp igjen.")
    else:
        print("Teamet står fast i storming-fasen. Flere konflikter er uløst, motivasjonen og")
        print("samarbeidet svekkes, og prosjektet blir forsinket.")
    print()
    print(f"Poengsum: {poeng} av 3")
    print()
    # Spør om spilleren vil spille igjen (gjentar til gyldig svar)
    igjen = ""
    while igjen == "":
        svar = input("Vil du prøve igjen? (A = ja, B = nei): ").strip().upper()
        if svar == "A" or svar == "B":
            igjen = svar
        else:
            print("Ugyldig valg. Vennligst velg A eller B.")
    print()
    print("=" * BREDDE)  # skille mellom spillet og det som kommer etterpå
    if igjen == "B":
        print()
        print("Takk for at du spilte!".center(BREDDE))
        print()
        break  # avslutter den ytre løkken, og programmet er ferdig