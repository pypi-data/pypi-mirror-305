from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
import pickle
import requests
import undetected_chromedriver as uc
from PIL import Image

# MidjourneyのWebページにアクセス
login_url = "https://www.midjourney.com"
generate_url = "https://www.midjourney.com/imagine"
prompt_text = "The cat will be sleeping on the couch."
cookie_file = "cookies.pkl"  # クッキーを保存するファイル名

# Chromeドライバーの設定
driver = uc.Chrome()
driver.get(login_url)  # クッキーが適用されるトップページにアクセス
time.sleep(3)  # ページ読み込みを待機

# クッキーが保存されていれば読み込む
if os.path.exists(cookie_file):
    with open(cookie_file, "rb") as file:
        cookies = pickle.load(file)
        for cookie in cookies:
            if 'sameSite' in cookie:
                del cookie['sameSite']
            if 'domain' in cookie:
                del cookie['domain']
            try:
                driver.add_cookie(cookie)
            except Exception as e:
                print(f"クッキーの設定に失敗しました: {cookie}. エラー: {e}")

# クッキー適用後に画像生成ページにアクセス
driver.get(generate_url)
time.sleep(3)  # ページの読み込み待機

# プロンプトを基に画像が既に生成されているか確認
script = f"""
const targetText = "{prompt_text}";
const targetElement = Array.from(document.querySelectorAll("span")).find(el => el.textContent.includes(targetText));
if (targetElement) {{
    const img = targetElement.parentNode.parentNode.parentNode.parentNode.parentNode.querySelector("img");
    return img ? img.src : null;
}} else {{
    return null;
}}
"""
image_url = driver.execute_script(script)

if image_url:
    print(f"既存の画像URLを利用: {image_url}")
else:
    # 画像が存在しない場合はプロンプトを入力して新規生成
    print("画像が存在しないため、新規生成を開始します。")
    prompt_box = driver.find_element(By.CSS_SELECTOR, "textarea")
    prompt_box.send_keys(prompt_text)
    prompt_box.send_keys(Keys.RETURN)

    # 生成完了まで待機（目安として30秒）
    time.sleep(30)

    # 再度スクリプトで画像URLを取得
    image_url = driver.execute_script(script)
    if image_url:
        print(f"生成された画像URL: {image_url}")
    else:
        print("画像の生成に失敗しました。")

# 続行処理（例：画像ダウンロードやトリミングなど）
if image_url:
    # URLを「grid」形式に変更
    grid_url = image_url.replace("0_0_640_N.webp?method=shortest", "grid_0.png")
    print(f"取得したグリッド画像URL: {grid_url}")

    # 画像URLのページにアクセスしてスクリーンショットを撮影
    driver.get(grid_url)
    driver.set_window_size(500, 640)  # ウィンドウサイズを調整
    time.sleep(5)  # ページ読み込みを待機

    # スクリーンショットの保存
    screenshot_path = os.path.join("output/media", "midjourney_image_screenshot.png")
    driver.save_screenshot(screenshot_path)
    print(f"スクリーンショットが{screenshot_path}に保存されました。")

    # ブラウザを閉じる
    driver.quit()
else:
    print("画像が見つからず、また生成に失敗しました。")

# 黒枠を明示的にトリミングする関数（色: (14, 14, 14) に基づく）
def trim_border_color(image_path, border_color=(14, 14, 14)):
    img = Image.open(image_path)
    pixels = img.load()

    # 上下左右のトリミング範囲を計算
    top, bottom, left, right = 0, img.height - 1, 0, img.width - 1

    # 上部の黒枠を検出
    for y in range(img.height):
        if any(pixels[x, y] != border_color for x in range(img.width)):
            top = y
            break

    # 下部の黒枠を検出
    for y in range(img.height - 1, -1, -1):
        if any(pixels[x, y] != border_color for x in range(img.width)):
            bottom = y
            break

    # 左側の黒枠を検出
    for x in range(img.width):
        if any(pixels[x, y] != border_color for y in range(img.height)):
            left = x
            break

    # 右側の黒枠を検出
    for x in range(img.width - 1, -1, -1):
        if any(pixels[x, y] != border_color for y in range(img.height)):
            right = x
            break

    # トリミングされた画像を取得
    img = img.crop((left, top, right + 1, bottom + 1))
    return img

# トリミングした画像を保存
if image_url:
    trimmed_image = trim_border_color(screenshot_path)
    trimmed_image_path = os.path.join("output/media", "midjourney_image_trimmed.png")
    trimmed_image.save(trimmed_image_path)
    print(f"トリミングされた画像が{trimmed_image_path}に保存されました。")
