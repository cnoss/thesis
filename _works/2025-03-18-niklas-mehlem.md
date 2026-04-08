---
layout: work-result
author: Niklas Mehlem
related-folder: 2025-niklas-mehlem
title: "Gesichtserkennung in historischen Gemälden: Evaluierung von Modellen für
  das Cranach-Archiv"
date: 2025-07-15
result-repo: https://github.com/NiklasMehlem/cranachDetector
slideshow: true
final-presentation: lD2ZZbAO25I
research-diary: false
type: Bachelorarbeit
status: finished
visibility: published
keywords: Machine Learning, Watermarks
main-examiner: true
thumbnail: /assets/uploads/photo-log-niklas-mehlem-2025-05-30-10.jpg
---
Im Zuge der automatisierten Wasserzeichenplatzierung auf Bildern historischer Gemälde des Cranach Digital Archive (CDA) wurde untersucht, ob und wie bestehende Gesichtserkennungsmodelle zur zuverlässigen Erkennung von Gesichtern in diesen Werken eingesetzt werden können. Ziel war es, Wasserzeichen ästhetisch sinnvoll zu positionieren, ohne zentrale Bildelemente wie Gesichter zu überdecken. Da viele etablierte Modelle auf modernen Fotos realer Personen trainiert sind, wurden insgesamt neun gängige Verfahren – darunter RetinaFace, MTCNN, Dlib CNN, Caffe und andere – hinsichtlich ihrer Eignung für historische Porträts getestet und verglichen.

Die Analyse umfasste Tests zur allgemeinen Erkennungstauglichkeit, zur Auflösungsabhängigkeit sowie zur optimalen Festlegung von Confidence-Grenzwerten. Dabei zeigte sich, dass keines der Modelle alleine alle Anforderungen vollständig erfüllt. Durch die Kombination mehrerer leistungsstarker Modelle konnte jedoch eine robuste Lösung entwickelt werden. Basierend auf den Testergebnissen wurde ein flexibles Python-Modul realisiert, das die Gesichtserkennung mit verschiedenen Modellen ermöglicht, deren Ergebnisse zusammenführt und die Überprüfung erlaubt, ob sich ein Wasserzeichen über einem erkannten Gesicht befindet.

Das Modul ist vielseitig einsetzbar und bietet eine grafische Benutzeroberfläche, verschiedene Eingabeoptionen sowie konfigurierbare Parameter zur Feinabstimmung der Detektion. Damit schafft die Arbeit eine technische Grundlage für den sensiblen Umgang mit digitalen Reproduktionen historischer Kunstwerke und eröffnet neue Möglichkeiten für die automatisierte Bildverarbeitung im Kulturerbebereich.

