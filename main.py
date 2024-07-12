import Zidian
if __name__ == '__main__':
    url = input("请输入url:")
    zidian = Zidian.ZiDian(url=url)
    zidian.put_txt_contents()




