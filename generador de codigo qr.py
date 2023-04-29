import qrcode
#creamos la funcion para hacer el codigo qr
qr = qrcode.QRCode(
    version=None, #dejamos la funcion en nula 
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size = 10,
    border = 4
)
#agregamos el link al qr
qr.add_data("https://www.youtube.com/")
#Generamos el codigo qr
img = qr.make_image(fill_collo = "black", back_color = "white")
img.save("qrcode.png")