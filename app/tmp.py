from curses.ascii import SI
import os, django
from urllib import request
import requests
import csv
import re
from django.core.files import File
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'abig.settings')
django.setup()

from aproperty.models import AreaPeculiarity, Area, Specialist, SiteData
from resale.models import ResaleProperty, ReImage


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

site_pk = input('Enter Site Data PK :\n')
site_data = SiteData.objects.get(pk=int(site_pk))

resale_file_dir = input('Enter the file dir with Resale Property:\n')
resale = read_csv(resale_file_dir)[26:]
for n, row in enumerate(resale):
    if len(row) > 1:
        row = list(map(lambda x: (None if str(x) == 'nan' else x), row))
        obj = ResaleProperty.objects.create(
            site=site_data,
            name=row[7],
            slug=f'room-{n}',
            price=row[8],
            area=Area.objects.first(),
            map_script=MAP.format(url=row[11]),
            addres=row[12].strip(),
            description=row[15],
            specialist=Specialist.objects.first(),
            square=float(row[18].strip()) if row[18] else None,
            rooms_number=int(re.findall('\d+', row[19])[0]) if re.findall('\d+', row[19]) else None,
            floor=int(re.findall('\d+', row[20].strip())[0]),
            floor_number=int(re.findall('\d+', row[21].strip())[0]),
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
            im = ReImage.objects.create(
                property=obj,
                name=row[0]
            )
            im.save()
            im.photo.save(name, file)
            im.save()
        obj.save()
        print(f'#{n:4}:  Resale Property {obj} created')

print(' - - - - - - - - - - Done - - - - - - - - - - ')
