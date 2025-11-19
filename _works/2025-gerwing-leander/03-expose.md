# Exposé: Masterarbeit von Leander Gerwing

## Arbeitstitel: Live-Sensorchoreographie: Entwicklung eines visuellen Programmier-Interfaces für die Live-Orchestrierung kollaborativer audiovisueller Smartphone-Performances

### Problemfeld und Kontext

Fortschritte in der Informatik ermöglichen immer wieder neue Möglichkeiten und Formen der künstlerischen Ausdrucksweise.
Software ist dabei ein zentrales Werkzeug für die Erstellung und Aufführung digitaler audiovisueller Kunstwerke.
Geläufig sind hier Digital Audio Workstations (DAWs) wie Ableton Live und grafische Programmierumgebungen wie Max/MSP
für die Musikproduktion,
sowie Game Engines wie Unity oder Unreal Engine oder Tools wie TouchDesigner für die Erstellung visueller Inhalte auf
Basis von Audio. Viele
der genannten Tools wie Max/MSP, die Unreal Engine oder TouchDesigner bieten dazu sogenannte "Node-based
Programming"-Interfaces an, die es Nutzer:innen erlauben, komplexe Abläufe durch das Verbinden von modularen
Bausteinen zu erstellen.

Eine weitere Form der Erstellung von audiovisuellen Performances hat sich in den letzten Jahren etabliert: das Konzept
des Live-Codings.
Hierbei schreiben Performer während der Aufführung Code, der in Echtzeit Klang- und Bildinhalte generiert oder
verändert. Bekannte Umgebungen hierfür sind Sonic Pi, Strudel oder Hydra. Letztere beide sind webbasiert und ermöglichen
das
Nutzen neuartige Web-APIs
wie Sensor- und MIDI-Zugriff direkt im Browser.

