import os, django
from urllib import request
import requests
import csv
import re
from django.core.files import File
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'abig.settings')
django.setup()

from aproperty.models import AreaPeculiarity, Area, Specialist, Image
from primary.models import PrimaryProperty


def read_csv(url):
    data = []
    with open('tmp.txt', 'w') as outer:
        csvfile = requests.get(url).content.decode('utf-8')
        outer.write(csvfile)
    with open('tmp.txt', 'r') as iner:
        data = [row for row in csv.reader(iner)]
        
    os.remove('tmp.txt')
    return data

def __get_file(url):
    result = request.urlretrieve(url)
    file = File(open(result[0], 'rb'))
    file_name = os.path.basename(url).split('.')[-1]
    return os.path.basename(url), file

MAP = """<script 
    type="text/javascript" 
	charset="utf-8" 
	async src="{url}">
</script>
"""
kinder_carden = """
<svg xmlns="http://www.w3.org/2000/svg" version="1.0" width="100%" viewBox="0 0 100.000000 100.000000" preserveAspectRatio="xMidYMid meet">
<g transform="translate(0.000000,100.000000) scale(0.100000,-0.100000)" fill="currentcolor" stroke="none">
<path d="M168 920 c-86 -44 -159 -84 -162 -89 -8 -13 43 -222 58 -237 8 -9 29 -9 71 -4 33 5 60 8 61 7 1 -1 -3 -40 -8 -87 -9 -80 -4 -248 9 -312 5 -24 16 -34 57 -52 61 -28 96 -63 105 -108 l7 -33 134 0 134 0 7 33 c9 45 44 80 106 108 49 22 52 26 57 66 12 100 14 200 7 303 -5 61 -7 111 -6 112 1 2 28 -8 61 -21 45 -19 62 -22 70 -13 18 20 66 228 55 241 -5 6 -81 47 -169 90 l-160 80 -29 -31 c-64 -68 -201 -69 -264 -2 -15 16 -31 29 -36 28 -4 0 -79 -36 -165 -79z m193 5 c72 -60 207 -59 280 2 l31 27 143 -72 143 -71 -19 -78 c-11 -43 -22 -84 -24 -90 -3 -10 -18 -8 -57 8 -100 41 -94 54 -89 -187 4 -238 0 -270 -33 -278 -42 -10 -104 -64 -122 -105 l-18 -41 -96 0 -96 0 -18 41 c-18 41 -80 95 -122 105 -17 4 -24 16 -30 47 -6 36 -7 249 -1 367 l2 35 -74 0 -74 0 -23 88 -22 88 137 69 c75 38 140 69 145 69 4 1 21 -10 37 -24z"></path>
<path d="M452 731 c-15 -16 -36 -31 -47 -33 -10 -2 -26 -16 -35 -31 -14 -25 -13 -30 3 -58 9 -17 17 -44 17 -60 0 -43 34 -73 73 -65 41 8 47 8 79 0 34 -8 68 24 68 66 0 17 7 42 16 55 22 33 11 72 -24 87 -15 7 -39 25 -54 40 -34 36 -62 35 -96 -1z m75 -42 c7 -14 24 -26 39 -29 35 -6 40 -24 16 -48 -13 -13 -18 -28 -15 -49 6 -37 -7 -47 -41 -31 -21 9 -31 8 -50 -2 -33 -17 -49 -5 -42 32 5 23 1 34 -16 47 -27 23 -18 51 16 51 18 0 30 9 41 31 18 34 34 34 52 -2z"></path>
<path d="M490 641 c0 -5 -8 -12 -17 -14 -17 -4 -17 -5 0 -6 14 -1 17 -6 12 -23 -5 -18 -4 -20 4 -8 10 13 12 13 22 0 8 -12 9 -11 4 7 -4 15 -1 23 12 26 17 4 17 5 1 6 -10 0 -18 6 -18 11 0 6 -4 10 -10 10 -5 0 -10 -4 -10 -9z"></path>
</g>
</svg>
"""
med = """
<svg viewBox="0 0 54 54" fill="none" xmlns="http://www.w3.org/2000/svg">
<g clip-path="url(#clip0_3_1642)">
<path d="M17 9.61243C17 18.2734 22 19.4404 26.666 19.4404C32 19.4404 36 18.5 36.44 9.77443C36.44 1.23869 35.2623 0.000429153 26.72 0.000429153C18.2816 0.000429153 17 1.16059 17 9.61243ZM34.172 10.3144C33.9901 17.7724 26.72 17.0104 26.72 17.0104C26.72 17.0104 19.268 17.6285 19.268 10.3144C19.268 3.00038 19.3219 2.16043 26.72 2.16043C34.3533 2.16043 34.3539 2.85642 34.172 10.3144Z" fill="black"></path>
<path d="M26.24 6.61965C26.24 8.07765 26.078 8.23965 24.62 8.23965C23.378 8.23965 23 8.45565 23 9.31965C23 10.1836 23.378 10.3996 24.62 10.3996C26.078 10.3996 26.24 10.5616 26.24 12.0196C26.24 13.2616 26.456 13.6396 27.32 13.6396C28.184 13.6396 28.4 13.2616 28.4 12.0196C28.4 10.5616 28.562 10.3996 30.02 10.3996C31.262 10.3996 31.64 10.1836 31.64 9.31965C31.64 8.45565 31.262 8.23965 30.02 8.23965C28.562 8.23965 28.4 8.07765 28.4 6.61965C28.4 5.37765 28.184 4.99965 27.32 4.99965C26.456 4.99965 26.24 5.37765 26.24 6.61965Z" fill="black"></path>
<path d="M4.24023 31.0497V48.6797H12.9602H21.6802V43.1997V36.7197V35.7197H22.6802H27.0002H31.3202H32.3202V36.7197V43.1997V48.6797H41.5802H50.8402V31.0497V13.7591L49.68 11.6703C49.4452 11.4307 49.2767 11.2853 49.11 11.1797C48.9366 11.07 48.726 10.9792 48.3834 10.908C47.6297 10.7515 46.4268 10.7197 44.0102 10.7197H39.8802V14.3637C39.8802 15.3767 39.7097 17.1197 39.1553 18.6465C38.6291 20.0957 37.5558 21.8437 35.5 21.8437H28.5C26.9703 21.8437 25.4043 21.8867 23.9794 21.9258C23.4567 21.9401 22.953 21.9539 22.4771 21.9649C21.5992 21.9852 20.809 21.9959 20.1856 21.9801C19.8744 21.9721 19.5882 21.9573 19.3448 21.9309C19.1374 21.9084 18.8675 21.8693 18.6318 21.7735C17.3436 21.2854 16.1423 20.633 15.3085 19.3405C14.4897 18.0711 14.1202 16.3312 14.1202 13.8777V10.7197H10.5302C8.38322 10.7197 7.323 10.7522 6.64575 10.9045C6.13556 11.0193 5.86937 11.1909 5.40061 11.6702L4.24023 13.7591V31.0497ZM17.2002 31.3197V32.3197H16.2002H12.4202H8.64023H7.64023V31.3197V28.0797V26V25H8.64023H12.4202H16.2002H17.2002V26V28.0797V31.3197ZM32.3202 31.3197V32.3197H31.3202H27.0002H22.6802H21.6802V31.3197V28.0797V26.5V25.5H22.6802H27.0002H31.3202H32.3202V26.5V28.0797V31.3197ZM46.3602 31.3197V32.3197H45.3602H41.5802H37.8002H36.8002V31.3197V28.0797V26V25H37.8002H41.5802H45.3602H46.3602V26V28.0797V31.3197ZM17.2002 43.1997V44.1997H16.2002H12.4202H8.64023H7.64023V43.1997V39.9597V36.7197V35.7197H8.64023H12.4202H16.2002H17.2002V36.7197V39.9597V43.1997ZM46.3602 43.1997V44.1997H45.3602H41.5802H37.8002H36.8002V43.1997V39.9597V36.7197V35.7197H37.8002H41.5802H45.3602H46.3602V36.7197V39.9597V43.1997Z" stroke="black" stroke-width="2"></path>
</g>
<defs>
<clipPath id="clip0_3_1642">
<rect width="54" height="54" fill="white"></rect>
</clipPath>
</defs>
</svg>
"""
shool = """
<svg viewBox="0 0 54 54" fill="none" xmlns="http://www.w3.org/2000/svg">
<g clip-path="url(#clip0_3_1642)">
<path d="M17 9.61243C17 18.2734 22 19.4404 26.666 19.4404C32 19.4404 36 18.5 36.44 9.77443C36.44 1.23869 35.2623 0.000429153 26.72 0.000429153C18.2816 0.000429153 17 1.16059 17 9.61243ZM34.172 10.3144C33.9901 17.7724 26.72 17.0104 26.72 17.0104C26.72 17.0104 19.268 17.6285 19.268 10.3144C19.268 3.00038 19.3219 2.16043 26.72 2.16043C34.3533 2.16043 34.3539 2.85642 34.172 10.3144Z" fill="black"></path>
<path d="M26.24 6.61965C26.24 8.07765 26.078 8.23965 24.62 8.23965C23.378 8.23965 23 8.45565 23 9.31965C23 10.1836 23.378 10.3996 24.62 10.3996C26.078 10.3996 26.24 10.5616 26.24 12.0196C26.24 13.2616 26.456 13.6396 27.32 13.6396C28.184 13.6396 28.4 13.2616 28.4 12.0196C28.4 10.5616 28.562 10.3996 30.02 10.3996C31.262 10.3996 31.64 10.1836 31.64 9.31965C31.64 8.45565 31.262 8.23965 30.02 8.23965C28.562 8.23965 28.4 8.07765 28.4 6.61965C28.4 5.37765 28.184 4.99965 27.32 4.99965C26.456 4.99965 26.24 5.37765 26.24 6.61965Z" fill="black"></path>
<path d="M4.24023 31.0497V48.6797H12.9602H21.6802V43.1997V36.7197V35.7197H22.6802H27.0002H31.3202H32.3202V36.7197V43.1997V48.6797H41.5802H50.8402V31.0497V13.7591L49.68 11.6703C49.4452 11.4307 49.2767 11.2853 49.11 11.1797C48.9366 11.07 48.726 10.9792 48.3834 10.908C47.6297 10.7515 46.4268 10.7197 44.0102 10.7197H39.8802V14.3637C39.8802 15.3767 39.7097 17.1197 39.1553 18.6465C38.6291 20.0957 37.5558 21.8437 35.5 21.8437H28.5C26.9703 21.8437 25.4043 21.8867 23.9794 21.9258C23.4567 21.9401 22.953 21.9539 22.4771 21.9649C21.5992 21.9852 20.809 21.9959 20.1856 21.9801C19.8744 21.9721 19.5882 21.9573 19.3448 21.9309C19.1374 21.9084 18.8675 21.8693 18.6318 21.7735C17.3436 21.2854 16.1423 20.633 15.3085 19.3405C14.4897 18.0711 14.1202 16.3312 14.1202 13.8777V10.7197H10.5302C8.38322 10.7197 7.323 10.7522 6.64575 10.9045C6.13556 11.0193 5.86937 11.1909 5.40061 11.6702L4.24023 13.7591V31.0497ZM17.2002 31.3197V32.3197H16.2002H12.4202H8.64023H7.64023V31.3197V28.0797V26V25H8.64023H12.4202H16.2002H17.2002V26V28.0797V31.3197ZM32.3202 31.3197V32.3197H31.3202H27.0002H22.6802H21.6802V31.3197V28.0797V26.5V25.5H22.6802H27.0002H31.3202H32.3202V26.5V28.0797V31.3197ZM46.3602 31.3197V32.3197H45.3602H41.5802H37.8002H36.8002V31.3197V28.0797V26V25H37.8002H41.5802H45.3602H46.3602V26V28.0797V31.3197ZM17.2002 43.1997V44.1997H16.2002H12.4202H8.64023H7.64023V43.1997V39.9597V36.7197V35.7197H8.64023H12.4202H16.2002H17.2002V36.7197V39.9597V43.1997ZM46.3602 43.1997V44.1997H45.3602H41.5802H37.8002H36.8002V43.1997V39.9597V36.7197V35.7197H37.8002H41.5802H45.3602H46.3602V36.7197V39.9597V43.1997Z" stroke="black" stroke-width="2"></path>
</g>
<defs>
<clipPath id="clip0_3_1642">
<rect width="54" height="54" fill="white"></rect>
</clipPath>
</defs>
</svg>
"""
parks = """
<svg viewBox="0 0 54 54" fill="none" xmlns="http://www.w3.org/2000/svg">
<g clip-path="url(#clip0_3_1642)">
<path d="M17 9.61243C17 18.2734 22 19.4404 26.666 19.4404C32 19.4404 36 18.5 36.44 9.77443C36.44 1.23869 35.2623 0.000429153 26.72 0.000429153C18.2816 0.000429153 17 1.16059 17 9.61243ZM34.172 10.3144C33.9901 17.7724 26.72 17.0104 26.72 17.0104C26.72 17.0104 19.268 17.6285 19.268 10.3144C19.268 3.00038 19.3219 2.16043 26.72 2.16043C34.3533 2.16043 34.3539 2.85642 34.172 10.3144Z" fill="black"></path>
<path d="M26.24 6.61965C26.24 8.07765 26.078 8.23965 24.62 8.23965C23.378 8.23965 23 8.45565 23 9.31965C23 10.1836 23.378 10.3996 24.62 10.3996C26.078 10.3996 26.24 10.5616 26.24 12.0196C26.24 13.2616 26.456 13.6396 27.32 13.6396C28.184 13.6396 28.4 13.2616 28.4 12.0196C28.4 10.5616 28.562 10.3996 30.02 10.3996C31.262 10.3996 31.64 10.1836 31.64 9.31965C31.64 8.45565 31.262 8.23965 30.02 8.23965C28.562 8.23965 28.4 8.07765 28.4 6.61965C28.4 5.37765 28.184 4.99965 27.32 4.99965C26.456 4.99965 26.24 5.37765 26.24 6.61965Z" fill="black"></path>
<path d="M4.24023 31.0497V48.6797H12.9602H21.6802V43.1997V36.7197V35.7197H22.6802H27.0002H31.3202H32.3202V36.7197V43.1997V48.6797H41.5802H50.8402V31.0497V13.7591L49.68 11.6703C49.4452 11.4307 49.2767 11.2853 49.11 11.1797C48.9366 11.07 48.726 10.9792 48.3834 10.908C47.6297 10.7515 46.4268 10.7197 44.0102 10.7197H39.8802V14.3637C39.8802 15.3767 39.7097 17.1197 39.1553 18.6465C38.6291 20.0957 37.5558 21.8437 35.5 21.8437H28.5C26.9703 21.8437 25.4043 21.8867 23.9794 21.9258C23.4567 21.9401 22.953 21.9539 22.4771 21.9649C21.5992 21.9852 20.809 21.9959 20.1856 21.9801C19.8744 21.9721 19.5882 21.9573 19.3448 21.9309C19.1374 21.9084 18.8675 21.8693 18.6318 21.7735C17.3436 21.2854 16.1423 20.633 15.3085 19.3405C14.4897 18.0711 14.1202 16.3312 14.1202 13.8777V10.7197H10.5302C8.38322 10.7197 7.323 10.7522 6.64575 10.9045C6.13556 11.0193 5.86937 11.1909 5.40061 11.6702L4.24023 13.7591V31.0497ZM17.2002 31.3197V32.3197H16.2002H12.4202H8.64023H7.64023V31.3197V28.0797V26V25H8.64023H12.4202H16.2002H17.2002V26V28.0797V31.3197ZM32.3202 31.3197V32.3197H31.3202H27.0002H22.6802H21.6802V31.3197V28.0797V26.5V25.5H22.6802H27.0002H31.3202H32.3202V26.5V28.0797V31.3197ZM46.3602 31.3197V32.3197H45.3602H41.5802H37.8002H36.8002V31.3197V28.0797V26V25H37.8002H41.5802H45.3602H46.3602V26V28.0797V31.3197ZM17.2002 43.1997V44.1997H16.2002H12.4202H8.64023H7.64023V43.1997V39.9597V36.7197V35.7197H8.64023H12.4202H16.2002H17.2002V36.7197V39.9597V43.1997ZM46.3602 43.1997V44.1997H45.3602H41.5802H37.8002H36.8002V43.1997V39.9597V36.7197V35.7197H37.8002H41.5802H45.3602H46.3602V36.7197V39.9597V43.1997Z" stroke="black" stroke-width="2"></path>
</g>
<defs>
<clipPath id="clip0_3_1642">
<rect width="54" height="54" fill="white"></rect>
</clipPath>
</defs>
</svg>
"""
beuty = """
<svg viewBox="0 0 54 54" fill="none" xmlns="http://www.w3.org/2000/svg">
<g clip-path="url(#clip0_3_1642)">
<path d="M17 9.61243C17 18.2734 22 19.4404 26.666 19.4404C32 19.4404 36 18.5 36.44 9.77443C36.44 1.23869 35.2623 0.000429153 26.72 0.000429153C18.2816 0.000429153 17 1.16059 17 9.61243ZM34.172 10.3144C33.9901 17.7724 26.72 17.0104 26.72 17.0104C26.72 17.0104 19.268 17.6285 19.268 10.3144C19.268 3.00038 19.3219 2.16043 26.72 2.16043C34.3533 2.16043 34.3539 2.85642 34.172 10.3144Z" fill="black"></path>
<path d="M26.24 6.61965C26.24 8.07765 26.078 8.23965 24.62 8.23965C23.378 8.23965 23 8.45565 23 9.31965C23 10.1836 23.378 10.3996 24.62 10.3996C26.078 10.3996 26.24 10.5616 26.24 12.0196C26.24 13.2616 26.456 13.6396 27.32 13.6396C28.184 13.6396 28.4 13.2616 28.4 12.0196C28.4 10.5616 28.562 10.3996 30.02 10.3996C31.262 10.3996 31.64 10.1836 31.64 9.31965C31.64 8.45565 31.262 8.23965 30.02 8.23965C28.562 8.23965 28.4 8.07765 28.4 6.61965C28.4 5.37765 28.184 4.99965 27.32 4.99965C26.456 4.99965 26.24 5.37765 26.24 6.61965Z" fill="black"></path>
<path d="M4.24023 31.0497V48.6797H12.9602H21.6802V43.1997V36.7197V35.7197H22.6802H27.0002H31.3202H32.3202V36.7197V43.1997V48.6797H41.5802H50.8402V31.0497V13.7591L49.68 11.6703C49.4452 11.4307 49.2767 11.2853 49.11 11.1797C48.9366 11.07 48.726 10.9792 48.3834 10.908C47.6297 10.7515 46.4268 10.7197 44.0102 10.7197H39.8802V14.3637C39.8802 15.3767 39.7097 17.1197 39.1553 18.6465C38.6291 20.0957 37.5558 21.8437 35.5 21.8437H28.5C26.9703 21.8437 25.4043 21.8867 23.9794 21.9258C23.4567 21.9401 22.953 21.9539 22.4771 21.9649C21.5992 21.9852 20.809 21.9959 20.1856 21.9801C19.8744 21.9721 19.5882 21.9573 19.3448 21.9309C19.1374 21.9084 18.8675 21.8693 18.6318 21.7735C17.3436 21.2854 16.1423 20.633 15.3085 19.3405C14.4897 18.0711 14.1202 16.3312 14.1202 13.8777V10.7197H10.5302C8.38322 10.7197 7.323 10.7522 6.64575 10.9045C6.13556 11.0193 5.86937 11.1909 5.40061 11.6702L4.24023 13.7591V31.0497ZM17.2002 31.3197V32.3197H16.2002H12.4202H8.64023H7.64023V31.3197V28.0797V26V25H8.64023H12.4202H16.2002H17.2002V26V28.0797V31.3197ZM32.3202 31.3197V32.3197H31.3202H27.0002H22.6802H21.6802V31.3197V28.0797V26.5V25.5H22.6802H27.0002H31.3202H32.3202V26.5V28.0797V31.3197ZM46.3602 31.3197V32.3197H45.3602H41.5802H37.8002H36.8002V31.3197V28.0797V26V25H37.8002H41.5802H45.3602H46.3602V26V28.0797V31.3197ZM17.2002 43.1997V44.1997H16.2002H12.4202H8.64023H7.64023V43.1997V39.9597V36.7197V35.7197H8.64023H12.4202H16.2002H17.2002V36.7197V39.9597V43.1997ZM46.3602 43.1997V44.1997H45.3602H41.5802H37.8002H36.8002V43.1997V39.9597V36.7197V35.7197H37.8002H41.5802H45.3602H46.3602V36.7197V39.9597V43.1997Z" stroke="black" stroke-width="2"></path>
</g>
<defs>
<clipPath id="clip0_3_1642">
<rect width="54" height="54" fill="white"></rect>
</clipPath>
</defs>
</svg>
"""
photos = [kinder_carden, shool, parks, med, beuty]
for i, p in enumerate(photos):
    with open(f'file-{i}.svg', 'w') as f:
        f.write(p)


