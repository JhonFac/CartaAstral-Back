import base64
import os

from dotenv import load_dotenv
from yagmail import SMTP

load_dotenv()

class EmailSender:
    
    def __init__(self):
        self.yag = SMTP(os.getenv('EMAIL'), os.getenv('EMAIL_KEY'))
        self.url = os.getenv('HOST_PROD')+"?carta_astral="

    def send_email(self, to_email, subject, body):
        self.yag.send(to=to_email, subject=subject, contents=body)
        print("Correo enviado con éxito!")

    def create_email(self,email, name, id_carta):


        data_to_encode = f"{id_carta}-{email}"
        name_svg = base64.b64encode(data_to_encode.encode("utf-8")).decode("utf-8")

        to_email = email
        subject = "Carta Astral"
        body = f"""
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
        </head>
        <body>
            <div class="container">
                <div class="content">
                    <h1>Hola { name }</h1>
                    <p>Sé que ha tardado un poco. Siento haberte hecho esperar.</p>
                    <p>He preparado tu carta natal.</p>
                    <p>Puedes hacer clic en el siguiente enlace para acceder a tu carta natal, que te ayudará a entenderte aún mejor.</p>
                    <a href="<a href="{self.url+str(name_svg)}" style="text-decoration:none;">">Ver Carta Astral</a>
                    <a href="{self.url + str(name_svg)}" style="text-decoration:none;">
                        <button style="background-color:blue; color:white; padding:10px; border:none; border-radius:5px; text-decoration:none;">Ver Carta Astral</button>
                    </a>
                    <p>Por último, enviaré otro correo electrónico dentro de un rato. Este correo electrónico contendrá información sobre mi servicio de consulta astrológica que se proporcionará mientras dure tu suscripción.</p>
                    <p>Si tienes algún problema, no dudes en ponerte en contacto con nosotros en <a href="https://elresultadodelaloteria.com/">support@elresultadodelaloteria.com</a>.</p>
                </div>

                <div class="footer">
                    <p>&copy; 2024 El Resultado De La Loteria</p>
                </div>
            </div>
        </body>
        """


        self.send_email(to_email, subject, body)

