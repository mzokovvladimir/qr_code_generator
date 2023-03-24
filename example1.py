""" pip install segno
https://segno.readthedocs.io/en/latest/
"""
import segno

"""
Для створення qr-коду використовуються функції segno.make() та segno.make_qr(). Ці функції як обов'язковий
параметра приймають кодований зміст і повертають створений QR-код:
"""
qr_code_1 = segno.make_qr("Hello, visit site: VladimirMzokov.pythonanywhere.com")
qr_code_2 = segno.make("Hello, visit site: VladimirMzokov.pythonanywhere.com", micro=False)

"""
За замовчуванням segno.make() створює мікро-код. Щоб створити звичайний QR-код, вказується параметр micro=False
Далі створений qr-код можна зберегти за допомогою методу save() в один з наступних форматів: .svg, .png, .eps та .pdf
"""

# створюємо код
# зберігаємо його у файл "test_qr.png"
qr_code_1.save("test_qr1.png")
qr_code_2.save("test_qr2.png")
# аналогічно можна зберегти в інші формати
qr_code_1.save("test_qr1.pdf")
qr_code_1.save("test_qr1.eps")
qr_code_1.save("test_qr1.svg")

# Одразу відобразити створений код у програмі перегляду за замовчуванням, можна застосувати метод show():
qr_code_1.show()
"""
При збереженні у файл метод save() можна передати ряд параметрів. Деякі з них:
* scale: коефіцієнт збільшення зображення
* border: розмір кордону
* dark: колір темної частини QR коду у вигляді кортежу (R, G, B) або рядка з ім'ям кольору (наприклад, "red") або з 
шістнадцятковим значенням кольору, наприклад (#RGB і #RRGGBB)
"""
qr_code_1.save("test_qr1.png", dark="#15524B", border=5, scale=7)
qr_code_2.save("test_qr2.png", dark="#15524B", border=5, scale=7)
