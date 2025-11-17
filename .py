import qrcode

def generate_qr():
    data = input("Enter the text or URL for QR code: ")
    file_name = input("Enter file name to save (e.g., myqr.png): ")

    try:
        qr_img = qrcode.make(data)
        qr_img.save(file_name)
        print(f"✅ QR Code generated and saved as {file_name}")
    except Exception as e:
        print("⚠️ Error:", e)

# Run the tool
generate_qr()
