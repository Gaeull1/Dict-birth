# coding=utf-8
import exrex


class ZiDian:


    def __init__(self, url, new_file_name="new_dict.txt", file_name="muben.txt"):
        self.url = url
        self.file_name = file_name
        self.new_file_name = new_file_name


    def get_url(self):
        url_new_list = []
        url_list = self.url.split('.')
        a = url_list[0].split('://')[-1]
        url_new_list.append(a)
        for value in url_list:
            if value == url_list[0] or value == url_list[-1]:
                continue
            url_new_list.append(value)
        return url_new_list

    def get_txt_contents(self):
        with open('muben.txt', 'r') as f:
            new_list = f.read().splitlines()
            return new_list

    def put_txt_contents(self):
        with open("new_dict.txt", "a", newline="") as f:
            for value in self.get_txt_contents():
                for value1 in self.get_url():
                    for value2 in self.get_url():
                        dicts = list(exrex.generate(rf"{value1}{value}{value2}"))
                        f.write(dicts[0] + "\n")



