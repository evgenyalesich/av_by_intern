# Generated by Django 5.0 on 2023-12-30 10:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(choices=[('Audi', 'Audi'), ('BMW', 'BMW'), ('Mercedes-Benz', 'Mercedes-Benz')], max_length=100, verbose_name='Марка')),
                ('model', models.CharField(choices=[('100', '100'), ('200', '200'), ('50', '50'), ('80', '80'), ('90', '90'), ('920', '920'), ('A1', 'A1'), ('A2', 'A2'), ('A3', 'A3'), ('A4', 'A4'), ('A4 Allroad', 'A4 Allroad'), ('A5', 'A5'), ('A6', 'A6'), ('A6 Allroad', 'A6 Allroad'), ('A7', 'A7'), ('A8', 'A8'), ('Cabriolet', 'Cabriolet'), ('Coupe', 'Coupe'), ('E-Tron', 'E-Tron'), ('E-Tron S', 'E-Tron S'), ('E-Tron S Sportback', 'E-Tron S Sportback'), ('E-Tron Sportback', 'E-Tron Sportback'), ('NSU RO 80', 'NSU RO 80'), ('Q2', 'Q2'), ('Q3', 'Q3'), ('Q3 Sportback', 'Q3 Sportback'), ('Q4 e-tron', 'Q4 e-tron'), ('Q5', 'Q5'), ('Q5 Sportback', 'Q5 Sportback'), ('Q7', 'Q7'), ('Q8', 'Q8'), ('Quattro', 'Quattro'), ('R8', 'R8'), ('R8 LMP', 'R8 LMP'), ('RS 2', 'RS 2'), ('RS 3', 'RS 3'), ('RS 4', 'RS 4'), ('RS 5', 'RS 5'), ('RS 6', 'RS 6'), ('RS 7', 'RS 7'), ('RS Q3', 'RS Q3'), ('RS Q3 Sportback', 'RS Q3 Sportback'), ('RS Q8', 'RS Q8'), ('S1', 'S1'), ('S2', 'S2'), ('S3', 'S3'), ('S4', 'S4'), ('S5', 'S5'), ('S6', 'S6'), ('S7', 'S7'), ('S8', 'S8'), ('SQ2', 'SQ2'), ('SQ5', 'SQ5'), ('SQ5 Sportback', 'SQ5 Sportback'), ('SQ7', 'SQ7'), ('SQ8', 'SQ8'), ('TT', 'TT'), ('TT RS', 'TT RS'), ('TTS', 'TTS'), ('Typ R', 'Typ R'), ('V8', 'V8'), ('02 (E10)', '02 (E10)'), ('1 Серии', '1 Серии'), ('1M', '1M'), ('2 Серии', '2 Серии'), ('2 Серии A', '2 Серии A'), ('2 Серии G', '2 Серии G'), ('2000 C/Cs', '2000 C/Cs'), ('3 Серии', '3 Серии'), ('3/15', '3/15'), ('315', '315'), ('3200', '3200'), ('321', '321'), ('326', '326'), ('327', '327'), ('340', '340'), ('4 Серии', '4 Серии'), ('5 Серии', '5 Серии'), ('501', '501'), ('502', '502'), ('503', '503'), ('507', '507'), ('6 Серии', '6 Серии'), ('600', '600'), ('7 Серии', '7 Серии'), ('700', '700'), ('8 Серии', '8 Серии'), ('E3', 'E3'), ('E9', 'E9'), ('M2', 'M2'), ('M3', 'M3'), ('M4', 'M4'), ('M5', 'M5'), ('M6', 'M6'), ('M8', 'M8'), ('New Class', 'New Class'), ('X1', 'X1'), ('X2', 'X2'), ('X3', 'X3'), ('X3 M', 'X3 M'), ('X4', 'X4'), ('X4 M', 'X4 M'), ('X5', 'X5'), ('X5 M', 'X5 M'), ('X6', 'X6'), ('X6 M', 'X6 M'), ('X7', 'X7'), ('XM', 'XM'), ('Z1', 'Z1'), ('Z3', 'Z3'), ('Z3 M', 'Z3 M'), ('Z4', 'Z4'), ('Z4 M', 'Z4 M'), ('Z8', 'Z8'), ('i3', 'i3'), ('i4', 'i4'), ('i8', 'i8'), ('iX', 'iX'), ('iX3', 'iX3'), ('190 (W201)', '190 (W201)'), ('190 SL', '190 SL'), ('A-Класс', 'A-Класс'), ('A-Класс AMG', 'A-Класс AMG'), ('AMG GT', 'AMG GT'), ('B-Класс', 'B-Класс'), ('C-Класс', 'C-Класс'), ('C-Класс AMG', 'C-Класс AMG'), ('CL-Класс', 'CL-Класс'), ('CL-Класс AMG', 'CL-Класс AMG'), ('CLA', 'CLA'), ('CLA AMG', 'CLA AMG'), ('CLC-Класс', 'CLC-Класс'), ('CLK-Класс', 'CLK-Класс'), ('CLK-Класс AMG', 'CLK-Класс AMG'), ('CLS', 'CLS'), ('CLS AMG', 'CLS AMG'), ('Citan', 'Citan'), ('E-Класс', 'E-Класс'), ('E-Класс AMG', 'E-Класс AMG'), ('EQA', 'EQA'), ('EQC', 'EQC'), ('EQE', 'EQE'), ('EQS', 'EQS'), ('EQS SUV', 'EQS SUV'), ('EQV', 'EQV'), ('G-Класс', 'G-Класс'), ('G-Класс AMG', 'G-Класс AMG'), ('G-Класс AMG 6x6', 'G-Класс AMG 6x6'), ('GL-Класс', 'GL-Класс'), ('GL-Класс AMG', 'GL-Класс AMG'), ('GLA', 'GLA'), ('GLA AMG', 'GLA AMG'), ('GLB', 'GLB'), ('GLB AMG', 'GLB AMG'), ('GLC', 'GLC'), ('GLC AMG', 'GLC AMG'), ('GLC Coupe', 'GLC Coupe'), ('GLC Coupe AMG', 'GLC Coupe AMG'), ('GLE', 'GLE'), ('GLE AMG', 'GLE AMG'), ('GLE Coupe', 'GLE Coupe'), ('GLE Coupe AMG', 'GLE Coupe AMG'), ('GLK-Класс', 'GLK-Класс'), ('GLS', 'GLS'), ('GLS AMG', 'GLS AMG'), ('M-Класс', 'M-Класс'), ('M-Класс AMG', 'M-Класс AMG'), ('MB', 'MB'), ('Maybach G 650 Landaulet', 'Maybach G 650 Landaulet'), ('Maybach GLS', 'Maybach GLS'), ('Maybach S-Класс', 'Maybach S-Класс'), ('Metris', 'Metris'), ('R-Класс', 'R-Класс'), ('R-Класс AMG', 'R-Класс AMG'), ('S-Класс', 'S-Класс'), ('S-Класс AMG', 'S-Класс AMG'), ('SL', 'SL'), ('SL AMG', 'SL AMG'), ('SLC', 'SLC'), ('SLC AMG', 'SLC AMG'), ('SLK', 'SLK'), ('SLK-Класс AMG', 'SLK-Класс AMG'), ('SLR Mclaren', 'SLR Mclaren'), ('SLS AMG', 'SLS AMG'), ('Simplex', 'Simplex'), ('V-Класс', 'V-Класс'), ('Vaneo', 'Vaneo'), ('Viano', 'Viano'), ('Vito', 'Vito'), ('W100', 'W100'), ('W105', 'W105'), ('W108', 'W108'), ('W110', 'W110'), ('W111', 'W111'), ('W114', 'W114'), ('W115', 'W115'), ('W120', 'W120'), ('W121', 'W121'), ('W123', 'W123'), ('W124', 'W124'), ('W128', 'W128'), ('W136', 'W136'), ('W142', 'W142'), ('W186', 'W186'), ('W188', 'W188'), ('W189', 'W189'), ('W191', 'W191'), ('W29', 'W29')], max_length=100, verbose_name='Модель')),
                ('year', models.CharField(choices=[('2023', '2023'), ('2022', '2022'), ('2021', '2021'), ('2020', '2020'), ('2019', '2019'), ('2018', '2018'), ('2017', '2017'), ('2016', '2016'), ('2015', '2015'), ('2014', '2014'), ('2013', '2013'), ('2012', '2012'), ('2011', '2011'), ('2010', '2010'), ('2009', '2009'), ('2008', '2008'), ('2007', '2007'), ('2006', '2006'), ('2005', '2005'), ('2004', '2004'), ('2003', '2003'), ('2002', '2002'), ('2001', '2001'), ('2000', '2000'), ('1999', '1999'), ('1998', '1998'), ('1997', '1997'), ('1996', '1996'), ('1995', '1995'), ('1994', '1994'), ('1993', '1993'), ('1992', '1992'), ('1991', '1991'), ('1990', '1990'), ('1989', '1989'), ('1988', '1988'), ('1987', '1987'), ('1986', '1986'), ('1985', '1985'), ('1984', '1984'), ('1983', '1983'), ('1982', '1982'), ('1981', '1981'), ('1980 или ранее', '1980 или ранее')], max_length=200, verbose_name='Год')),
                ('body_type', models.CharField(choices=[('Седан', 'Седан'), ('Универсал', 'Универсал'), ('Хэтчбек', 'Хэтчбек'), ('Минивэн', 'Минивэн '), ('Внедорожник', 'Внедорожник'), ('Купе', 'Купе'), ('Кабриолет', 'Кабриолет'), ('Микроавтобус', 'Микроавтобус'), ('Фургон', 'Фургон'), ('Пикап', 'Пикап'), ('Лимузин', 'Лимузин'), ('Лифтбек', 'Лифтбек')], max_length=200, verbose_name='Кузов')),
                ('transmission', models.CharField(choices=[('Автоматическая (автомат)', 'Автоматическая (автомат)'), ('Автоматическая (робот)', 'Автоматическая (робот)'), ('Автоматическая (вариатор)', 'Автоматическая (вариатор)'), ('Механика', 'Механика')], max_length=200, verbose_name='Коробка передач')),
                ('engine_type', models.CharField(choices=[('Бензин', 'Бензин'), ('Бензин (пропан-бутан)', 'Бензин (пропан-бутан)'), ('Бензин (метан)', 'Бензин (метан)'), ('Бензин (гибрид)', 'Бензин (гибрид)'), ('Дизель', 'Дизель'), ('Дизель (гибрид)', 'Дизель (гибрид)'), ('Электричество', 'Электричество')], max_length=200, verbose_name='Тип двигателя')),
                ('drive_unit', models.CharField(choices=[('Передний', 'Передний'), ('Задний', 'Задний'), ('Полный', 'Полный')], max_length=200, verbose_name='Привод')),
                ('engine_volume', models.CharField(choices=[('1.0 л', '1.0 л'), ('1.1 л', '1.1 л'), ('1.2 л', '1.2 л'), ('1.3 л', '1.3 л'), ('1.4 л', '1.4 л'), ('1.5 л', '1.5 л'), ('1.6 л', '1.6 л'), ('1.7 л', '1.7 л'), ('1.8 л', '1.8 л'), ('1.9 л', '1.9 л'), ('2.0 л', '2.0 л'), ('2.1 л', '2.1 л'), ('2.2 л', '2.2 л'), ('2.3 л', '2.3 л'), ('2.4 л', '2.4 л'), ('2.5 л', '2.5 л'), ('2.6 л', '2.6 л'), ('2.7 л', '2.7 л'), ('2.8 л', '2.8 л'), ('2.9 л', '2.9 л'), ('3.0 л', '3.0 л'), ('3.2 л', '3.2 л'), ('3.3 л', '3.3 л'), ('3.5 л', '3.5 л'), ('3.6 л', '3.6 л'), ('3.7 л', '3.7 л'), ('3.8 л', '3.8 л'), ('3.9 л', '3.9 л'), ('4.0 л', '4.0 л'), ('> 4.0 л', ' > 4.0 л')], max_length=200, verbose_name='Объём двигателя')),
                ('vin', models.CharField(blank=True, default='', max_length=150, verbose_name='VIN')),
                ('state', models.CharField(choices=[('С пробегом', 'С пробегом'), ('Новый', 'Новый')], max_length=100, verbose_name='Состояние')),
                ('mileage', models.IntegerField(verbose_name='Пробег, км')),
                ('color', models.CharField(choices=[('Белый', 'Белый'), ('Бордовый', 'Бордовый'), ('Жёлтый', 'Жёлтый'), ('Зелёный', 'Зелёный'), ('Коричневый', 'Коричневый'), ('Красный', 'Красный'), ('Оранжевый', 'Оранжевый'), ('Серебристый', 'Серебристый')], default='Белый', max_length=200, verbose_name='Цвет')),
                ('interior_material', models.CharField(choices=[('натуральная кожа', 'натуральная кожа'), ('искусственная кожа', 'искусственная кожа'), ('ткань', 'ткань'), ('велюр', 'велюр'), ('алькантара', 'алькантара'), ('комбинированные материалы', 'комбинированные материалы')], default='ткань', max_length=100, verbose_name='Материал салона')),
                ('interior_color', models.CharField(choices=[('светлый', 'светлый'), ('комби', 'комби'), ('тёмный', 'тёмный')], default='комби', max_length=100, verbose_name='Цвет салона')),
                ('abs', models.BooleanField(blank=True, default=False, verbose_name='ABS')),
                ('esp', models.BooleanField(blank=True, default=False, verbose_name='ESP')),
                ('asr', models.BooleanField(blank=True, default=False, verbose_name='ASR')),
                ('anti_slip', models.BooleanField(blank=True, default=False, verbose_name='Антипробуксовочная')),
                ('immobilizer', models.BooleanField(blank=True, default=False, verbose_name='Иммобилайзер')),
                ('alarm_system', models.BooleanField(blank=True, default=False, verbose_name='Сигнализация')),
                ('alloy_wheels', models.BooleanField(blank=True, default=False, verbose_name='Легкосплавные диски')),
                ('roof_rails', models.BooleanField(blank=True, default=False, verbose_name='Рейлинги на крыше')),
                ('trailer_coupling', models.BooleanField(blank=True, default=False, verbose_name='Фаркоп')),
                ('seats', models.BooleanField(blank=True, default=False, verbose_name='Сидений')),
                ('windshield', models.BooleanField(blank=True, default=False, verbose_name='Лобового стекла')),
                ('mirrors', models.BooleanField(blank=True, default=False, verbose_name='Зеркал')),
                ('steering_wheel', models.BooleanField(blank=True, default=False, verbose_name='Руля')),
                ('autonomous_heater', models.BooleanField(blank=True, default=False, verbose_name='Автономный отопитель')),
                ('engine_autorun', models.BooleanField(blank=True, default=False, verbose_name='Автозапуск двигателя')),
                ('cruise_control', models.BooleanField(blank=True, default=False, verbose_name='Круиз-контроль')),
                ('multimedia', models.BooleanField(blank=True, default=False, verbose_name='Управление мультимедиа с руля')),
                ('electric_seat_adjustment', models.BooleanField(blank=True, default=False, verbose_name='Электрорегулировка сидений')),
                ('front_electric_windows', models.BooleanField(blank=True, default=False, verbose_name='Передние электро-стеклоподъёмники')),
                ('rear_electric_windows', models.BooleanField(blank=True, default=False, verbose_name='Задние электро-стеклоподъёмники')),
                ('hatch', models.BooleanField(blank=True, default=False, verbose_name='Люк')),
                ('panoramic_roof', models.BooleanField(blank=True, default=False, verbose_name='Панорамная крыша')),
                ('front_cushions', models.BooleanField(blank=True, default=False, verbose_name='Передние подушки')),
                ('side_cushions', models.BooleanField(blank=True, default=False, verbose_name='Боковые подушки')),
                ('rear_cushions', models.BooleanField(blank=True, default=False, verbose_name='Задние подушки')),
                ('xenon', models.BooleanField(blank=True, default=False, verbose_name='Ксеноновые')),
                ('fog_lights', models.BooleanField(blank=True, default=False, verbose_name='Противотуманные')),
                ('led_lights', models.BooleanField(blank=True, default=False, verbose_name='Светодиодные')),
                ('aux_or_ipod', models.BooleanField(blank=True, default=False, verbose_name='AUX или iPod')),
                ('bluetooth', models.BooleanField(blank=True, default=False, verbose_name='Bluetooth')),
                ('cd_or_mp3', models.BooleanField(blank=True, default=False, verbose_name='CD или MP3')),
                ('usb', models.BooleanField(blank=True, default=False, verbose_name='USB')),
                ('multimedia_screen', models.BooleanField(blank=True, default=False, verbose_name='Мультимедийный экран')),
                ('regular_navigation', models.BooleanField(blank=True, default=False, verbose_name='Штатная навигация')),
                ('rain_sensor', models.BooleanField(blank=True, default=False, verbose_name='Датчик дождя')),
                ('rear_view_camera', models.BooleanField(blank=True, default=False, verbose_name='Камера заднего вида')),
                ('parking_sensors', models.BooleanField(blank=True, default=False, verbose_name='Парктроники')),
                ('monitoring_dead_zones_mirrors', models.BooleanField(blank=True, default=False, verbose_name='Контроль мертвых зон на зеркалах')),
                ('climate_control', models.BooleanField(blank=True, default=False, verbose_name='Климат-контроль')),
                ('conditioner', models.BooleanField(blank=True, default=False, verbose_name='Кондиционер')),
                ('registration_country', models.CharField(choices=[('Беларусь', 'Беларусь'), ('Россия', 'Россия'), ('Другая страна', 'Другая страна')], max_length=100, verbose_name='Страна регистрации')),
                ('accounting', models.CharField(choices=[('Беларусь', 'Беларусь'), ('Россия', 'Россия'), ('Другая страна', 'Другая страна')], max_length=100, verbose_name='Учёт')),
                ('photo', models.FileField(upload_to='Car', verbose_name='Фото')),
                ('youtube', models.URLField(blank=True, default='', verbose_name='Видео из YouTube')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('region', models.CharField(choices=[('Брестская', 'Брестская'), ('Гомельская', 'Гомельская'), ('Гродненская', 'Гродненская'), ('Могилевская', 'Могилевская'), ('Минская', 'Минская'), ('Витебская', 'Витебская')], max_length=200, verbose_name='Область')),
                ('city', models.CharField(choices=[('Брест', 'Брест'), ('Барановичи', 'Барановичи'), ('Береза', 'Береза'), ('Белоозёрск', 'Белоозёрск'), ('Высокое', 'Высокое'), ('Ганцевичи', 'Ганцевичи'), ('Давид', 'Давид'), ('Дрогичин', 'Дрогичин'), ('Жабинка', 'Жабинка'), ('Иваново', 'Иваново'), ('Ивацевичи', 'Ивацевичи'), ('Каменец', 'Каменец'), ('Кобрин', 'Кобрин'), ('Лунинец', 'Лунинец'), ('Ляховичи', 'Ляховичи'), ('Малорита', 'Малорита'), ('Микашевичи', 'Микашевичи'), ('Пинск', 'Пинск'), ('Пружаны', 'Пружаны'), ('Столин', 'Столин'), ('Гомель', 'Гомель'), ('Брагин', 'Брагин'), ('Буда', 'Буда'), ('Василевичи', 'Василевичи'), ('Ветка', 'Ветка'), ('Добруш', 'Добруш'), ('Ельск', 'Ельск'), ('Житковичи', 'Житковичи'), ('Жлобин', 'Жлобин'), ('Калинковичи', 'Калинковичи'), ('Корма', 'Корма'), ('Лельчицы', 'Лельчицы'), ('Лоев', 'Лоев'), ('Мозырь', 'Мозырь'), ('г.п. Октябрьский', 'г.п. Октябрьский'), ('Наровля', 'Наровля'), ('Петриков', 'Петриков'), ('Речица', 'Речица'), ('Рогачев', 'Рогачев'), ('Светлогорск', 'Светлогорск'), ('Хойники', 'Хойники'), ('Чечерск', 'Чечерск'), ('Гродно', 'Гродно'), ('Березовка', 'Березовка'), ('Берестовица', 'Берестовица'), ('Волковыск', 'Волковыск'), ('Вороново', 'Вороново'), ('Дятлово', 'Дятлово'), ('Зельва', 'Зельва'), ('Ивье', 'Ивье'), ('Кореличи', 'Кореличи'), ('Лида', 'Лида'), ('Мосты', 'Мосты'), ('Новогрудок', 'Новогрудок'), ('Островец', 'Островец'), ('Ошмяны', 'Ошмяны'), ('Свислочь', 'Свислочь'), ('Скидель', 'Скидель'), ('Слоним', 'Слоним'), ('Сморгонь', 'Сморгонь'), ('Щучин', 'Щучин'), ('Могилев', 'Могилев'), ('Белыничи', 'Белыничи'), ('Бобруйск', 'Бобруйск'), ('Быхов', 'Быхов'), ('Глуск', 'Глуск'), ('Горки', 'Горки'), ('Дрибин', 'Дрибин'), ('Кировск', 'Кировск'), ('Климовичи', 'Климовичи'), ('Кличев', 'Кличев'), ('Краснополье', 'Краснополье'), ('Круглое', 'Круглое'), ('Костюковичи', 'Костюковичи'), ('Кричев', 'Кричев'), ('Мстиславль', 'Мстиславль'), ('Осиповичи', 'Осиповичи'), ('Славгород', 'Славгород'), ('Чаусы', 'Чаусы'), ('Чериков', 'Чериков'), ('Шклов', 'Шклов'), ('Хотимск', 'Хотимск'), ('Минск', 'Минск'), ('Березино', 'Березино'), ('Борисов', 'Борисов'), ('Вилейка', 'Вилейка'), ('Воложин', 'Воложин'), ('Дзержинск', 'Дзержинск'), ('Жодино', 'Жодино'), ('Заславль', 'Заславль'), ('Клецк', 'Клецк'), ('Копыль', 'Копыль'), ('Крупки', 'Крупки'), ('Логойск', 'Логойск'), ('Любань', 'Любань'), ('Марьина горка', 'Марьина горка'), ('Молодечно', 'Молодечно'), ('Мядель', 'Мядель'), ('Несвиж', 'Несвиж'), ('Руденск', 'Руденск'), ('Слуцк', 'Слуцк'), ('Смолевичи', 'Смолевичи'), ('Солигорск', 'Солигорск'), ('Старые', 'Старые'), ('Столбцы', 'Столбцы'), ('Узда', 'Узда'), ('Фаниполь', 'Фаниполь'), ('Червень', 'Червень'), ('Витебск', 'Витебск'), ('Бешенковичи', 'Бешенковичи'), ('Барань', 'Барань'), ('Браслав', 'Браслав'), ('Верхнедвинск', 'Верхнедвинск'), ('Глубокое', 'Глубокое'), ('Городок', 'Городок'), ('Докшицы', 'Докшицы'), ('Дубровно', 'Дубровно'), ('Лепель', 'Лепель'), ('Лиозно', 'Лиозно'), ('Миоры', 'Миоры'), ('Новолукомль', 'Новолукомль'), ('Новополоцк', 'Новополоцк'), ('Орша', 'Орша'), ('Полоцк', 'Полоцк'), ('Поставы', 'Поставы'), ('Россоны', 'Россоны'), ('Сенно', 'Сенно'), ('Толочин', 'Толочин'), ('Ушачи', 'Ушачи'), ('Чашники', 'Чашники'), ('Шарковщина', 'Шарковщина'), ('Шумилино', 'Шумилино')], max_length=200, verbose_name='Город')),
                ('name', models.CharField(max_length=200, verbose_name='Имя продавца')),
                ('phone', models.CharField(max_length=9, verbose_name='Номер телефона')),
                ('phone2', models.CharField(max_length=9, verbose_name='Номер телефона 2')),
                ('phone3', models.CharField(max_length=9, verbose_name='Номер телефона 3')),
                ('user_create', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь, создавший запись')),
            ],
            options={
                'verbose_name': 'Легковой автомобиль',
                'verbose_name_plural': 'Легковые авто',
            },
        ),
    ]
