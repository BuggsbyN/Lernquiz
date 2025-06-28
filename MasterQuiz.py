
import streamlit as st

st.title("Python Quiz-Kapitel 1!")

score = 0

#Fragen Operatoren

st.subheader("Welcher Operator gibt den ganzzahligen Anteil einer Division zurück?")
antwort1 = st.radio("Wähle eine Antwort",["/","//","%","**"])
if antwort1 == "/":
    score = score + 1

st.subheader("Welche Aussage ist Falsch?:")
antwort2 = st.radio("Wähle eine Antwort",["5<10 ist True","4=="4" ist True","5!=6 ist True","3>=3 ist True"])
if antwort2 == "5<10 ist True":
    score = score + 1

st.subheader("Was gibt 2**3 zurück?:")
antwort3 = st.text_input("Deine Antwort")
if antwort3 == "6":
    score = score + 1

st.subheader("Welche Eingabe ergibt bei int(input(Zahl: + 5 das Ergebnis 15?")
antwort4 = st.radio("Wähle eine Antwort",["5","10",""10"","fünf"])
if antwort4 == "10":
    score = score + 1

st.subheader("Was bewirkt der Operator !=?")
antwort5 = st.radio("Wähle eine Antwort",["Er prüft, ob zwei Werte gleich sind","Er prüft, ob zwei Werte unterschiedlich sind","Er gibt den Rest einer Divison wieder","Er wandelt einen String in Integer um"])
if antwort5 == "Er prüft ob zwei Werte unterschiedlich sind":
    score = score + 1

st.subheader("Was ergibt bool(0)?:")
antwort6 = st.radio("Wähle eine Antwort",["True","False","none","0"])
if antwort6 == "False":
    score = score + 1

#Fragen Kontrollstrukturen

st.subheader("Wofür wird eine If-Anweisung verwendet?")
antwort7 = st.text_input("Deine Antwort")
if antwort7 == "Für die wenn dann Logik":
    score = score + 1

st.subheader("Was passiert, wenn die Bedingung in einer if Anweisung nicht erfüllt ist?")
antwort8 = st.radio("Wähle eine Antwort",["Der code im if_Block wird trotzdem ausgeführt","Das Programm stürzt sofort ab","Der Code im if-Block wird übersprungen und das Programm läuft normal weiter","Python wählt zufällig einen anderen Block aus, den es stattdessen ausführt"])
if antwort8 =="Der Code im if Block wird übersprungen und das Programm läuft normal weiter":
    score = score + 1

st.subheader("Wie viele elif-Blöcke kann man in einer verzweigung verwenden?")
antwort9 = st.text_input("Deine Antwort")
if antwort9 == "So viele, wie man möchte"
    score = score + 1

st.subheader("Kann man eine if-Anweisung ohne else schreiben?")
antwort10 = st.radio("Wähle eine Antwort",["JA!","Nein!"])
if antwort10 =="JA!":
    score = score + 1

st.subheader("Was bedeutet != in Python?:")
antwort11 = st.text_input("Deine Antwort")
if antwort11 == "Ungleich":
    score = score + 1

st.subheader("Welcher Code prüft, ob eine Zahl größer als 100 ist?")
antwort12 = st.radio("Wähle eine Antwort",["If zahl >= 100","if zahl == 100","if zahl > 100","if 100 < zahl"])
if antwort12 == "if zahl > 100":
    score = score + 1

