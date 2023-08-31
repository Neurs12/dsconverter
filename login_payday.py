import requests, time, json, re

cTrash = requests.get("https://user.vnedu.vn/sso/").cookies

userLoginToken = requests.post("https://user.vnedu.vn/sso/?call=auth.login",
                data={
                "txtUsername": "ahahaha",
                "txtPassword": "hahah"
            }, cookies=cTrash)

# print(userLoginToken.text, userLoginToken.cookies.get_dict(),sep="\n\n")

verify = requests.get("https://diendan.vnedu.vn/security/ssoVnedu{}".format(json.loads(userLoginToken.text)["data"]), cookies=userLoginToken.cookies, allow_redirects=False)

theDamnCookie = dict(verify.cookies.get_dict())
theDamnCookie.update(dict(userLoginToken.cookies.get_dict()))

#https://diendan.vnedu.vn/quan-ly-truong-hoc

getUrl = requests.get("https://gd1.vnedu.vn/v3/", cookies=theDamnCookie, allow_redirects=False)
theDamnCookie.update(dict(getUrl.cookies.get_dict()))

page = requests.get(getUrl.headers["location"] + "/v3/", cookies=theDamnCookie)
theDamnCookie.update(dict(page.cookies.get_dict()))

teachId = requests.get(getUrl.headers["location"] + "/v3/?call=edu.giao_vien.getGVId&nam_hoc=2022", cookies=theDamnCookie)
theDamnCookie.update(dict(teachId.cookies.get_dict()))

print(teachId.text)

print(requests.get(f"https://moommmmsssitessgdquangtri.vnedu.vn/v3/?call=edu.lop_hoc.getLopAndMonChuyen&app_status_lop_hoc=*&nam_hoc=2022&page=1&start=0&limit=1000&my_user_id={teachId.text}&app_nam_hoc=2022", cookies=theDamnCookie).text)

time.sleep(4)

requests.get("https://user.vnedu.vn/sso/?call=auth.logout", cookies=cTrash)