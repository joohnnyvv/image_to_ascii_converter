import os

from PIL import Image

def draw_stars(stars_count):
    for x in range(stars_count):
        print('*', end='')

def convert_image_to_ascii(image):
    img_w, img_h = image.size
    output = ""
    pixels_count = img_h * img_w
    pixels_processed = 0

    for y in range(img_h):
        for x in range(img_w):
            pixel = image.getpixel((x, y))
            brightness = (0.2126 * pixel[0] + 0.7152 * pixel[1] + 0.0722 * pixel[2])
            output += get_correct_ascii(brightness)
            pixels_processed += 1
            progress_percentage = int(pixels_processed * 100 / pixels_count)
            print(f"[{progress_percentage}%]", end='\r')
        output += '\n'
    return output

def get_correct_ascii(brightness):
    ascii_chars = ".-':_,^=;><+!rc*/z?sLTv)J7(|Fi{C}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@"
    char_index = int(brightness * (len(ascii_chars) - 1) / 255)
    return ascii_chars[char_index]


def main():
    reminder = 'REMEMBER TO ADD YOUR IMAGE TO IMAGES DIRECTORY!'
    new_dir_manual = '\nIf you added the image to a new folder in the /images folder, add it before the image name, e.g. my_images/my_image.jpg'
    images_path = './images/'
    results_path = './results/'


    print(reminder)
    draw_stars(len(reminder))
    print(new_dir_manual)
    draw_stars(len(new_dir_manual))
    print('\n\n')

    image_name = input('Enter an image name: ')

    image = Image.open(images_path + image_name)
    ascii_art = convert_image_to_ascii(image)
    output_file_path, output_file_name = os.path.split(image_name)
    os.makedirs(os.path.join(results_path, output_file_path), exist_ok=True)
    output_file = os.path.join(results_path, output_file_path, output_file_name + '.txt')

    with open(output_file, "w") as text_file:
        text_file.write(ascii_art)

if __name__ == "__main__":
    main()
