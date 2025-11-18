# Titel und Forschungsfrage

## 10 Titel-Vorschläge

1. **Dezentrales Orchester: Explorative Entwicklung eines WebRTC-basierten Peer-to-Peer-Systems zur Live-Orchestrierung von audiovisuellen Erlebnissen**
2. **Live-Sensorchoreographie: Entwicklung eines visuellen Programmier-Interfaces für die Live-Orchestrierung kollaborativer Smartphone-Performances**
3. **Von Sensoren zum Sound: Gestaltung eines Real-time Mapping-Systems für verteilte mobile Geräte als Musikinstrumente**
4. **Das Smartphone als Instrument: Untersuchung niedrigschwelliger Zugänge zum kollaborativen Musizieren durch browser-native Sensor-Integration**
5. **Bidirektionale Partizipation: Konzeption eines Browser-basierten Systems zur haptisch-visuell-auditiven Publikumsintegration in Live-Performances**
6. **DecentraBand : Konzeption und Implementation von Benutzeroberflächen für die Echtzeitsteuerung audiovisueller Inhalte in einem dezentralen, kollaborativem Szenario**
7. **Distributed Embodied Performance: Erforschung multimodaler Feedback-Mechanismen für webbasierte kollaborative Sensor-Orchestration**
8. **Strudel meets WebRTC: Erweiterung des Strudel-Frameworks zur Integration von WebRTC für dezentrales audiovisuelles Live-Coding**
9. **Programmable Peers: Entwicklung eines Systems zur dynamischen Generierung und Live-Distribution adaptiver Benutzeroberflächen für kollaborative webbasierte Musikperformances**
10. **10. Remote Interface Orchestration: Konzeption eines bidirektionalen Systems zur Laufzeit-Gestaltung verteilter Eingabe-Interfaces für sensor-basierte audiovisuelle Performances**

---

## 5 Forschungsfragen

### Frage 1: WebRTC als Basis für drahtlose Musik-Controller

**Hauptfrage:**
Lässt sich mittels WebRTC ein System realisieren, mit welchem sich Endgeräte (z.B. Smartphones) als Musikinstrument oder MIDI-Controller nutzen lassen?

**Teilfragen:**
- Ist die Latenz bei der Übertragung von Steuerdaten über WebRTC für musikalische Anwendungen ausreichend gering?
- Welche Herausforderungen ergeben sich bei der Synchronisation von mehreren Endgeräten in Echtzeit?
- Falls die Latenz zu hoch ist, welche Optimierungen oder Alternativen zu WebRTC gibt es, um die Performance zu verbessern, oder lässt sich das Problem durch Design-Entscheidungen (z.B. Quantisierung) im System umgehen?
- Wie lässt sich eine benutzerfreundliche Oberfläche gestalten, die es Nutzern ermöglicht, ihre Endgeräte einfach zu koppeln und intuitiv als Musikinstrumente zu verwenden?
- Kann durch Rückmeldungen über WebRTC an die Endgeräte die Nutzererfahrung verbessert werden, z.B. durch haptisches Feedback oder visuelle Signale?
- Wie unterscheidet sich die wahrgenommene Latenz zwischen unidirektionaler (nur Sensor → Host) und bidirektionaler Kommunikation (Sensor → Host → Feedback), und welchen Einfluss hat sofortiges Feedback auf die musikalische Ausdrucksfähigkeit?

---

### Frage 2: Verarbeitung dezentral gesammelter Daten zu Klang und Bild

**Hauptfrage:**
Was für Möglichkeiten gibt es, Daten von mehreren verteilten Endgeräten zu sammeln und in einem zentralen System zu verarbeiten, um daraus Klang- und Bildinhalte zu generieren?

**Teilfragen:**
- Ist WebRTC dafür geeignet, kontinuierliche Datenströme von mehreren Clients zu einem Server zu übertragen, auch bei einem hohen Datenaufkommen?
- Wie können Sensordaten (z.B. Beschleunigungssensoren, Klicks bzw. Touch-Ereignisse) genutzt werden, um musikalische Parameter (Generierung von Sounds, Abspielen von Samples etc.) zu steuern?
- Ist es möglich, die Sensordaten auch für die Generierung von visuellen Inhalten (z.B. Projektionen, Visuals auf dem Host-Screen) zu verwenden?
- Was sind in diesem Kontext Stärken und Schwächen von sensorbasierten Eingaben im Vergleich zu traditionellen Eingaben über Benutzeroberflächen?
- Wie könnte eine Oberfläche gestaltet werden, mit dem Ersteller solcher Erlebnisse die gesammelten Daten sinnvoll zu Klang- und Bildinhalten verarbeiten können?
- Welche Herausforderungen ergeben sich bei der Synchronisation und Verarbeitung der Datenströme in Echtzeit, und wie können diese gelöst werden?
- Welche kreativen Möglichkeiten ergeben sich durch die Nutzung von verteilten Endgeräten für die Generierung von Klang- und Bildinhalten?
- Kann der Host Audio-Streams oder synthesierte Sounds zurück an einzelne oder alle Peers senden, um verteilte Spatial-Audio-Installationen zu ermöglichen, bei denen jedes Smartphone zum Lautsprecher wird?

### Frage 3: Gestaltung einer Nutzeroberfläche zur Live-Steuerung audiovisueller Inhalte

