# Usa una imagen oficial de Python como base
FROM python:3.9

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de requerimientos al contenedor
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el contenido del proyecto al contenedor
COPY . .

# Expone el puerto en el que correrá el servidor Django
EXPOSE 8000

# Comando para correr el servidor de desarrollo Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
