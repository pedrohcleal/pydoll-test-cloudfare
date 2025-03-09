import asyncio
from pydoll.browser.chrome import Chrome
import json

def format_url(company) -> str:
    cnpj = company["cnpj"]
    razao_social = company["razao_social"]
    param = (
        "-".join(razao_social.lower().replace("&", "and").replace(",", "").split(" "))
        + "-"
        + cnpj
    )
    return "https://casadosdados.com.br/solucao/cnpj/" + param

async def main(url_list: list[str]):
    async with Chrome() as browser:
        await browser.start()
        page = await browser.get_page()
        
        for url in url_list:
            print(f'acessando {url}')
            await page.go_to(url)

if __name__ == '__main__':
    with open('lista.json', mode='r') as js:
        js_obj = json.load(js)
        url_list: list[str] = [format_url(x) for x in js_obj]
        print(f'quantidade de urls = {len(url_list)}')
    
    asyncio.run(main(url_list))