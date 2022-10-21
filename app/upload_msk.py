import os, django
import requests
import csv
from urllib import request
import re
from django.core.files import File
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'abig.settings')
django.setup()

from aproperty.models import Area, SiteData, AreaPeculiarity, Specialist
from primary.models import PrimaryProperty
from primary.models import Image as PImage
from resale.models import ResaleProperty
from resale.models import Image as RImage



def read_csv(url):
    data = []
    with open('tmp.txt', 'w') as outer:
        csvfile = requests.get(url).content.decode('utf-8')
        outer.write(csvfile)
    with open('tmp.txt', 'r') as iner:
        data = [row for row in csv.reader(iner)]
        
    os.remove('tmp.txt')
    return data


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
<svg xmlns="http://www.w3.org/2000/svg" version="1.0" width="100%" viewBox="0 0 100.000000 100.000000" preserveAspectRatio="xMidYMid meet">
<g transform="translate(0.000000,100.000000) scale(0.100000,-0.100000)" fill="currentcolor" stroke="none">
<path d="M245 815 c-131 -68 -241 -128 -243 -134 -11 -33 47 -11 257 93 127 64 238 116 247 116 9 0 120 -52 246 -117 164 -83 232 -113 239 -106 6 6 8 16 4 22 -9 15 -481 251 -497 250 -7 -1 -121 -57 -253 -124z"></path>
<path d="M181 670 c-25 -5 -65 -20 -90 -32 l-46 -23 0 -265 0 -265 178 -3 c156 -2 181 -5 210 -22 40 -25 76 -25 125 -3 29 14 74 19 217 23 l180 5 3 259 c2 178 -1 263 -9 272 -6 7 -36 23 -67 35 -82 32 -243 32 -324 0 l-58 -22 -57 21 c-65 24 -194 34 -262 20z m252 -58 l47 -21 0 -197 c0 -183 -1 -196 -17 -189 -116 45 -250 45 -365 0 -17 -7 -18 6 -18 189 l0 195 30 16 c78 40 239 44 323 7z m440 0 l47 -21 0 -197 c0 -183 -1 -196 -17 -189 -116 45 -250 45 -365 0 -17 -7 -18 6 -18 189 l0 195 30 16 c78 40 239 44 323 7z m-429 -445 l56 -26 57 27 c52 24 70 27 163 27 86 0 113 -4 153 -22 26 -12 47 -29 47 -37 0 -14 -23 -16 -171 -16 -156 0 -173 -2 -196 -20 -33 -25 -73 -25 -106 0 -23 18 -40 20 -196 20 -144 0 -171 2 -171 15 0 17 43 41 97 55 69 17 204 6 267 -23z"></path>
</g>
</svg>
"""
parks = """
<svg xmlns="http://www.w3.org/2000/svg" version="1.0" width="100%" viewBox="0 0 100.000000 100.000000" preserveAspectRatio="xMidYMid meet">
<g transform="translate(0.000000,100.000000) scale(0.100000,-0.100000)" fill="currentcolor" stroke="none">
<path d="M277 993 c-14 -13 -6 -33 33 -94 22 -34 50 -89 62 -122 20 -55 23 -59 50 -55 32 5 32 5 29 -93 -3 -75 10 -94 59 -87 19 3 30 1 27 -6 -2 -6 -14 -43 -27 -82 -26 -79 -23 -104 14 -104 14 0 28 -5 31 -10 4 -6 -9 -44 -28 -85 -49 -103 -43 -109 92 -107 l102 2 -3 -37 c-3 -34 -7 -39 -48 -53 -33 -11 -46 -22 -48 -38 -3 -22 21 -32 32 -13 3 4 19 11 35 14 51 10 73 41 70 95 -3 41 -1 47 17 50 18 3 22 -4 28 -40 4 -24 14 -53 22 -66 20 -30 102 -68 116 -54 15 15 2 30 -40 50 -39 18 -56 45 -65 103 -5 33 -3 36 38 58 49 26 125 98 125 118 0 21 -45 104 -78 143 l-29 35 20 42 21 43 -34 35 c-19 20 -56 50 -83 68 -44 30 -47 34 -42 65 9 52 -26 81 -140 112 -47 13 -61 22 -65 40 -8 35 -48 59 -115 70 -69 11 -169 13 -178 3z m218 -57 c34 -14 37 -19 30 -43 -13 -53 -37 -92 -68 -112 l-31 -20 -38 77 c-20 42 -45 88 -55 101 l-18 24 71 -6 c39 -3 88 -13 109 -21z m197 -118 c26 -11 48 -25 48 -30 0 -21 -41 -86 -77 -121 -42 -43 -91 -71 -140 -82 l-33 -7 3 89 c2 77 6 93 28 123 14 19 29 42 32 52 5 14 12 15 48 7 23 -6 64 -19 91 -31z m115 -156 c71 -57 78 -68 65 -97 -18 -38 -91 -114 -137 -141 -48 -28 -132 -46 -174 -38 l-28 6 27 84 c25 78 30 87 72 113 25 16 60 47 79 70 19 22 37 41 41 41 3 0 28 -17 55 -38z m127 -272 l26 -48 -26 -31 c-14 -17 -63 -50 -110 -72 -77 -39 -91 -42 -184 -47 l-100 -5 30 64 c16 35 30 70 30 76 0 7 12 15 28 19 89 20 164 58 212 109 l24 25 21 -20 c13 -12 34 -43 49 -70z"></path>
<path d="M4 267 c-3 -8 -4 -39 -2 -68 l3 -54 38 -3 c20 -2 37 -5 37 -7 0 -2 -9 -30 -21 -61 -14 -38 -18 -59 -11 -66 17 -17 29 -1 54 67 l23 65 95 0 95 0 23 -65 c25 -68 37 -84 54 -67 7 7 3 28 -11 66 -12 31 -21 59 -21 61 0 2 17 5 38 7 l37 3 0 65 0 65 -213 3 c-174 2 -213 0 -218 -11z m396 -57 l0 -30 -180 0 -180 0 0 30 0 30 180 0 180 0 0 -30z"></path>
</g>
</svg>
"""
beuty = """
<svg xmlns="http://www.w3.org/2000/svg" version="1.0" width="100%" viewBox="0 0 100.000000 100.000000" preserveAspectRatio="xMidYMid meet">
<g transform="translate(0.000000,100.000000) scale(0.100000,-0.100000)" fill="currentcolor" stroke="none">
<path d="M667 974 c-4 -4 -7 -81 -7 -171 0 -157 1 -163 20 -163 20 0 20 5 18 167 -3 156 -9 189 -31 167z"></path>
<path d="M550 941 c0 -8 45 -235 55 -278 3 -15 13 -23 26 -23 15 0 19 5 15 18 -3 9 -17 79 -32 155 -23 117 -30 137 -45 137 -11 0 -19 -4 -19 -9z"></path>
<path d="M746 813 c-15 -76 -29 -146 -32 -155 -4 -13 0 -18 15 -18 23 0 21 -7 56 169 30 148 30 141 6 141 -15 0 -22 -20 -45 -137z"></path>
<path d="M536 584 c-20 -20 -20 -68 0 -88 9 -10 33 -16 59 -16 33 0 45 -4 48 -17 16 -57 17 -81 7 -129 -11 -51 -13 -54 -41 -54 -27 0 -29 2 -23 28 4 15 7 29 6 32 0 41 -7 57 -36 86 -29 29 -41 34 -80 34 -42 0 -46 2 -46 24 0 54 -72 104 -133 92 -39 -7 -83 -49 -92 -88 -6 -24 -12 -28 -42 -28 -94 0 -152 -93 -106 -170 9 -16 27 -34 40 -41 20 -11 23 -18 16 -39 -16 -55 -8 -99 23 -131 44 -44 97 -49 148 -14 l39 26 22 -21 c48 -45 133 -32 171 25 16 25 16 90 0 128 -7 15 -2 17 52 17 l61 0 -6 -50 c-5 -42 -3 -50 11 -50 9 0 16 5 16 11 0 8 5 8 15 -1 12 -10 18 -10 30 0 10 9 15 9 15 1 0 -6 7 -11 16 -11 14 0 16 8 11 50 l-6 50 94 0 95 0 0 -52 c-1 -97 -24 -108 -217 -108 -143 0 -173 -6 -173 -32 0 -4 76 -8 169 -8 158 0 170 1 202 23 50 34 59 59 59 177 0 64 -5 115 -13 130 -18 35 -74 70 -113 70 -40 0 -46 26 -14 55 24 22 26 67 4 89 -23 23 -265 23 -288 0z m264 -44 c0 -19 -7 -20 -120 -20 -113 0 -120 1 -120 20 0 19 7 20 120 20 113 0 120 -1 120 -20z m-433 -22 c29 -27 30 -71 3 -115 -22 -36 -35 -43 -25 -14 7 22 -18 46 -41 37 -12 -4 -15 -15 -12 -36 3 -17 3 -30 2 -30 -9 0 -54 90 -54 109 0 31 43 71 76 71 15 0 38 -10 51 -22z m393 -66 c0 -37 17 -52 57 -52 40 0 88 -23 97 -45 3 -9 6 -30 6 -46 l0 -29 -99 0 -100 0 -11 54 c-10 48 -9 72 7 129 2 9 13 17 24 17 14 0 19 -7 19 -28z m-535 -72 c38 -39 40 -49 6 -31 -9 5 -23 6 -30 2 -20 -13 -8 -45 19 -51 32 -8 15 -18 -43 -26 -40 -6 -49 -3 -71 19 -31 31 -33 65 -5 101 32 41 75 36 124 -14z m302 25 c29 -20 37 -59 18 -94 -18 -35 -43 -45 -93 -36 -51 8 -77 25 -39 25 33 0 46 25 24 47 -14 15 -18 14 -43 -2 l-27 -18 22 32 c43 60 94 77 138 46z m-279 -166 c-23 -13 -23 -48 -1 -56 10 -4 23 2 36 18 l20 24 -7 -49 c-11 -89 -78 -125 -131 -71 -43 42 -29 92 33 124 39 21 83 30 50 10z m175 -3 c48 -19 67 -43 67 -81 0 -61 -72 -96 -120 -57 -17 14 -24 31 -26 73 -3 42 -2 49 6 32 11 -26 48 -31 57 -8 3 9 -3 25 -12 35 -21 24 -16 25 28 6z"></path>
</g>
</svg>
"""
def __get_file(url):
    result = request.urlretrieve(url)
    file = File(open(result[0], 'rb'))
    return os.path.basename(url), file

MAP = """<script 
    type="text/javascript" 
	charset="utf-8" 
	async src="{url}">
