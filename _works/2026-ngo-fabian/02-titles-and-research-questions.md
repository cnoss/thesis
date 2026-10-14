# Titel und Forschungsfrage

Bitte notieren Sie mindestens 10 mögliche Titel der Arbeit und mindestens 5 mögliche Forschungsfragen/ Zielsetzungen in dieses Dokument. 


## 1. Iteration

### Titel
1. Quantitative Bewertung der visuellen Designkonsistenz in Text-to-Code-generierten UIs aus Figma-Make-Designs
2. Einfluss von Text-to-Code-Generierung auf die Performance und Ladezeiten von Web-UIs aus Figma-Make-Designs
3. Automatisierte Validierung der Designsystem-Konsistenz in Text-to-Code-generiertem Frontend-Code aus Figma Make
4. Evaluierung der Systemtreue generativer UI-Tools: Eine quantitative Analyse der Designkonsistenz basierend auf einem UI-Kit

### Forschungsfragen

1. Inwiefern stimmt der visuelle Output von Text-to-Code-Lösungen, basierend auf Figma-Designs, mit den ursprünglichen Designspezifikationen überein, und welche Abweichungen treten am häufigsten auf?
2. In welchem Maße halten sich Text-to-Code-Lösungen an die Spezifikationen eines vordefinierten Designsystems in Figma, und welche Arten von Inkonsistenzen werden dabei im generierten Code beobachtet?
3. Inwiefern beeinflusst die Zerlegung von Design-Anforderungen (Prompt Decomposition) die Einhaltung visueller Konsistenz-Metriken in KI-gestützten Figma-Workflows im Vergleich zu Single-Shot-Ansätzen
4. Inwieweit ist eine Text-to-UI KI in der Lage, bei der Generierung von Interfaces die vordefinierten atomaren Regeln, Komponenten-Strukturen und Styles eines spezifischen Design Systems konsistent anzuwenden?

### Zielbilder 

1. Ziel dieser Arbeit soll es sein, die Designkonsistenz des Text-to-UI Tools zu messen basierend auf einem vorhandenen Design System. Dafür wird das in Figma integrierte Tool „Figma Make“ verwendet. Als Ausgangslage soll ein bestehendes Design System verwendet werden. Es werden mit verschiedene Parametern geprüft, wie konsistent die Design-Richtlinien eingehalten werden. Das Ergebnis dieser Arbeit soll ein Artefakt entstehen, dass als Leitfaden der  Best Practices mit Figma Make dient um Zeit-Effizient, die besten Ergebnisse zu erhalten.

2. Das Ziel ist die Etablierung eines Automated Style Audits. Es soll nachgewiesen werden, dass die KI nicht nur optisch ähnliche Designs erstellt, sondern technisch präzise die Instanzen und Tokens des UI-Kits nutzt, anstatt neue, redundante Elemente (Hardcoded Values) zu erschaffen. Ein "perfektes" Ergebnis wäre ein generierter Screen, der zu 100% aus bestehenden Library-Komponenten besteht.

### Mögliche Messbare Parameter/Metriken:
- Library Linkage Rate (Primäre Metrik -> Anzahl Verbundener Instanzen / Gesamtzahl der UI-Elemente x 100)
- Layout Grid & Spacing Accuracy
- Komplexität der Prompts
- Iterierte Prompts & One Shots (Anzahl an Prompts -> Maß für Zeiteffizienz)
- Token Compliance 


## Intiale Entwürfe

### Titel 
1. Mensch vs KI: Wie unterscheidet sich die wahrgenommene Usability eines KI-generierten-Prototypen von einem manuellen Entwurf für eine Hochschulplattform?
2. Best Practices: Explorative Analyse von KI-Tools in den Phasen des Design Thinking.
3. Mensch vs. Maschine im kreativen Prozess: Eine experimentelle Untersuchung zur User Experience KI-generierter Prototypen im Design Thinking Kontext.
4. Generative AI im Interface Design: Eine vergleichende Studie zur Design-Treue und Nutzerakzeptanz von Figma Make.
5. Effizienz vs. Empathie: Evaluation der Nutzerzentrierung von KI-generierten Prototypen im Vergleich zum klassischen User-Centered Design.
6. Prompt-Engineering als neue Design-Disziplin: Einfluss der Instruktionsqualität auf die Usability von Text-to-Prototype Ergebnissen.
7. Die Demokratisierung des Prototypings: Eine quantitative Untersuchung der Barrierefreiheit von KI-generierten Web-Interfaces.
8. Vom Prompt zum Produkt: Eine vergleichende Untersuchung der hedonischen und pragmatischen Qualität von KI-gestützten App-Entwürfen.
9. KI-gestütztes Rapid Prototyping: Ein A/B-Vergleich der Fehlerraten und Bearbeitungszeit in studentischen Nutzungsszenarien. 
10. Automatisierte Ästhetik: Der Einfluss von Figma Make auf die visuelle Konsistenz und Usability in frühen Design-Phasen.

### Forschungsfragen
1. Inwieweit verbessert KI-gestütztes Prototyping die Einhaltung von WCAG-Richtlinien (Barrierefreiheit) bei der automatischen Generierung von Web-Frontends?
2. Wie unterscheidet sich die wahrgenommene User Experience eines Prototyps, der mittels KI-gestützter Design-Methoden (Figma Make) erstellt wurde, von einem manuell nach klassischen Design Thinking Prinzipien entwickelten Artefakt?
3. Welchen Einfluss hat die Nutzung von generativer KI auf die wahrgenommene „Originalität“ eines Prototyps aus Sicht der Endnutzer?
4. In welchem Maße korreliert die Präzision des Text-Prompts in Figma Make mit dem SUS-Score (System Usability Scale) des resultierenden Prototyps?

### Zielbilder

### Barrierefreiheits Validierungs Framework
Validierungs-Framework für KI-generierte Barrierefreiheit Entwicklung eines Prüfkatalogs, der misst, wie zuverlässig Figma Make spezifische Barrierefreiheits-Standards (z.B. Kontrast, Screenreader-Kompatibilität) im Vergleich zu einem manuell optimierten Prototyp umsetzt.

### Kriterienkatalog
Kriterienkatalog für "Effective Prompting" im Prototyping Erstellung eines evidenzbasierten Leitfadens, der aufzeigt, wie Design-Anforderungen formuliert sein müssen, damit das KI-Tool Prototypen mit einer hohen pragmatischen Qualität (nach AttrakDiff) produziert.

### Erarbeitung eines KI-gestützten Design-Thinking-Workflow
Ein konzeptionelle Erarbeitung eines KI-gestützten Design-Thinking-Workflows, der die Interaktion zwischen menschlicher Expertise und künstlicher Intelligenz transparent macht und kritisch bewertet, in welchen Prozessphasen KI sinnvoll unterstützend wirkt und wo menschliche Entscheidungs- und Gestaltungskompetenz unverzichtbar bleibt.

### Evaluierung Usability von KI-Gestützten Prototypen
Es werden 2 Prototypen erstellt. Eine KI Generierte (A) und eine manuell erstellt (B). Durch eine randomisierte kontrollierte Studie (RCT) bestehenden aus Studenten wird überprüft welcher Prototyp nutzerfreundlicher ist mit verschiedenen Qualitativen und oder / Quantitativer Metriken (z.B. SUS oder AttrakDiff) 




