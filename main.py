import requests
import

def login(loginUrl, headers):
    loginCapId = requests.get(loginUrl,headers = headers)
    bs =
    capId = loginCapId.
    capValue = input("请输入验证码：")
    data = {
        "form_email": "1187800629@qq.com",
        "form_password": "GC5204douban",
        "login": "登录",
        "redir": "https://www.douban.com/",
        "remember": "on",
        "source": "index_nav",
        "captcha-id": capId,
        "captcha-solution": capValue
    }
    re = requests.post(loginUrl,headers = headers,data = data)
    print(re.text)

if __name__ == '__main__':
    loginUrl = "https://accounts.douban.com/login"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3192.0 Safari/537.36",
                        "Host":"accounts.douban.com"}

    login(loginUrl, headers)
    print("主函数")
