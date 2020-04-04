import yaml


def readyml(filePath):

    f = open(filePath, "r", encoding="utf-8")
    y = f.read()
    data = yaml.load(y)
    print("读取yaml转字典:%s"%data)
    return data

if __name__ == '__main__':
    a = readyml(r'D:\soft\code\web_pytest_2020\case\testdata.yml')
    print(a['test_add_param_demo'])