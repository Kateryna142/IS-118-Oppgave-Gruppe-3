print("Velkommen til beslutningsspillet om medborgerportalen!")
print("Du spiller Erling, som leder utviklingen av kommunens nye digitale tjeneste.")
print("Underveis må du ta tre viktige valg som former hvordan teamet jobber sammen.")
input("Trykk enter for å begynne.")

poeng = 0

print("Utfordring 1: Uenigheten mellom Silje og Elias")
print("De to krangler om retningen for portalens tekniske løsning.")
print("Som leder må Erling velge hvordan konflikten skal håndteres.")
print("A: Diskutere saken åpent i hele gruppen")
print("B: Snakke med hver av dem separat")
valg1 = input("Velg A eller B: ").upper()
while valg1 != "A" and valg1 != "B":
    valg1 = input("Det valget finnes ikke. Prøv igjen (A/B): ").upper()

if valg1 == "A":
    print("Konflikten tas opp foran alle. Stemningen blir anspent, og flere velger side.")
elif valg1 == "B":
    print("Erling tar separate samtaler. Begge føler seg hørt, og roen senker seg.")
    poeng = poeng + 1

print("Poeng så langt:", poeng)
print()

if valg1 == "A":
    print("Den urolige stemningen gjør at også Hamdi og Hallgeirs uenighet blir tydeligere.")
else:
    print("Selv om roen har senket seg, gjenstår uenigheten mellom Hamdi og Hallgeir.")

print("Utfordring 2: Hamdi og Hallgeir er uenige")
print("De to har ulikt syn på hvordan innbyggerne skal involveres digitalt.")
print("Erling vurderer hvordan situasjonen bør løses.")
print("A: Innkalle til et felles møte")
print("B: La situasjonen roe seg av seg selv")
valg2 = input("Velg A eller B: ").upper()
while valg2 != "A" and valg2 != "B":
    valg2 = input("Det valget finnes ikke. Prøv igjen (A/B): ").upper()

if valg2 == "A":
    print("Møtet gir rom for dialog, og de to finner en løsning sammen.")
    poeng = poeng + 1
elif valg2 == "B":
    print("Ingenting blir gjort. Irritasjonen vokser, og samarbeidet blir tyngre.")

print("Poeng til nå:", poeng)
print()

if poeng == 2:
    print("Begge konfliktene virker løst, men gruppen trenger fortsatt å bygge tillit.")
elif poeng == 1:
    print("Én konflikt er håndtert, men spenning preger fortsatt gruppen.")
else:
    print("Ingen av konfliktene er løst, og samarbeidet sliter.")

print("Utfordring 3: Hold motivasjonen oppe")
print("Fristen for prototypen nærmer seg - tre uker gjenstår.")
print("Erling må avgjøre hvordan gruppen skal jobbe videre.")
print("A: Prioritere tid til å bli bedre kjent som team")
print("B: Fokusere kun på fremdrift i prosjektet")
valg3 = input("Velg A eller B: ").upper()
while valg3 != "A" and valg3 != "B":
    valg3 = input("Det valget finnes ikke. Prøv igjen (A/B): ").upper()

if valg3 == "A":
    print("Gruppen bruker tid sammen, og tilliten mellom medlemmene styrkes.")
    poeng = poeng + 1
elif valg3 == "B":
    print("Arbeidet går fremover, men underliggende spenninger forblir uløst.")

print()
print("Spillet er over!")
print("Din endelige poengsum er:", poeng)

if poeng == 3:
    print("Gruppen har løst konfliktene og bygget et sterkere samarbeid.")
    print("Teamet beveger seg videre fra storming- til norming-fasen.")
elif poeng == 2:
    print("Noen problemer er løst, men samarbeidet er fortsatt skjørt.")
    print("Erling bør fortsette å jobbe med tillit og kommunikasjon.")
else:
    print("Flere konflikter står fortsatt uløst i gruppen.")
    print("Teamet blir værende i storming-fasen, og fremdriften er truet.")