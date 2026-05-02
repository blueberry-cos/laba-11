import os
from PIL import Image
input_folder = "lol"
output_folder = "обработанные"
if not os.path.exists(output_folder):
    os.mkdir(output_folder)
фото = ["dog1.jpg", "dog2.jpg", "dog3.jpg"]
for файл in фото:
    путь = os.path.join(input_folder, файл)
    картинка = Image.open(путь)
    новая = картинка.resize((200, 200))
    новый_путь = os.path.join(output_folder, f"новая_{файл}")
    новая.save(новый_путь)
    print(f"Обработано: {файл}")
print("Все три фото обработаны!")