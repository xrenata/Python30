import qrcode

input_URL = "https://www.codare.fun/"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=15,
    border=4,
)

qr.add_data(input_URL)
qr.make(fit=True)

img = qr.make_image(fill_color="red", back_color="white") #colors
img.save("qr_image.png")

print(qr.data_list)
