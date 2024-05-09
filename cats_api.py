import requests
import shutil
import os
import httpx
import aiofiles

def download_cat_image(status_code):
    url = f"https://http.cat/{status_code}"
    response = requests.get(url, stream=True)

    folder_path = 'images'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    if response.status_code == 200:

        file_path = os.path.join(folder_path, f"cat_{status_code}.jpg")
        
        with open(file_path, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)

        print(f"Imagem baixada com sucesso: {file_path}")
        return 1
    else:
        print(f"Erro ao baixar a imagem: status code {response.status_code}")
        return 0  

async def async_download_cat_image(status_code):
    url = f"https://http.cat/{status_code}"

    folder_path = 'images'

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    async with httpx.AsyncClient() as client:

        response = await client.get(url)
        
        if response.status_code == 200:
            file_path = os.path.join(folder_path, f"cat_{status_code}.jpg")    
            
            async with aiofiles.open(file_path, 'wb') as out_file:
                await out_file.write(response.content)

            print(f"Imagem baixada com sucesso: {file_path}")
        else:
            print(f"Erro ao baixar a imagem: status code {response.status_code}")


status_list = [100,101,102,103,200,201,202,203,204,205,206,207,208,214,226,300,301,302,303,304,305,307,308,400,401,402,403,
               404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,420,421,422,423,424,425,426,428,429,431,444,450,
               451,497,498,499,500,501,502,503,504,506,507,508,509,510,511,521,522,523,525,530,599]

'''
#para executar a versão sincrona
for status in status_list:
    async_download_cat_image(status)
'''