from openrgb import OpenRGBClient
from openrgb.utils import RGBColor, DeviceType
import time

def main():
    # Connect to the OpenRGB server (default is localhost:6742)
    client = OpenRGBClient()

    # Find the keyboard device
    keyboard = None
    for device in client.devices:
        if device.type == DeviceType.KEYBOARD:
            keyboard = device
            break

    if keyboard is None:
        print("No keyboard device found. Make sure your keyboard is supported by OpenRGB.")
        return

    # Example 1: Set the entire keyboard to red
    print("Setting the entire keyboard to red...")
    red_color = RGBColor(255, 0, 0)
    new_func(keyboard, red_color)
    time.sleep(2)

    # Example 2: Cycle through a range of colors
    print("Cycling through a range of colors...")
    for i in range(256):
        # Create a color that shifts from (i, 255-i, 128)
        color = RGBColor(i, 255 - i, 128)
        keyboard.set_color(color)
        time.sleep(0.01)

    # Example 3: Set individual keys (if supported by your keyboard)
    print("Setting WASD keys to green (if supported)...")
    green_color = RGBColor(0, 255, 0)

    # Ensure correct key mapping based on keyboard LED names
    key_names = ["W", "A", "S", "D"]
    wasd_keys = [led for led in keyboard.leds if led.name and any(k in led.name.upper() for k in key_names)]

    if wasd_keys:
        for led in wasd_keys:
            led.set_color(green_color)
        print(f"Successfully set {len(wasd_keys)} WASD keys to green.")
    else:
        print("Could not find WASD keys. Try manually checking LED names.")

    time.sleep(2)

    print("All done!")

if __name__ == "__main__":
    main()
