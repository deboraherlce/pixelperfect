import ctypes
from ctypes import wintypes
import subprocess

def get_screen_resolution():
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    width = user32.GetSystemMetrics(0)
    height = user32.GetSystemMetrics(1)
    return width, height

def set_screen_resolution(width, height):
    subprocess.run(f"powershell -Command \"Add-Type -AssemblyName System.Windows.Forms;[System.Windows.Forms.Screen]::PrimaryScreen.Bounds.Width = {width}; [System.Windows.Forms.Screen]::PrimaryScreen.Bounds.Height = {height}\"", shell=True)

def get_color_depth():
    gdi32 = ctypes.windll.gdi32
    hdc = gdi32.CreateDCW("DISPLAY", None, None, None)
    bits_per_pixel = gdi32.GetDeviceCaps(hdc, 12)  # BITSPIXEL
    gdi32.DeleteDC(hdc)
    return bits_per_pixel

def set_color_depth(bits):
    subprocess.run(f"powershell -Command \"Set-DisplayResolution -Width {get_screen_resolution()[0]} -Height {get_screen_resolution()[1]} -ColorDepth {bits}\"", shell=True)

def adjust_display_settings():
    print("Adjusting display settings for optimal resolution and color accuracy...")
    current_width, current_height = get_screen_resolution()
    print(f"Current resolution: {current_width}x{current_height}")
    # Set to a common optimal resolution
    optimal_width, optimal_height = 1920, 1080
    if (current_width, current_height) != (optimal_width, optimal_height):
        print(f"Setting resolution to {optimal_width}x{optimal_height}...")
        set_screen_resolution(optimal_width, optimal_height)
    else:
        print("Resolution is already optimal.")

    current_color_depth = get_color_depth()
    print(f"Current color depth: {current_color_depth} bits per pixel")
    optimal_color_depth = 32
    if current_color_depth != optimal_color_depth:
        print(f"Setting color depth to {optimal_color_depth} bits per pixel...")
        set_color_depth(optimal_color_depth)
    else:
        print("Color depth is already optimal.")

    print("Display settings adjusted.")

if __name__ == "__main__":
    adjust_display_settings()