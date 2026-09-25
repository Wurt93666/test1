"""练习项目：抓取网页标题
运行前先激活虚拟环境并安装依赖：
    pip install -r requirements.txt
"""
import requests
import re


def fetch_title(url: str) -> str:
    """获取网页的 <title> 内容。"""
    headers = {"User-Agent": "Mozilla/5.0 (practice)"}
    resp = requests.get(url, headers=headers, timeout=10)
    resp.raise_for_status()
    match = re.search(r"<title>(.*?)</title>", resp.text, re.S | re.I)
    return match.group(1).strip() if match else "(未找到标题)"


if __name__ == "__main__":
    url = "https://www.example.com"
    print(f"目标: {url}")
    print(f"标题: {fetch_title(url)}")
