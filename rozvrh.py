import openpyxl

from datetime import datetime


# Nahraďte následující proměnné svými vlastními údaji

EXCEL_FILE = 'export.xlsx'

OUTPUT_ICS_FILE = 'rozvrh.ics'


# Načtení Excel souboru

workbook = openpyxl.load_workbook(EXCEL_FILE)

sheet = workbook.active


# Vytvoření prázdného ICS souboru

ics_file = open(OUTPUT_ICS_FILE, 'w')


# Název kalendáře

ics_file.write("BEGIN:VCALENDAR\n")

ics_file.write("VERSION:2.0\n")

ics_file.write("PRODID:-//Example Corp.//My Product//EN\n")


# Slovník pro převod dvoupísmenných zkratka dnů v týdnu na třípísmenné

den_v_tydnu_zkratka = {

    'Po': 'Mon',

    'Út': 'Tue',

    'St': 'Wed',

    'Čt': 'Thu',

    'Pá': 'Fri',

    'So': 'Sat',

    'Ne': 'Sun'

}


# Procházíme řádky v Excel souboru a vytváříme události v ICS formátu

for row in sheet.iter_rows(min_row=2, values_only=True):

    datum_str = row[0]

    cas_od_str = row[1]

    cas_do_str = row[2]

    nazev_predmetu = row[3]

    popis = f"{row[4]}\n{row[5]}\n{row[6]}"


    # Převod dvoupísmenného zkratky na třípísmennou pro den v týdnu

    den_v_tydnu = den_v_tydnu_zkratka.get(datum_str[:2], '')


    # Převod řetězců na objekty datetime

    datum_str = datum_str.replace(datum_str[:2], den_v_tydnu)  # Nahradíme zkratku dnů

    datum = datetime.strptime(datum_str, '%a %d.%m.%Y')

    cas_od = datetime.strptime(cas_od_str, '%H:%M')

    cas_do = datetime.strptime(cas_do_str, '%H:%M')


    # Vytvoření události v ICS formátu s časy

    ics_file.write("BEGIN:VEVENT\n")

    ics_file.write(f"DTSTART;VALUE=DATE-TIME:{datum.strftime('%Y%m%d')}T{cas_od.strftime('%H%M%S')}\n")

    ics_file.write(f"DTEND;VALUE=DATE-TIME:{datum.strftime('%Y%m%d')}T{cas_do.strftime('%H%M%S')}\n")

    ics_file.write(f"SUMMARY:{nazev_predmetu}\n")

    ics_file.write(f"DESCRIPTION:{popis}\n")

    ics_file.write("END:VEVENT\n")


# Ukončení kalendáře

ics_file.write("END:VCALENDAR\n")

ics_file.close()


print(f"Soubor {OUTPUT_ICS_FILE} byl vytvořen pro import do kalendáře.")
