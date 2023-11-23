from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# ウェブドライバーのパス
driver_path = ""

# オプション設定
options = Options()
options.add_experimental_option("detach", True)
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service, options=options)

# ターゲットのウェブページにアクセス
url = "https://portal.nap.gsic.titech.ac.jp/GetAccess/Login?Template=userpass_key&AUTHMETHOD=UserPassword"
driver.get(url)

# アカウント名入力
account = driver.find_element(
    by=By.XPATH,
    value="/html/body/center[3]/form/table/tbody/tr/td/table/tbody/tr[2]/td/div/div/input",
)
account.send_keys("")  # あなたのアカウント名

# パスワード入力
password = driver.find_element(
    by=By.XPATH,
    value="/html/body/center[3]/form/table/tbody/tr/td/table/tbody/tr[3]/td/div/div/input",
)
password.send_keys("")  # あなたのパスワード

# ログインボタンをクリック
login_button1 = driver.find_element(
    by=By.XPATH,
    value="/html/body/center[3]/form/table/tbody/tr/td/table/tbody/tr[5]/td/input[1]",
)
login_button1.click()

# マトリックスを入力
matrix = {
    "A": ["", "", "", "", "", "", ""],
    "B": ["", "", "", "", "", "", ""],
    "C": ["", "", "", "", "", "", ""],
    "D": ["", "", "", "", "", "", ""],
    "E": ["", "", "", "", "", "", ""],
    "F": ["", "", "", "", "", "", ""],
    "G": ["", "", "", "", "", "", ""],
    "H": ["", "", "", "", "", "", ""],
    "I": ["", "", "", "", "", "", ""],
    "J": ["", "", "", "", "", "", ""],
}

# 3つのキーの内容を取得
key1 = driver.find_element(
    by=By.XPATH,
    value="/html/body/center[3]/form/table/tbody/tr/td/table/tbody/tr[4]/th[1]",
).text
parsed_key1 = key1.strip("[]").split(",")
key1_value = matrix[parsed_key1[0]][int(parsed_key1[1]) - 1]

key2 = driver.find_element(
    by=By.XPATH,
    value="/html/body/center[3]/form/table/tbody/tr/td/table/tbody/tr[5]/th[1]",
).text
parsed_key2 = key2.strip("[]").split(",")
key2_value = matrix[parsed_key2[0]][int(parsed_key2[1]) - 1]

key3 = driver.find_element(
    by=By.XPATH,
    value="/html/body/center[3]/form/table/tbody/tr/td/table/tbody/tr[6]/th[1]",
).text
parsed_key3 = key3.strip("[]").split(",")
key3_value = matrix[parsed_key3[0]][int(parsed_key3[1]) - 1]

# フォームの取得
key1_form = driver.find_element(
    by=By.XPATH,
    value="/html/body/center[3]/form/table/tbody/tr/td/table/tbody/tr[4]/td/div/div/input",
)
key2_form = driver.find_element(
    by=By.XPATH,
    value="/html/body/center[3]/form/table/tbody/tr/td/table/tbody/tr[5]/td/div/div/input",
)
key3_form = driver.find_element(
    by=By.XPATH,
    value="/html/body/center[3]/form/table/tbody/tr/td/table/tbody/tr[6]/td/div/div/input",
)

# マトリックスの入力
key1_form.send_keys(key1_value)
key2_form.send_keys(key2_value)
key3_form.send_keys(key3_value)

# ログインボタンをクリック
login_button2 = driver.find_element(
    by=By.XPATH,
    value="/html/body/center[3]/form/table/tbody/tr/td/table/tbody/tr[8]/td/input[1]",
)
login_button2.click()

# seleniumを終了
driver.service.stop()
