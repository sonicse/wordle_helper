from xml.etree import ElementTree


with open("data/slovar1_0.fb2", "rb") as fin:
    tree = ElementTree.parse(fin)
    raw = tree.getroot()
    print(raw)