st.subheader("Was prüft folgender Code? if x ==10 print x ist gleich 10)"
antwort13 = st.radio("Wähle eine Antwort",["Ob x kleiner als 10 ist","Ob x ungleich 10 ist","Ob x gleich 10 ist","Ob x größer als 10 ist"])
if antwort13 == "Ob x kleiner als 10 ist":
    score = score + 1

st.subheader("Was ist korrekt bei if,elif und else?")
antwort14 = st.radio("Wähle eine Antwort",["Es darf nur if verwendet werden","Jedes if muss ein else haben","Elif kann nur einmal vorkommen","if,elif und else sind optional, aber if is Vorraussetzung"])
if antwort14 == "if,elif und else sind optional, aber if is Vorraussetzung":
    score = score + 1

#Fragen zu Funktionen / Wiederverwendbarkeit

st.subheader("Wie startet man eine Funktion in Python?")
antwort15 = st.text_input("Deine Antwort")
if antwort15 == "def funktion()":
    score = score + 1

st.subheader("Welche Funktion hat zwei Parameter?")
antwort16 = st.radio("Wähle eine Antwort",["def sagen():","def rechnen(a):","def vergleichen(a, b)","def_hallo(nico)"])
if antwort16 == "def vergleichen(a, b):"
    score = score + 1

st.subheader("Was ist eine Funktion in Python?")
antwort17 = st.radio("Wähle eine Antwort",["Eine Schleife,die unendlich oft läuft","Eine Art variabe für Zahlen","Ein wiederverwendbarer Codeblock mit einem Namen","Eine spezielle Art von Kommentar"])
if antwort17 == "Ein wiederverwendbarer Codeblock mit einem Namen":
    score = score + 1

st.subheader("Welche der Zeilen ruft ene Funktion namens begrüßung aus")
antwort18 = st.radio("Wähle eine Antwort",["def begrüßung","call begrüßung","begrüßung()","return begrüßung"])
if antwort18 == "begrüßung()"
    score = score + 1

st.subheader("Was ist der Hauptvorteil von Funktionen?")
antwort19 = st.radio("Wähle eine Antwort",["Sie machen den Code länger","Sie speichern Daten","Sie helfen, den Code wiederzuverweden,"Sie löschen Daten automaitsch"])
if antwort19 == "Sie helfen, den Code wiederzuverweden":
    score = score + 1

st.subheader("Was sind Parameter?")
antwort20 = st.radio("Wähle eine Antwort",["Eine Fehlermeldung","Ein anderer Name für print","Ein Wert, den du einer Funktion übergibst","Der Titel eines Codes"])
if antwort20 == "Ein Wert, den du einer Funktion übergibst"
    score = score + 1

st.subheader("Wie viele Parameter kann eine Funktion haben?")
antwort21 = st.text_input("Deine Antwort")
if antwort21 == "unbegrenzt"
    score = score + 1

#Listen,Tuple,Set & Dictionaries

st.subheader("Wie greifst du auf den Wert im Dictionary zu ?")
antwort22 = st.radio("Wähle eine Antwort",["person.get(alter)","person.alter","person["28"]","person[alter]"])
if antwort22 == "person.get(alter)":
    score = score + 1

st.subheader("Welche Methode entfernt ein Element aus einer Liste")
antwort23 = st.radio("Wähle eine Antwort",[".delete",".remove",".cut",".destroy"])
if antwort23 == ".remove"
    score = score + 1

st.subheader("welche Struktur erlaubt keine doppelten Werte?")
antwort24 = st.radio("Wähle eine Antwort",["List","Tuple","Dictionary","Set"])
if antwort24 == "Set"
    score = score + 1

st.subheader("Wofür ist.append() zuständig?")
antwort25 = st.radio("Wähle eine Antwort",["Einen Wert zu einem Dictionary hinzufügen","Einen Wert am Ende einer Liste hinzufügen","Einen Wert aus einem Set entfernen,"Einen Wert aus einem Tupel entfernen"])
if antwort25 == "Einen Wert am Ende einer Liste hinzuzufügen"
    score = score + 1

st.subheader("Welchen Datentypen sind nicht veränderbar?")
antwort26 = st.radio("Wähle eine Antwort",["List","Tuple","Dictionary","Set"])
if antwort26 == "Tuple"
    score = score + 1

st.markdown("-----")
st.subheader(f"Dein aktueller Punktestand: {score}")


