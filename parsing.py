import requests
from bs4 import BeautifulSoup

def get_laptops():
    url = 'https://www.sulpak.kg/f/noutbuki'
    try:
        response = requests.get(url, verify=False)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching data from Sulpak: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')

    laptops = []
    product_containers = soup.select('.product__item-inner')

    if not product_containers:
        print("No products found. Check the selectors.")
        return laptops

    for item in product_containers:
        title_element = item.select_one('.product__item-name a')
        price_element = item.select_one('.product__item-price')
        if title_element and price_element:
            title = title_element.get_text(strip=True)
            price = price_element.get_text(strip=True).replace('сом', '').strip()
            laptops.append({
                'title': title,
                'price': price
            })

    return laptops
