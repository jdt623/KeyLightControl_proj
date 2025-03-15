# from openrgb import OpenRGBClient
# from openrgb.utils import RGBColor, DeviceType
# import time

# def main():
#     # Connect to the OpenRGB server (default is localhost:6742)
#     client = OpenRGBClient()

#     # Find the keyboard device
#     keyboard = None
#     for device in client.devices:
#         if device.type == DeviceType.KEYBOARD:
#             keyboard = device
#             break

#     if keyboard is None:
#         print("No keyboard device found. Make sure your keyboard is supported by OpenRGB.")
#         return

#     # Example 1: Set the entire keyboard to red
#     print("Setting the entire keyboard to red...")
#     red_color = RGBColor(255, 0, 0)
#     keyboard.set_color(red_color)
#     time.sleep(2)

#     # Example 2: Cycle through a range of colors
#     print("Cycling through a range of colors...")
#     for i in range(256):
#         # Create a color that shifts from (i, 255-i, 128)
#         color = RGBColor(i, 255 - i, 128)
#         keyboard.set_color(color)
#         time.sleep(0.01)

#     # Example 3: Set individual keys (if supported by your keyboard)
#     # This example sets the WASD keys to green
#     print("Setting WASD keys to green (if supported)...")
#     green_color = RGBColor(0, 255, 0)
#     wasd_keys = [keyboard.leds[i] for i in range(len(keyboard.leds))
#                  if keyboard.leds[i].name in ["W", "A", "S", "D"]]
#     for led in wasd_keys:
#         led.set_color(green_color)
#     time.sleep(2)

#     print("All done!")

# if __name__ == "__main__":
#     main()
