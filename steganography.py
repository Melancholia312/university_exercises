import random


#создаем файл с секретной инфой
def make_secret(secret_msg):
    dump_file = open("secret_file.txt", "w+")
    dump_file.writelines(secret_msg)
    dump_file.close()


#создаем файл с рандомной информацией
def make_dump():
    dump_file = open("dump.txt", "w+")
    random_words = ["Hi", "bye", "he llo", "q world", "qweq"]
    for line in range(1000):
        dump_file.writelines(random.choice(random_words) + "\n")
    dump_file.close()


#функция перевода строки в биты
def text_to_bits(text):
    bits = bin(int.from_bytes(text.encode("utf-8", "surrogatepass"), "big"))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


#функция перевода битов в строку
def text_from_bits(bits):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, "big").decode("utf-8", "surrogatepass") or '\0'


def hide_secret_text(secret_file_name, dump_file_name):
    with open(secret_file_name, "r") as secret:
        with open(dump_file_name, "r") as dump:
            result_file = open("result.txt", "w+")

            secret_bytes = str(text_to_bits(secret.read()))
            #дописываем пробелы в конец строки файла если значение бита равно единице
            for index, line in enumerate(dump.readlines()):
                try:
                    if secret_bytes[index] == "1":
                        result_file.write(line.replace("\n", " \n"))
                    else:
                        result_file.write(line)
                except IndexError:
                    result_file.write(line)

            secret.close()
            dump.close()
            result_file.close()


def seek_secret_text(file_with_secret):
    with open(file_with_secret, "r") as f:
        secret_bits = ""
        file_text = f.readlines()
        #проверяем каждую строку на наличие хвостового пробела
        for line in file_text:
            if line[-2] == " ":
                secret_bits += "1"
            else:
                secret_bits += "0"
        f.close()
    #убираем лишние нулевые биты
    secret_text = text_from_bits(secret_bits).split()
    secret_text[-1] = secret_text[-1].replace("\x00", "")
    return " ".join(secret_text)


#создание файлов для последующей работы с ними
make_dump()
make_secret("hello i am hidden text")

#прячем и находим скрытую информацию
hide_secret_text("secret_file.txt", "dump.txt")
print(seek_secret_text("result.txt")) # hello i am hidden text