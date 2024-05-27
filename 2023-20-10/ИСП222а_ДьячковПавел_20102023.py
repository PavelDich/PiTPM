indexes = []
languages = [
    {"name": "Python", "index": ["простой", "популярный", "развивается", "бесплатный", "мобильный", "браузерный"]},
    {"name": "C++", "index": ["низкоуровневый", "популярный", "развивается", "быстрый", "бесплатный", "мобильный"]},
    {"name": "Java",
     "index": ["низкоуровневый", "простой", "популярный", "развивается", "быстрый", "мобильный", "браузерный"]},
    {"name": "C#", "index": ["простой", "популярный", "развивается", "быстрый", "бесплатный", "мобильный"]},
    {"name": "C", "index": ["низкоуровневый", "быстрый", "бесплатный"]},
    {"name": "JavaScript", "index": ["мобильный", "популярный", "развивается", "быстрый", "бесплатный", "браузерный"]},
    {"name": "PHP", "index": ["простой", "бесплатный", "браузерный"]},
    {"name": "Kotlin", "index": ["простой", "популярный", "развивается", "быстрый", "мобильный"]}]
massage = ""

for a in languages:
    for b in a["index"]:
        if b not in massage:
            massage += b + ", "

print("Имееютьбся такие характеристики как:", massage + "введите какие из вас интерисуют или 'end' для завершения.")

while True:
    index = input()
    if index == "end":
        break
    else:
        indexes.append(index)

for a in languages:
    for b in indexes:
        if b not in a["index"]:
            break
        if b == indexes[len(indexes) - 1]:
            massage = ""
            for c in a["index"]:
                massage += c + ", "
            print("Вам подходит " + a["name"] + " он " + massage)

print("все языки в чем то хороши кроме паскаля.")