# IMPORTAR RECURSOS NECESARIOS
from dotenv import load_dotenv # Función para cargar las variables de entorno desde el archivo .env
import requests # Librería para realizar solicitudes HTTP a APIs
import os # Librería para acceder a variables de entorno y funciones del sistema de archivos

# Función que carga las variables de entorno y las retorna para que puedan ser ocupadas en distintas partes del código
def load_variable():
    try:
        load_dotenv()

        # Guardar las variables de entorno en variables locales 
        api_key = os.getenv("API_KEY")
        search_engine_id = os.getenv("SEARCH_ENGINE_ID")


        # Verificar que las variables de entorno esten asignadas correctmente dentro de las variables locales
        if not api_key:
            raise ValueError("No se encontró la API key.")
        if not search_engine_id:
            raise ValueError("No se encontró el Search Engine ID.")

        # Imprimir las variables de entorno, solo con motivos de prueba
        print(f"Tus variables de entorno son:\n- API key: {api_key}\n- Search Engine ID: {search_engine_id}")

        # Retorna los valores de las variables globales cargadas
        return api_key, search_engine_id

    except ValueError as e:
        print(f"Error al cargar variables de entorno: {e}")
        return None, None

# Función para realizar la solicitud a la api de google
def request_api(api_key, search_engine_id):
    try:
        # Definir las variables necesarias para realizar la solicitud
        query =  'filetype:sql "MySQL dump" (pass|password|passwd|pwd)'
        page = 1
        lang = "lang_es"

        # Concatenar la url con las variables necesarias
        url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={search_engine_id}&q={query}&start={page}&lr={lang}"

        # Realizar la solicitud con la libreria requests
        response = requests.get(url)

        # Cargar la respuesta como un diccionario json
        data = response.json()

        # Obtener todos los items de la respuesta y almacenarlos en un array/lista
        result = data.get("items", [])

        # Verificar la existencia de los resultados
        if not result:
            raise ValueError("No se encontraron resultados.")
        else:
            show_result(result)

    except ValueError as e:
        print(e)
        return None

# Función para imprimir todos los resultados en consola de manera ordenada   
def show_result(result):
    # Loop "for" que permite imprimir cada item uno por uno 
    for item in result:
        title = item.get('title')
        link = item.get('link')
        snippet = item.get('snippet')

        print(f"Title: {title}")
        print(f"Link: {link}")
        print(f"Snippet: {snippet}")
        print("-" * 80)        

# Función principal que ejecuta el resto de funciones de el código
def main():
    # Cargar las variables de entorno
    api_key, search_engine_id = load_variable()

    # Verificar las variables cargadas y enviar la solicitud de api
    if api_key and search_engine_id:
        request_api(api_key, search_engine_id)

if __name__ == "__main__":
    main()