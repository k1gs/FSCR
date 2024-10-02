import psutil
import ctypes
import time

def set_mouse_speed(speed):
    SPI_SETMOUSESPEED = 0x0071
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETMOUSESPEED, 0, speed, 0)

def is_fallout4_running():
    for process in psutil.process_iter(['name']):
        if process.info['name'] == 'Fallout4.exe':
            return True
    return False

def main():
    mouse_speed_normal = 5
    mouse_speed_game = 2
    game_running = False
    
    try:
        while True:
            if is_fallout4_running():
                if not game_running:
                    print("Fallout 4 has been started")
                    set_mouse_speed(mouse_speed_game)
                    game_running = True
            else:
                if game_running:
                    print("Fallout 4 ends")
                    set_mouse_speed(mouse_speed_normal)
                    game_running = False

            time.sleep(5)
    except KeyboardInterrupt:
        set_mouse_speed(mouse_speed_normal)

if __name__ == "__main__":
    main()
