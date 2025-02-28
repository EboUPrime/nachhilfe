# Kategorisierung in Maschinellem Lernen (ML)

Kategorisierung (oder Klassifikation) ist ein überwachtes Lernverfahren im maschinellen Lernen, bei dem das Ziel darin besteht, Eingabedaten (Features) einer oder mehreren vordefinierten Klassen (Labels) zuzuordnen. In der überwachten Lernumgebung sind die Daten im Trainingsdatensatz bereits mit den korrekten Kategorien (Labels) versehen.

## Schritte der Kategorisierung

### 1. **Datensammlung und Vorverarbeitung**

Bevor das Modell trainiert werden kann, müssen die Daten gesammelt und vorverarbeitet werden. Diese Daten können aus verschiedenen Quellen stammen, wie z.B. Text, Bilder, Audio oder numerische Daten. 

**Beispiel 1: E-Mail-Spam-Klassifikation**

- **Datenquelle**: Eine Sammlung von E-Mails.
- **Ziel**: Klassifizieren der E-Mails als „Spam“ oder „Nicht-Spam“ (Ham).

Die E-Mails müssen dann vorverarbeitet werden, zum Beispiel durch:
- Entfernen von Stoppwörtern (wie „der“, „die“, „das“).
- Vektorisierung (Umwandlung des Textes in numerische Werte, z.B. mit dem **Bag-of-Words**-Modell).
- Tokenisierung (Aufteilen des Textes in kleinere Einheiten wie Wörter oder Sätze).

### 2. **Labeling**

Der Trainingsdatensatz muss mit Labels versehen werden. Für jede Eingabe gibt es eine bekannte Kategorie.

**Beispiel 2: Handgeschriebene Ziffern**

- **Datenquelle**: Bilder von handgeschriebenen Ziffern (z.B. MNIST-Datensatz).
- **Ziel**: Klassifizieren der Bilder in eine von 10 Kategorien: 0, 1, 2, ..., 9.

Die Bilder sind bereits mit Labels versehen (die tatsächliche Zahl, die auf dem Bild zu sehen ist).

### 3. **Modellwahl**

Je nach Problemstellung kann ein unterschiedliches Modell verwendet werden. Hier einige gängige Modelle:

#### Logistische Regression

Ein einfaches Modell für binäre Klassifikation (z.B. Spam vs. Nicht-Spam).

**Beispiel 3: E-Mail-Spam**

- **Modell**: Logistische Regression.
- **Eingaben**: Text der E-Mail, z.B. Vektoren aus dem Bag-of-Words-Modell.
- **Ausgabe**: Wahrscheinlichkeit, dass die E-Mail „Spam“ ist.

#### Entscheidungsbaum

Ein Modell, das Daten anhand von Entscheidungsregeln klassifiziert.

**Beispiel 4: Krankheitsdiagnose**

- **Modell**: Entscheidungsbaum.
- **Eingaben**: Symptome wie Fieber, Husten, Müdigkeit.
- **Ausgabe**: Diagnose, z.B. „Grippe“ oder „Erkältung“.

#### Support Vector Machines (SVM)

Ein Modell, das eine Grenze zwischen den Kategorien zieht, um die Daten zu trennen.

**Beispiel 5: Kreditkartenbetrug**

- **Modell**: SVM.
- **Eingaben**: Transaktionsdaten wie Betrag, Uhrzeit, Ort.
- **Ausgabe**: „Betrug“ oder „Kein Betrug“.

#### Neuronale Netzwerke

Diese sind besonders effektiv bei komplexeren Aufgaben wie der Bild- oder Spracherkennung.

**Beispiel 6: Bilderkennung**

- **Modell**: Convolutional Neural Network (CNN).
- **Eingaben**: Bilder von Tieren.
- **Ausgabe**: „Hund“, „Katze“, „Vogel“ usw.

### 4. **Training**

Während des Trainings wird das Modell mit einem Datensatz von bekannten Eingaben und den zugehörigen Labels gefüttert. Der Algorithmus versucht, ein Modell zu finden, das die Beziehung zwischen Eingaben und Ausgaben (Labels) so gut wie möglich lernt. Dabei wird der Fehler (z.B. die Differenz zwischen den vorhergesagten und tatsächlichen Labels) minimiert.

**Beispiel 7: E-Mail-Spam**

- **Daten**: Ein Trainingsdatensatz mit E-Mails und den Labels „Spam“ oder „Nicht-Spam“.
- **Modell**: Das Modell lernt, welche Merkmale (z.B. bestimmte Wörter oder Phrasen) Spam-E-Mails kennzeichnen.
- **Optimierung**: Der Fehler wird durch Anpassung der Gewichtungen im Modell minimiert.

### 5. **Evaluierung**

Nach dem Training wird das Modell mit einem separaten Testdatensatz überprüft, der nicht im Training verwendet wurde. Metriken wie **Genauigkeit**, **Präzision**, **Recall** und **F1-Score** helfen dabei, die Leistung des Modells zu bewerten.

- **Genauigkeit**: Der Anteil der richtig klassifizierten Beispiele.
- **Präzision**: Der Anteil der tatsächlich positiven Ergebnisse unter den vorhergesagten positiven Ergebnissen.
- **Recall**: Der Anteil der tatsächlichen positiven Ergebnisse, die korrekt erkannt wurden.
- **F1-Score**: Der harmonische Durchschnitt von Präzision und Recall.

**Beispiel 8: Krankheitsdiagnose**

- **Testdaten**: Ein Testdatensatz von Patienten mit bekannten Diagnosen.
- **Metriken**: Überprüfen, wie genau das Modell bei der Vorhersage der Diagnose ist.

### 6. **Vorhersage**

Nach dem Training und der Evaluierung wird das Modell auf neuen, unbekannten Daten angewendet, um Vorhersagen zu treffen.

**Beispiel 9: Kreditkartenbetrug**

- **Neue Eingabe**: Eine Transaktion mit unbekanntem Label (Betrug oder kein Betrug).
- **Vorhersage**: Das Modell gibt eine Klassifikation (Betrug oder kein Betrug) basierend auf den gelernten Mustern ab.

## Zusammenfassung

Die Kategorisierung in maschinellem Lernen besteht darin, Eingabedaten mit einem Modell so zu analysieren, dass es diese in eine von mehreren vordefinierten Klassen einordnet. Der Prozess umfasst mehrere Schritte: Datensammlung und Vorverarbeitung, Labeling, Modellwahl, Training, Evaluierung und Vorhersage. Die Wahl des Modells hängt von der Art des Problems und der verfügbaren Daten ab.

## Häufige Modelle für Kategorisierung

- **Logistische Regression**: Einfach, für binäre Klassifikation.
- **Entscheidungsbäume**: Baumstruktur, gut für interpretierbare Modelle.
- **Support Vector Machines (SVM)**: Effektiv bei der Trennung von Klassen.
- **Neuronale Netzwerke**: Besonders bei komplexen, unstrukturierten Daten wie Bildern oder Texten effektiv.
