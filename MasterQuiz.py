
import streamlit as st
score= 0

st.title("Python Quiz-Kapitel 1!")
def berechne_score():
    st.session_state.score = 0

if "score" not in st.session_state:
    st.session_state.score = 0

#Fragen Operatoren
st.subheader("Welcher Operator gibt den ganzzahligen Anteil einer Division zurück?")
antwort1 = st.multiselect("Wähle eine Antwort",["/","//","%","**"],key="antwort1",default=[])
if antwort1 == "/":
    st.session_state.score = score + 1

st.subheader("Welche Aussage ist Falsch?:")
antwort2 = st.multiselect("Wähle eine Antwort",["5<10 ist True","4== 4 ist True","5!=6 ist True","3>=3 ist True"],key="antwort2",default=[])
if antwort2 == "5<10 ist True":
    st.session_state.score = score + 1

st.subheader("Was gibt 2**3 zurück?:")
antwort3 = st.text_input("Deine Antwort",key= "frage3") #jedes Streamlit-Element wie st.txt_input,/st.radio/st.checkbox braucht einen eindeutigen key, wenn du den gleichen text mehrfach verwendest.
if antwort3 == "6":
    st.session_state.score = score + 1

st.subheader("Welche Eingabe ergibt bei int(input(Zahl: + 5 das Ergebnis 15?")
antwort4 = st.multiselect("Wähle eine Antwort",["5","10","fünf"],key="antwort4",default=[])
if antwort4 == "10":
    st.session_state.score = score + 1

st.subheader("Was bewirkt der Operator !=?")
antwort5 = st.multiselect("Wähle eine Antwort",["Er prüft, ob zwei Werte gleich sind","Er prüft, ob zwei Werte unterschiedlich sind","Er gibt den Rest einer Divison wieder","Er wandelt einen String in Integer um"],key="antwort5",default=[])
if antwort5 == "Er prüft ob zwei Werte unterschiedlich sind":
    st.session_state.score = score + 1

st.subheader("Was ergibt bool(0)?:")
antwort6 = st.multiselect("Wähle eine Antwort",["True","False","none","0"],key="antwort6",default=[])
if antwort6 == "False":
    st.session_state.score = score + 1

#Fragen Kontrollstrukturen

st.subheader("Wofür wird eine If-Anweisung verwendet?")
antwort7 = st.text_input("Deine Antwort",key="frage7")
if antwort7 == "Für die wenn dann Logik":
    st.session_state.score = score + 1

st.subheader("Was passiert, wenn die Bedingung in einer if Anweisung nicht erfüllt ist?")
antwort8 = st.multiselect("Wähle eine Antwort",["Der code im if_Block wird trotzdem ausgeführt","Das Programm stürzt sofort ab","Der Code im if-Block wird übersprungen und das Programm läuft normal weiter","Python wählt zufällig einen anderen Block aus, den es stattdessen ausführt"],key="antwort8",default=[])
if antwort8 =="Der Code im if Block wird übersprungen und das Programm läuft normal weiter":
    st.session_state.score = score + 1

st.subheader("Wie viele elif-Blöcke kann man in einer verzweigung verwenden?")
antwort9 = st.text_input("Deine Antwort",key="frage9")
if antwort9 == "So viele, wie man möchte":
    st.session_state.score = score + 1

st.subheader("Kann man eine if-Anweisung ohne else schreiben?")
antwort10 = st.multiselect("Wähle eine Antwort",["JA!","Nein!"],key="antwort10",default=[])
if antwort10 =="JA!":
    st.session_state.score = score + 1

st.subheader("Was bedeutet != in Python?:")
antwort11 = st.text_input("Deine Antwort",key="frage11")
if antwort11 == "Ungleich":
    st.session_state.score = score + 1

st.subheader("Welcher Code prüft, ob eine Zahl größer als 100 ist?")
antwort12 = st.multiselect("Wähle eine Antwort",["If zahl >= 100","if zahl == 100","if zahl > 100","if 100 < zahl"],key="antwort12",default=[])
if antwort12 == "if zahl > 100":
    st.session_state.score = score + 1

st.subheader("Was prüft folgender Code? if x ==10 print x ist gleich 10")
antwort13 = st.multiselect("Wähle eine Antwort",["Ob x kleiner als 10 ist","Ob x ungleich 10 ist","Ob x gleich 10 ist","Ob x größer als 10 ist"],key="antwort13",default=[])
if antwort13 == "Ob x kleiner als 10 ist":
    st.session_state.score = score + 1

