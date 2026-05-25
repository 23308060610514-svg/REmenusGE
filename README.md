# 1.Propósito:
El propósito principal de nuestro proyecto es desarrollar un menú digital destinado a tres tipos derestaurantes: uno de comida mexicana, uno de comida china y otro de mariscos.
El objetivo de esta aplicación surge debido a que, usualmente, en los establecimientos físicos suelen faltar cartas de menú. Nuestra solución no solo brinda el menú digital, sino que optimiza el proceso de orden al permitir reservar una mesa por internet. Esto facilita la experiencia del usuario, permitiéndole visualizar en tiempo real cuáles mesas están ocupadas y cuáles disponibles.
Además de tener el menú al alcance de la mano y conocer los detalles de cada platillo, la aplicación ofrecerá información sobre el restaurante, destacando sus especialidades y mejores comidas para guiar al comensal en su elección.

## 1.1 Su Alcance:
Fase Inicial y Validación El alcance actual del proyecto se centra en una fase de lanzamiento controlada, enfocada exclusivamente en el sector restaurantero. En esta etapa inicial, el sistema operará con tres restaurantes modelo (comida mexicana, china y mariscos), los cuales permitirán validar la funcionalidad del menú digital y el sistema de reservaciones en tiempo real.
Escalabilidad y Visión a Futuro Aunque el arranque es selectivo, el proyecto está diseñado bajo una arquitectura escalable. La visión a largo plazo contempla la integración masiva de establecimientos, desde grandes cadenas internacionales hasta pequeños negocios locales que requieran digitalizar su oferta para mantenerse competitivos. El objetivo es proporcionarles las herramientas técnicas necesarias para optimizar su flujo de trabajo y mejorar la atención al cliente.
Adaptación a la Transformación Digital Este alcance máximo responde a la tendencia global de digitalización. Proyectamos un futuro donde la interacción física con cartas impresas será mínima, y la gestión de servicios —desde la elección de una mesa hasta el conocimiento detallado de los ingredientes— se realizará de forma virtual. Nuestra plataforma busca ser el puente que facilite esta transición tecnológica.

## 1.2 entidades que intervienen en el flujo de información:
Entendido, aquí tienes el texto exactamente como lo redactaste, pero con la ortografía, las tildes y las letras corregidas:
En este sistema, la información se articula a través de 3 cosas fundamentales que nos podrán garantizar una gestión más eficiente entre el usuario y el establecimiento.
En primera, se encuentran los actores externos, que se integran por el comensal, quien genera las solicitudes de reserva y consulta, y el administrador, el responsable de mantener actualizada la oferta gastronómica.
En segundo, viene la plataforma digital, la cual contiene procesamientos encargados de transformar los datos en una interfaz visual interactiva.
Y por último, tenemos el sistema de una base de datos centralizada, la cual actúa como la entidad de almacenamiento donde se registra en tiempo real la disponibilidad de las mesas y los detalles de los menús para los tres restaurantes.
# 2.Diagrama De Flujo 
![](https://github.com/23308060610514-svg/REmenusGE/blob/c40a7e9f5c08e5e5a6e8cb44aaf5ff4456bb21ee/Captura%20de%20pantalla%202026-05-13%20224926.png)


Alumnos:
Del Rio De La Cruz Erik Ruben
23308060610614

![](https://github.com/23308060610514-svg/REmenusGE/blob/0c45426f389ce6acf083b2879fe6fdefb00b2cd7/erik.jpeg)

Ruelas Lopez Guillermo Adiel
23308060610328
![](https://github.com/23308060610514-svg/REmenusGE/blob/7b4035e93b229936c24a186d5d48abcb1aef755d/yo.jpeg)







informacion que necesito para que se ejecute bien:powershell
# 1. Sal del entorno virtual actual
deactivate

# 2. Elimina el entorno virtual viejo
rm -r .venv

# 3. Crea un nuevo entorno virtual
python -m venv .venv

# 4. Activa el nuevo entorno
.venv\Scripts\activate

# 5. Verifica que ahora apunta al lugar correcto
where python
# Debería mostrar: C:\Users\SALA2-PC2\Desktop\REmenusGE\.venv\Scripts\python.exe

# 6. Instala los paquetes (ya no debería decir "user installation")
pip install email-validator
pip install 'pydantic[email]'
pip install mysql-connector-python

# 7. Ejecuta tu aplicación
python src/main.py

# 8. por si acaso:
uv add pyjwt

uv add sync