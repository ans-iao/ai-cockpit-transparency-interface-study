# AI-Cockpit: Transparency Interface Study

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Marker System](#marker-system)
- [Scenarios](#scenarios)

## Overview

This project studies transparency interfaces for AI systems through eye tracking analysis. It examines user interaction
and understanding of different AI transparency elements across various application scenarios.

## Installation

#### 1. Install required dependencies

    pip install -r requirements.txt

#### 2. Configure eye tracking hardware

This project uses the eyelogic logic one eye-tracker. The LSL client is therefore
needed: https://www.eyelogicsolutions.com/downloads/

However, any eye-tracker will do as long as the data is transmitted via LSL https://labstreaminglayer.org/#/
In the `config.py` file, you need to change the `lsl_name` variable to your eye-tracker LSL stream name.

#### 3. Run the application

Start the `main.py` script to run the application.

    python main.py

#### 4. Optional: Run Eye-Tracker Visualization

Start the `vis_eye_tracker.py` script to visualize the eye-tracker LSL stream in real-life. Serves as a sanity check,
whether the data is obtained by LSL. If you can see the data in the visualization window, the internal recorder will
also see it.

## Data acquisition

On default, this app saves the data in a `data` folder of this root directory. The folder can be adjusted in the
`config.py` file by replacing the `save_dir` variable. The markers are saved in with eye-tracker data (usually the last
column).

## Marker System

### Eye Tracker Views

- **0: MainView** - Primary interface view
- **1: QuestionView** - User questionnaire interface
- **2: Plaintext** - Text display view
- **3: ControlQuestionView** - Control questions interface
- **4: EndView** - Study completion view

### Marker Types

    # TI-Text marker
    [scenario][ti_type][level/page]
    => 111 (a, system_goal, page 1)
    => 532 (e, data, page 2)

### Scenario Names

    scenario = {
        'a': "1",
        'b': "2",
        'c': "3",
        'd': "4",
        'e': "5",
        'f': "6"
    }
    a = KI-basiertes Job-Matching-System
    b = Gesundheitskurse und Sonferleistungen durch eine Krankenkasse
    c = Überprüfung von Fotos auf sozialen Netzwerken
    d = Videoplattformen
    e = Supermarkt Bonussystem
    f = Firmeninternes Business Intelligence und Analytics Tool

# Contribution

This study is a collaborative effort between:

- Hochschule Aalen - University of Applied Sciences
- Institute of Human Factors and Technology Management (IAT), University of Stuttgart

This publication is a result of the "KI-Cockpit" research project and was funded by the Directorate-General „Policy Lab
Digital, Work \& Society“ at the Federal Ministry of Labour and Social Affairs. The contents of this publication are
solely the responsibility of the authors. https://www.kicockpit.eu/

# License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details


