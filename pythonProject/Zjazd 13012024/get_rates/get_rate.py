import click
import httpx

@click.command()
@click.argument("currency")
def main(currency: str):
    response = httpx.get(f"https://api.nbp.pl/api/exchangerates/rates/a/{currency}/last/")
    rate_dict = response.json()["rates"][0]
    print(f"Kurs: {rate_dict['mid']} PLN")