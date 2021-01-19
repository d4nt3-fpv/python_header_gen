


print("Okay erst mal nen paar fragen...")
autor_name = input("Wie ist dein Name?: ")
project_name = input("Wie heißt das Projekt?: ")
version_number = str(input("Welche Version?: "))
project_date = input("Projektdatum: ")
pr_or_cmment = input("print or comment?: ")      # Chose print or comment...
file_or_not = input("Soll das Resultat in eine Datei geschrieben werden?: (y/n)")

if file_or_not == "y":
    filename = input("Wie soll die Datei heißen? ")


if pr_or_cmment == "print":
    befehl = "print('"
    abschluss = "')"
else:
    befehl = "# "
    abschluss = ""


umrandung_oben_unten = "="
zeichen = " "
laenge_autor = len(autor_name)  # Die Laenge des Autor strings
laenge_Block = 40       # Die Laenge der gesammten striche
laenge_createdby = 12   # Die Laenge des Create by logos
laenge_version = 9# Die Laenge des Version Logos
laenge_project_name = len(project_name) # Die Laenge des strings mit dem Projektnamen
laenge_version_number = len(version_number)
laenge_project_date = len(project_date)
cb_laenge_seiten = round((laenge_Block-laenge_createdby-laenge_autor)/2) # Formel für das Automatische zentrieren
pn_laenge_seiten = round((laenge_Block-laenge_project_name)/2)  # Formel für das Automatische zentrieren
vn_laenge_seiten = round((laenge_Block-laenge_version_number-laenge_version)/2)  # Formel für das Automatische zentrieren
pd_laenge_seiten = round((laenge_Block-laenge_project_date)/2)  # Formel für das Automatische zentrieren


print(befehl + umrandung_oben_unten*laenge_Block + abschluss)  # Obere Strichreihe
print(befehl + zeichen*pn_laenge_seiten + project_name + zeichen*pn_laenge_seiten + abschluss)
print(befehl + zeichen*vn_laenge_seiten + "Version: " + version_number + zeichen*vn_laenge_seiten + abschluss)
print(befehl + zeichen*cb_laenge_seiten + "Created by: " + autor_name + zeichen*cb_laenge_seiten + abschluss)
print(befehl + zeichen*pd_laenge_seiten + project_date + zeichen*pd_laenge_seiten + abschluss)
print(befehl + umrandung_oben_unten*laenge_Block + abschluss)  # untere Strichreihe


if file_or_not == "y":
    with open(filename, "w") as f:
        f.write(befehl + umrandung_oben_unten*laenge_Block + abschluss + "\n")  # Obere Strichreihe
        f.write(befehl + zeichen*pn_laenge_seiten + project_name + zeichen*pn_laenge_seiten + abschluss + "\n")
        f.write(befehl + zeichen*vn_laenge_seiten + "Version: " + version_number + zeichen*vn_laenge_seiten + abschluss + "\n")
        f.write(befehl + zeichen*cb_laenge_seiten + "Created by: " + autor_name + zeichen*cb_laenge_seiten + abschluss + "\n")
        f.write(befehl + zeichen*pd_laenge_seiten + project_date + zeichen*pd_laenge_seiten + abschluss + "\n")
        f.write(befehl + umrandung_oben_unten*laenge_Block + abschluss + "\n")  # untere Strichreihe

else:
    quit()

    


# Hinweis:  Die kleinen schönheitsfeher liegen bei derm runden der Zahlen.