Parallel dazu öffnen sich durch mobile Endgeräte neue Räume für kollaborative Performances. Projekte wie das Stanford
Mobile Phone Orchestra (MoPhO) [[1]](#1-)[[2]](#2-)demonstrierten bereits 2008, dass Smartphones nicht nur
Kommunikationsgeräte, sondern
auch ernstzunehmende Instrumente innerhalb komplexer Klangensembles sein können. Neuere Arbeiten wie "Speakers, More
Speakers!!!" [[3]](#3-) zeigen zudem, wie sich Smartphone-Sensorik, WebRTC und verteilte Interaktion zu neuartigen
audiovisuellen
Erfahrungen verweben lassen, inklusive experimenteller Setups wie dezentraler stochastischer Musik oder kollaborativ
erzeugten Gemälden [[4]](#4-).

Trotz dieser Entwicklungen fehlt ein Werkzeug, das Live-Coding-Ansätze und kollaborative dezentrale Performances
vereint, insbesondere in einer gemeinsamen, zugänglichen Oberfläche vereint. Zwar existieren Bibliotheken wie "
Soundworks",
die den technischen Unterbau für kollaborative mobile Web-Performances bereitstellen [[5]](#5-), jedoch bleibt die
kreative Ebene
dort nur Programmieraffinen Nutzer:innen vorbehalten.

An genau dieser Lücke setzt das geplante Projekt an: Es untersucht, wie sich eine visuelle, leicht zugängliche
Orchestrierungsoberfläche gestalten lässt, die es Performer erlaubt, Sensordaten mehrerer Smartphones in Echtzeit
für audiovisuelle Prozesse zu nutzen. Das Tool soll benutzbar sein ohne programmieren zu müssen, aber dennoch genug
Flexibilität bieten, um das Erstellen komplexer Performances zu ermöglichen.
Angelehnt an das Konzept des Live-Codings soll dieses Tool designt sein für Live-Performances, es steht allerdings kein
Code im Zentrum, sondern ein grafisches Interface, das die Spontanität und Expressivität einer Live-Performance mit der
technischen Komplexität eines
verteilten Systems zusammenführt.

### Forschungsfrage (provisorisch)

Die Forschungsfrage, die dieses Projekt leiten soll, lautet:
**Wie kann eine benutzerfreundliche Oberfläche gestaltet werden, die es Performern ermöglicht, audiovisuelle Inhalte in
Echtzeit auf Basis von Sensordaten von mehreren Endgeräten zu orchestrieren?**

Teil der Beantwortung dieser Frage sind unter anderem folgende Unterfragen:

- Wie kann die Komplexität der Steuerung mehrerer Endgeräte übersichtlich und intuitiv in einer Oberfläche abgebildet
  werden?
- Können Design-Patterns aus der DAW- und Live-Coding-Welt (z.B. Node-basierte Programmierung, Clip-Launchers) auf die
  Steuerung von verteilten Endgeräten übertragen werden?
- Welche visuellen Rückmeldungen sind notwendig, damit Performer den Status und die Beiträge der einzelnen Endgeräte
  nachvollziehen können?
- Wie kann die Oberfläche so gestaltet werden, dass sie sowohl für Anfänger als auch für erfahrene Performer zugänglich
  ist?
- Wie kann einem Performer das Mapping von Sensordaten zu Klang- und Bildparametern erleichtert werden (z.B. durch
  Drag-and-Drop, Presets, visuelle Hilfen)?
- Welche Rolle spielen Voreinstellungen und anpassbare Templates, um den Einstieg in die Nutzung des Systems zu
  erleichtern?
- Wie lässt sich die Bidirektionalität der Kommunikation für Performer nutzbar machen, um audiovisuelles Feedback an die
  Peers zu senden oder deren Beiträge in Echtzeit zu modifizieren?
- Gibt es eine Möglichkeit für Performer, für die Peers variable Interfaces zu erstellen, um diese an unterschiedliche
  Performance-Szenarien anzupassen? Beispielsweise, einem Nutzer, der ein Klavier-Layout auf seinem Smartphone angezeigt
  bekommt, während ein anderer Nutzer ein XY-Pad sieht.

### Zielsetzung

Ziel dieser Arbeit ist die Entwicklung eines webbasierten Tools zur Liveorchestrierung dezentraler Peers über einen
zentralen Host in ein audiovisuelles Erlebnis.
Teil ist ein Editor, in welchem Daten von Sensoren der Peers als Parameter verwendet werden können,
um Visualisierungen zu erstellen und Klänge zu erzeugen, und auch von Nicht-Programmierer:innen genutzt werden kann.

### Meilensteine und Zeitplan

Hier ein vorläufiger Zeitplan für die Masterarbeit mit groben Aufwandsschätzungen:

#### Vertiefende Anforderungsanalyse und Exploration bestehender Systeme (2 Wochen)

- Genauere Sichtung relevanter Arbeiten (Live-Coding, TouchDesigner, kollaborative Webmusik, Smartphone-Orchester)
- Ableitung funktionaler sowie gestalterischer Anforderungen.

#### Konzeption des Gesamtsystems (2 Wochen)

- Definition des Interaktionsmodells, Datenflusses und der zentralen Komponenten (Host, Peers, Node-Editor,
  audiovisuelle Engine).

#### Implementierung der technischen Basis (3 Wochen)

- Aufbau der WebRTC-Kommunikation, Sensorstreaming, Peer-Management und QR-basiertem Pairing.
- Umsetzung erster Klang- und Visualisierungsbausteine (z.B. via Tone.js, P5.js oder Three.js) sowie
  Mapping-Mechanismen.

#### Entwurf des visuellen Programmierinterfaces (2 Wochen)

- Entwicklung eines prototypischen Editors, der Sensordaten einbindet und mit welchem sich erste Performances erstellen lassen.

#### Weitere Iterative Entwicklung und Usability-Optimierung (3 Wochen)

- Erweiterung des Editors, Implementierung von Presets/Templates, Gestaltung von Feedback-Mechanismen und
  UI-Optimierungen.
- Durchführung und Auswertung von Testsessions zu Bedienbarkeit, Verständlichkeit und Performance-Tauglichkeit.
- Fertigstellung eines stabilen Demonstrators für eine Beispielperformance.

#### Verschriftlichung der Masterarbeit (2 Wochen)

- Verfassung der schriftlichen Ausarbeitung und weiterer Artefakte (Bilddokumentation, Abschlussvideo, etc.).

#### Pufferzeit (3 Wochen)

### Formales

Geplanter Start: Anfang Dezember 2025
Sperrvermerk: Nein
Externer Kooperationspartner: Nein

### Literaturverzeichnis

#### [1]

Wang, G., Essl, G., & Penttinen, H. (2008, August). Do mobile phones dream of electric orchestras?. In _ICMC._

#### [2]

Oh, J., Herrera, J., Bryan, N. J., Dahl, L., & Wang, G. (2010, June). Evolving The Mobile Phone Orchestra. In _NIME (pp.
82-87)._

#### [3]

Forgette, A., Manaris, B., Gillikin, M., & Ramdsen, S. (2022, June). Speakers, More Speakers!!!–Developing Interactive,
Distributed,
Smartphone-Based, Immersive Experiences for Music and Art. In _Proceedings of the International Symposium on Electronic
Art._

#### [4]

Manaris, B. (2025). Research. _https://blogs.charleston.edu/manaris/research/#Memory_of_Wind_2025_

#### [5]

Robaszkiewicz, S., & Schnell, N. (2015). Soundworks–a playground for artists and developers to create collaborative
mobile web
performances. In _WAC-1st Web Audio Conference._