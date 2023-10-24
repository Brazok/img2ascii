from PIL import Image
import numpy as np

## CONFIGURATION
srcPath = "monImage.jpg"
outputPath = "output.txt"

# 0 = noir, 67 = blanc
brightness = 0

# 1 = 1 pixel = 1 caractère
# 2 = 2 pixels = 1 caractère
size = 2

## CODE
srcImage = Image.open(srcPath)

srcImageArray = np.asarray(srcImage)
nb_lignes, nb_colonnes, _ = srcImageArray.shape

print(f"""
    Source : {srcPath}
    Lignes : {nb_lignes}
    Colonnes : {nb_colonnes}""")

print(f"""
    Output : {outputPath}
    Lignes : {nb_lignes//size}
    Colonnes : {nb_colonnes//size}""")


char_table = " .,';:Il!i<>~+_-=?:][}{1)(|/tfjrxnuvczxYUJCLQ0OZmwqpdbkha*#MWM&8%B@$"
char_map = np.array(list(char_table))

with open(outputPath, "w") as file:
    pixels = srcImage.getdata()
    for ligne in range(0, nb_lignes, size*2):
        for col in range(0, nb_colonnes, size):
            r = 0
            g = 0
            b = 0
            valTmp = 1
            for i in range(0, size*2):
                for j in range(0, size):
                    index = (ligne+i)*nb_colonnes + col+j
                    if index >= len(pixels):
                        break
                    rTmp, gTmp, bTmp = pixels[index]
                    r += rTmp
                    g += gTmp
                    b += bTmp
                    valTmp += 3

            lumi = (r+g+b) // valTmp
            lumif = int(lumi / 255 * 67) + brightness
            lumif = max(0, min(lumif, 67))
            b = char_map[lumif]
            file.write(b)

        file.write("\n")