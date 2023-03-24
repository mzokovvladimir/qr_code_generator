from segno import helpers

# Кодування email
qr_code_1 = helpers.make_email("mzokovvladimir@gmail.com", cc=None, bcc=None, subject="Test", body="Hello!")
# Параметри:
# to - кому лист
# cc - список отримувачів копії листа
# bcc - список одержувачів прихованої копії листа
# subject - тема листа
# body - текст листа
qr_code_1.save("test_qr21.png", dark="#15521B", border=5, scale=7)
qr_code_1.show()
