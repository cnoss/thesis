---
layout: work
title: "Informationsarchitektur als räumliche Klanglandschaft"
datum: 01.10.2026
status: proposal
keywords: Sound, Web Audio, Spatial Audio, Interaktionsdesign, Barrierefreiheit
---
### TL;DR
Websites denken wir fast nur visuell. Hier geht es um eine Website, die man vor allem über Raumklang erkundet: Inhalte haben einen Ort im Klangraum, Navigation fühlt sich an wie Bewegung und Hierarchie wird hörbar. Das kann ein schönes Hörerlebnis werden, aber auch ein ernst gemeinter neuer Zugang zum Web ohne Bildschirm.

---

### Worum geht's?
Mit der Web Audio API kann der Browser längst 3D-Sound. Der `PannerNode` mit HRTF setzt Klänge über Kopfhörer erstaunlich plastisch in den Raum, also vorne, hinten, nah oder fern. Mit [Resonance Audio](https://resonance-audio.github.io/resonance-audio/) kommt noch Raumakustik dazu. Im Webdesign spielt Klang trotzdem kaum eine Rolle, höchstens als Klick-Sound oder Hintergrundmusik.

Dabei ist visuelle Gestaltung durch und durch räumlich: Nähe heißt Zusammengehörigkeit, Größe heißt Wichtigkeit, Position heißt Reihenfolge. Screenreader machen daraus einen linearen Sprachstrom, und genau diese räumliche Ordnung geht dabei verloren. Sonic Interaction Design, Auditory Displays und Earcons liefern seit Jahren die Grundlagen, und Audio Games zeigen, dass man sich in rein akustischen Welten gut zurechtfindet. Was bisher fehlt, ist die Übertragung auf ganz normale Websites.

### Mögliche Zielbilder

1. **Der Klangraum als Website:** Ein Portfolio, ein Ausstellungskatalog oder ein kleines Magazin, das man hörend erkundet. Der Bildschirm ist dabei Nebensache.
2. **Der hörbare Layer:** Eine Library oder Browser-Extension, die sauber ausgezeichnete Seiten in einen Klangraum übersetzt. Überschriften, Landmarks und Links bekommen dann einen Ort und einen eigenen Klang.
3. **Das Gestaltungsvokabular:** Ein Baukasten, in dem man ausprobieren kann, wie sich Nähe, Kontrast, Hierarchie und Rhythmus anhören. Am Ende steht ein Pattern-Set für akustische Interfaces.

### Spannende Fragen

* Lassen sich Nähe, Kontrast und Hierarchie in Klang übersetzen, und wo hinkt die Analogie?
* Wie viel Rauminformation verträgt das Ohr, bevor es zu viel wird?
* Ergänzt so ein Klangraum den Screenreader oder ersetzt er ihn sogar stellenweise?
* Wie klingt eigentlich eine Überschrift, ein Link, eine Fehlermeldung oder ein Ladezustand?

### Wie groß darf's sein?

* **Praxisprojekt:** Gestaltungsvokabular plus ein kleiner Klangraum mit wenigen Inhaltstypen, getestet im Kreis der Kommiliton:innen.
* **Bachelorarbeit:** Eine komplette hörbare Website zu einem konkreten Inhalt, getestet mit verschiedenen Nutzer:innengruppen.
* **Masterarbeit:** Ein verallgemeinerbarer Ansatz (Zielbild 2 oder 3) mit solider Evaluation, Vergleich mit Screenreader-Nutzung und daraus abgeleiteten Gestaltungsrichtlinien.

Zur Präsentation gehört auf jeden Fall eine Hörstation mit Kopfhörern. Für Video und Bilddoku bietet sich eine Draufsicht an, in der man sieht, wie sich die Hörposition durch den Raum bewegt.

### Worauf Sie sich einstellen sollten
HRTF funktioniert nicht bei allen Menschen gleich gut, und vorne und hinten werden gern verwechselt, also früh testen. Ohne Kopfhörer geht es nicht. Klänge, die anfangs charmant sind, nerven nach zehn Minuten oft gewaltig, deshalb brauchen Sie viele Iterationen. Und Tests mit blinden und sehbehinderten Menschen brauchen Vorlauf und Fingerspitzengefühl, Kontakte also am besten früh knüpfen, zum Beispiel über Selbsthilfeverbände.

### Darauf können Sie aufbauen
Auf der Sound-Seite: [Soundgenerierung mit Webtechnologien](https://cnoss.github.io/thesis/research-questions/soundgenerierung-im-web.html) und Sebastian Brocks [WebSynth](https://cnoss.github.io/thesis/works/-explorative-konzeption-und-implementierung-einer-web-basierten-plattform-zur-musikalischen-echtzeit-kollaboration-an-modular-synthesizern-august-5-2024-12-00-am.html). Auf der Accessibility-Seite: Meike Jungilligens' Arbeit zur [Screenreader-Unterstützung in Vuetify](https://cnoss.github.io/thesis/works/2026-02-24-meike-jungilligens.html) und Mia Charlotte Henrichsmeyers Arbeit zu [barrierefreien Mikrointeraktionen](https://cnoss.github.io/thesis/works/2026-03-09-mia-charlotte-henrichsmeyer.html). Der Unterschied: Hier geht es nicht ums Prüfen, sondern ums Gestalten.

### Passt zu Ihnen, wenn …
… Sie ein gutes Ohr haben, Lust auf Sounddesign und Interaktionsgestaltung mitbringen, mit JavaScript klarkommen (in Web Audio kann man sich einarbeiten) und gern mit echten Menschen testen. Zusammenarbeit mit Leuten aus Musik- oder Audio-Studiengängen ist ausdrücklich willkommen.

---
### Einstieg & Inspiration
- [Web Audio API: PannerNode](https://developer.mozilla.org/en-US/docs/Web/API/PannerNode)
- [Resonance Audio](https://resonance-audio.github.io/resonance-audio/)
- Franinović, K. & Serafin, S. (Hrsg.): *Sonic Interaction Design*, MIT Press 2013
- *A Blind Legend*: ein Audio Game, das zeigt, wie Orientierung rein akustisch funktioniert
- Janet Cardiffs Audio Walks als künstlerische Referenz für erzählenden Raumklang