**Hauptfrage:**
Wie kann eine benutzerfreundliche Oberfläche gestaltet werden, die es Performern ermöglicht, audiovisuelle Inhalte in Echtzeit auf Basis von Sensordaten von mehreren Endgeräten zu orchestrieren?

**Teilfragen:**
- Wie kann die Komplexität der Steuerung mehrerer Endgeräte übersichtlich und intuitiv in einer Oberfläche abgebildet werden?
- Können Design-Patterns aus der DAW- und Live-Coding-Welt (z.B. Node-basierte Programmierung, Clip-Launchers) auf die Steuerung von verteilten Endgeräten übertragen werden?
- Welche visuellen Rückmeldungen sind notwendig, damit Performer den Status und die Beiträge der einzelnen Endgeräte nachvollziehen können?
- Wie kann die Oberfläche so gestaltet werden, dass sie sowohl für Anfänger als auch für erfahrene Performer zugänglich ist?
- Wie kann einem Performer das Mapping von Sensordaten zu Klang- und Bildparametern erleichtert werden (z.B. durch Drag-and-Drop, Presets, visuelle Hilfen)?
- Welche Rolle spielen Voreinstellungen und anpassbare Templates, um den Einstieg in die Nutzung des Systems zu erleichtern?
- Wie lässt sich die Bidirektionalität der Kommunikation für Performer nutzbar machen, um audiovisuelles Feedback an die Peers zu senden oder deren Beiträge in Echtzeit zu modifizieren?
- Gibt es eine Möglichkeit für Performer, für die Peers variable Interfaces zu erstellen, um diese an unterschiedliche Performance-Szenarien anzupassen? Beispielsweise, einem Nutzer, der ein Klavier-Layout auf seinem Smartphone angezeigt bekommt, während ein anderer Nutzer ein XY-Pad sieht.

### Frage 4: Partizipative Performance und Publikumsrolle

**Hauptfrage:**
Wie verändert sich die Dynamik zwischen Performer und Publikum, wenn Zuschauer durch eigene Smartphones aktiv am audiovisuellen Erlebnis teilnehmen können?

**Teilfragen:**
- Welche Strategien ermöglichen es, dass viele Teilnehmer (50+) sinnvoll zur Performance beitragen, ohne dass Chaos entsteht?
- Wie kann ein "Conductor Mode" gestaltet werden, der dem Host die Kontrolle über den kreativen Output behält, während Peers Input liefern?
- Welche psychologischen und sozialen Effekte ergeben sich, wenn Publikum von passiven Konsumenten zu aktiven Mitgestaltern wird?
- Inwiefern unterscheidet sich die Experience zwischen kontrollierten Workshops (z.B. 10 Teilnehmer mit Einweisung) und spontanen Public Installations (z.B. 50+ unvorbereitete Besucher)?
- Können durch gamifizierte Elemente oder visuelle Rückmeldung auf dem Host-Screen Teilnehmer motiviert werden, spezifische Gesten oder Bewegungen auszuführen?
- Welche Rolle spielt multimodales Feedback (Vibration, Display-Farben, Audio-Returns) für das Gefühl der Agency und Co-Authorship bei Teilnehmern? Fühlen sich Peers mehr als "Instrumente" oder als "Mitmusiker", wenn sie direktes Feedback erhalten?
- Lässt sich durch verteiltes Spatial Audio (jedes Smartphone als Lautsprecher) ein immersiveres räumliches Klangerlebnis schaffen als mit zentraler Beschallung, und wie beeinflusst dies die Partizipationsbereitschaft?

---

### Frage 5: Barrierefreiheit und Zugänglichkeit digitaler Musikinstrumente

**Hauptfrage:**
Inwiefern kann ein browserbasiertes, sensor-gesteuertes System die Zugangshürden zu musikalischem Ausdruck und Kollaboration im Vergleich zu traditioneller Hardware senken?

**Teilfragen:**
- Welche Zielgruppen (Kinder, Menschen mit Behinderungen, Musikanfänger, professionelle Performer) profitieren am meisten von einem installationsfreien, hardware-unabhängigen Ansatz?
- Wie können unterschiedliche motorische Fähigkeiten durch flexible Sensor-Mappings (z.B. große vs. feine Bewegungen) berücksichtigt werden?
- Eignet sich das System für musikpädagogische Kontexte (Schulen, Workshops), und welche didaktischen Konzepte lassen sich damit umsetzen?
- Welche Limitationen ergeben sich durch die Abhängigkeit von Smartphone-Besitz und stabiler Internetverbindung, und wie könnten diese adressiert werden?
- Kann das System als "Gateway" dienen, um Interesse an tiefergehenden Musik-Technologien (DAWs, Hardware-Controller, Live-Coding) zu wecken?
- Inwiefern ermöglicht multimodales Feedback barrierefreiere Zugänge zu musikalischer Expression (z.B. für Gehörlose durch Haptic-Only-Mode, für Sehbehinderte durch Audio-Cues)?
- Welche kreativen und technischen Herausforderungen ergeben sich, wenn Peers nicht nur Input-Devices, sondern gleichzeitig Output-Devices (Lautsprecher) sind? Wie beeinflusst das die Latenzwahrnehmung?

---