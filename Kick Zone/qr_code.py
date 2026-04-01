import qrcode

url = "https://mutinously-tolerant-deana.ngrok-free.dev"  # replace with your ngrok URL

img = qrcode.make(url)
img.show()  # opens the QR code image
img.save("ngrok_qr.png")  # saves it