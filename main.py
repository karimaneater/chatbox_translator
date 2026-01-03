from capture import grab_chat_region
from ocr import ocr_image


def main():
    img = grab_chat_region()
    img.save("chat_capture.png")
    # print("chat_capture.png – check the crop.")
    # img.save("debug_capture.png")
    # text = ocr_image(img, lang="eng")  
    # if text:
    #     print("OCR RESULT:")
    #     print(text)
    # else:
    #     print("[no text detected]")

    try:
        text = ocr_image(img, lang="eng")
        print("OCR RESULT:", repr(text))
    except Exception as e:
        print("OCR ERROR:", repr(e))

if __name__ == "__main__":
    main()