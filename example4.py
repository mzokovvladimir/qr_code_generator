from segno import helpers

# Кодування геокоординат
qr_code_1 = helpers.make_wifi(ssid="Test_Wifi", password="1234567890", security="WPA")
"""
* ssid - SSID мережі
* password - пароль
* security - тип автентифікації ("WEP" або "WPA").
* hidden - чи є мережа прихованою
"""
qr_code_1.save("wifi-access.png", dark="#15521B", border=5, scale=7)
qr_code_1.show()
