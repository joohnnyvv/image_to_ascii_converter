from PIL import Image

def drawStars(starsCount):
    for x in range(starsCount):
        print('*', end='')

def convertImageToAscii(image):
    imgW, imgH = image.size
    output = ""

    for y in range(imgH):
        for x in range(imgW):
            pixel = image.getpixel((x, y))
            brightness = (0.2126 * pixel[0] + 0.7152 * pixel[1] + 0.0722 * pixel[2])
            output += getCorrectAscii(brightness)
        output += '\n'
    return output

def getCorrectAscii(brightness):
    asciiChars = ".-':_,^=;><+!rc*/z?sLTv)J7(|Fi{C}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@"
    char_index = int(brightness * (len(asciiChars) - 1) / 255)
    return asciiChars[char_index]


def main():
    reminder = 'REMEMBER TO ADD YOUR IMAGE TO IMAGES DIRECTORY!'
    newDirManual = '\nIf you added the image to a new folder in the /images folder, add it before the image name, e.g. /my_images/my_image.jpg'
    imagesPath = './images/'
    resultsPath = './results/'


    print(reminder)
    drawStars(len(reminder))
    print(newDirManual)
    drawStars(len(newDirManual))
    print('\n\n')

    imageName = input('Enter an image name: ')

    image = Image.open(imagesPath + imageName)

    asciiArt = convertImageToAscii(image)

    with open(resultsPath + imageName + '.txt', "w") as text_file:
        text_file.write(asciiArt)

if __name__ == "__main__":
    main()
