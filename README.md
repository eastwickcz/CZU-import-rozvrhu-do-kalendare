# Školní Rozvrh do Kalendáře


Tento skript vytvoří kalendářní soubor ze školního rozvrhu, který lze snadno importovat do kalendářových aplikací.

Soubory `export.xlsx` a `rozvrh.ics` jsou pouze příkladové soubory, jak má vypadat vstupní soubor `export.xlsx` a výsledný `rozvrh.ics`


## Jak to funguje


Pro úspěšné použití tohoto skriptu je třeba mít následující:


1. **Export Rozvrhu**: Musíte exportovat rozvrh ze školního systému do formátu XLSX a uložit jej v adresáři, kde je umístěn tento skript. Tento soubor musí nést název `export.xlsx`.


2. **Python**: Skript je napsán v Pythonu, takže budete potřebovat Python na svém počítači. Můžete si ho stáhnout z [python.org](https://www.python.org/).


## Jak používat tento skript


1. Stáhněte si tento repozitář na svůj počítač.


2. Exportujte svůj školní rozvrh do souboru `export.xlsx` a uložte ho do adresáře s tímto skriptem.


3. Otevřete příkazový řádek (terminal) a přejděte do adresáře, kde je uložen tento skript.


4. Spusťte skript pomocí následujícího příkazu:


   python3 rozvrh.py

Skript vytvoří soubor s názvem rozvrh.ics, který obsahuje kalendářní události z vašeho rozvrhu.


Importujte soubor rozvrh.ics do své oblíbené kalendářové aplikace.


Poznámky

Skript je určený pro exporty rozvrhu v XLSX formátu. Ostatní formáty nemusí být podporovány.


Kalendářní soubor rozvrh.ics může být importován do různých kalendářových aplikací, jako jsou Google Kalendář, Outlook, Apple Kalendář a další.


Tento skript byl vytvořen za účelem zjednodušení procesu převodu školního rozvrhu do kalendářového formátu. Pokud narazíte na problémy nebo máte nápady na vylepšení, prosím, otevřete problém v tomto repozitáři.


Licence

Tento projekt je licencován pod MIT licencí.


Autor: Lukáš Hájek aka eastwickcz
