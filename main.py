#/1. Atskirose eilutėse išveskite skaičius 15, 12, 89 ir 5.8
print(15)
print(19)
print(89)
print(5.8)
#/2. Išveskite šių matematinių veiksmų atsakymus
print(78 * 2)
print(5 + 3)
print(7 / 2)
print(85 - 32)
print(5.2 * 3)
#/3. Išveskite šių matematinių veiksmų atsakymus:
print(9.4 * 0.5)
print(4.2 / 2)
#/4. Išveskite šių matematinių veiksmų atsakymus
print(7 + 2 * 3)
print((7 + 2) * 3)
print(52 + 74 + 32)
print(87 - 65 + 14)
print(79 / (5 - 2))
#/5. Apskaičiuokite išveskite šiuos atsakymus (naudojant ** operatorių)
print(2 ** 4)
print(8 ** 3)
print(14 ** 0.5)
#/5. 6. Raskite šių dalybų liekanas (naudojant % operatorių)
print(2 % 2)
print(3 % 2)
print(11 % 2)
print(13 % 2)
print(10 % 2)
#/7. Raskite šių dalybų liekanas (naudojant % operatorių):
# /1. 15 iš kiekvieno skaičiaus nuo 2 iki 9 (15 iš 2, 15 iš 3 ir pan.)
print(15%2)
print(15%3)
print(15%4)
print(15%5)
print(15%6)
print(15%7)
print(15%8)
print(15%9)
#8. Atlikite tokias integer dalybas (naudojant // operatorių):
# 1. 5 iš 2 2. 6 iš 3 3. 6 iš 4 4. 80 iš 3 5. 45 iš 4 6. 45 iš 3
print(5//2)
print(6//3)
print(6//4)
print(80//3)
print(45//4)
print(45//3)
#9. Išsiaiškinkite duomenų tipus (panaudokite type) šiems atvejams:
#1. jeigu yra skaičius 6
#2. jeigu yra skaičius 2.5
#3. jeigu yra skaičius 157
#4. jeigu yra skaičius -8.2
#5. jeigu yra dalyba 2 iš 5
#6. jeigu yra sudėtis 8 su 9
#7. jeigu yra sudėtis 8.5 su 3
print(type(6))
print(type(2.5))
print(type(157))
print(type(-8.2))
print(type(2/5))
print(type(8+9))
print(type(8.5+3))
#1. Aprašykite ir išveskite (atskirose eilutėse) kintamuosius, saugančius šią
#informaciją apie studentą: #1. Vardas; #2. Pavardė; #3. Amžius; #4. Ūgis; #5. Svoris;
#6. Aukštoji mokykla; #7. Akademinės grupės kodas; #8. Kursas; #9. Studijų programos pavadinimas; #10. Atsiskaitytų kreditų skaičius;
vardas = "Teresa"
pavarde = "Saviciute"
amzius = 53
ugis = "165cm"
svoris = "70kg"
aukstojiMokykla = "Vilniaus Universitetas"
akademinesGrupesKodas = 777
kursas = 4
studijuProgramosPavadinimas = "phyton"
atsiskaitytuKredituSkaicius = 50
print(vardas)
print(pavarde)
print(amzius)
print(ugis)
print(svoris)
print(aukstojiMokykla)
print(akademinesGrupesKodas)
print(kursas)
print(studijuProgramosPavadinimas)
print(atsiskaitytuKredituSkaicius)

print(vardas, pavarde, amzius)
print(ugis, svoris)
print(aukstojiMokykla, kursas, studijuProgramosPavadinimas, atsiskaitytuKredituSkaicius)

#2. Aprašykite ir išveskite (atskirose eilutėse) kintamuosius, saugančius šią informaciją apie miestą:
#1. Pavadinimas; 2. Valstybė; 3. Apskritis; 4. Įkūrimo data; 5. Meras; 6. Plotas kv. km.; 7. Gyventojų skaičius;
pavadinimas = "pasaulio pabaiga"
valstybe = "LT"
apskritis = "Vilniaus apskr."
ikurimoData = 2024
meras = "BBBBBB"
plotasKvKm = "25 m2"
gyventojuSkaicius = "3 mln"

print(pavadinimas)
print(valstybe)
print(apskritis)
print(ikurimoData)
print(meras)
print(plotasKvKm)
print(gyventojuSkaicius)

print(pavadinimas, valstybe, apskritis, ikurimoData)
print(meras, plotasKvKm, gyventojuSkaicius)

#3. Susikurkite kintamąjį savo vardui saugoti.
# Išveskite į konsolę tekstą "mano vardas yra " ir turimo kintamojo reikšmę.
vardas = 'Terese'
print("mano vardas yra", vardas)

#4. Susikurkite kintamuosius studento akademinei grupei ir vidurkiui saugoti.
# Išveskite į konsolę, atskirose eilutėse pagalbinius tekstus, po kurių sektų
# dvitaškis ir atitinkamas kintamasis. Pavyzdžiui: akademinė grupė: ifzm-6 vidurkis: 8

akademineGrupe = "ifzm"
vidurkis =  8
print('akademinė grupė:', akademineGrupe )
print("vidurkis:", vidurkis )

#5. Susikurkite kintamąjį, kuris saugotų bet kokį žodį.
# Išveskite šį žodį naudojant vieną print(). Žodis turi būti išvestas 5 kartus toje pačioje
# eilutėje, atskiriant tarpo simboliu
tekstas = "Labas vakaras"
print(tekstas, tekstas, tekstas, tekstas, tekstas)
print(5 * "Labas vakaras ")

#klausimai- GERI 3 variantai
tekstas = "Labas vakaras"
print(tekstas, tekstas, tekstas, tekstas, tekstas)
print(5 * "Labas vakaras ")
print(5 * (tekstas + " "))

#1. Pirmoje eilutėje išveskite savo vardą ir amžių.
# Antroje eilutėje išveskite kodėl pasiryžote išbandyti programavimą

vardas = "Terese"
amzius = 57
tekstas = ", Kodėl pasiryžote išbandyti programavimą: noras tobuleti"

formatuotas = f"{vardas} {amzius} \nKodėl pasiryžote išbandyti programavimą: noras tobuleti"
print(formatuotas)

formatuotas = f"{str(vardas)} {str(amzius)}"
formatuotas += f"{tekstas}"
print(formatuotas)

#2. Išveskite bet kokį eilėraštį, kurį sudarytų bent 5 eilutės.
tekstas1 = "du gaideliai, du gaideliai"
tekstas2 = "baltus zirnius kule,"
tekstas3 = "dvi visteles dvi visteles"
tekstas4 = "i maluna veze."

print('du gaideliai, du gaideliai\nbaltus zirnius kule,\ndvi visteles dvi visteles\ni maluna veze :)')

print(tekstas1)
print(tekstas2)
print(tekstas3)
print(tekstas4)

#3. Išveskite 3x3 dydžio tuščiavidurį kvadratą iš * simbolio. Galutinio rezultato pavyzdys:
#***
#* *
#***
print('***\n* *\n***')

#4. Susikurkite šiuos kintamuosius, saugančius informaciją apie gyvūną:
#pavadinimas, amžius, kailio spalva, svoris. Išveskite šiuos duomenis gražiai
#suformatuotus vienoje eilutėje, sakinio forma. Pavyzdžiui:
#Gyvūnas - šuo (2 m.) turi rudą kailio spalvą ir sveria 1.4 kg.
pavadinimas = "Šuo"
amzius = 2
kailioSpalva = "ruda"
svoris = 1.4
print(f'Gyvūnas- {pavadinimas} ({amzius} m.) turi {kailioSpalva} kailio spalva ir sveria {svoris} kg.')

#5. Susikurkite skaičiaus kintamąjį, kurį išveskite penkis kartus toje pačioje eilutėje be tarpų
# tarp šių skaičių. Pavyzdžiui: skaičius - 25, išvedimas - 2525252525
print(5*"25")
print('2525252525')

#6. Susikurkite skaičiaus kintamąjį, kurį išveskite penkis kartus toje pačioje eilutėje
# su tarpais tarp šių skaičių. Pavyzdžiui: skaičius - 25, rezultatas - 25 25 25 25 25
print(5*"25 ")
print('25 25 25 25 25')

#7. Išveskite:
#*
#**
#***
print(f'*\n**\n***')

#8. Per vieną print() išveskite tris skirtingas teksto eilutes
tekstas = 'bega kiskis per dirvona\nopa opa opapa\nir t.t.'
print(tekstas)

#9. Konsolėje iš brūkšniukų ir kitų simbolių išveskite lentelę. Pavyzdžiui:
#+--------+--------+
#| Vardas | Amzius |
#+--------+--------+
#| Tomas | 24 |
#| Jonas | 26 |
#| Justė | 25 |
#+--------+--------+
print(f'+--------+--------+\n| Vardas | Amzius |\n+--------+--------+\n| Tomas | 24 |\n| Jonas | 26 |\n| Justė | 25 |\n+--------+--------+')

# #2024-09-19- PAMOKA
#
# 1. Išveskite atsakymus šių veiksmų:
# 1. 8 * 4 + 2
# 2. 8 * (4 + 2)
# 3. 48 / 4
# 4. 3 + 6 * 2
# print(8 * 4 +2 )
# print(8 * (4 + 2))
# print(48 / 4)
# print(3 + 6 * 2)

#2. Susikurkite du kintamuosius skaičiams saugoti. Į juos įrašykite norimus skaičius.
# Susikurkite trečiąjį kintamąjį, kurio reikšmė būtų pirmų dviejų
# kintamųjų suma. Visus kintamuosius išveskite.
#sukuriau 3
# sk1 = "pirmas skaicius"
# sk2 = "antras skaicius"
# sk3 = 'trecias skaicius'
# sandauga = 'sk1 + sk2 * sk3'
# print("sk1")
# sk1 = int(input())
# print('sk2')
# sk2 = int(input())
# print('sk3')
# sk3 = int(input())
# print(f'{sk1} + {sk2} + {sk3}= {sk1 + sk2 + sk3}')
# #geras
# sk1 = int(input())
# sk2 = int(input())
# sk3 = int(input())
# print(f'{sk1} + {sk2} + {sk3} = {sk1 + sk2 + sk3}')

#2/2-3. Susikurkite tris kintamuosius skaičiams saugoti. Į juos įrašykite norimus skaičius.
# #Raskite šių skaičių suma, skirtumą, sandaugą ir dalmenį.
# #Atsakymus išveskite kartu su atliekamu veiksmu (pvz 8 + 2 + 4 = 14).
# print("2/3.3 - paduok 3 sk")
# sk1 = int(input())
# sk2 = int(input())
# sk3 = int(input())
# suma = sk1 + sk2 + sk3
# skirtumas = sk1 - sk2 - sk3
# sandauga = sk1 * sk2 * sk3
# dalmuo = sk1 / sk2 / sk3
# print(f'{sk1} + {sk2} + {sk3} = {suma}')
# print(f'{sk1} - {sk2} - {sk3} = {skirtumas}')
# print(f'{sk1} * {sk2} * {sk3} = {sandauga}')
# print(f'{sk1} / {sk2} / {sk3} = {dalmuo}')

# 4. Susikurkite du kintamuosius skaičiams saugoti. Į juos įrašykite norimus
# skaičius. Pirmąjį kintamąjį padidinkite 5-iais. Antrajį padidinkite 2 kartus.
# Išveskite visus atsakymus (pradines reikšmes ir pakeistas reikšmes).
# print("2/3.4 - paduok 5 + 2k sk")
# sk1 = int(input())
# sk2 = int(input())
# sk3 = sk1 + 5
# sk4 = sk2 * 2
# print(f'{sk1} + 5 = {sk3}')
# print(f'{sk2} * 2 = {sk4}')

# Užduotys (1/3) 1. Paprašykite vartotojo įvesti savo vardą, amžių ir kodėl pasirinko
# programavimą. Įvestą informaciją išveskite kaip nors tvarkingai, sakiniu ar
# atskirose eilutėse su prierašais.
# print('1/3) 1- vart info')
# vardas = (input())
# amzius = (input())
# pasirinkimas = (input())
# print(f'vartotojo vardas yra:\n {vardas},\n {amzius} metai\n priezastis: {pasirinkimas}')

# print('1/3) 1- vart info')
# vardas = (input())
# amzius = int(input())
# pasirinkimas = (input())
# print(f'vartotojo vardas yra:\n {vardas},\n {amzius} metai\n priezastis: {pasirinkimas}')

# Susikurkite tris kintamuosius skaičiams saugoti. Parašykite šias atskiras if sąlygas:
# 1-Ar pirmas ir antras skaičiai yra lygūs?
# 2-Ar antras ir trečias skaičiai yra lygūs?
# 3-Ar pirmas skaičius yra didesnis už antrąjį?
# 4-Ar antras skaičius yra didesnis už dvigubą trečiojo skaičiaus reikšmę
# (trečias skaičius padaugintas iš 2)?
# 5-Ar pirmas skaičius yra lyginis (ar dalinasi iš 2)?
# 6-Ar antras skaičius yra nelyginis (ar nesidalina iš 2)?
# 7-Ar trečias skaičius yra teigiamas (didesnis už 0)?
# 8-Ar pirmas skaičius yra neigiamas (mažesnis už 0)?
# 9-Ar antras skaičius dalinasi iš 4?
# 10-Ar trečias skaičius dalinasi iš 8?

# 1-Ar pirmas ir antras skaičiai yra lygūs?
# sk1 = int(input())
# sk2 = int(input())
# if sk1 == sk2:
#     print("sk1 lygu sk2")
# else:
#     print("sk1 nelygu sk2")

# 2-Ar antras ir trečias skaičiai yra lygūs?
# sk1 = int(input())
# sk2 = int(input())
# sk3 = int(input())
# if sk2 == sk3:
#     print("sk2 lygu sk3")
# else:
#     print("sk2 nelygu sk3")

# 3-Ar pirmas skaičius yra didesnis už antrąjį?
# print('3uzd: 1>2')
# sk1 = int(input())
# sk2 = int(input())
# if sk1 > sk2:
#     print('pirmas didesnis uz antra')
# else:
#     print('pirmas neDidesnis uz antra')

# 4-Ar antras skaičius yra didesnis už dvigubą trečiojo skaičiaus reikšmę
# (trečias skaičius padaugintas iš 2)?
# print('4 uzd 2 > 3*2')
# sk1 = int(input())
# sk2 = int(input())
# sk3 = int(input())
# if sk2 > sk3 * 2:
#     print('antras didesnis uz dviguba trecia')
# else:
#     print('antras NE didesnis uz dviguba trecia')

# 5-Ar pirmas skaičius yra lyginis (ar dalinasi iš 2)?
# print('5 uzd 1 lyginis, ar /2')
# sk1 = int(input())
# if sk1 % 2 == 0:
#     print('pirmas skaicius= lyginis')
# else:
#     print('pirmas skaicius NELYGINIS')

# 6-Ar antras skaičius yra nelyginis (ar nesidalina iš 2)?
# print('6 uzd 2 nelyginis')
# sk2 = int(input())
# if sk2 % 2 == 1:
#     print('sk NELYGINIS ir nesidalina is 2')
# else:
#     print('sk LYGINIS')

# 7-Ar trečias skaičius yra teigiamas (didesnis už 0)?
# print('7 uzd 3-as sk teigiamas > uz 0')
# # sk1 = int(input())
# # sk2 = int(input())
# sk3 = int(input())
# if sk3 > 0:
#     print('3-as sk teigiamas > uz 0')
# else:
#     print('mazesnis uz nuli')

# 8-Ar pirmas skaičius yra neigiamas (mažesnis už 0)?
# print('8 uzd 1-as sk neigiamas < uz 0')
# sk1 = int(input())
# if sk1 < 0:
#     print('1-as sk neigiamas < uz 0')
# else:
#     print('didesnis uz nuli')

# 9-Ar antras skaičius dalinasi iš 4?
# print('9 uzd 2-as sk DALINASI is 4')
# sk2 = int(input())
# if sk2 % 4 == 0:
#     print('2-as sk DALINASI is 4')
# else:
#     print('2-as sk NESIDALINA is 4')

# 10-Ar trečias skaičius dalinasi iš 8?
# print('10 uzd 3-as sk DALINASI is 8')
# sk1 = int(input())
# sk2 = int(input())
# sk3 = int(input())
# if sk3 % 8 == 0:
#     print('3-as sk DALINASI is 8')
# else:
#     print('3-as sk NESIDALINA is 8')


# print('100000 uzd ... -as sk DALINASI is ...')
# sk1 = int(input())
# sk2 = int(input())
# sk3 = int(input())
# if sk1 % 4 == 0:
#     print('pirmas / is 4')
# elif sk2 % 3 == 0:
#     print('antras / is 3')
# elif sk3 % 8 == 0:
#     print('trecias / is 8')
# else:
#     print('visa kita')
sss
Ę# 2024-09-23- paskaita
git config --global user.name "Teresiukas7777"
git config --global user.email "teresasaviciute@gmail.com"