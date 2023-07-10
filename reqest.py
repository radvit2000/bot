import requests as req
def rusInfo(adress):
    bigAlfavit = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    alfavit = bigAlfavit.lower()
    headers = {"User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}

    info = req.get(adress, headers = headers)
    if info.status_code == 200:
        inf = info.text
        rusInfo = []
        newElement = True
        j = 0
        for i in inf:
            if (i in bigAlfavit or i in alfavit) and not newElement:
                rusInfo[j] += i

            if (i in bigAlfavit or i in alfavit) and newElement:
                rusInfo.append("")
                rusInfo[j] += i
                newElement = False

            if not newElement and not(i in bigAlfavit or i in alfavit):
                newElement = True
                j += 1
        return rusInfo
    else:
        return info.status_code

