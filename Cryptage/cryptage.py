from PIL import Image, ImageDraw                                                                # le module gère la créations d'image et reconnait les pixels d'une image
import os                                                                                       # le module sert à modifier ou voir un fichier
import json                                                                                     # le module json sert à acceder et le transformer en du code python

with open("Cryptage\\color.json", encoding="utf8") as dico_text:                                # On prend le color.json pour obtenir chaque couleur avec les caractères (utf8 c'est l'encodage avec les lettres spéciaux (é, à, ç))
    data = json.load(dico_text)    

def cryptage_pic(text):                                                                         # Créer une fonction pour crypter à partir d'une image
    length = len(text)                                                                          # On prend la longueur de la phrase ou le mot
    longueur_pic = int(length**0.5) + 1                                                         # On défini la longueur de l'image qui est la racine carré de la longueur du text + 1
    img = Image.new('RGBA', (longueur_pic, longueur_pic), color=(255, 255, 255, 255))           # On défini une Image en RGBA (R: red, G: green, B: blue, A: Opacity (alpha)) avec la longueur de l'image et la hauteur et qui a une couleur de base en blanc
    draw = ImageDraw.Draw(img)                                                                  # On defini que draw est pour dessiner sur l'image
    longueur, hauteur = 0, 0                                                                    # On defini deux variables qui vont servir à ce reperer dans l'image

    for i in text:                                                                              # Pour chaque caractères (char) dans le text
        draw.point((longueur, hauteur), fill=(data[i][0], data[i][1], data[i][2], data[i][3]))  # Le programme dessine à la pos de la longueur et la hauteur la couleur associé au json
        longueur += 1                                                                           # On ajoute 1 à la longueur 

        if longueur == longueur_pic:                                                            # Si la longueur atteint la taille de l'image
            hauteur += 1                                                                        # On mets + 1 à la hauteur
            longueur = 0                                                                        # On remets la longueur à 0

    img = img.crop((0, 0, longueur_pic, hauteur+1))                                             # On redimensionne l'image pour eviter un surplus de blanc
    img.save('Images\\image.png')                                                               # On sauvegarde l'image dans le fichier Images
    
def decryptage_pic():                                                                           # On defini une fonction decryptage_pic
    text = ""                                                                                   # On defini un text vide
    image = Image.open("Images\\image.png")                                                     # On ouvre l'image
    ligne, col = image.size                                                                     # On prend la taille de l'image

    for y in range(col):                                                                        # On fait un for y in range(col) pour faire cette action sur toute les colonnes 
        for x in range(ligne):                                                                  # On fait un for x in range(ligne) pour faire cette action sur toute les lignes
            color = image.getpixel((x, y))                                                      # On defini la couleur du pixel avec les coordonnées de x et y
            if type(color) != tuple:                                                            # Si il y a pas plusieurs valeurs dans color (Si c'est pas du RGBA (r, g, b, a)) on sort de la boucle x
                break

            for cle, valeur in data.items():                                                    # Pour la clé et la valeur du dico dans le json
                if valeur == list(color):                                                       # Si la lettre associé au json est présente
                    text += cle                                                                 # On l'ajoute sur text
                    break                                                                       # On sort de la boucle dès qu'on l'a trouvé pour l'optimisation
    print(text)                                                                                 # on print le text et on le return
    return text
