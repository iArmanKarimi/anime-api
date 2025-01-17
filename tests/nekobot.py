"""
Run tests for the NekoBotAPI class

Usage:
    cd tests
    poetry run python -m pytest nekobot.py
"""
from anime_api.apis import NekoBotAPI
from anime_api.apis.nekobot.objects import Image
from anime_api.apis.nekobot.types import ImageCategory, ImageGenType


def test_get_random_image():
    """
    Tests the get_random_image method
    """
    api = NekoBotAPI()
    image = api.get_random_image(ImageCategory.SFW.KEMONOMIMI)
    assert isinstance(image, Image)
    assert image.nsfw is False


def test_generate_image():
    """
    Tests the generate_image method
    """
    api = NekoBotAPI()
    image = api.generate_image(
        ImageGenType.THREATS,
        url="https://i.pinimg.com/originals/6b/8d/86/6b8d866222ce86cda7e176c0f17cb676.jpg",
    )
    assert isinstance(image, Image)
    assert image.nsfw is False
