import base64
import os
from pathlib import Path

from kerykeion import AstrologicalSubject, KerykeionChartSVG, Report
from kerykeion.utilities import setup_logging

from .email_script import EmailSender


class ProcessData:

    def process_email(self, array_info, id_carta):
        print(array_info)
        print(id_carta)
        email = EmailSender()
        email.create_email(array_info['email_usuario'], array_info['nombre_usuario'], id_carta)


    def crear_carta_astral(self, name, date, hour, city, long, latid, id, email):
        print(date)
        print(hour)
        fecha = date.split("-")
        hora = hour.split(":")
        setup_logging(level="debug")
        # Args: Name, year, month, day, hour, minuts, city
        _object = AstrologicalSubject(name, int(fecha[0]), int(fecha[1]), int(fecha[2]), int(hora[0]), int(hora[1]), city=city, lng=long, lat=latid, zodiac_type="Tropic")
        image_svg = KerykeionChartSVG(
            _object, new_output_directory="./static"
        )

        data_to_encode = f"{id}-{email}"
        print(data_to_encode)
        name_svg = base64.b64encode(data_to_encode.encode("utf-8")).decode("utf-8")
        print("")
        print("Encoded data:", name_svg)
        print("")

        image_svg.makeSVG()
        os.rename(f'./media/{name}NatalChart.svg', f'./media/{name_svg}.svg')
    