</script>
"""
decode = {
    'Детские сады': 'Детских садов',
    'Общеобразовательные школы': 'Школ',
    'Парки, скверы': 'Парков',
    'Медицинские центры': 'Меди. центров',
    'Салоны красоты': 'Салонов красоты',
}
photos = [kinder_carden, shool, parks, med, beuty]
for i, p in enumerate(photos):
    with open(f'file-{i}.svg', 'w') as f:
        f.write(p)


site_pk = input('Enter Site Data PK :\n')
site_data = SiteData.objects.get(pk=int(site_pk))
print()

area_kw = {}
area_file_dir = input('Enter the file dir with Area Peculiarity:\n')
areas = read_csv(area_file_dir)
indexes = areas.pop(0)
for n, row in enumerate(areas):
    if len(row) > 1:
        obj = Area.objects.create(name=row[0], site=site_data)
        area_kw[row[1]] = obj.pk
        obj.save()
        for k, i in enumerate(range(7, len(row)-1, 2)):
            AreaPeculiarity.objects.create(
                area=obj,
                name=row[i+1] if row[i+1] else decode[indexes[i]],
                amount=re.findall('\d+', row[i])[0] if re.findall('\d+', row[i]) else 0,
                photo=File(open(f'file-{k}.svg', 'rb'))
            ).save()
        
        print(f'#{n:4}:  Area {obj} with 5 AreaPeculiarity created')


for i, p in enumerate(photos):
    os.remove(f'file-{i}.svg')


sp_file_dir = input('Enter the file dir with Specialist:\n')
if len(sp_file_dir) > 1:
    for k, sp in enumerate(read_csv(sp_file_dir)[1:]):
        specialist = Specialist.objects.create(
            site=site_data,
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
if len(primary_file_dir) > 1:
    primary = read_csv(primary_file_dir)[1:]
    for n, row in enumerate(primary):
        if len(row) > 1:
            min_square = re.findall('\d+', row[19])
            max_square = re.findall('\d+', row[20])
            obj = PrimaryProperty.objects.create(
                site=site_data,
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
                area=Area.objects.get(pk=area_kw[row[8]]),
                specialist=Specialist.objects.filter(site=site_data).first(),
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
                im = PImage.objects.create(
                    property=obj,
                    name=row[0]
                )
                im.save()
                im.photo.save(name, file)
                im.save()
            obj.save()
            print(f'#{n:4}:  Primary Property {obj} created')
print()

resale_file_dir = input('Enter the file dir with Resale Property:\n')
resale = read_csv(resale_file_dir)[1:]
prev = ResaleProperty.objects.count()
for n, row in enumerate(resale):
    if len(row) > 1:
        row = list(map(lambda x: (None if str(x) == 'nan' else x), row))
        obj = ResaleProperty.objects.create(
            site=site_data,
            name=row[7],
            slug=f'room-{prev+n}',
            price=row[8],
            area=Area.objects.get(pk=area_kw[row[10]]),
            map_script=MAP.format(url=row[11]),
            addres=row[12].strip(),
            description=row[15],
            specialist=Specialist.objects.filter(site=site_data).first(),
            square=float(row[18].strip()) if row[18] else None,
            rooms_number=int(re.findall('\d+', row[19])[0]) if re.findall('\d+', row[19]) else None,
            floor=int(re.findall('\d+', row[20].strip())[0]),
            floors_number=int(re.findall('\d+', row[21].strip())[0]),
            decor=row[22].strip(),
            construction_year=int(row[23]) if row[23] else '',
            bulding_material=row[24].strip(),
            ceiling_height=row[26].strip() if row[26] else None,
            elevators=row[27].strip() if row[27] and row[27] != 'Нет' else None,
            freight_elevators=row[28].strip() if row[28] else None,
            parking=row[29].strip(),
            ownership=row[30].strip(),
            entrances=row[31].strip() if row[31] else None,
            rooms_on_floor=row[32].strip() if row[32] else None,
            penthouse=bool(row[33].strip()),
            terrace=bool(row[34].strip()),
            rooms_in_hous=row[35].strip() if row[35] else None,
            window_to=row[36].strip(),
        )
        obj.save()

        if row[13]:
            name, file = __get_file(row[13])
            obj.title_image.save(name, file)
        obj.save()

        for photo in row[14].split(';'):
            name, file = __get_file(photo.replace(' ', ''))
            im = RImage.objects.create(
                property=obj,
                name=row[0]
            )
            im.save()
            im.photo.save(name, file)
            im.save()
        obj.save()
        print(f'#{n:4}:  Resale Property {obj} created')

print(' - - - - - - - - - - Done - - - - - - - - - - ')
