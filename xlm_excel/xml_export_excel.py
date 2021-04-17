# auth Bernard
# date 2020-08-01
import xlwt
from xml.dom.minidom import parse
import xml.etree.ElementTree as ET


def excel(self, f, sheet=1):
    self.workbook = xlwt.Workbook()
    self.worksheet = self.workbook.add_sheet('test')

    self.worksheet.write(0, 27, 'A1data')
    self.workbook.save('excelwrite.xls')


def test_read_01():

    tree = ET.parse('01.xml')
    root = tree.getroot()

    for node in list(root):
        print(node.tag, node.get('Index'), node.get('Name'), node.text)
        if node.get('Name') == "姓名":
            node.text = "某某人不在家"

    # print('\n')
    # print('修改后：')
    # for node in list(root):
    #     print(node.tag, node.get('Index'), node.get('Name'), node.text)


def test_read_02():
    from xml.etree import ElementTree as ET


    # tree就是一个ElementTree对象

    # tree = ET.parse("02.xml")
    # root = tree.getroot()

def read03():
    data = open("02.xml").read()
    root = ET.fromstring(data)

    for person in root:
        print("root, tag:{}, attrib:{}".format(person.tag, person.attrib))

        for data in person:
            print("person:{}, type:{}".format(data.tag, type(data.tag)))
            print("person: ",data.text)

    # open_xml = parse("./02.xml")
    # root_node = open_xml.documentElement
    # print(root_node.nodeName)


def readXML():
    domTree = parse("./03.xml")
    # 文档根元素
    rootNode = domTree.documentElement
    print(rootNode.nodeName)

    # 所有顾客
    customers = rootNode.getElementsByTagName("customer")
    print("****所有顾客信息****")
    for customer in customers:
        if customer.hasAttribute("ID"):
            print("ID:", customer.getAttribute("ID"))
            # name 元素
            name = customer.getElementsByTagName("name")[0]
            print(name.nodeName, ":", name.childNodes[0].data)

            # phone 元素
            phone = customer.getElementsByTagName("phone")[0]
            print(phone.nodeName, ":", phone.childNodes[0].data)

            # comments 元素
            comments = customer.getElementsByTagName("comments")[0]
            print(comments.nodeName, ":", comments.childNodes[0].data)
            # print(comments.childNodes)


if __name__ == "__main__":
    # readXML()
    # test_read_02()
    read03()