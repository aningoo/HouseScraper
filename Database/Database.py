import sqlite3

# static fields
from datetime import datetime

database_extension = ".db"
database_directory = "backend/"

# parameters
database_name = "houses"


# https://inloop.github.io/sqlite-viewer/


def create_database():
    database = sqlite3.connect("../Database/" + database_directory + database_name + database_extension)
    cursor = database.cursor()
    cursor.execute("""
        CREATE TABLE house(
            straat text,
            postcode text,
            plaats text,
            bouwjaar text,
            woon_oppervlakte text,
            perceel_oppervlakte text,
            prijs text,
            date text)
    """)


def insert(house_information):
    database = sqlite3.connect("../Database/" + database_directory + database_name + database_extension)
    cursor = database.cursor()
    value_string_to_insert = convert_list_to_string(house_information)
    print(value_string_to_insert)
    cursor.execute(
        'INSERT INTO house (straat, postcode, plaats, bouwjaar, woon_oppervlakte, perceel_oppervlakte, prijs, date) '
        'VALUES(' + value_string_to_insert + ')')
    database.commit()
    database.close()


def prep(string):
    return '"' + string + '"' + ','


def convert_list_to_string(house_information):
    string_value = ""
    for value in house_information:
        string_value = string_value + prep(value.strip())
    return string_value[:-1]