areas_keys = {}
area_file_dir = input('Enter the file dir with Area Peculiarity:\n')
areas = read_csv(area_file_dir)
indexes = areas.pop(0)
for n, row in enumerate(areas):
    if len(row) > 1:
        obj = Area.objects.create(name=row[0])
        obj.save()
        areas_keys[row[1]] = obj.pk
        for k, i in enumerate(range(7, len(row)-1, 2)):
            AreaPeculiarity.objects.create(
                area=obj,
                name=indexes[i],
                amount=row[i+1] if row[i+1] else 0,
                photo=File(open(f'file-{k}.svg', 'rb'))
            ).save()
        print(f'#{n:4}:  Area {obj} with 5 AreaPeculiarity created')
print('Done')
print()
for i, p in enumerate(photos):
    os.remove(f'file-{i}.svg')


primary_file_dir = input('Enter the file dir with Specialist:\n')
for k, sp in enumerate(read_csv(primary_file_dir)[1:]):
    specialist = Specialist.objects.create(
        name=sp[0],
        phone=sp[8],
        email=sp[9] if sp[9] else '',
        role=sp[10],
        tg_link=sp[-2],
        wh_link=sp[-1]
    )
    name, file = __get_file(sp[7])
    specialist.photo.save(name, file)
    specialist.save()
    print(f'#{k:4}:  Specialist {specialist} created')
