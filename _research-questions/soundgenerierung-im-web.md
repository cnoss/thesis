---
title: Soundgenerierung mit Webtechnologien
keywords: Audio, WebDev, Web Audio API, Klangsynthese, Echtzeit-Kollaboration
layout: work
status: proposal
datum: 07.11.2023
---
### TL;DR
Was geht eigentlich im Browser, wenn es um Sound geht? Und zwar nicht ums Abspielen von MP3s, sondern ums Erzeugen, Verarbeiten und gemeinsame Orchestrieren von Klang in Echtzeit. Genau das wollen wir ausloten.

---

### Worum geht's?
Im Browser steckt inzwischen ein ziemlich vollständiges Audio-Studio: Die [Web Audio API](https://developer.mozilla.org/de/docs/Web/API/Web_Audio_API) mit Oszillatoren, Filtern und Effekten, AudioWorklets für eigene DSP, WebAssembly, um Engines wie Faust oder Csound laufen zu lassen, Web MIDI für Hardware und WebRTC, um alles miteinander zu vernetzen. Spannend ist aber nicht nur, *ob* das geht, sondern auch: Wo sind die Grenzen (Latenz, Timing, Performance)? Und welche Arten, Musik zu machen, werden erst dadurch möglich, dass es im Web läuft?

### Darauf können Sie aufbauen
Es gibt schon zwei Masterarbeiten, die man super weiterdenken kann:

* **Sebastian Brock:** [WebSynth](https://cnoss.github.io/thesis/works/-explorative-konzeption-und-implementierung-einer-web-basierten-plattform-zur-musikalischen-echtzeit-kollaboration-an-modular-synthesizern-august-5-2024-12-00-am.html) ist ein virtueller Modular-Synthesizer, an dem mehrere Leute gleichzeitig von verschiedenen Orten aus patchen.
* **Leander Gerwing:** [Leitmotif](https://cnoss.github.io/thesis/works/2026-06-09-leander-gerwing.html) ist ein visuelles Programmier-Interface, das die Smartphones des Publikums über WebRTC und Sensoren zu einem Teil der audiovisuellen Performance macht.

Beide Projekte laufen und der Code ist offen. Sie können also weiterbauen, die beiden kombinieren oder sie einfach als Sprungbrett für eine eigene Idee nehmen.

### Mögliche Richtungen

* **Klangerzeugung:** Wie weit kommt man mit Synthese im Browser? Web Audio, AudioWorklet und WASM im Vergleich, eigene Module.
* **Verarbeitung:** Effekte, Analyse von Live-Input, Sound trifft Visuals, vielleicht auch mal ML im Browser.
* **Orchestrierung:** Mehrere Geräte im Takt halten, mit Latenz umgehen, gemeinsam spielen. Was passiert z. B., wenn das Publikum am WebSynth mitpatcht?
* **Interfaces:** Instrumente jenseits von Tasten und Drehreglern, zum Beispiel über Sensoren, Gesten oder Live-Coding.

### Was am Ende rauskommen sollte
Ein spielbarer Prototyp und eine ehrliche Einschätzung, was das Web als Plattform für Klang heute kann und was (noch) nicht. Am besten untermauert mit Messungen und einem echten Test mit Musiker:innen oder auf der Bühne.

### Passt zu Ihnen, wenn …
… Sie JavaScript gut draufhaben, selbst Musik machen oder auf Synths, Sounddesign oder Medienkunst stehen und Lust haben, sich auch mal in fremden Code einzuwühlen. DSP-Vorwissen schadet nicht, ist aber kein Muss.

---
### Weitere Infos
- [Web Audio API (MDN)](https://developer.mozilla.org/de/docs/Web/API/Web_Audio_API)
- [Tone.js](https://tonejs.github.io/)
- [Strudel – Live Coding im Browser](https://strudel.cc/)
- [Faust](https://faust.grame.fr/)
