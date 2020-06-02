def sanitize(house_information):
    house_information[4] = house_information[4].replace("m²", "").strip()
    house_information[5] = house_information[5].replace("m²", "").strip()

    # prijs
    house_information[6] = house_information[6].replace("k", "").strip()
    house_information[6] = house_information[6].replace("€", "").strip()
    house_information[6] = house_information[6].replace(".", "").strip()

    if house_information[6] == 'aanvraa':
        house_information[6] = "Aanvraag"

    return house_information