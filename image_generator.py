import requests
from io import BytesIO
from PIL import Image

from urllib.parse import quote
def generate_image(prompt):


    url = f"https://image.pollinations.ai/prompt/{quote(prompt)}"

    try:

        response = requests.get(
            url,
            timeout=120
        )

        response.raise_for_status()

        return Image.open(BytesIO(response.content))

    except requests.exceptions.Timeout:

        print("Request timed out.")

        return None

    except requests.exceptions.ConnectionError:

        print("Connection error.")

        return None

    except Exception as e:

        print(e)

        return None