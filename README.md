1.	Frontend (React):
o	Ubicación: crypto-dashboard/
o	Descripción: La interfaz de usuario de la aplicación. Muestra los datos de precios de criptomonedas en un gráfico utilizando la biblioteca Recharts.
o	Dependencias Principales: React, Recharts, Axios.
o	Instrucciones para Ejecutar:
1.	Navegar al directorio crypto-dashboard/.
2.	Ejecutar npm install para instalar las dependencias.
3.	Ejecutar npm start para iniciar la aplicación en modo desarrollo.
o	
2.	Backend (Django):
o	Ubicación: DjangoApi/
o	Descripción: La consulta  el precio  actual de las criptomonedas seleccionadas en este caso (  bitcoin, Ethereum, tether, usd-coin)
o	Dependencias Principales: Django, Django REST framework, PostgreSQL.
o	Instrucciones para Ejecutar:
1.	Navegar al directorio DjangoApi/.
2.	Ejecutar pip install -r requirements.txt para instalar las dependencias.
3.	Ejecutar python manage.py migrate para aplicar las migraciones de la base de datos.
4.	Ejecutar python manage.py runserver para iniciar el servidor.
Instrucciones de Ejecución
1.	Instalar Docker y Docker Compose: Asegúrate de tener Docker y Docker Compose instalados en tu máquina.
2.	Configurar el Entorno:
o	Clona el repositorio del proyecto.
o	Navega a la carpeta raíz del proyecto.
3.	Construir y Ejecutar los Contenedores: Ejecuta el siguiente comando en la raíz del proyecto:
docker-compose up –build


4.	Acceder a la Aplicación:
o	Frontend: Abre tu navegador y visita http://localhost:3000 para ver la interfaz de usuario.
o	Backend: La API estará disponible en http://localhost:8000/api/cryptoprices/.
5.	Detener los Contenedores: Para detener y eliminar los contenedores, ejecuta:
docker-compose down
Funcionalidad de la Aplicación
•	Visualización de Datos: La aplicación permite a los usuarios ver los precios actuales de diferentes criptomonedas en un gráfico.
•	Actualización en Tiempo Real: Los datos de precios se actualizan en tiempo real utilizando la API de CoinGecko recargando la página.
•	Interactividad: Los usuarios pueden interactuar con el gráfico para ver detalles específicos de las criptomonedas.

