import requests

def test_translate():
    url = 'http://localhost:8000/api/translate/'
    body = {
        "text": "а) Имеются две веревки. Если любую из них поджечь с одного конца, то она сгорит за час. Веревки горят неравномерно. Например, нельзя гарантировать, что половина веревки сгорает за 30 минут. Как, имея две такие веревки, отмерить промежуток времени в 15 минут? б) Сколько промежутков времени (считая нулевой) можно отмерить, имея три такие веревки?",
        "lang": "ru",
        "method": "offline"
    }
    response = requests.post(url, json=body)
    print(response.json())

    body ={
        "text": "### CHỦ ĐỀ ĐẠI SỐ 1",
        "lang": "vi",
        "method": "api"
    }
    response = requests.post(url, json=body)
    print(response.json())

if __name__ == '__main__':
    test_translate()