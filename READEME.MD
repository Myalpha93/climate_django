# La instalacion es facil realmente

# Requisitos 
## Tener instalado Docker
## Ejecutar siguientes comandos

### 1. docker build -t cr_clima .
### 2. docker run -p 8000:8000 cr_clima

# Aplicativo contenerizado y encendido en el puerto 8000

# url de contener cloud run - https://cr-clima-ifelqlekta-uc.a.run.app
# Si deseas verificar la documentacion utiliza la API  de docs/ o en su defect redocs/ - metodo GET
# API para actualizar localidades api/climas/ - Metodo Post
# API para obtener datos de una localidad api/climas/{id} - Metodo Get
# Ids de ciudades 
## 3871336	Santiago
## 2657896	Zürich
## 2193733	Auckland
## 2147714	Sydney
## 2643743	London
## 4064006	Georgiana

## example API

## https://cr-clima-ifelqlekta-uc.a.run.app/api/climas/ - METODO POST
## https://cr-clima-ifelqlekta-uc.a.run.app/api/climas/3871336 - METODO GET
## https://cr-clima-ifelqlekta-uc.a.run.app/docs/ - METODO GET, visualizar en navegador

# Ahora para actualizar la API cada 5 minutos utilice un servicio llamado cloud scheduler con un cron de 5 minutos */5 * * * *
# Documentacion de cloud scheduler: https://cloud.google.com/scheduler/docs/creating?hl=es-419

# Credenciales de adminsitracion
## user: hugo pass: 1234 
## https://cr-clima-ifelqlekta-uc.a.run.app/admin/