<div align="center">
<h1>Neptune F1 Integration</h1>

______________________________________________________________________
[![LICENSE - MIT](https://img.shields.io/github/license/Raalsky/neptune-f1.svg?color=blue)](https://github.com/Raalsky/neptune-f1/blob/master/LICENSE)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/neptune-f1)](https://pypi.org/project/neptune-f1/)
[![PyPI Status](https://badge.fury.io/py/neptune-f1.svg)](https://badge.fury.io/py/neptune-f1)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](https://github.com/Raalsky/neptune-f1/blob/master/.github/CODE_OF_CONDUCT.md)
[![Codecov](https://codecov.io/gh/Raalsky/neptune-f1/branch/master/graph/badge.svg?token=AFBHUE7GBQ)](https://codecov.io/gh/Raalsky/neptune-f1)
______________________________________________________________________
</div>

## How to use
```python
from neptune_f1 import *
# TO BE UPDATED
```

## Appendices

Source: https://github.com/raweceek-temeletry/f1-2021-udp

Here are the values used for the team ID, driver ID and track ID parameters.


### Team IDs

| ID  | Team                      | ID  | Team              | ID  | Team |
| --- | ------------------------- | --- | ----------------- | --- | ---- |
| 0   | Mercedes                  | 76  | MP Motorsport ‘20 |     |      |
| 1   | Ferrari                   | 77  | Prema ‘20         |     |      |
| 2   | Red Bull Racing           | 78  | Trident ‘20       |     |      |
| 3   | Williams                  | 79  | BWT ‘20           |     |      |
| 4   | Aston Martin              | 80  | Hitech ‘20        |     |      |
| 5   | Alpine                    | 85  | Mercedes 2020     |     |      |
| 6   | Alpha Tauri               | 86  | Ferrari 2020      |     |      |
| 7   | Haas                      | 87  | Red Bull 2020     |     |      |
| 8   | McLaren                   | 88  | Williams 2020     |     |      |
| 9   | Alfa Romeo                | 89  | Racing Point 2020 |     |      |
| 42  | Art GP ’19                | 90  | Renault 2020      |     |      |
| 43  | Campos ’19                | 91  | Alpha Tauri 2020  |     |      |
| 44  | Carlin ’19                | 92  | Haas 2020         |     |      |
| 45  | Sauber Junior Charouz ’19 | 93  | McLaren 2020      |     |      |
| 46  | Dams ’19                  | 94  | Alfa Romeo 2020   |     |      |
| 47  | Uni-Virtuosi ‘19          |     |                   |     |      |
| 48  | MP Motorsport ‘19         |     |                   |     |      |
| 49  | Prema ’19                 |     |                   |     |      |
| 50  | Trident ’19               |     |                   |     |      |
| 51  | Arden ’19                 |     |                   |     |      |
| 70  | Art GP ‘20                |     |                   |     |      |
| 71  | Campos ‘20                |     |                   |     |      |
| 72  | Carlin ‘20                |     |                   |     |      |
| 73  | Charouz ‘20               |     |                   |     |      |
| 74  | Dams ‘20                  |     |                   |     |      |
| 75  | Uni-Virtuosi ‘20          |     |                   |     |      |


 
### Driver IDs

| ID  | Driver             | ID  | Driver              | ID  | Driver               |
| --- | ------------------ | --- | ------------------- | --- | -------------------- |
| 0   | Carlos Sainz       | 39  | Santiago Moreno     | 76  | Alain Prost          |
| 1   | Daniil Kvyat       | 40  | Benjamin Coppens    | 77  | Ayrton Senna         |
| 2   | Daniel Ricciardo   | 41  | Noah Visser         | 78  | Nobuharu Matsushita  |
| 3   | Fernando Alonso    | 42  | Gert Waldmuller     | 79  | Nikita Mazepin       |
| 4   | Felipe Massa       | 43  | Julian Quesada      | 80  | Guanya Zhou          |
| 6   | Kimi Räikkönen     | 44  | Daniel Jones        | 81  | Mick Schumacher      |
| 7   | Lewis Hamilton     | 45  | Artem Markelov      | 82  | Callum Ilott         |
| 9   | Max Verstappen     | 46  | Tadasuke Makino     | 83  | Juan Manuel Correa   |
| 10  | Nico Hulkenburg    | 47  | Sean Gelael         | 84  | Jordan King          |
| 11  | Kevin Magnussen    | 48  | Nyck De Vries       | 85  | Mahaveer Raghunathan |
| 12  | Romain Grosjean    | 49  | Jack Aitken         | 86  | Tatiana Calderon     |
| 13  | Sebastian Vettel   | 50  | George Russell      | 87  | Anthoine Hubert      |
| 14  | Sergio Perez       | 51  | Maximilian Günther  | 88  | Guiliano Alesi       |
| 15  | Valtteri Bottas    | 52  | Nirei Fukuzumi      | 89  | Ralph Boschung       |
| 17  | Esteban Ocon       | 53  | Luca Ghiotto        | 90  | Michael Schumacher   |
| 19  | Lance Stroll       | 54  | Lando Norris        | 91  | Dan Ticktum          |
| 20  | Arron Barnes       | 55  | Sérgio Sette Câmara | 92  | Marcus Armstrong     |
| 21  | Martin Giles       | 56  | Louis Delétraz      | 93  | Christian Lundgaard  |
| 22  | Alex Murray        | 57  | Antonio Fuoco       | 94  | Yuki Tsunoda         |
| 23  | Lucas Roth         | 58  | Charles Leclerc     | 95  | Jehan Daruvala       |
| 24  | Igor Correia       | 59  | Pierre Gasly        | 96  | Gulherme Samaia      |
| 25  | Sophie Levasseur   | 62  | Alexander Albon     | 97  | Pedro Piquet         |
| 26  | Jonas Schiffer     | 63  | Nicholas Latifi     | 98  | Felipe Drugovich     |
| 27  | Alain Forest       | 64  | Dorian Boccolacci   | 99  | Robert Schwartzman   |
| 28  | Jay Letourneau     | 65  | Niko Kari           | 100 | Roy Nissany          |
| 29  | Esto Saari         | 66  | Roberto Merhi       | 101 | Marino Sato          |
| 30  | Yasar Atiyeh       | 67  | Arjun Maini         | 102 | Aidan Jackson        |
| 31  | Callisto Calabresi | 68  | Alessio Lorandi     | 103 | Casper Akkerman      |
| 32  | Naota Izum         | 69  | Ruben Meijer        | 109 | Jenson Button        |
| 33  | Howard Clarke      | 70  | Rashid Nair         | 110 | David Coulthard      |
| 34  | Wilheim Kaufmann   | 71  | Jack Tremblay       | 111 | Nico Rosberg         |
| 35  | Marie Laursen      | 72  | Devon Butler        |
| 36  | Flavio Nieves      | 73  | Lukas Weber         |
| 37  | Peter Belousov     | 74  | Antonio Giovinazzi  |
| 38  | Klimek Michalski   | 75  | Robert Kubica       |




 
### Track IDs

| ID  | Track             |
| --- | ----------------- |
| 0   | Melbourne         |
| 1   | Paul Ricard       |
| 2   | Shanghai          |
| 3   | Sakhir (Bahrain)  |
| 4   | Catalunya         |
| 5   | Monaco            |
| 6   | Montreal          |
| 7   | Silverstone       |
| 8   | Hockenheim        |
| 9   | Hungaroring       |
| 10  | Spa               |
| 11  | Monza             |
| 12  | Singapore         |
| 13  | Suzuka            |
| 14  | Abu Dhabi         |
| 15  | Texas             |
| 16  | Brazil            |
| 17  | Austria           |
| 18  | Sochi             |
| 19  | Mexico            |
| 20  | Baku (Azerbaijan) |
| 21  | Sakhir Short      |
| 22  | Silverstone Short |
| 23  | Texas Short       |
| 24  | Suzuka Short      |
| 25  | Hanoi             |
| 26  | Zandvoort         |
| 27  | Imola             |
| 28  | Portimão          |
| 29  | Jeddah            |


 
### Nationality IDs

| ID  | Nationality | ID  | Nationality    | ID  | Nationality   |
| --- | ----------- | --- | -------------- | --- | ------------- |
| 1   | American    | 31  | Greek          | 61  | Paraguayan    |
| 2   | Argentinean | 32  | Guatemalan     | 62  | Peruvian      |
| 3   | Australian  | 33  | Honduran       | 63  | Polish        |
| 4   | Austrian    | 34  | Hong Konger    | 64  | Portuguese    |
| 5   | Azerbaijani | 35  | Hungarian      | 65  | Qatari        |
| 6   | Bahraini    | 36  | Icelander      | 66  | Romanian      |
| 7   | Belgian     | 37  | Indian         | 67  | Russian       |
| 8   | Bolivian    | 38  | Indonesian     | 68  | Salvadoran    |
| 9   | Brazilian   | 39  | Irish          | 69  | Saudi         |
| 10  | British     | 40  | Israeli        | 70  | Scottish      |
| 11  | Bulgarian   | 41  | Italian        | 71  | Serbian       |
| 12  | Cameroonian | 42  | Jamaican       | 72  | Singaporean   |
| 13  | Canadian    | 43  | Japanese       | 73  | Slovakian     |
| 14  | Chilean     | 44  | Jordanian      | 74  | Slovenian     |
| 15  | Chinese     | 45  | Kuwaiti        | 75  | South Korean  |
| 16  | Colombian   | 46  | Latvian        | 76  | South African |
| 17  | Costa Rican | 47  | Lebanese       | 77  | Spanish       |
| 18  | Croatian    | 48  | Lithuanian     | 78  | Swedish       |
| 19  | Cypriot     | 49  | Luxembourger   | 79  | Swiss         |
| 20  | Czech       | 50  | Malaysian      | 80  | Thai          |
| 21  | Danish      | 51  | Maltese        | 81  | Turkish       |
| 22  | Dutch       | 52  | Mexican        | 82  | Uruguayan     |
| 23  | Ecuadorian  | 53  | Monegasque     | 83  | Ukrainian     |
| 24  | English     | 54  | New Zealander  | 84  | Venezuelan    |
| 25  | Emirian     | 55  | Nicaraguan     | 85  | Barbadian     |
| 26  | Estonian    | 56  | Northern Irish | 86  | Welsh         |
| 27  | Finnish     | 57  | Norwegian      | 87  | Vietnamese    |
| 28  | French      | 58  | Omani          |
| 29  | German      | 59  | Pakistani      |
| 30  | Ghanaian    | 60  | Panamanian     |




### Surface types

These types are from physics data and show what type of contact each wheel is experiencing.

| ID  | Surface      |
| --- | ------------ |
| 0   | Tarmac       |
| 1   | Rumble strip |
| 2   | Concrete     |
| 3   | Rock         |
| 4   | Gravel       |
| 5   | Mud          |
| 6   | Sand         |
| 7   | Grass        |
| 8   | Water        |
| 9   | Cobblestone  |
| 10  | Metal        |
| 11  | Ridged       |

### Button flags

These flags are used in the telemetry packet to determine if any buttons are being held on the controlling device. If the value below logical ANDed with the button status is set then the corresponding button is being held.

| Bit Flag   | Button            |
| ---------- | ----------------- |
| 0x00000001 | Cross or A        |
| 0x00000002 | Triangle or Y     |
| 0x00000004 | Circle or B       |
| 0x00000008 | Square or X       |
| 0x00000010 | D-pad Left        |
| 0x00000020 | D-pad Right       |
| 0x00000040 | D-pad Up          |
| 0x00000080 | D-pad Down        |
| 0x00000100 | Options or Menu   |
| 0x00000200 | L1 or LB          |
| 0x00000400 | R1 or RB          |
| 0x00000800 | L2 or LT          |
| 0x00001000 | R2 or RT          |
| 0x00002000 | Left Stick Click  |
| 0x00004000 | Right Stick Click |
| 0x00008000 | Right Stick Left  |
| 0x00010000 | Right Stick Right |
| 0x00020000 | Right Stick Up    |
| 0x00040000 | Right Stick Down  |
| 0x00080000 | Special           |

### Penalty types

| ID  | Penalty meaning                                  |
| --- | ------------------------------------------------ |
| 0   | Drive through                                    |
| 1   | Stop Go                                          |
| 2   | Grid penalty                                     |
| 3   | Penalty reminder                                 |
| 4   | Time penalty                                     |
| 5   | Warning                                          |
| 6   | Disqualified                                     |
| 7   | Removed from formation lap                       |
| 8   | Parked too long timer                            |
| 9   | Tyre regulations                                 |
| 10  | This lap invalidated                             |
| 11  | This and next lap invalidated                    |
| 12  | This lap invalidated without reason              |
| 13  | This and next lap invalidated without reason     |
| 14  | This and previous lap invalidated                |
| 15  | This and previous lap invalidated without reason |
| 16  | Retired                                          |
| 17  | Black flag timer                                 |


### Infringement types

| ID  | Infringement meaning                            |
| --- | ----------------------------------------------- |
| 0   | Blocking by slow driving                        |
| 1   | Blocking by wrong way driving                   |
| 2   | Reversing off the start line                    |
| 3   | Big Collision                                   |
| 4   | Small Collision                                 |
| 5   | Collision failed to hand back position single   |
| 6   | Collision failed to hand back position multiple |
| 7   | Corner cutting gained time                      |
| 8   | Corner cutting overtake single                  |
| 9   | Corner cutting overtake multiple                |
| 10  | Crossed pit exit lane                           |
| 11  | Ignoring blue flags                             |
| 12  | Ignoring yellow flags                           |
| 13  | Ignoring drive through                          |
| 14  | Too many drive throughs                         |
| 15  | Drive through reminder serve within n laps      |
| 16  | Drive through reminder serve this lap           |
| 17  | Pit lane speeding                               |
| 18  | Parked for too long                             |
| 19  | Ignoring tyre regulations                       |
| 20  | Too many penalties                              |
| 21  | Multiple warnings                               |
| 22  | Approaching disqualification                    |
| 23  | Tyre regulations select single                  |
| 24  | Tyre regulations select multiple                |
| 25  | Lap invalidated corner cutting                  |
| 26  | Lap invalidated running wide                    |
| 27  | Corner cutting ran wide gained time minor       |
| 28  | Corner cutting ran wide gained time significant |
| 29  | Corner cutting ran wide gained time extreme     |
| 30  | Lap invalidated wall riding                     |
| 31  | Lap invalidated flashback used                  |
| 32  | Lap invalidated reset to track                  |
| 33  | Blocking the pitlane                            |
| 34  | Jump start                                      |
| 35  | Safety car to car collision                     |
| 36  | Safety car illegal overtake                     |
| 37  | Safety car exceeding allowed pace               |
| 38  | Virtual safety car exceeding allowed pace       |
| 39  | Formation lap below allowed speed               |
| 40  | Retired mechanical failure                      |
| 41  | Retired terminally damaged                      |
| 42  | Safety car falling too far back                 |
| 43  | Black flag timer                                |
| 44  | Unserved stop go penalty                        |
| 45  | Unserved drive through penalty                  |
| 46  | Engine component change                         |
| 47  | Gearbox change                                  |
| 48  | League grid penalty                             |
| 49  | Retry penalty                                   |
| 50  | Illegal time gain                               |
| 51  | Mandatory pitstop                               |
