---
layout: work
title: "Die Umgebung als Theme: Kamerabasierte Ableitung von Farbsystemen für Interfaces"
datum: 01.10.2026
status: proposal
keywords: Farbe, OKLCH, Designsystem, Kamera, Screendesign, Generative Gestaltung
---
### TL;DR
Kamera drauf halten, auf die Umgebung, ein Foto oder ein Objekt, und daraus entsteht ein komplettes Farbsystem für ein Interface. Der Herbstwald vor dem Fenster wird zum Dark Mode, die Kaffeetasse zum Akzent. Ein Werkzeug, das die Farbstimmung der echten Welt einfängt und sie in Screendesign übersetzt.

---

### Worum geht's?
Ein Farbsystem in einem Interface ist mehr als eine hübsche Palette. Es trägt Stimmung und Marke, baut Hierarchie auf und zeigt Zustände an. Dafür braucht es Rollen wie Hintergrund, Oberfläche, Text, Akzent und Status, und zwar im Light Mode wie im Dark Mode. Josef Albers hat in *Interaction of Color* gezeigt, wie sehr Farben voneinander abhängen. In Designsystemen landen sie trotzdem oft als lose Liste von Hex-Werten.

Die meisten Palettengeneratoren ziehen einfach die häufigsten Farben aus einem Bild und hören dann auf. Spannender ist die Frage, wie man aus einer Farbstimmung ein *funktionierendes* System macht. Mit OKLCH gibt es in CSS dafür jetzt einen wahrnehmungsnahen Farbraum, in dem sich Helligkeit, Buntheit und Farbton unabhängig voneinander steuern lassen. Dass die Grundidee alltagstauglich ist, zeigt Material You, das sein Farbschema aus dem Hintergrundbild des Smartphones ableitet. Hier soll es aber um mehr gehen: um die Kamera als Live-Werkzeug und um die gestalterischen Entscheidungen hinter der Ableitung.

### Mögliche Zielbilder

1. **Das Gestaltungswerkzeug:** Eine Web-App für Designer:innen, mit der man die Kamera auf etwas richtet und Farbsysteme vorgeschlagen bekommt, inklusive Varianten und Export als Design Tokens.
2. **Die Live-Website:** Eine Website, die ihr Farbschema über die Kamera an die Umgebung der Besucher:innen anpasst. Ein Experiment rund um adaptive Interfaces.
3. **Der Farbspaziergang:** Eine mobile App, mit der man unterwegs Farbsysteme sammelt. Das ist eine Art Moodboard, aus dem direkt nutzbare Themes entstehen.

### Eine mögliche Variante: der Kontrast-Schalter
Man kann das System auch per Knopfdruck auf barrierefreie Kontraste trimmen (WCAG 2 oder das neuere APCA). Gerade OKLCH macht das gut machbar, weil sich die Helligkeit gezielt verschieben lässt, ohne dass der Farbcharakter verloren geht. Dann wird es richtig interessant: Wie viel Stimmung überlebt, wenn der Schalter an ist? Und in Systemen, in denen Kund:innen eigene Farben wählen, wäre das ein echter Mehrwert.

### Spannende Fragen

* Was macht die Farbstimmung eines Ortes oder Objekts aus, und wie bringt man sie in ein Interface?
* Lassen sich ästhetische Qualitäten von Farbkombinationen algorithmisch beschreiben?
* Wie sieht ein Werkzeug aus, das inspiriert statt vorschreibt?
* Was unterscheidet eine *gute* Palette von einer *korrekten*?

### Wie groß darf's sein?

* **Praxisprojekt:** Farben aus Fotos extrahieren, ein einfaches Rollensystem ableiten, dazu eine Vorschau an einer Beispieloberfläche und ein Export.
* **Bachelorarbeit:** Live-Modus mit der Kamera, Light und Dark Mode, Varianten und eine Evaluation mit Gestalter:innen.
* **Masterarbeit:** Verschiedene Ableitungsverfahren im Vergleich, eine Studie zur ästhetischen Bewertung, ggf. mit Kontrast-Schalter und Übertragung auf mandantenfähige Designsysteme.

In der Präsentation lässt sich das live vorführen: Kamera auf ein Objekt im Raum halten, und das Interface färbt sich um. In der Bilddoku stehen sich dann Fotos und die daraus entstandenen Interfaces gegenüber.

### Worauf Sie sich einstellen sollten
Kamerabilder hängen von Weißabgleich und Belichtung ab, und was die Kamera liefert, ist nicht das, was man sieht. Die häufigste Farbe ist außerdem nicht unbedingt die prägendste, Sie sollten also nach Wahrnehmung gewichten und nicht nach Fläche. Und aus fünf schönen Farben wird noch lange kein System. Die Zuordnung zu Rollen ist die eigentliche Gestaltungsarbeit.

### Darauf können Sie aufbauen
Erfahrungen mit der Kamera im Browser stecken in der [Selfie-basierten Webanwendung](https://cnoss.github.io/thesis/works/2025-10-30-cosima-hiromi-zink.html) von Cosima Hiromi Zink. Für den Kontrast-Schalter lohnt sich ein Blick in die Masterarbeit [Accessibility as a Service](https://cnoss.github.io/thesis/works/2026-01-27-methusshan-elankumaran.html) von Methusshan Elankumaran, die gezeigt hat, dass mandantenspezifische Farbanpassungen regelmäßig die Barrierefreiheit verletzen.

### Passt zu Ihnen, wenn …
… Sie ein Faible für Farbe und visuelle Gestaltung haben, HTML, CSS und JavaScript beherrschen und Lust haben, sich in Farbräume einzuarbeiten. Das Thema ist sehr praxisnah für Designsysteme und bietet trotzdem viel Raum zum Experimentieren.

---
### Einstieg & Inspiration
- [oklch() (MDN)](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/oklch)
- [Material Design 3: Dynamic Color](https://m3.material.io/styles/color/dynamic/user-generated-source)
- [APCA: Accessible Perceptual Contrast Algorithm](https://git.apcacontrast.com/documentation/APCA_in_a_Nutshell)
- Josef Albers: *Interaction of Color* (1963)
