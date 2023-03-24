from segno import helpers

# Кодування геокоординат
qr_code_1 = helpers.make_geo(30, 50)
"""
# Параметри:
# lat -  широта
# lng -  довгота
"""
qr_code_1.save("test_qr3.png", dark="#15521B", border=5, scale=7)
qr_code_1.show()
