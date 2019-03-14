import xml.etree.ElementTree as ET

tree = ET.parse('C:\Users\XBBNN71\PycharmProjects\PythonListyTG\PythonListyTG\\5_Materialy_Pomocnicze\kraje.xml')
root = tree.getroot()

for child in root:
    print(child.attrib["name"])

for neighbor in root.iter('neighbor'):
    print(neighbor.attrib["name"])