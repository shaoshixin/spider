import re
import requests
from bs4 import BeautifulSoup


def login(loginUrl, headers, data):
    loginReq = requests.post(loginUrl, headers=headers, data=data)
    if loginReq.url != loginUrl:
        print(loginReq.url)
    else:
        soup = BeautifulSoup(loginReq.text, "html.parser")
        imgSrc = soup.find(id="captcha_image")["src"]   #注意bs4中find和findall返回的类型
        # print(type(img))  # 获取的是一个标签组，因为实际只有一个所以直接指定第0个位置即可
        # capId = re.findall(r'^https://www.douban.com/misc/captcha?id=(.*?)&size=s$',"src) #特殊字符？ 暂时无法使用正则表达式匹配
        capId1 = imgSrc.replace("https://www.douban.com/misc/captcha?id=", "")
        capId = capId1.replace("&size=s", "")
        print(capId)
        imgData = requests.get(imgSrc, headers=headers)
        with open("img.png", "wb") as f:
            f.write(imgData.content)
        capValue = input("请输入验证码：")
        data["captcha-id"] = [capId]
        data["captcha-solution"] = [capValue]
        loginReq = requests.post(loginUrl, headers=headers, data=data)
        print("输入验证码登陆成功！" + loginReq.url)


def test(headers):
    data1 = {
        "ck": "tnZ-",
        "interest": "collect",
        "rating": "",
        "foldcollect": "F",
        "tags": "真心觉得没一好看！",
        "comment": "剧情算有点起伏，但是还是感觉整个观影体验平平淡淡！"
    }
    # res = requests.get("https://www.douban.com/people/45261576/", headers=headers)
    # print(res.text)
    url = "https://movie.douban.com/j/subject/20435622/interest"
    headers1 = {
        "Host": "movie.douban.com",
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        "Referer": "https://movie.douban.com/subject/20435622/?from=showing",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3192.0 Safari/537.36",
    }
    res = requests.post(url, headers=headers1, data=data1)
    if "真心觉得没一好看！" in res.text:
        print("评论成功！")
    else:
        # res = requests.get("https://www.douban.com/people/45261576/", headers=headers)
        # print(res.text)
        return


if __name__ == '__main__':
    requests = requests.session()  # 保持会话
    loginUrl = "https://accounts.douban.com/login"
    headers = {
        "Referer": "https://www.douban.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3192.0 Safari/537.36",
    }
    data = {
        "form_email": "1187800629@qq.com",
        "form_password": "GC5204douban",
        "login": "登录",
        "redir": "https://www.douban.com/",
        "remember": "on",
        "source": "index_nav"
    }
    login(loginUrl, headers, data)
    test(headers)
