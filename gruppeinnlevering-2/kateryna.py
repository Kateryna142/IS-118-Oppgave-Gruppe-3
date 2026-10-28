# kateryna.py
# Gruppeinnlevering 2 - IS-118
# Interaktiv historie: Erling og prosjektteamet i storming-fasen
print()
print("=" * 80)
print("Velkommen til den interaktive historien".center(80))
print("=" * 80)
# Ytre løkke: hele spillet gjentas så lenge spilleren vil spille igjen
while True:
    # ---------- Variabler (nullstilles for hver runde) ----------
    valg1 = ""   # Beslutning 1: "plenum" eller "individuelle samtaler"
    valg2 = ""   # Beslutning 2: "felles møte" eller "avvente"
    valg3 = ""   # Beslutning 3: "relasjonsbygging" eller "fremdrift"
    poeng = 0    # 0 eller 1 poeng per beslutning, maks 3
    print()
    print()
    print("Erling og prosjektteamet i storming-fasen!".center(80))
    print()
    # ---------- Introduksjon ----------
    print("Du er Erling, prosjektleder for utviklingen av kommunens nye digitale medborgerportal.")
    print("Teamet består av medlemmer fra flere fagområder: IT, design, kulturavdelingen,")
    print("politikk, sikkerhet og en lokal innbyggerforening. Målet er en portal som gir innbyggerne")
    print("mer innflytelse og åpenhet.")
    print()
    print("Det har gått seks uker siden du samlet teamet for første gang. Oppstarten var full av")
    print("energi, men nå begynner samarbeidet å knirke. Teamet er i storming-fasen: stemningen")
    print("er spent og kommunikasjonen hakkete.")
    print()
    print("Første prototype skal være klar om tre uker. Valgene dine avgjør om teamet går videre")
    print("mot norming, eller blir stående fast i stormen.")
    print()
    input("Trykk Enter for å starte... ")
    print()
    print("Beslutning 1: Silje og Elias".center(80))
    print()
    print("Silje (UX-designer) vil ha en løsning som gir best mulig brukeropplevelse og rom for")
    print("innovasjon. Elias (IT-rådgiver) er mer opptatt av sikkerhet og kostnader. Diskusjonene")
    print("har blitt mer personlige, og begge søker støtte hos andre i teamet.")
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
    # Situasjonen før beslutning 2 avhenger av valg 1
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
    print("Beslutning 2: Hamdi og Hallgeir".center(80))
    print()
    print("Hamdi (kulturavdelingen) og Hallgeir (innbyggerforeningen) uenige om hvordan")
    print("innbyggerne skal delta i digitale folkemøter. Hamdi vil ha en kontrollert løsning via")
    print("kommunens eksisterende plattform, mens Hallgeir vil ha et åpnere system med rom for")
    print("spontane innspill. Foreløpig er uenigheten lavmælt, men frustrasjonen vokser.")
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
        print("Du får mer tid til å sikre fremdriften, og Hamdi og Hallgeir får ta ansvar for")
        print("samarbeidet selv. Men uenigheten fortsetter å utvikle seg, og frustrasjonen")
        print("vokser i det stille.")
    elif valg2 == "felles møte":
        print("Hamdi og Hallgeir får presentere synspunktene sine og finner et kompromiss mellom")
        print("kontroll og åpenhet. Møtet tok likevel tid fra arbeidet med prototypen.")
    print()
    input("Trykk Enter hvis du er klar til å fortsette... ")
    print()
    print("Litt senere... Fristen for prototypen nærmer seg.")
    print()
    # Situasjonen før beslutning 3 avhenger av valg 1 og valg 2:
    # Betingelsene sjekkes i rekkefølge, så hver elif forutsetter at de forrige ikke traff.
    if valg1 == "individuelle samtaler" and valg2 == "felles møte":
        # Begge konfliktene er håndtert
        print("Begge konfliktene er dempet, og ingen har tatt side. Teamet har et godt")
        print("utgangspunkt, men tilliten etter seks uker med uro er ikke helt på topp.")
    elif valg1 == "individuelle samtaler":
        # Her er valg 1 individuelle samtaler, men ikke begge håndtert, så valg 2 er "avvente".
        # Bare Silje og Elias er håndtert
        print("Konflikten mellom Silje og Elias har roet seg, og teamet er fortsatt samlet.")
        print("Men uenigheten mellom Hamdi og Hallgeir har vokst i det stille og er i ferd")
        print("med å blusse opp.")
    elif valg2 == "felles møte":
        # Valg 1 er ikke individuelle samtaler, ellers hadde forrige gren truffet, så det er "plenum".
        # Bare Hamdi og Hallgeir er håndtert
        print("Hamdi og Hallgeir har funnet et kompromiss, men teamet bærer fortsatt preg")
        print("av splittelsen etter plenumsmøtet.")
    else:
        # Det eneste som gjenstår: valg 1 er "plenum" og valg 2 er "avvente".
        # Ingen av konfliktene er håndtert
        print("Teamet er delt i to leirer, og uenigheten mellom Hamdi og Hallgeir har blusset")
        print("opp og blitt en del av splittelsen. Teamet er preget av mistillit, og det blir")
        print("vanskelig å skape et godt samarbeidsmiljø. Arbeidet står i fare.")
    print()
    print("Beslutning 3: Motivasjon".center(80))
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
    if valg3 == "relasjonsbygging":
        print("Teamet blir bedre kjent, og tilliten og kommunikasjonen blir åpnere. Men en sosial")
        print("aktivitet løser ikke konfliktene automatisk, og den tar tid fra prototypen.")
    elif valg3 == "fremdrift":
        print("Konkrete mål og synlige resultater gir teamet mestringsfølelse. Men problemene")
        print("kan bli liggende, og mistilliten består.")
    print()
    input("Trykk Enter hvis du er klar til å fortsette... ")
    print()
    print("=" * 80)
    print("Utfall".center(80))
    print("=" * 80)
    print()
    # Utfall basert på poengsummen: 3 = norming, 2 = delvis løst, 0-1 = forsinket, fast i storming
    if poeng == 3:
        print("Teamet går over i norming-fasen. Både konfliktene og samarbeidet er håndtert,")
        print("og tilliten er styrket. Ikke alle uenigheter er borte, men teamet har et bedre")
        print("grunnlag for å håndtere dem sammen.")
    elif poeng == 2:
        print("Konfliktene er delvis løst. Teamet gjør fremgang, men relasjonene er fortsatt")
        print("sårbare. Du bør følge opp kommunikasjonen, slik at konfliktene ikke blusser opp igjen.")
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
    if igjen == "B":
        print()
        print("Takk for at du spilte!")
        print()
        break  # avslutter den ytre løkken, og programmet er ferdig