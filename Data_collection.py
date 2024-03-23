from bs4 import BeautifulSoup
from lxml import etree
import re
import requests
import random


class Data_collection:
    def collectMessage(self):
        self.collect(0,[])
        self.collect(1,[])
        self.collect(2,[])
        self.collect(3,[])
    def collect(self, kind: int, keyword: list):
        if kind == 0:
            self.__collectPassage1(keyword)
        elif kind == 1:
            self.__collectPassage2(keyword)
        elif kind == 2:
            self.__collectPassage3(keyword)
        elif kind == 3:
            self.__collectPassage4(keyword)

    def Data_collection(self):
        pass

    def __collectPassage1(self, keyword: list):
        url = 'https://www.cas.cn/kx/kpwz/index.shtml'
        poem_urls = []
        html_content = self.__fetch_kpw_html(url)

        if html_content:
            poem_urls.extend(self.__extract_kpw_urls(html_content))
        else:
            print("Failed to fetch or parse HTML content.")
        for url in poem_urls:
            try:
                details = self.__fetch_kpw_details(url)
                if len(details['content']) > 2500 or len(details['content']) < 900:
                    continue
                if details['content'] != '':
                    with open("Doc/现代文阅读I.txt", "w", encoding='utf-8') as file:
                        file.write(details['title']+'\n')
                        file.write(details["content"] + "\n")
                        # file.write("end" + "\n")
                        # file.write(details["title"])
                    break
            except IndexError as i:
                pass

    def __collectPassage2(self, keyword: list):
        url = "https://www.gzywtk.com/kaodian/xdw-list.aspx"
        poem_urls = []
        html_content = self.__fetch_novel_html(url)
        if html_content:
            poem_urls.extend(self.__extract_novel_urls(html_content))
        else:
            print("Failed to fetch or parse HTML content.")
        for url in poem_urls:
            try:
                details = self.__fetch_novel_details(url)
                if len(details['content']) > 2000 or len(details['content']) < 900:
                    print("找到了不符合要求的文章，正在重试！")
                    continue
                if details['content'] != '':
                    with open("Doc/现代文阅读II.txt", "w", encoding='utf-8') as file:
                        file.write(details["Title"] + '\n')
                        file.write(details["author"] + "\n")
                        file.write(details["content"] + "\n")
                    break
            except IndexError as i:
                pass

    def __collectPassage3(self, keyword: list):
        kind = random.randint(1, 3)
        if kind == 1:
            url = "https://so.gushiwen.cn/guwen/book_7723bfd24ca1.aspx"
        elif kind == 2:
            url = "https://so.gushiwen.cn/guwen/book_b59f91268b84.aspx"
        elif kind == 3:
            url = "https://so.gushiwen.cn/guwen/book_62efc075fe05.aspx"
        poem_urls = []
        html_content = self.__fetch_html(url)
        if html_content:
            poem_urls.extend(self.__extract_guwen_urls(html_content))
            sel = random.randint(0, len(poem_urls))
            details = self.__fetch_guwen_details(poem_urls[sel])
            while len(details['content']) < 200:
                sel = random.randint(0, len(poem_urls)-1)
                details = self.__fetch_guwen_details(poem_urls[sel])
            with open("Doc/文言文阅读.txt", "w", encoding='utf-8') as file:
                file.write(details["name"] + '\n')
                file.write(details["content"] + "\n")
        else:
            print("Failed to fetch or parse HTML content.")

    def __collectPassage4(self, keyword: list):
        # 爬取古诗文阅读的文章
        kind = random.randint(1, 3)
        if kind == 1:
            url = "https://so.gushiwen.cn/gushi/tangshi.aspx"
        elif kind == 2:
            url = "https://so.gushiwen.cn/gushi/sanbai.aspx"
        elif kind == 3:
            url = "https://so.gushiwen.cn/gushi/songsan.aspx"
        poem_urls = []
        html_content = self.__fetch_html(url)
        if html_content:
            poem_urls.extend(self.__extract_poem_urls(html_content))
            sel = random.randint(0, len(poem_urls))
            details = self.__fetch_poem_details(poem_urls[sel])
            with open("Doc/古诗文.txt", "w", encoding='utf-8') as file:
                file.write(details["name"] + '\n')
                file.write(details["author"] + "\n")
                file.write(details["content"] + "\n")
        else:
            print("Failed to fetch or parse HTML content.")

    def __extract_kpw_urls(self, html_content):
        # print(html_content)
        soup = BeautifulSoup(html_content, 'html.parser')
        poem_urls = []
        temp = soup.find('ul', class_="gl_list2")
        temp = temp.find_all('a', href=True)
        for a_tag in temp:
            href = a_tag['href']
            if href.startswith("http"):
                full_url = f"{href}"
                # full_url.replace("../", '/')
                poem_urls.append(full_url)
            elif href.startswith('./'):
                href = str(href).replace('./', '/')
                full_url = f"https://www.cas.cn/kx/kpwz{href}"
                poem_urls.append(full_url)
        return poem_urls

    def __fetch_kpw_html(self, url):
        try:
            headers = {"user-agent": "Mizilla/5.0"}
            page = random.randint(1, 10)  # 选取一页数据进行解析
            if page != 1:
                url = f"https://www.cas.cn/kx/kpwz/index_{page - 1}.shtml"
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching HTML content: {e}")
            return None

    def __fetch_kpw_details(self, url):
        poem_details = {
            "title": "",
            "content": "",
        }
        try:
            soup = BeautifulSoup(self.__fetch_html(url), 'html.parser')
            # 提取题目信息
            title = soup.find('h2', class_="xl_title")
            poem_details['title'] = title.get_text()

            # 提取文章主要信息
            content_tag = soup.find('div', class_="xl_content", )  # 提取文章的所有信息
            temp = content_tag.get_text().strip().replace("\n", '')
            poem_details['content'] = temp
            return poem_details
        except AttributeError as a:
            return poem_details

    def __fetch_novel_html(self, url):
        try:
            page = random.randint(1, 376)  # 选取一页数据进行解析
            url = url + f"?p={page}"
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching HTML content: {e}")
            return None

    def __fetch_html(self, url: str):
        # 访问网站并返回所有数据
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching HTML content: {e}")
            return None

    def __extract_novel_urls(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        poem_urls = []

        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            if href.startswith("/tmshow"):
                full_url = f"https://www.gzywtk.com/{href}"
                # full_url.replace("../", '/')
                poem_urls.append(full_url)

        return poem_urls

    def __fetch_novel_details(self, url):
        poem_details = {
            "Title": "",
            "author": "",
            "content": "",
        }

        soup = BeautifulSoup(self.__fetch_html(url), 'html.parser')
        tag = soup.find_all("li", class_="li360")  # 提取文章的所有信息
        if (tag[0].get_text().strip().replace("\n", "")) == '考点详细：现代文阅读－文学类文本':
            temp = tag[1].get_text().strip().replace("\n", "").replace("\u3000", "d")  # 记录下标题等和作者等信息
            temp = temp.split("d")
            poem_details["Title"] = temp[0].replace("选文题目：", "")  # 提取出标题信息
            poem_details["author"] = temp[1].replace("作者：", "")  # 提取出作者信息
            # 下面提取正文内容
            content_tag = soup.find('div', class_='content')
            if content_tag:

                temp = content_tag.get_text().strip().replace("\n", "").replace(poem_details["author"], "division")
                temp = temp.split('division')[1]  # 提取出正文与题目部分
                temp = temp.replace('\u3000', '')
                temp = temp.replace('（1）', 'division')
                temp = temp.replace('(1)', 'division')
                temp = temp.replace('6.', 'division')
                temp = temp.replace('6．', 'division')
                temp = temp.replace('⑴', 'division')
                temp = temp.split("division")
                if len(temp[0]) > 500:
                    poem_details["content"] = temp[0]

        return poem_details

    def __extract_poem_urls(self, html_content):
        # 提取每一个
        soup = BeautifulSoup(html_content, 'html.parser')
        poem_urls = []

        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            if href.startswith("/shiwenv_"):
                full_url = f"https://so.gushiwen.cn{href}"
                poem_urls.append(full_url)

        return poem_urls

    def __fetch_poem_details(self, url):
        # 获取古诗关键信息
        poem_details = {
            "name": "",
            "author": "",
            "dynasty": "",
            "content": "",
            "trans": "",
            "annotation": "",
            "appreciation": "",
            "background": ""
        }

        soup = BeautifulSoup(self.__fetch_html(url), 'html.parser')
        title_tag = soup.find('h1')
        if title_tag:
            poem_details["name"] = title_tag.text.strip().replace("\n", "")

        source_tag = soup.find('p', class_='source')
        if source_tag:
            source_info = source_tag.find_all('a')
            if len(source_info) > 0:
                poem_details["author"] = source_info[0].text.strip().replace("\n", "")
                poem_details["dynasty"] = source_info[1].text.strip().replace("\n", "").replace("〔", "").replace("〕",
                                                                                                                 "")

        content_tag = soup.find('div', class_='contson')
        if content_tag:
            poem_details["content"] = content_tag.get_text().strip().replace("\n", "")

        trans_annotation_tag = soup.find('div', class_='contyishang')
        if trans_annotation_tag:
            p_tags = trans_annotation_tag.find_all('p')
            for p_tag in p_tags:
                if '译文' in p_tag.text:
                    poem_details["trans"] = p_tag.get_text().strip().replace("译文", "").replace("\n", "").replace(
                        "展开阅读全文 ∨", "")
                elif '注释' in p_tag.text:
                    annotation_text = p_tag.get_text().strip().replace("注释", "").replace("\n", "")
                    if "展开阅读全文 ∨" in annotation_text:
                        read_more_div = p_tag.find('a', text="展开阅读全文 ∨")
                        if read_more_div:
                            href_attr = read_more_div.get('href')
                            match = re.search(r"fanyiShow\((\d+),'([A-Z0-9]+)'\)", href_attr)
                            if match:
                                number = match.group(1)
                                string = match.group(2)
                                full_text_url = f"https://so.gushiwen.cn/nocdn/ajaxfanyi.aspx?id={number}&idjm={string}"
                                soup_ = BeautifulSoup(self.__fetch_html(full_text_url), 'html.parser')
                                paragraphs = soup_.find('div', class_='contyishang').find_all('p')
                                full_text = "".join(p.get_text().strip() for p in paragraphs).replace(
                                    "\n",
                                    "").replace(
                                    "▲", "")
                                match = re.compile(r"^译文(.*?)注释(.*)$", re.S).search(full_text)
                                if match:
                                    poem_details["trans"] = match.group(1).strip()
                                    annotation_text = match.group(2).strip()
                                else:
                                    match = re.compile(r"^韵译(.*?)意译(.*?)注释(.*)$", re.S).search(full_text)
                                    if match:
                                        poem_details["trans"] = "韵译:" + match.group(
                                            1).strip() + "意译:" + match.group(2).strip()
                                        annotation_text = match.group(3).strip()
                    poem_details["annotation"] = annotation_text

        appreciation_divs = soup.find_all('div', class_='contyishang')
        for div in appreciation_divs:
            if div.find('h2') and ('赏析' in div.find('h2').text or '鉴赏' in div.find('h2').text):
                appreciation_paragraphs = div.find_all('p')
                appreciation_text = "".join(p.get_text().strip() for p in appreciation_paragraphs).replace("\n", "")
                if "展开阅读全文 ∨" in appreciation_text:
                    read_more_div = div.find('a', text="展开阅读全文 ∨")
                    if read_more_div:
                        href_attr = read_more_div.get('href')
                        match = re.search(r"shangxiShow\((\d+),'([A-Z0-9]+)'\)", href_attr)
                        if match:
                            number = match.group(1)
                            string = match.group(2)
                            full_text_url = f"https://so.gushiwen.cn/nocdn/ajaxshangxi.aspx?id={number}&idjm={string}"
                            soup_ = BeautifulSoup(self.__fetch_html(full_text_url), 'html.parser')
                            paragraphs = soup_.find('div', class_='contyishang').find_all('p')
                            appreciation_text = "".join(p.get_text().strip() for p in paragraphs).replace("\n",
                                                                                                          "").replace(
                                "▲", "")
                poem_details["appreciation"] += appreciation_text

        background_divs = soup.find_all('div', class_='contyishang')
        for div in background_divs:
            if div.find('h2') and '创作背景' in div.find('h2').text:
                background_paragraphs = div.find_all('p')
                background_text = "".join(p.get_text().strip() for p in background_paragraphs).replace("\n",
                                                                                                       "")
                poem_details["background"] = background_text

        return poem_details

    def __extract_guwen_urls(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        poem_urls = []

        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            if href.startswith("/guwen"):
                full_url = f"https://so.gushiwen.cn{href}"
                poem_urls.append(full_url)

        return poem_urls

    def __fetch_guwen_details(self, url):
        poem_details = {
            "name": "",
            "content": "",
        }

        soup = BeautifulSoup(self.__fetch_html(url), 'html.parser')
        title_tag = soup.find('span')
        if title_tag:
            poem_details["name"] = title_tag.text.strip().replace("\n", "")

        content_tag = soup.find('div', class_='contson')
        content_tag = str(content_tag).replace('</p>', '').split('<p>')
        temp = ""
        for i in content_tag:
            temp += i.replace('\n', '').replace('\u3000', '').replace("<div class=\"contson\">", "").replace("</div>",'')
            print(len(temp))
            if len(temp) > 600:
                break
        if temp:
            poem_details["content"] = temp

        return poem_details
