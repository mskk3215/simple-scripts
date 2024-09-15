import os
import requests
# SSL証明書の警告を非表示にする
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# Google Custom Search APIの設定
API_KEY = "" 
SEARCH_ENGINE_ID = ""  


def search_images(query, num_images=100):
    image_urls = []
    start_index = 1  # 検索結果の開始インデックス
    
    while len(image_urls) < num_images:
        url = f"https://www.googleapis.com/customsearch/v1?q={query}&cx={SEARCH_ENGINE_ID}&key={API_KEY}&searchType=image&start={start_index}"
        response = requests.get(url, timeout=10, verify=False)
        
        if response.status_code == 200:
            search_results = response.json()
            items = search_results.get("items", [])
            image_urls.extend([item['link'] for item in items])
            
            if len(items) == 0:
                break  # これ以上の結果がない場合はループを終了
            
            start_index += len(items)  # 次のページの開始インデックスを更新
        else:
            print(f"Failed to retrieve search results. Status code: {response.status_code}")
            break
    
    return image_urls[:num_images]

def download_images(image_urls, insect_name, download_dir="insect_images"):
    insect_dir = os.path.join(download_dir, insect_name)
    if not os.path.exists(insect_dir):
        os.makedirs(insect_dir)
    
    for i, url in enumerate(image_urls):
        try:
            response = requests.get(url, timeout=10, verify=False)
            if response.status_code == 200:
                file_path = os.path.join(insect_dir, f"{insect_name}_image_{i+1}.jpg")
                with open(file_path, "wb") as f:
                    f.write(response.content)
                print(f"Downloaded {file_path}")
            else:
                print(f"Failed to download {url}")
        except Exception as e:
            print(f"Error downloading {url}: {e}")

def main():
    insects = [
        'アオスジアゲハ', 'アオタテハモドキ', 'アオハダトンボ', 'アオマツムシ',
        'アカシジミ', 'アカタテハ', 'アカハナカミキリ', 'アキアカネ',
        'アサギマダラ', 'アブラゼミ', 'アメンボ', 'イシガケチョウ',
        'イチモンジセセリ', 'エンマコオロギ', 'オオウラギンスジヒョウモン', 'オオクワガタ',
        'オオゴマダラ', 'オオスズメバチ', 'オオゾウムシ', 'オオムラサキ',
        'オトシブミ', 'オニヤンマ', 'オンブバッタ', 'カナブン',
        'カブトムシ', 'カラスアゲハ', 'カンタン', 'キリギリス',
        'ギンヤンマ', 'クマゼミ', 'クマバチ', 'クロアゲハ',
        'ゲンジボタル', 'コクワガタ', 'ゴマダラカミキリ', 'シオカラトンボ',
        'ショウリョウバッタ', 'トノサマバッタ', 'ナミテントウ', 'ノコギリクワガタ',
        'ハンミョウ', 'マイマイカブリ', 'ミヤマクワガタ', 'ミンミンゼミ',
        'ヤマトシジミ', 'リュウキュウアサギマダラ', 'ルリタテハ'
    ]
    
    for insect in insects:
        print(f"Searching for {insect} images...")
        image_urls = search_images(insect)
        if image_urls:
            download_images(image_urls, insect)
        else:
            print(f"No image URLs found for {insect}.")

if __name__ == "__main__":
    main()