st.subheader("Was ist korrekt bei if,elif und else?")
antwort14 = st.multiselect("Wähle eine Antwort",["Es darf nur if verwendet werden","Jedes if muss ein else haben","Elif kann nur einmal vorkommen","if,elif und else sind optional, aber if is Vorraussetzung"],key="antwort14",default=[])
if antwort14 == "if,elif und else sind optional, aber if is Vorraussetzung":
    st.session_state.score = score + 1

#Fragen zu Funktionen / Wiederverwendbarkeit

st.subheader("Wie startet man eine Funktion in Python?")
antwort15 = st.text_input("Deine Antwort",key="frage15")
if antwort15 == "def funktion()":
    st.session_state.score = score + 1

st.subheader("Welche Funktion hat zwei Parameter?")
antwort16 = st.multiselect("Wähle eine Antwort",["def sagen():","def rechnen(a):","def vergleichen(a, b)","def_hallo(nico)"],key="antwort16",default=[])
if antwort16 == "def vergleichen(a, b)":
    st.session_state.score = score + 1

st.subheader("Was ist eine Funktion in Python?")
antwort17 = st.multiselect("Wähle eine Antwort",["Eine Schleife,die unendlich oft läuft","Eine Art variabe für Zahlen","Ein wiederverwendbarer Codeblock mit einem Namen","Eine spezielle Art von Kommentar"],key="antwort17",default=[])
if antwort17 == "Ein wiederverwendbarer Codeblock mit einem Namen":
    st.session_state.score = score + 1

st.subheader("Welche der Zeilen ruft ene Funktion namens begrüßung aus")
antwort18 = st.multiselect("Wähle eine Antwort",["def begrüßung","call begrüßung","begrüßung()","return begrüßung"],key="antwort18",default=[])
if antwort18 == "begrüßung()":
    st.session_state.score = score + 1

st.subheader("Was ist der Hauptvorteil von Funktionen?")
antwort19 = st.multiselect("Wähle eine Antwort",["Sie machen den Code länger","Sie speichern Daten","Sie helfen, den Code wiederzuverweden"],key="antwort19",default=[])
if antwort19 == "Sie helfen, den Code wiederzuverweden":
    st.session_state.score = score + 1

st.subheader("Was sind Parameter?")
antwort20 = st.multiselect("Wähle eine Antwort",["Eine Fehlermeldung","Ein anderer Name für print","Ein Wert, den du einer Funktion übergibst","Der Titel eines Codes"],key="antwort20",default=[])
if antwort20 == "Ein Wert, den du einer Funktion übergibst":
    st.session_state.score = score + 1

st.subheader("Wie viele Parameter kann eine Funktion haben?")
antwort21 = st.text_input("Deine Antwort",key="frage21")
if antwort21 == "unbegrenzt":
    st.session_state.score = score + 1

#Listen,Tuple,Set & Dictionaries

st.subheader("Wie greifst du auf den Wert im Dictionary zu ?")
antwort22 = st.multiselect("Wähle eine Antwort",["person.get(alter)","person.alter","person[alter]"],key="antwort22",default=[])
if antwort22 == "person.get(alter)":
    st.session_state.score = score + 1

st.subheader("Welche Methode entfernt ein Element aus einer Liste")
antwort23 = st.multiselect("Wähle eine Antwort",[".delete",".remove",".cut",".destroy"],key="antwort23",default=[])
if antwort23 == ".remove":
    st.session_state.score = score + 1

st.subheader("welche Struktur erlaubt keine doppelten Werte?")
antwort24 = st.multiselect("Wähle eine Antwort",["List","Tuple","Dictionary","Set"],key="antwort24",default=[])
if antwort24 == "Set":
    st.session_state.score = score + 1

st.subheader("Wofür ist.append() zuständig?")
antwort25 = st.multiselect("Wähle eine Antwort",["Einen Wert zu einem Dictionary hinzufügen","Einen Wert am Ende einer Liste hinzufügen","Einen Wert aus einem Set entfernen", "Einen Wert aus einem Tupel entfernen"],key="antwort25",default=[])
if antwort25 == "Einen Wert am Ende einer Liste hinzuzufügen":
    st.session_state.score = score + 1

st.subheader("Welchen Datentypen sind nicht veränderbar?")
antwort26 = st.multiselect("Wähle eine Antwort",["List","Tuple","Dictionary","Set"],key="antwort26",default=[])
if antwort26 == "Tuple":
    st.session_state.score = score + 1






if st.button("Punkte anzeigen"):
    st.session_state.score = berechne_score()
st.markdown("-----")
st.subheader(f"Dein aktueller Punktestand: {st.session_state.score}")


