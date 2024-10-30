
import os
import time

import PyPDF2
import pyautogui
from PIL import Image
import cv2
import numpy as np
import sqlite3
import hashlib


"""获取指定目录下指定后缀文件"""

def get_files(dir_path,ext=''):
    files=os.listdir(dir_path)
    file_list=[]
    for file in files:
        if ext!='':
            if file[-len(ext):].upper()==ext.upper():
                file_list.append(os.path.join(dir_path,file))
        else:
            file_path=os.path.join(dir_path, file)
            if os.path.isfile(file_path):
                file_list.append(file_path)
    return file_list

"""获取指定目录含子目录下所有指定后缀的文件"""

def get_all_files(dir_path,ext=''):
    file_list=[]
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if ext!='':
                if file[-len(ext):].upper()==ext.upper():
                    file_path = os.path.join(root, file)
                    file_list.append(file_path)
            else:
                file_path = os.path.join(root, file)
                file_list.append(file_path)
    return file_list

"""将图片转换为PDF"""

def image_to_pdf(image_path, output_pdf_path):
    image = Image.open(image_path)
    im_list = [image]
    im_list[0].save(output_pdf_path, "PDF", resolution=100.0, save_all=True)


def images_to_pdf(image_paths, output_pdf_path):
    if len(image_paths)==0:
        return None
    elif len(image_paths)==1:
        image_to_pdf(image_paths[0],output_pdf_path)
    else:
       images = []
       for image_path in image_paths:
           image = Image.open(image_path)
           image=image.convert('RGB')
           images.append(image)
       images[0].save(output_pdf_path, "PDF", resolution = 100.0, save_all=True, append_images=images[1:])

"""合并多个PDF,input_files:PDF文件列表"""

def merge_pdfs(input_files, output_file):
    merger = PyPDF2.PdfMerger()
    for input_file in input_files:
        with open(input_file, 'rb') as f:
            pdf = PyPDF2.PdfReader(f)
            for page in range(len(pdf.pages)):
                merger.append(pdf, pages=(page, page + 1))
    with open(output_file, 'wb') as f:
        merger.write(f)

    """处理图片，使其变得可打印"""
def process_image(image_path):
    image=cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)

    # 1. 复制图层并进行高斯模糊
    blurred = cv2.GaussianBlur(image, (201, 201), 0).astype(float)
    # 2. 实现“划分”模式
    epsilon = 1e-7
    divided = image / (blurred + epsilon)
    # 将结果缩放到0-255范围并转换为8位无符号整数
    divided = np.clip(divided * 255, 0, 255).astype(np.uint8)
    merged = divided.astype(float)  # 转换为浮点数以避免操作中的整数截断
    # 3. 实现正片叠底模式
    multiply = (divided * merged) / 255
    # ret,img=cv2.threshold(multiply,180,255,cv2.THRESH_BINARY)
    cv2.imwrite(image_path[:-4]+'_print.png',multiply)

def remove_quark_watermark(dir_path):
    file_list=get_files(dir_path)
    for pdf_file_path in file_list:
        # 处理PDF文件
        if pdf_file_path[-4:].upper()=='.PDF':
            pdf_writer = PyPDF2.PdfWriter()
            has_mark = False
            with open(pdf_file_path, 'rb') as pdf_file:
                reader = PyPDF2.PdfReader(pdf_file)
                for page in reader.pages:
                    resources = page['/Resources']
                    if '/QuarkX2' in resources['/XObject']:
                        del resources['/XObject']['/QuarkX2']
                        has_mark = True
                        w=page.cropbox.width
                        h=page.cropbox.height
                        wc=25
                        hc=60
                        page.cropbox.lower_left=(wc,hc)
                        page.cropbox.upper_right=(w-wc,h)
                    pdf_writer.add_page(page)

            if has_mark:
                with open(pdf_file_path, 'wb') as pdf_file:
                    pdf_writer.write(pdf_file)
                    print("\033[32m夸克水印已经删除：", pdf_file_path,"\033[0m")
            else:
                print("\033[31m",pdf_file_path, "该文件没有夸克水印\033[0m")

def md5_file(file_path):
    with open(file_path, 'rb') as f:
        md5_obj = hashlib.md5()
        md5_obj.update(f.read())
        return md5_obj.hexdigest()
def md5_str(input_str):
    return hashlib.md5(input_str.encode('utf-8')).hexdigest()

def sha256_file(file_path):
    with open(file_path, 'rb') as f:
        sha256_obj = hashlib.sha256()
        sha256_obj.update(f.read())
        return sha256_obj.hexdigest()

def sha256_str(input_str):
    return hashlib.sha256(input_str.encode('utf-8')).hexdigest()
def get_file_size(file_path):
    return os.path.getsize(file_path)
def get_file_md5(file_path):
    return md5_file(file_path)
def get_file_sha256(file_path):
    return sha256_file(file_path)

def screen_shot(file_path):
    pyautogui.screenshot(file_path)

def pyautogui_test():

    time.sleep(1)
    pyautogui.hotkey('win', 'r')
    time.sleep(1)
    pyautogui.typewrite('notepad')
    time.sleep(1)
    pyautogui.press('shift')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.typewrite('hello  world')
    pyautogui.press('shift')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 's')
    time.sleep(1)
    pyautogui.typewrite('test.txt')
    time.sleep(1)
    pyautogui.press('enter')



"操作sqlite3数据库"
class SqliteHelper:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    # sqlite.execute_sql("create table users(id integer,name text,sex text,weight real)")
    def execute_sql(self, sql, params=None):
        if params:
            self.cursor.execute(sql, params)
        else:
            self.cursor.execute(sql)
            self.conn.commit()
    def close(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    remove_quark_watermark(r'C:\Users\huawei\Desktop\夸克扫描王合并文档_20241029')