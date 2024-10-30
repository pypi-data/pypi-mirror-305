import httpx
import asyncio
import logging
from tqdm.asyncio import tqdm_asyncio
import yaml
import random
import click

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("app.log")
    ]
)

solr_instance = 'https://api.library.tamu.edu/solr/sage-core/select?indent=on&q=collection:"School of Law Catalogs as part of Texas Wesleyan University, 1989-2013"&wt=json&fl=manifest,id&rows=10000'


async def fetch_manifest(client, url):
    logging.info(f"Starting request for {url}")
    try:
        response = await client.get(url, timeout=114)
        response.raise_for_status()
        logging.info(f"Completed request for {url}")
        return response.json()
    except httpx.RequestError as e:
        logging.error(f"Request error for {url}: {e}")
        return None
    except httpx.HTTPStatusError as e:
        logging.error(f"HTTP error for {url}: {e.response.status_code}")
        return None


async def start(collection):
    async with httpx.AsyncClient(timeout=httpx.Timeout(40)) as client:
        logging.info("Fetching main data from solr instance.")
        try:
            response = await client.get(collection)
            data = response.json()
        except httpx.RequestError as e:
            logging.error(f"Request error for Solr instance: {e}")
            return
        except ValueError as e:
            logging.error(f"JSON parsing error: {e}")
            return

        tasks = [
            asyncio.create_task(
                fetch_manifest(client, thing.get('manifest') or thing.get('iiif_manifest_url_ssi'))
            ) for thing in data['response']['docs'] if thing.get('manifest') or thing.get('iiif_manifest_url_ssi')
        ]

        manifests = []
        for task in tqdm_asyncio.as_completed(tasks, total=len(tasks)):  # Changed to tqdm_asyncio
            result = await task
            if result is not None:
                manifests.append(result)

        logging.info(f"Fetched {len(manifests)} manifests successfully.")


def kickstart():
    asyncio.run(start())


@click.group()
def cli() -> None:
    pass


@cli.command("random")
def random_collection() -> None:
    config = yaml.safe_load(open('config/config.yml'))
    random_collection = random.choice(config['collections'])
    asyncio.run(start(random_collection))


@cli.command("use")
@click.option(
    "--collection",
    "-c",
    required=True
)
def use(collection: str) -> None:
    config = yaml.safe_load(open('config/config.yml'))
    id_collection = config['collections'][int(collection)]
    asyncio.run(start(id_collection))


if __name__ == '__main__':
    kickstart()
