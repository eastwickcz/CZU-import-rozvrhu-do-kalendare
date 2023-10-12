# Školní Rozvrh do Kalendáře


Tento skript vytvoří kalendářní soubor ze školního rozvrhu, který lze snadno importovat do kalendářových aplikací.


Ukázkové soubory `export.xlsx` a `rozvrh.ics` jsou poskytnuty k tomu, aby ukázaly, jak by měl vypadat vstupní soubor `export.xlsx` a výsledný soubor `rozvrh.ics`.


## Jak to funguje


Pro úspěšné použití tohoto skriptu je třeba mít následující:


1. **Export Rozvrhu**: Musíte exportovat rozvrh ze školního systému do formátu XLSX a uložit jej v adresáři, kde je umístěn tento skript. Soubor musí nést název `export.xlsx`.


2. **Python**: Skript je napsán v Pythonu, takže budete potřebovat Python nainstalovaný na svém počítači. Stáhnout si ho můžete z [python.org](https://www.python.org/).


## Jak používat tento skript


1. Stáhněte si tento repozitář na svůj počítač.


2. Exportujte svůj školní rozvrh do souboru `export.xlsx` a uložte ho do adresáře s tímto skriptem.


3. Otevřete příkazový řádek (terminál) a přejděte do adresáře, kde je uložen tento skript.


4. Nainstalujte potřebné závislosti pomocí pip:


   ```bash

   pip install -r requirements.txt

Spusťte skript následujícím příkazem:


bash

Copy code

python3 rozvrh.py

Skript vytvoří soubor s názvem rozvrh.ics, který obsahuje kalendářní události z vašeho rozvrhu.


Importujte soubor rozvrh.ics do své oblíbené kalendářové aplikace.


Poznámky

Skript je určen pro exporty rozvrhu ve formátu XLSX. Ostatní formáty nemusí být podporovány.


Kalendářní soubor rozvrh.ics lze importovat do různých kalendářových aplikací, jako je Google Kalendář, Outlook, Apple Kalendář a další.


Tento skript byl vytvořen za účelem zjednodušení procesu převodu školního rozvrhu do kalendářového formátu. Pokud narazíte na problémy nebo máte nápady na vylepšení, prosím, otevřete problém v tomto repozitáři.


Licence

Tento projekt je licencován pod licencí MIT.


Autor: Lukáš Hájek (aka eastwickcz)


# English version

# School Schedule to Calendar


This script creates a calendar file from your school schedule that can be easily imported into calendar applications.


Sample files `export.xlsx` and `schedule.ics` are provided to demonstrate what the input file `export.xlsx` should look like and the resulting `schedule.ics`.


## How it Works


To successfully use this script, you will need the following:


1. **Export Your Schedule**: You need to export your schedule from your school system in XLSX format and save it in the same directory as this script. The file must be named `export.xlsx`.


2. **Python**: The script is written in Python, so you'll need Python installed on your computer. You can download it from [python.org](https://www.python.org/).


## How to Use This Script


1. Download this repository to your computer.


2. Export your school schedule to a file named `export.xlsx` and save it in the directory with this script.


3. Open the command line (terminal) and navigate to the directory where this script is located.


4. Install the required dependencies using pip:


   ```bash

   pip install -r requirements.txt

Run the script with the following command:


bash

Copy code

python3 schedule.py

The script will create a file named schedule.ics that contains calendar events from your schedule.


Import the schedule.ics file into your favorite calendar application.


Notes

The script is designed for XLSX schedule exports. Other formats may not be supported.


The calendar file schedule.ics can be imported into various calendar applications such as Google Calendar, Outlook, Apple Calendar, and more.


This script was created to simplify the process of converting your school schedule into a calendar format. If you encounter any issues or have ideas for improvements, please open an issue in this repository.


License

This project is licensed under the MIT License.


Author: Lukáš Hájek (aka eastwickcz)
