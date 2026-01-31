from PIL import Image, ImageColor
from collections import defaultdict
from tkinter import filedialog
import os
import ast

def closest_color_manhattan(target_rgb, parsed_palette):
    target_r, target_g, target_b, _ = target_rgb
    closest_color = None
    min_distance = float('inf')
    for color in parsed_palette:
        r, g, b, *__ = color
        distance = abs(r - target_r) + abs(g - target_g) + abs(b - target_b)
        if distance < min_distance:
            min_distance = distance
            closest_color = color
    return closest_color

def walk_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.split('.')[-1] == 'png':
                yield os.path.join(root, file)

def recolor_picture(image_path, parsed_palette):
    img = Image.open(image_path).convert('RGBA')
    rgba_array = image_to_rgba_array(image_path)
    for x in range(len(rgba_array)):
        for y in range(len(rgba_array[x])):
            pixel = rgba_array[x][y]
            if pixel[3] != 0:
                new_color = closest_color_manhattan(pixel, parsed_palette)
                if len(new_color) < 4:
                    new_color.append(255)
                img.putpixel((y, x), tuple(new_color))
    save_path = f'result/{image_path.split("Source")[-1]}'
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    img.save(save_path)

def image_to_rgba_array(image_path):
    img = Image.open(image_path)
    img = img.convert('RGBA')
    width, height = img.size
    rgba_array = []
    for y in range(height):
        row = []
        for x in range(width):
            r, g, b, a = img.getpixel((x, y))
            row.append([r, g, b, a])
        rgba_array.append(row)
    return rgba_array

def recolor_folder(folder_dir, parsed_palette):
    for file_path in walk_files(folder_dir):
        recolor_picture(file_path, parsed_palette)

def parse_palette(palette_file_dir):
    with open(palette_file_dir) as file:
        file_data = file.readlines()
        file_data.pop(0)
        new_file_data = []
        for line in file_data:
            if line[0] != '#':
                new_file_data.append(line)
        file_data = new_file_data

        separator = None
        for i, char in enumerate(file_data[0]):
            if char in '0123456789':
                if not file_data[0][i + 1] in '0123456789':
                    separator = file_data[0][i + 1]
                    break

        parsed_palette = []
        for line in file_data:
            splitted_line = line.split(separator)
            if separator != '\t':
                splitted_line[-1] = splitted_line[-1].split('\t')[0]
            new_splitted_line = []
            for char in splitted_line:
                if char != '':
                    new_splitted_line.append(char)
            splitted_line_color_part from PIL import Image, ImageColor
from collections import defaultdict
from tkinter import filedialog
import os
import ast

def closest_color_manhattan(target_rgb, parsed_palette):
    target_r, target_g, target_b, _ = target_rgb
    closest_color = None
    min_distance = float('inf')
    for color in parsed_palette:
        r, g, b, *__ = color
        distance = abs(r - target_r) + abs(g - target_g) + abs(b - target_b)
        if distance < min_distance:
            min_distance = distance
            closest_color = color
    return closest_color

def walk_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.split('.')[-1] == 'png':
                yield os.path.join(root, file)

def recolor_picture(image_path, parsed_palette):
    img = Image.open(image_path).convert('RGBA')
    rgba_array = image_to_rgba_array(image_path)
    for x in range(len(rgba_array)):
        for y in range(len(rgba_array[x])):
            pixel = rgba_array[x][y]
            if pixel[3] != 0:
                new_color = closest_color_manhattan(pixel, parsed_palette)
                if len(new_color) < 4:
                    new_color.append(255)
                img.putpixel((y, x), tuple(new_color))
    save_path = f'result/{image_path.split("Source")[-1]}'
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    img.save(save_path)

def image_to_rgba_array(image_path):
    img = Image.open(image_path)
    img = img.convert('RGBA')
    width, height = img.size
    rgba_array = []
    for y in range(height):
        row = []
        for x in range(width):
            r, g, b, a = img.getpixel((x, y))
            row.append([r, g, b, a])
        rgba_array.append(row)
    return rgba_array

def recolor_folder(folder_dir, parsed_palette):
    for file_path in walk_files(folder_dir):
        recolor_picture(file_path, parsed_palette)

def parse_palette(palette_file_dir):
    with open(palette_file_dir) as file:
        file_data = file.readlines()
        file_data.pop(0)
        new_file_data = []
        for line in file_data:
            if line[0] != '#':
                new_file_data.append(line)
        file_data = new_file_data

        separator = None
        for i, char in enumerate(file_data[0]):
            if char in '0123456789':
                if not file_data[0][i + 1] in '0123456789':
                    separator = file_data[0][i + 1]
                    break

        parsed_palette = []
        for line in file_data:
            splitted_line = line.split(separator)
            if separator != '\t':
                splitted_line[-1] = splitted_line[-1].split('\t')[0]
            new_splitted_line = []
            for char in splitted_line:
                if char != '':
                    new_splitted_line.append(char)
            splitted_line_color_part = new_splitted_line[:3]

            parsed_palette.append(list(map(int, splitted_line_color_part)))
            print(list(map(int, splitted_line_color_part)))

    return parsed_palette


folder_dir = filedialog.askdirectory(
    title="Выберите папку со спрайтами для реколора",
    initialdir="C:/",
    mustexist=True
)
palette_file_dir = filedialog.askopenfilename(
    title="Выберите целевую палитру",
    initialdir="C:/",
    defaultextension=".gpl",
    filetypes=[("Палитры GIMP", "*.gpl"),]
)
try:
    os.mkdir('result')
except: pass

parsed_palette = parse_palette(palette_file_dir)
recolor_folder(folder_dir, parsed_palette)

print('Готово! Результаты сохранены в папочку result')
= new_splitted_line[:3]

            parsed_palette.append(list(map(int, splitted_line_color_part)))
            print(list(map(int, splitted_line_color_part)))

    return parsed_palette


folder_dir = filedialog.askdirectory(
    title="Выберите папку со спрайтами для реколора",
    initialdir="C:/",
    mustexist=True
)
palette_file_dir = filedialog.askopenfilename(
    title="Выберите целевую палитру",
    initialdir="C:/",
    defaultextension=".gpl",
    filetypes=[("Палитры GIMP", "*.gpl"),]
)
try:
    os.mkdir('result')
except: pass

parsed_palette = parse_palette(palette_file_dir)
recolor_folder(folder_dir, parsed_palette)

print('Готово! Результаты сохранены в папочку result')
