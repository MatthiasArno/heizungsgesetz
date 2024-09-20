import csv

def read_csv(file:str, delimiter:str=",", units:dict={}) -> list[dict]:
    """Lese csv file in ein dictionary

    Args:
        file (str): Dateiname
        delimiter (str, optional): Spaltentrenner, ',' oder ';'
        units (dict, optional): Ein Dictionary aus Überschrift:Einheit, mit Einheit 'i' oder'f'. Default ist string.

    Returns:
        dict: Pro Zeile ein Dictionary mit den (typisierten) Spalten
    """
    items=list()
    with open(file, "r") as tsv_file:
        tsv_reader = csv.reader(tsv_file, delimiter=delimiter, skipinitialspace=True)
        headers=next(tsv_reader)
        for row in tsv_reader: 
            if not row:
                continue    
            row_dict = {headers[i]: value for i, value in enumerate(row)}
            for h,v in row_dict.items():
                t=units.get(h)
                if t=="i":
                    row_dict[h]=int(v)
                elif t=="f":
                    row_dict[h]=float(v)
                else:
                    pass # type remains string
            items.append(row_dict)
        return items


def get_heater_types(heaters:list[dict]) -> set[str]:
    """ Reduziere die Liste der verbauten Heizkörper auf deren Hersteller, Typ und Höhe.
        Die Leistungsabgabe ergibt sich dann aus den Datenblättern durch Multiplikation mit der Breite.
    Args:
        heaters (list[dict]): Liste von Heizkörpertypen

    Returns:
        _type_: Ein set in aus: Hersteller.Serie.Type.Hoehe
    """
    
    try:
        vsthb=set()
        for h in heaters:        
            vsthb.add(f'{h["Hersteller"]}.{h["Serie"]}.{h["Typ"]}.{h["H"]}')
    except Exception as e:
        print(f"Exception: {h}, {e}")
    return vsthb


