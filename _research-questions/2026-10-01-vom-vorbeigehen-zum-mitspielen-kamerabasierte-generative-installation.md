---
layout: work
title: "Kamerabasierte, generative Installation für den öffentlichen Raum"
datum: 01.10.2026
status: proposal
keywords: Installation, Creative Coding, Pose Detection, Interaktionsdesign, Generative Gestaltung
---
### TL;DR
Ein großer Screen oder eine Projektion im Foyer oder Flur reagiert auf Leute, die vorbeilaufen. Die Kamera erkennt Körperhaltung und Bewegung, daraus entsteht generative Grafik. Die eigentliche Herausforderung ist aber eine gestalterische: Aus Leuten, die vorbeigehen, sollen Leute werden, die mitspielen, und zwar ganz ohne Erklärtext.

---

### Worum geht's?
Installationen, die auf den Körper reagieren, gibt es schon lange, von Myron Kruegers *Videoplace* in den 70ern bis zu den *Mechanical Mirrors* von Daniel Rozin. Früher brauchte man dafür Spezialhardware. Heute läuft Pose Detection wie MediaPipe flüssig im Browser, und zwar mit einer ganz normalen Webcam. Zusammen mit WebGL oder WebGPU lässt sich so eine Installation komplett mit Webtechnologien bauen.

Technisch ist das also gar nicht mehr so schwer, gestalterisch aber schon. Die Forschung zu öffentlichen Displays beschreibt den *Audience Funnel*: vorbeigehen, etwas bemerken, kapieren, dass es reagiert, ausprobieren, spielen, weitergehen. Außerdem gibt es den *Honeypot-Effekt*: Wenn schon jemand mitmacht, trauen sich andere eher. Die meisten Installationen scheitern allerdings schon an Stufe eins, weil niemand merkt, dass sie überhaupt interaktiv sind.

### Mögliche Zielbilder

- **Der Spiegel:** Die Installation spiegelt den Körper abstrahiert, zum Beispiel als Partikel, Typo oder Formen, und entfaltet sich immer weiter, je länger man bleibt.
- **Das Gemeinschaftsbild:** Richtig spannend wird es erst, wenn mehrere Leute davorstehen, weil dann ihre Bewegungen miteinander interagieren.
- **Das Gedächtnis:** Die Installation sammelt über den Tag anonymisierte Bewegungsspuren zu einem kollektiven Bild, das abends als Plakat rausfällt.

### Spannende Fragen

* Welche visuellen Signale bringen Leute zum Interagieren, ohne dass man etwas erklären muss?
* Wie unterscheiden sich Einzelne und Gruppen, und lässt sich der Honeypot-Effekt gezielt gestalten?
* Wie lange bleiben Menschen, und was hält sie dort?
* Wie geht man mit Privatsphäre um, wenn eine Kamera im Spiel ist?

### Wie groß darf's sein?

**Praxisprojekt:** Ein visuelles Konzept, eine lauffähige Installation und ein Einsatz an einem Tag oder bei einem Event, inklusive Beobachtung.

**Bachelorarbeit:** Mehrere Varianten, die über ein paar Wochen laufen, systematisch beobachtet und miteinander verglichen werden.

**Masterarbeit:** Eine fundierte Untersuchung der Beteiligungsphasen mit Beobachtungsprotokollen und daraus abgeleiteten Gestaltungsprinzipien für Installationen ohne Erklärtext.

Für Abschlussvideo und Bilddoku ist das ein Geschenk, denn Sie können echte Interaktionen filmen (natürlich nur mit Einverständnis der Leute).

### Worauf Sie sich einstellen sollten
Licht ist der größte Feind, sowohl für Projektion als auch für Tracking, also den Ort früh und zu verschiedenen Tageszeiten testen. Beim Datenschutz gilt: nur lokal verarbeiten, keine Bilder speichern und vor Ort sichtbar darauf hinweisen. Das gehört übrigens auch offen in die Arbeit. Die Performance müssen Sie auf der Zielhardware über Stunden testen, nicht nur kurz auf dem eigenen Laptop. Und die Installation muss auch dann gut aussehen, wenn gerade niemand davorsteht, sonst bleibt erst gar keiner stehen.

### Darauf können Sie aufbauen
Das Thema setzt die generativ-künstlerische Linie fort, etwa Leander Gerwings [Live-Sensorchoreographie](https://cnoss.github.io/thesis/works/2026-06-09-leander-gerwing.html) (partizipative audiovisuelle Performance) oder den Vorschlag [Darstellung der Bezüge zwischen den Werken des Cranach Digital Archives](https://cnoss.github.io/thesis/research-questions/darstellung-der-bezuege-innerhalb-des-cda.html). Neu ist der öffentliche Raum und dass es um Menschen geht, die eigentlich gar nicht vorhatten, mit irgendwas zu interagieren.

### Passt zu Ihnen, wenn …
… Sie Spaß an visueller Gestaltung und generativen Systemen haben, JavaScript können (Erfahrung mit Canvas, p5.js oder Three.js ist ein Plus) und Lust haben, Leute zu beobachten und daraus etwas zu lernen. Am Ende haben Sie ein Werk, das man bei Ausstellungen, am Tag der offenen Tür und bei Hochschulevents direkt erleben kann.

---
### Einstieg & Inspiration
- [MediaPipe Pose Landmarker](https://ai.google.dev/edge/mediapipe/solutions/vision/pose_landmarker)
- Myron Krueger: *Videoplace* (ab 1974)
- Daniel Rozin: *Mechanical Mirrors*
- Brignull, H. & Rogers, Y.: *Enticing People to Interact with Large Public Displays in Public Spaces* (2003)
- Michelis, D. & Müller, J.: *The Audience Funnel* (2011)
