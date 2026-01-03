from capture import grab_chat_region

def main():
    img = grab_chat_region()
    img.save("chat_capture.png")
    print("chat_capture.png – check the crop.")

if __name__ == "__main__":
    main()