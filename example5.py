from segno import helpers


name = input("Input your data: ")
# Кодування геокоординат
qr_code_1 = helpers.make_mecard("name", reading=None, email=None, phone=None, videophone=None, memo=None, nickname=None,
                                birthday=None, url=None, pobox=None, roomno=None, houseno=None, city=None,
                                prefecture=None, zipcode=None, country=None)

qr_code_2 = helpers.make_vcard("name", displayname, email=None, phone=None, fax=None, videophone=None, memo=None,
                               nickname=None, birthday=None, url=None, pobox=None, street=None, city=None, region=None,
                               zipcode=None, country=None, org=None, lat=None, lng=None, source=None, rev=None,
                               title=None, photo_uri=None, cellphone=None, homephone=None, workphone=None)
"""
* ssid - SSID мережі
* password - пароль
* security - тип автентифікації ("WEP" або "WPA").
* hidden - чи є мережа прихованою
"""
qr_code_1.save("test_qr51.png", dark="#15521B", border=5, scale=7)
qr_code_1.show()
qr_code_2.save("test_qr52.png", dark="#15521B", border=5, scale=7)
qr_code_2.show()