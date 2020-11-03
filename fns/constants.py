# URLS:
BASE_URL = "https://proverkacheka.nalog.ru:9999/v1/"

URL_LOGIN = BASE_URL + "mobile/users/login"
URL_RESTORE = BASE_URL + "mobile/users/restore"
URL_REGISTRATION = BASE_URL + "mobile/users/signup"
URL_RECEIVE = BASE_URL + "inns/*/kkts/*/fss/{}/tickets/{}?fiscalSign={}&sendToEmail=no"
URL_RECEIPT_EXIST = BASE_URL + "ofds/*/inns/*/fss/{}/operations/{}/tickets/{}?fiscalSign={}&date={}&sum={}"

# Headers:
HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla",
    "Device-Id": 'androidID',
    "Device-OS": "Android 6.0.1"
}
