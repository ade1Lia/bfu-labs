
import xml.etree.ElementTree as ET

def process_xml(input_file, output_file):
    # Загружаем XML-файл
    tree = ET.parse(input_file)
    root = tree.getroot()
    total_sum, total_rows = 0, 0

    for detail in root.findall('Detail'):
        new_item = ET.Element('Item', tail="\n    ")
        new_item.text = "\n            "
        elements_data = {
            'ArtName': "Сыр Моцарелла",
            'Barcode': "2000000000113",
            'QNT': "254,7",
            'QNTPack': "254,7",
            'Unit': "шт",
            'SN1': "00000003",
            'SN2': "10.05.2021",
            'QNTRows': "21"
        }
        for tag, text in elements_data.items():
            sub_element = ET.SubElement(new_item, tag, tail="\n            ")
            sub_element.text = text
        detail.append(new_item)

        for item in detail.findall('Item'):
            for param in item:
                if param.tag == "QNT":
                    total_sum += float(param.text.replace(',', '.'))
                elif param.tag == "QNTRows":
                    total_rows += int(param.text)

    summary = root.find('Summary')
    if summary is not None:
        for param in summary:
            if param.tag == "Summ":
                param.text = str(total_sum).replace('.', ',')
            elif param.tag == "SummRows":
                param.text = str(total_rows)

    tree.write('ex_2_new.xml', encoding='UTF-8')

if __name__ == "__main__":
    process_xml('ex_2.xml', 'ex_2_new.xml')