print('Done')
print()


primary_file_dir = input('Enter the file dir with Primary Property:\n')
primary = read_csv(primary_file_dir)[1:]
for n, row in enumerate(primary):
    if len(row) > 1:
        min_square = re.findall('\d+', row[19])
        max_square = re.findall('\d+', row[20])
        obj = PrimaryProperty.objects.create(
            name=row[0],
            slug=row[1],
            price=row[12],
            addres=row[13].strip(),
            district=row[14].replace('-', ''),
            subway=row[15].replace('-', ''),
            map_script=MAP.format(url=row[16]),
            min_square=float(min_square[0]) if len(min_square)==1 else 0,
            max_square=float(max_square[0]) if len(max_square)==1 else 0,
            short_phrase=row[21],
            description=row[22],
            lots_number=row[18],
            area=Area.objects.get(pk=areas_keys[row[8]]),
            specialist=specialist,
        )
        obj.save()

        if row[24]:
            name, file = __get_file(row[24])
            obj.title_image.save(name, file)
        if row[25]:
            name, file = __get_file(row[25])
            obj.second_image.save(name, file)
        if row[26]:
            name, file = __get_file(row[26])
            obj.logo.save(name, file)
        if row[27]:
            name, file = __get_file(row[27])
            obj.presentation.save(name, file)
        obj.save()

        for photo in row[28].split(';'):
            name, file = __get_file(photo.replace(' ', ''))
            ph = Image.objects.create(name=row[0])
            ph.photo.save(name, file)
            ph.save()
            obj.images.add(ph)
        obj.save()
        print(f'#{n:4}:  PrimaryProperty {obj} created')

print(' - - - - - - - - - - Done - - - - - - - - - - ')