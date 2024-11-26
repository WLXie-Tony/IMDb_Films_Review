import requests

headers = {
    "authority": "www.imdb.com",
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
    "referer": "https://www.imdb.com/title/tt15314262/reviews?ref_=tt_urv",
    "sec-ch-ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.289 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}
cookies = {
    "uu": "eyJpZCI6InV1ODMyYzUyNTViZWQ0NDY2NzhmN2EiLCJwcmVmZXJlbmNlcyI6eyJmaW5kX2luY2x1ZGVfYWR1bHQiOmZhbHNlfX0=",
    "session-id": "140-8033594-1760024",
    "session-id-time": "2341114482",
    "ubid-main": "135-4128638-6075920",
    "session-token": "aotp91utm73+0rVyA3SPFXQW7H4ENJjcHrW8vzFV3ZVZ2gpi5mxGXPm1D8etglmdAcVgZO9RVyXuA7nIeWeGJqKCY6E31BINAle07Q25BsEymoFx5yEY6OeqmLhilYRg+DkBa6azkmut9332DYklqngOs2209P+25ekbAOGA9JS3JfyaW6HVZ3dhbjX3J4DGfEs/qJ2JZikdH/o3xQgxp/A4Zru1g+SqR7CYECMQWS4EVacOSYTrOb6BcY5OPXrGdf74Amra5LdeEGO4JDfyitxCqi4hoFNeRz/g+rcRYs7+IgMV+bXYXyeNGxQgjoB8g53jRxKhtLUDjZCcbaVfpZpCLt6orMZY",
    "ci": "e30",
    "csm-hit": "tb:0T36PXVVNPGKFPPKM36X+s-0T36PXVVNPGKFPPKM36X|1710485804331&t:1710485804331&adb:adblk_no"
}
url = "https://www.imdb.com/title/tt15314262/reviews/_ajax"
params = {
    "ref_": "undefined",
    "paginationKey": "g4w6ddbmqyzdo6ic4oxwjnbsrlrm4abs3ymdr4hlahepeud5pjt6ubc5oazfvprlb4dtscypqasrgmmpj2mo7o6a63r4y"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)