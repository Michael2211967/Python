#!/usr/bin/env cbmbasic

10 INPUT "Preis pro Kilo Farbe ";KP
20 INPUT "Kilo pro Quadratmeter ";KQ
30 PRINT
40 INPUT "Laenge ";L
50 INPUT "Breite ";B
60 F=L*B
70 M=F*KQ
80 P=M*KP
90 PRINT
100 PRINT "Fuer die Flaeche von ";F;" qm"
110 PRINT "werden ";M;" Kilo Farbe benoetigt."
120 PRINT "Der Preis fuer diese ";M;" kg Farbe betraegt ";P;" EUR:"
124 INPUT "Wollen Sie eine neue Flaeche berechnen ";W$
125 IF W$="ja" THEN GOTO 30
126 PRINT "Auf Wiedersehen!"
130 END
