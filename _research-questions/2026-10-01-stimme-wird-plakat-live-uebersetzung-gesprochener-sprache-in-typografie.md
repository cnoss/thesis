---
layout: work
title: "Live-Übersetzung gesprochener Sprache in typografische Kompositionen"
datum: 01.10.2026
status: proposal
keywords: Typografie, Variable Fonts, Sprachanalyse, Web Audio, Plakatgestaltung, Creative Coding
---
### TL;DR
Beim Sprechen steckt viel Bedeutung in Lautstärke, Tempo, Tonhöhe und Pausen, und geschriebener Text verliert all das. Hier wird gesprochene Sprache live zum typografischen Plakat: Die Stimme bestimmt Schnitt, Größe, Laufweite und Rhythmus. Ein geflüstertes Wort sieht dann anders aus als ein gerufenes.

---

### Worum geht's?
Expressive Typografie hat Tradition: Die Futuristen haben Lärm und Geschwindigkeit in Schrift gesetzt, Schwitters hat mit der *Ursonate* Lautpoesie gemacht, die konkrete Poesie hat mit der Gestalt von Wörtern gespielt. Und im Comic ist ein Schrei schon immer größer als ein Flüstern. Im Web dagegen ist Text meistens brav und gleichförmig.

Dabei liegen die Bausteine längst bereit. Spracherkennung liefert den Text, zum Teil sogar lokal im Browser (z.B. Whisper über Transformers.js). Die Audioanalyse liefert Lautstärke, Tonhöhe, Klangfarbe und Pausen. Und mit Variable Fonts lassen sich Gewicht, Breite, Neigung und weitere Achsen für jedes einzelne Zeichen stufenlos verändern. Zusammen ergibt das eine Typografie, die nicht nur zeigt, *was* gesagt wurde, sondern auch *wie*. Die eigentliche Kunst ist das Mapping: Es soll ausdrucksstark sein und trotzdem lesbar bleiben.

### Mögliche Zielbilder

1. **Das Bühnenwerkzeug:** Bei Lesungen, Poetry Slams oder Vorträgen wächst das Gesprochene live als Typografie auf der Leinwand mit.

2. **Das Archiv der Stimmen:** Viele Menschen sprechen denselben Text, und daraus entsteht eine Ausstellung samt Website, die zeigt, wie unterschiedlich ein einziger Satz klingen kann.

### Erste Fragen

* Erkennt man eine Stimme an ihrer Typografie wieder?
* Welche Sprechmerkmale lassen sich verlässlich messen, und welche sind gestalterisch überhaupt interessant?
* Wie bleibt ein Plakat lesbar, wenn jedes Wort anders aussieht?
* Lesen Betrachtende aus der Schrift die Emotion heraus, die die sprechende Person gemeint hat?

### Wie groß darf's sein?

* **Praxisprojekt:** Wenige Merkmale (z.B. Lautstärke und Tempo), ein Mapping und am Ende ein Export als Plakat.

* **Bachelorarbeit:** Mehrere Merkmale, ein ausgearbeitetes Layoutsystem und ein Einsatz bei einem Event, der anschließend ausgewertet wird.

* **Masterarbeit:** Verschiedene Mapping-Strategien im Vergleich, eine Studie zur Wiedererkennung von Stimme und Emotion und vielleicht sogar ein eigener Variable Font mit Achsen speziell für Prosodie.

Am Ende stehen ein Echtzeitsystem und eine Serie gedruckter Plakate, also etwas, das sich hervorragend ausstellen lässt. Im Abschlussvideo sieht man dann, wie Stimme und Schrift gleichzeitig entstehen.

### Worauf Sie sich einstellen sollten
Die Web Speech API hängt vom Browser ab und schickt die Audiodaten teilweise an einen Server, deshalb sollten Sie Datenschutz und Offline-Betrieb mitdenken. Spracherkennung und Audioanalyse laufen nicht synchron, und die Merkmale den einzelnen Wörtern zuzuordnen ist eine Aufgabe für sich. Nicht jeder Variable Font taugt dafür, prüfen Sie Achsen und Lizenzen also früh. Und die Balance zwischen Ausdruck und Lesbarkeit finden Sie nur über viele Iterationen.

### Darauf können Sie aufbauen
In der Bachelorarbeit [Die Kunst der Titelsequenz](https://cnoss.github.io/thesis/works/2025-03-14-vassilij-misenko.html) hat Vassilij Misenko filmische Typografie ins Web übertragen und dabei festgestellt, dass der Kontext fehlte. Hier liefert die Stimme diesen Kontext gleich mit. Weitere Anknüpfungspunkte sind [Typographie im Web](https://cnoss.github.io/thesis/research-questions/typo-im-web.html), [Kurze Geschichte der Typographie als Film](https://cnoss.github.io/thesis/research-questions/history-of-typo-film.html) sowie die Sound-Themen wie [Soundgenerierung mit Webtechnologien](https://cnoss.github.io/thesis/research-questions/soundgenerierung-im-web.html).

### Passt zu Ihnen, wenn …
… Sie Schrift lieben, gern experimentieren und mit JavaScript klarkommen (Erfahrung mit Web Audio ist ein Plus). Am Ende entsteht etwas, das man ausstellen, drucken und mitnehmen kann.

---
### Einstieg & Inspiration
- [Meyda: Audio Feature Extraction](https://meyda.js.org/)
- [Variable Fonts Guide (MDN)](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_fonts/Variable_fonts_guide)
- [Web Speech API (MDN)](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API)
- [Transformers.js](https://huggingface.co/docs/transformers.js)
- Historische Referenzen: futuristische Typografie (Marinetti), Kurt Schwitters' *Ursonate*, konkrete Poesie
