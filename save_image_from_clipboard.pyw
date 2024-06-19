from PIL import ImageGrab
from os import listdir, remove, system
from re import findall
from keyboard import is_pressed
from time import sleep

def bind_images():
    while True:
        sleep(1.5)
        if is_pressed("Ctrl+F2"):
            names_list = listdir(r"C:\screenshots")

            if names_list == []:
                last_num = 0
            else:
                arr_all_nums = []
                for i in names_list:
                    num_in_string = "".join(findall(r"\d*", i))
                    arr_all_nums.append(int(num_in_string))
                last_num = max(arr_all_nums)
            image_clipboard = ImageGrab.grabclipboard()
            try:
                image_clipboard.save(f"C:\screenshots\screenshot{last_num + 1}.png")
                print(f"image saved with name screenshot{last_num + 1}.png")
            except Exception:
                continue
        if is_pressed("Ctrl+del"):
            names_list = listdir(r"C:\screenshots")
            for i in names_list:
                remove(f"C:\screenshots\{i}")
                print(f"Removed C:\screenshots\{i}")
                sleep(0.3)
        if is_pressed("Ctrl+F6"):
            system(r"explorer C:\screenshots")


if __name__ == "__main__":
    bind_images()
