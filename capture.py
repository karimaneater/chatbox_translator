import mss
from PIL import Image

# TODO: adjust these numbers for your screen/chatbox
# resolution (1920x1080)
REGION = {"left": 0, "top": 720, "width": 450, "height": 330}

def grab_chat_region() -> Image.Image:
    """Grab a screenshot of the chatbox region and return a PIL Image."""
    with mss.mss() as sct:
        sct_img = sct.grab(REGION)
        img = Image.frombytes("RGB", sct_img.size, sct_img.rgb)
        return img