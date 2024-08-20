<<<<<<< HEAD
import requests  
import time  
import os  
from concurrent.futures import ThreadPoolExecutor, as_completed  

def download_and_delete_image_worker(url, file_path, total_bytes):  
    headers = {  
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'  
    }  
    try:  
        response = requests.get(url, headers=headers)  
        if response.status_code == 200:  
            content_size = len(response.content)  
            total_bytes[0] += content_size  # 累加下载的字节数  
            
            with open(file_path, "wb") as file:  
                file.write(response.content)  
            print(f"下载完成: {file_path} (大小: {content_size} bytes)")  
            
            os.remove(file_path)  
            print(f"已删除: {file_path}")  

            # 输出当前总下载流量  
            total_download_size_mb = convert_bytes_to_mb(total_bytes[0])  
            print(f"当前总下载流量: {total_download_size_mb:.2f} MB")  # 输出当前总流量，格式化为两位小数  

        else:  
            print(f"下载失败，状态码：{response.status_code}")  
    except Exception as e:  
        print(f"在下载或删除文件时发生异常：{str(e)}")  

def convert_bytes_to_mb(num):  
    """  
    将字节转换为MB  
    """  
    return num / (1024 * 1024)  # 将字节转换为MB  

def download_and_delete_image(url, save_path, num_downloads=10, delay=1):  
    total_bytes = [0]  # 用于存储总的下载字节数  
    with ThreadPoolExecutor() as executor:  
        futures = []  
        for i in range(num_downloads):  
            file_path = f"{save_path}_{i+1}.jpg"  
            futures.append(executor.submit(download_and_delete_image_worker, url, file_path, total_bytes))  
            if i < num_downloads - 1:  
                time.sleep(delay)  

        for future in as_completed(futures):  
            pass  

# 使用示例  
save_path = "daia"  # 你需要提供一个有效的保存路径  
url = "http://pmt823bd6.pic46.websiteonline.cn/upload/ym.png"  # 示例URL  
num_downloads = 55555 # 控制下载次数  
delay = 0.1  # 指定下载间隔时间（秒）  
download_and_delete_image(url, save_path, num_downloads, delay)
