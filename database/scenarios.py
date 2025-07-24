scenarios = {
    "Header": "<b>Bitte nehmen Sie sich etwas Zeit, um sich so gut wie möglich in die folgende Situation zu "
              "versetzen:</b>",
    "Desc": "Es folgen nun die Informationen über die allgemeine Arbeitsweise des Systems auf der Webseite des "
            "Anbieters. Diese sind anhand der vier übergreifenden Kategorien Ziele, Art des System, verwendete Daten "
            "und Kontrolloptionen dargestellt. <br><br>Bitte lesen Sie sich die Texte aufmerksam durch, da es hier um Ihre "
            "Wahrnehmung der Informationstexte geht. Im Anschluss folgen Verständnisfragen zu den Texten.",
    "a": {
        "Title": "KI-basiertes Job-Matching-System",
        "Operator": "Sie arbeiten im Personalwesen und bekommen die Aufgabe zugewiesen, über den Einsatz eines "
                    "KI-basierten Job-Matching Systems zu entscheiden und dieses in seiner Funktionsweise zu "
                    "überwachen. Das Job-Matching-System dient dazu, den offenen Stellen bestmöglich die geeignetsten "
                    "Bewerber:innen zuzuordnen. Hierbei ist es insbesondere wichtig, dass das System faire "
                    "Entscheidungen trifft. Der Algorithmus der Zuordnung („Job-Matching“) ist dabei KI-basiert.",

        "User": "Sie suchen einen neuen Job, weil Sie in Ihrer aktuellen Position unzufrieden sind. Ihr Ziel ist es, "
                "eine neue Stelle zu finden, die perfekt zu Ihnen passt. Ein Bekannter empfiehlt Ihnen eine "
                "Job-Matching-Plattform, die mithilfe von KI ihre Wünsche sowie Kompetenzen analysiert und passende "
                "Stellenangebote zuordnet. Sie stehen nun vor der Entscheidung, ob Sie dieses Systems nutzen möchten "
                "oder nicht.",
        "Text": {
            "system_goal": {
                "Files": ["database/ti_png/a_system_goal_1.png", "database/ti_png/a_system_goal_2.png",
                          "database/ti_png/a_system_goal_3.png"]
            },
            "system_type": {
                "Files": ["database/ti_png/a_system_type_1.png", "database/ti_png/a_system_type_2.png",
                          "database/ti_png/a_system_type_3.png"]
            },
            "data": {
                "Files": ["database/ti_png/a_data_1.png", "database/ti_png/a_data_2.png",
                          "database/ti_png/a_data_3.png"]
            },
            "control": {
                "Files": ["database/ti_png/a_control_1.png", "database/ti_png/a_control_2.png",
                          "database/ti_png/a_control_3.png"]
            }
        },
        "Question": "<b>Was ist das Ziel des soeben beschriebenen KI-Systems und mit welchen Daten arbeitet es?</b>",
        "Answers": [
            ("0",
             "Mit Hilfe von Nutzer:innen bereitgestellten und automatisch generierten Daten die richtige Übereinstimmung zwischen Bewerber:innen und Stellenanbieter:innen zu gewährleisten."),
            ("1",
             "Mit Hilfe von öffentlichen Quellen Nutzer:innen bei der Wahl der besten Online-Plattform zu unterstützen."),
            ("2",
             "Mit Hilfe von öffentlichen Quellen Nutzer:innen bei der Erstellung von Bewerbungsunterlagen zu helfen.")
        ]
    },
    "b": {
        "Title": "Gesundheitskurse und Sonderleistungen durch eine Krankenkasse",
        "Operator": "Sie arbeiten bei einer Krankenkasse und bekommen die Aufgabe zugewiesen, über den Einsatz eines "
                    "KI-basierten Systems zu entscheiden, das Bewegungs- und Schlafprofile der "
                    "Versicherungsnehmer:innen auf gesundheitliche Risiken bewertet. Darüber hinaus haben Sie die "
                    "Aufgabe dieses System in seiner Funktionsweise zu überwachen. Dabei ist es besonders wichtig, "
                    "dass das System faire Entscheidungen trifft. Für diese Aufgabe steht Ihnen eine spezielle "
                    "Software zur Verfügung, mit der Sie die Funktionsweise des Systems kontrollieren.",

        "User": "Sie haben Ihre Krankenkasse gewechselt, da Sie mit Ihrer alten Krankenkasse unzufrieden waren. "
                "Die neue Krankenkasse bietet Ihnen ein KI-basiertes System an. Es bewertet Bewegungs- und "
                "Schlafprofile auf gesundheitliche Risiken, weist Ihnen maßgeschneiderte Gesundheitskurse zu und "
                "ermöglicht die Teilnahme an einem Bonusprogramm, das gesundheitsförderndes Verhalten  belohnt. Sie "
                "stehen nun vor der Entscheidung, der Nutzung dieses Systems zuzustimmen oder diese abzulehnen.",
        "Text": {
            "system_goal": {
                "Files": ["database/ti_png/b_system_goal_1.png", "database/ti_png/b_system_goal_2.png",
                          "database/ti_png/b_system_goal_3.png"]
            },
            "system_type": {
                "Files": ["database/ti_png/b_system_type_1.png", "database/ti_png/b_system_type_2.png",
                          "database/ti_png/b_system_type_3.png"]
            },
            "data": {
                "Files": ["database/ti_png/b_data_1.png", "database/ti_png/b_data_2.png",
                          "database/ti_png/b_data_3.png"]
            },
            "control": {
                "Files": ["database/ti_png/b_control_1.png", "database/ti_png/b_control_2.png",
                          "database/ti_png/b_control_3.png"]
            }
        },
        "Question": "<b>Mit welchen Daten arbeitet das soeben beschriebene KI-System und wie wird dessen Arbeit kontrolliert?</b>",
        "Answers": [
            ("0",
             "Durch regelmäßige Überprüfung aller KI-Prozesse auf Unstimmigkeiten wird das System, welches mit Orts- und Bewegungsdaten der Nutzer:innen arbeitet, bestenfalls kontrolliert."),
            ("1",
             "Das System arbeitet mit persönlichen Nachrichten von Nutzer:innen und muss deshalb nur durch zufällige Stichproben kontrolliert werden."),
            ("2",
             "Das System arbeitet mit persönlichen Nachrichten von Nutzer:innen, weshalb eine manuelle Überprüfung jedes einzelnen Datensatzes zur Kontrolle erforderlich ist. ")
        ]
    },
    "c": {
        "Title": "Überprüfung von Fotos auf sozialen Netzwerken",
        "Operator": "Sie arbeiten bei einem Software-Unternehmen, das ein soziales Netzwerk betreibt. Ihre Aufgabe "
                    "ist es, darüber zu entscheiden, ob ein KI-basiertes System zur Überprüfung von hochgeladenen "
                    "Fotos genutzt wird und dieses System zu überwachen. Dieses System prüft die Fotos auf die "
                    "Einhaltung der Nutzungsrichtlinien. Für Ihre Aufgabe bekommen Sie eine Software zur Verfügung "
                    "gestellt.",

        "User": "Ihre Bekannten nutzen begeistert ein neues soziales Netzwerk und möchten, dass Sie auch beitreten, "
                "um gemeinsame Fotos auszutauschen. Sie haben noch wenig Erfahrung mit sozialen Medien und haben "
                "herausgefunden, dass die Plattform ein KI-System zur Überprüfung von Fotos auf unerlaubte "
                "Inhalte verwendet. Sie stehen nun vor der Entscheidung der Nutzung dieses Systems zuzustimmen oder "
                "diese abzulehnen.",

        "Text": {
            "system_goal": {
                "Files": ["database/ti_png/c_system_goal_1.png", "database/ti_png/c_system_goal_2.png",
                          "database/ti_png/c_system_goal_3.png"]
            },
            "system_type": {
                "Files": ["database/ti_png/c_system_type_1.png", "database/ti_png/c_system_type_2.png",
                          "database/ti_png/c_system_type_3.png"]
            },
            "data": {
                "Files": ["database/ti_png/c_data_1.png", "database/ti_png/c_data_2.png",
                          "database/ti_png/c_data_3.png"]
            },
            "control": {
                "Files": ["database/ti_png/c_control_1.png", "database/ti_png/c_control_2.png",
                          "database/ti_png/c_control_3.png"]
            }
        },
        "Question": "<b>Was ist das Ziel des soeben beschriebenen KI-Systems und wie sollte es bestenfalls kontrolliert werden?</b>",
        "Answers": [
            ("0",
             "Eine sichere und angenehme Online-Umgebung zu schaffen. Die Kontrolle sollte durch regelmäßige Überprüfungen und Anpassungen bei Auffälligkeiten des Systems erfolgen."),
            ("1",
             "Die Optimierung der Werbung für soziale Netzwerke. Zur Kontrolle sollten zur Sicherheit alle Inhalte gelöscht werden."),
            ("2",
             "Die Optimierung der Werbung für soziale Netzwerke. Die Kontrolle sollte durch ständige manuelle Eingaben erfolgen.")
        ]
    },
    "d": {
        "Title": "Videoplattform",
        "Operator": "Sie arbeiten bei einer Videoplattform und sollen darüber entscheiden, ob ein KI-basiertes System "
                    "zum Einsatz kommt, das personalisierte Werbeanzeigen zuweist. Sie sollen dieses System außerdem "
                    "im Betrieb überwachen. Dabei ist es besonders wichtig, dass das System relevante Werbung für die "
                    "Nutzenden anzeigt. Zur Unterstützung Ihrer Aufgabe steht Ihnen eine spezielle Software zur "
                    "Verfügung.",

        "User": "Sie möchten sich bei einer Videoplattform anmelden, da Sie das Programm und die Werbung im "
                "„klassischen“ Fernsehen als uninteressant empfinden. Das KI-System der Videoplattform "
                "weist Ihnen personalisierte Werbungen zu, die genau Ihren Vorlieben und Interessen "
                "entsprechen. Sie stehen nun vor der Entscheidung, ob sie bei dieser Plattform einen Account anlegen "
                "wollen oder nicht.",

        "Text": {
            "system_goal": {
                "Files": ["database/ti_png/d_system_goal_1.png", "database/ti_png/d_system_goal_2.png",
                          "database/ti_png/d_system_goal_3.png"]
            },
            "system_type": {
                "Files": ["database/ti_png/d_system_type_1.png", "database/ti_png/d_system_type_2.png",
                          "database/ti_png/d_system_type_3.png"]
            },
            "data": {
                "Files": ["database/ti_png/d_data_1.png", "database/ti_png/d_data_2.png",
                          "database/ti_png/d_data_3.png"]
            },
            "control": {
                "Files": ["database/ti_png/d_control_1.png", "database/ti_png/d_control_2.png",
                          "database/ti_png/d_control_3.png"]
            }
        },
        "Question": "<b>Was ist das Ziel des soeben beschriebenen KI-Systems und mit welchen Daten arbeitet es?</b>",
        "Answers": [
            ("0",
             "Mit Hilfe von Daten, die beim Surfen auf der Videoplattform generiert werden, Nutzer:innen relevante Anzeigen basierend auf ihren Interessen zu zeigen."),
            ("1",
             "Mit Hilfe von gekauften Produkten der Nutzer:innen die Anzahl der Werbeanzeigen auf der Plattform zu reduzieren."),
            ("2",
             "Mit Hilfe von gekauften Produkten der Nutzer:innen die Ladegeschwindigkeit von Anzeigen zu verbessern.")
        ]
    },
    "e": {
        "Title": "Supermarkt Bonussystem",
        "Operator": "Sie arbeiten in einem Einzelhandelsunternehmen und sollen über den Einsatz eines KI-basierten "
                    "Bonussystems entscheiden und dieses überwachen. Dabei ist es wichtig, dass das System "
                    "maßgeschneiderte Belohnungen für die Kund:innen bietet, um deren Interaktion und Bindung zu "
                    "stärken. Für Ihre Überwachungsaufgabe steht Ihnen eine spezielle Software zur Verfügung. ",

        "User": "Sie sind umgezogen und haben einen neuen Supermarkt neben Ihrer Wohnung. "
                "Bekannte empfehlen Ihnen für dieses Geschäft ein Bonussystem, das Ihnen für Einkäufe Punkte gibt, "
                "die Sie gegen "
                "Gutscheine oder Aktionen einlösen können. Das KI-System schlägt Ihnen personalisierte Rabatte und "
                "Prämien vor, die Ihren Vorlieben entsprechen. Sie stehen nun vor der Entscheidung der Nutzung dieses "
                "Systems zuzustimmen oder dieses abzulehnen.",

        "Text": {
            "system_goal": {
                "Files": ["database/ti_png/e_system_goal_1.png", "database/ti_png/e_system_goal_2.png",
                          "database/ti_png/e_system_goal_3.png"]
            },
            "system_type": {
                "Files": ["database/ti_png/e_system_type_1.png", "database/ti_png/e_system_type_2.png",
                          "database/ti_png/e_system_type_3.png"]
            },
            "data": {
                "Files": ["database/ti_png/e_data_1.png", "database/ti_png/e_data_2.png",
                          "database/ti_png/e_data_3.png"]
            },
            "control": {
                "Files": ["database/ti_png/e_control_1.png", "database/ti_png/e_control_2.png",
                          "database/ti_png/e_control_3.png"]
            }
        },
        "Question": "<b>Für was werden Nutzer:innen bei jedem Einkauf belohnt und welche Art von Daten werden gesammelt?</b>",
        "Answers": [
            ("0",
             "Die Nutzer:innen werden für das Punktesammeln bei jedem Einkauf belohnt und gleichzeitig sammelt das System Anmeldedaten und Einkaufsverhalten."),
            ("1",
             "Die Nutzer:innen werden für das Ansehen von Werbevideos belohnt und das System sammelt persönliche Nachrichten und Anruflisten."),
            ("2",
             "Die Nutzer:innen werden für das Punktesammeln bei einem Einkauf ab 60€ belohnt und das System sammelt allgemeine demografische Daten.")
        ]
    },
    "f": {
        "Title": "Firmeninternes Business Intelligence und Analytics Tool",
        "Operator": "Sie arbeiten in einem Unternehmen und sollen über den Einsatz eines KI-basierten Systems zur "
                    "Erstellung von Geschäftsanalysen entscheiden und dieses in seiner Funktionsweise überwachen. "
                    "Dieses System ist entscheidend für präzise Analysen und Prognosen. Es ist wichtig, "
                    "dass das System zuverlässig und nachvollziehbar arbeitet. Für Ihre Aufgabe steht Ihnen eine "
                    "spezielle Überwachungssoftware zur Verfügung.",

        "User": "Sie sind in einem mittelgroßen Unternehmen beschäftigt und "
                "sollen verschiedene Unternehmensdaten analysieren und Geschäftsprognosen erstellen. Dafür steht "
                "Ihnen ein firmeninternes, KI-basiertes System zur Verfügung. Dieses System erkennt Muster und Trends "
                "in den bereitgestellten Daten und erstellt Berichte sowie Schaubilder. Sie stehen nun vor der "
                "Entscheidung der Nutzung dieses Systems zuzustimmen oder abzulehnen.",

        "Text": {
            "system_goal": {
                "Files": ["database/ti_png/f_system_goal_1.png", "database/ti_png/f_system_goal_2.png",
                          "database/ti_png/f_system_goal_3.png"]
            },
            "system_type": {
                "Files": ["database/ti_png/f_system_type_1.png", "database/ti_png/f_system_type_2.png",
                          "database/ti_png/f_system_type_3.png"]
            },
            "data": {
                "Files": ["database/ti_png/f_data_1.png", "database/ti_png/f_data_2.png",
                          "database/ti_png/f_data_3.png"]
            },
            "control": {
                "Files": ["database/ti_png/f_control_1.png", "database/ti_png/f_control_2.png",
                          "database/ti_png/f_control_3.png"]
            }
        },
        "Question": "<b>Was ist das Ziel des soeben beschriebenen KI-Systems und wie unterstützt es das Fachpersonal?</b>",
        "Answers": [
            ("0", "Geschäftsprognosen erstellen, indem es Muster und Trends erkennt. Dabei unterstützt es das Fachpersonal durch umfassende Kontrollmöglichkeiten zur Sicherstellung von Transparenz und Sicherheit."),
            ("1", "Unorganisierte Unternehmensdaten zu löschen. Dabei unterstützt es das Fachpersonal durch automatische Korrekturen ohne menschliche Eingriffe."),
            ("2", "Nur strukturierte Unternehmensdaten zu sammeln. Dabei unterstützt es das Fachpersonal durch automatische Korrekturen ohne menschliche Eingriffe.")
        ]
    }
}
