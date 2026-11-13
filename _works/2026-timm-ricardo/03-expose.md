# Exposé

## Semantic Motion in User Interfaces

*Bedeutung Transport durch animierte UI-Zustände - Framework und Editor-Prototyp*

| **Typ** Framework + Tool | **Stack** React, TypeScript, Framer Motion | **Theoriebasis** Semiotik, Wahrnehmungspsychologie |
|---|---|---|

---

**KONTEXT & PROBLEM**

Animationen in modernen User Interfaces sind allgegenwärtig und werden dabei überwiegend intuitiv oder rein ästhetisch eingesetzt. Existierende Motion-Guidelines großer Design Systeme (Material Design 3, Apple HIG, IBM Carbon, Fluent) beschreiben, welche Animationen verwendet werden sollen, liefern jedoch keine theoretisch begründete Antwort darauf, warum eine bestimmte Bewegung eine bestimmte Bedeutung transportiert. Eine Fehlermeldung, die nach links schlägt, kommuniziert Ablehnung, aber auf welcher theoretischen Grundlage? Diese Frage ist bislang nicht systematisch beantwortet.

---

**ZIELSETZUNG**

Ziel der Arbeit ist die Entwicklung eines theorie-gestützten Frameworks, das UI-Animationen nach ihrer semantischen Bedeutung klassifiziert. Grundlage bilden drei Theoriebereiche: Semiotik (Zeichentheorie nach Peirce und Saussure), Wahrnehmungspsychologie (präattentive Verarbeitung, Direction Bias, Object Continuity) sowie Motion-Design-Prinzipien (Disney-Prinzipien, Easing als semantischer Träger). Das Framework mündet in einem interaktiven Prototyp, dem Semantic Motion Editor, der das Mapping von Animationen auf Bedeutungen visuell erfahrbar macht.

| **Forschungsfrage** Wie lässt sich ein theorie-gestütztes Framework zur semantischen Klassifikation von UI-Animationen konzipieren, und wie kann dieses Framework in einem interaktiven Werkzeug prototypisch demonstriert werden? |
|---|

---

**PROTOTYP**

Der Semantic Motion Editor ist ein browserbasiertes Tool, in dem Nutzer eine UI-Komponente (Button, Toggle, Toast, Modal) und ein Motion-Pattern auswählen. Das Tool zeigt die Animation in Echtzeit, erklärt die semantische Bedeutung mit theoretischer Begründung und exportiert den fertigen Animations-Code (Framer Motion oder CSS). Kern des Tools ist eine strukturierte Mapping-Datenbank, die das Framework direkt implementiert.

---

**ABGRENZUNG**

Die Arbeit führt keine empirische Nutzerstudie durch. Der wissenschaftliche Beitrag liegt in der theoretischen Herleitung und Systematisierung des Frameworks. Der Prototyp ist Demonstration, nicht Evaluation.

---

| **Schluesselquellen** **Peirce, C. S. (1931).** *Collected Papers.* Harvard University Press. - Grundlage der Zeichentypologie (Ikon, Index, Symbol) als theoretisches Rückgrat des Mappings. **Johnston, O. & Thomas, F. (1981).** *The Illusion of Life: Disney Animation.* Abbeville Press. - Die 12 Animationsprinzipien als Basis fuer semantisch aufgeladene Bewegungsqualitäten im UI-Kontext. **Treisman, A. & Gelade, G. (1980).** *A feature-integration theory of attention.* Cognitive Psychology, 12(1). - Präattentive Verarbeitung als wissenschaftliche Grundlage dafür, warum Bewegung Bedeutung vor bewusster Wahrnehmung transportiert. |
|---|