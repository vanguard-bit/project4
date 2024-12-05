import qrcode
qr = qrcode.QRCode(
    version=9,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=31,
    border=2,
)
qr.add_data('https://9009-103-146-217-178.ngrok-free.app/')
qr.make(fit=True)

img = qr.make_image(fill_color="orange", back_color="blue")
img.save("code.png")
