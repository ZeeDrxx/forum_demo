import qrcode

# URL de votre site
url = "https://zeedrxx.github.io/forum_demo/"

# Génération du QR Code
qr = qrcode.QRCode(
    version=1,  # Taille du QR Code (1 = petit, 40 = grand)
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,  # Taille des boîtes
    border=4,  # Taille de la bordure
)
qr.add_data(url)
qr.make(fit=True)

# Création de l'image
img = qr.make_image(fill_color="black", back_color="white")
img.save("qr_code.png")  # Le fichier sera sauvegardé dans le dossier courant
print("QR Code généré : qr_code.png")
