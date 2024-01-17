import requests
import json
def plag_cheker(text_to_check):

    # text_to_check = input("[?] Input text to check with Turnitin > ")

    burp0_url = "https://papersowl.com:443/plagiarism-checker-send-data"

    burp0_cookies = {"PHPSESSID": "qjc72e3vvacbtn4jd1af1k5qn1", "first_interaction_user": "%7B%22referrer%22%3A%22https%3A%5C%2F%5C%2Fwww.google.com%5C%2F%22%2C%22internal_url%22%3A%22%5C%2Ffree-plagiarism-checker%22%2C%22utm_source%22%3Anull%2C%22utm_medium%22%3Anull%2C%22utm_campaign%22%3Anull%2C%22utm_content%22%3Anull%2C%22utm_term%22%3Anull%2C%22gclid%22%3Anull%2C%22msclkid%22%3Anull%2C%22adgroupid%22%3Anull%2C%22targetid%22%3Anull%2C%22appsflyer_id%22%3Anull%2C%22appsflyer_cuid%22%3Anull%2C%22cta_btn%22%3Anull%7D", "first_interaction_order": "%7B%22referrer%22%3A%22https%3A%5C%2F%5C%2Fwww.google.com%5C%2F%22%2C%22internal_url%22%3A%22%5C%2Ffree-plagiarism-checker%22%2C%22utm_source%22%3Anull%2C%22utm_medium%22%3Anull%2C%22utm_campaign%22%3Anull%2C%22utm_content%22%3Anull%2C%22utm_term%22%3Anull%2C%22gclid%22%3Anull%2C%22msclkid%22%3Anull%2C%22adgroupid%22%3Anull%2C%22targetid%22%3Anull%2C%22appsflyer_id%22%3Anull%2C%22appsflyer_cuid%22%3Anull%2C%22cta_btn%22%3Anull%7D", "affiliate_user": "a%3A3%3A%7Bs%3A9%3A%22affiliate%22%3Bs%3A9%3A%22papersowl%22%3Bs%3A6%3A%22medium%22%3Bs%3A9%3A%22papersowl%22%3Bs%3A8%3A%22campaign%22%3Bs%3A9%3A%22papersowl%22%3B%7D", "sbjs_migrations": "1418474375998%3D1", "sbjs_current_add": "fd%3D2022-05-24%2019%3A01%3A22%7C%7C%7Cep%3Dhttps%3A%2F%2Fpapersowl.com%2Ffree-plagiarism-checker%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F", "sbjs_first_add": "fd%3D2022-05-24%2019%3A01%3A22%7C%7C%7Cep%3Dhttps%3A%2F%2Fpapersowl.com%2Ffree-plagiarism-checker%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F", "sbjs_current": "typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29", "sbjs_first": "typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29", "sbjs_udata": "vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%206.3%3B%20Win64%3B%20x64%3B%20rv%3A100.0%29%20Gecko%2F20100101%20Firefox%2F100.0", "sbjs_session": "pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fpapersowl.com%2Ffree-plagiarism-checker", "_ga_788D7MTZB4": "GS1.1.1653411683.1.0.1653411683.0", "_ga": "GA1.1.1828699233.1653411683", "trustedsite_visit": "1", "trustedsite_tm_float_seen": "1", "AppleBannercookie_hide_header_banner": "1", "COOKIE_PLAGIARISM_CHECKER_TERMS": "1", "plagiarism_checker_progress_state": "1"}

    burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0", "Accept": "*/*", "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Referer": "https://papersowl.com/free-plagiarism-checker", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest", "Origin": "https://papersowl.com", "Dnt": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "no-cors", "Sec-Fetch-Site": "same-origin", "Pragma": "no-cache", "Cache-Control": "no-cache", "Te": "trailers", "Connection": "close"}

    burp0_data = {"is_free": "false", "plagchecker_locale": "en", "product_paper_type": "1", "title": '', "text": str(text_to_check)}

    r = requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)

    result = json.loads(r.text)

    try:word_count = str(result["words_count"])
    except:word_count=0
    try:Index_value = str(100 - float(result["percent"]))
    except:Index_value=0
    # print("\n[!] Word count : " + str(result["words_count"]))
    # print("\n[!] Turnitin index : " + str(100 - float(result["percent"])))
    # print("\n[!] Matches : " + str(result["matches"]),type(result["matches"]))
    copied_links=[]
    try:
        for dictionaries in result["matches"]:
            copied_links+=[dictionaries["url"]]
    except:pass
    print(copied_links,word_count,Index_value)
    return copied_links,word_count,Index_value
#print(plag_cheker("# Python program to demonstrate # image steganography using OpenCV import cv2 import numpy as np import random # Encryption function def encrypt(): # img1 and img2 are the # two input images img1 = cv2.imread('pic1.jpg') img2 = cv2.imread('pic2.jpg') for i in range(img2.shape[0]): for j in range(img2.shape[1]): for l in range(3): # v1 and v2 are 8-bit pixel values # of img1 and img2 respectively v1 = format(img1[i][j][l], '08b') v2 = format(img2[i][j][l], '08b') # Taking 4 MSBs of each image v3 = v1[:4] + v2[:4] img1[i][j][l]= int(v3, 2) cv2.imwrite('pic3in2.png', img1) # Decryption function def decrypt(): # Encrypted image img = cv2.imread('pic3in2.png') width = img.shape[0] height = img.shape[1] # img1 and img2 are two blank images img1 = np.zeros((width, height, 3), np.uint8) img2 = np.zeros((width, height, 3), np.uint8) for i in range(width): for j in range(height): for l in range(3): v1 = format(img[i][j][l], '08b') v2 = v1[:4] + chr(random.randint(0, 1)+48) * 4 v3 = v1[4:] + chr(random.randint(0, 1)+48) * 4 # Appending data to img1 and img2 img1[i][j][l]= int(v2, 2) img2[i][j][l]= int(v3, 2) # These are two images produced from # the encrypted image cv2.imwrite('pic2_re.png', img1) cv2.imwrite('pic3_re.png', img2) # Driver's code encrypt() decrypt()"))
