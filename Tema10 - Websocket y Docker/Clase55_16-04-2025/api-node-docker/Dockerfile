# Imagen base
FROM node:18

# Directorio de trabajo en el contenedor
WORKDIR /app

#Copiar archivos
COPY . .

# Instalar dependencias
RUN npm install

# Exponer puerto
EXPOSE 3000

# Comando por defecto
CMD ["npm","start"]