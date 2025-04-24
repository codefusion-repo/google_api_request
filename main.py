from env_manager import EnvManager
import requests

# Función para realizar la solicitud a la api de google
def request_api():
    try:
        # Definir las variables necesarias para realizar la solicitud
        query =  'filetype:sql "MySQL dump" (pass|password|passwd|pwd)'
        page = 1
        lang = "lang_es"

        api_key = EnvManager.get_api_key()
        if not api_key:
            raise ValueError("No se encontro el api key.")
        
        search_engine_id = EnvManager.get_search_engine_id()
        if not search_engine_id:
            raise ValueError("No se encontro el search engine id.")
        
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
    request_api()

if __name__ == "__main__":
    main()