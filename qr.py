import wifi_qrcode_generator as qr



def wifiInfo(wifiname, password):
    type = 'WPA'
    # Use wifi_qrcode() to create a QR image
    qrcode = qr.wifi_qrcode(wifiname, False, type, password)

    global filename
    filename =  wifiname+'-qr.png'
    # Save QR code
    qrcode.save(filename)


def getFileName():
    return filename