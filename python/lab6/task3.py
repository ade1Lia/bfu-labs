import xmltodict
def process_xml(input_file):
    with open(input_file, encoding="windows-1251") as rawXml:
        xml_dict = xmltodict.parse(rawXml.read(), encoding="windows-1251")

        products = xml_dict["Файл"]["Документ"]["ТаблСчФакт"]["СведТов"]

        for product in products:
            name = product.get("@НаимТов")
            quantity = product.get("@КолТов")
            price = product.get("@ЦенаТов")

            print(f'Товар: {name}, Количество: {quantity}, Цена: {price}')

if __name__ == "__main__":
    process_xml('ex_3.xml')
