import qrcode

# 取得用户輸入的連結
link = input("請輸入連結: ")

# 生成QR碼
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(link)
qr.make(fit=True)

# 創建QRcode碼
img = qr.make_image(fill_color="black", back_color="white")

# 保存QR碼圖像
img.save("ioncamp.png")

print("QR碼以生成為圖片")
