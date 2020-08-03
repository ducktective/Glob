/* AUTHOR: DIGAYLOVAAM, DESCRIPTION: DDL на создание таблицы ADRC в слое ODS */

CREATE TABLE ODS_SAPERP.ADRC
(
    address_id varchar(256),    --(не поддерживается) Ид. адреса физического адреса
    addrnumber varchar(256) NOT NULL,    --Номер адреса
    addr_group varchar(256),    --Группа адресов (ключ) (сервисы бизнес-адресов)
    adrc_err_status varchar(256),    --Ошибочный статус адреса
    adrc_uuid varchar(256),    --UUID, используемый в адресе
    building varchar(256),    --Здание (номер или код)
    chckstatus varchar(256),    --Контрольный статус для файла города
    city1 varchar(256),    --Город
    city2 varchar(256),    --Район города
    cityh_code varchar(256),    --Кодировка другого местожит. для файла города/станд. файла
    cityp_code varchar(256),    --Кодирование района города для файла города и улицы
    city_code varchar(256),    --Кодирование города для файла города и улицы
    city_code2 varchar(256),    --Код города - почтовый индекс (файл города)
    client integer NOT NULL,    --Мандант
    country varchar(256),    --Код страны
    county varchar(256),    --Округ (США: county)
    county_code varchar(256),    --Код округа
    date_from date NOT NULL,    --Дата "Действительно с" - в акт. версии возм. только 00010101
    date_to date,    --Дата действ. по - в актуал. версии возм. только 99991231
    deflt_comm varchar(256),    --Вид связи (ключ) (сервисы бизнес-адресов)
    deli_serv_number varchar(256),    --Номер сервиса доставки
    deli_serv_type varchar(256),    --Вид сервиса доставки
    dont_use_p varchar(256),    --Индикатор непоставки для адреса почтового ящика
    dont_use_s varchar(256),    --Индикатор непоставки при адресе улицы
    duns varchar(256),    --Номер Dun&Bradstreet (D-U-N-S)
    dunsp4 varchar(256),    --Номер D-U-N-S+4 (последние 4 знака)
    extension1 varchar(256),    --Расширение (только для преобр. данных) (напр. канал данных)
    extension2 varchar(256),    --Расширение (только для преобр. данных) (напр. телебокс)
    fax_extens varchar(256),    --Первый номер факса: внутренний номер
    fax_number varchar(256),    --Первый номер факса: код + номер
    flagcomm10 varchar(256),    --Индикатор: принтер введен
    flagcomm11 varchar(256),    --Индикатор: SSF введен
    flagcomm12 varchar(256),    --Индикатор: URI/FTP-адрес введен
    flagcomm13 varchar(256),    --Индикатор: адрес пейджера введен
    flagcomm2 varchar(256),    --Индикатор: номер(а) телефона(ов) введен(ы)
    flagcomm3 varchar(256),    --Индикатор: номер(а) факса(ов) введен(ы)
    flagcomm4 varchar(256),    --Индикатор: номер(а) телетекса(ов) введен(ы)
    flagcomm5 varchar(256),    --Индикатор: номер(а) телекса(ов) введен(ы)
    flagcomm6 varchar(256),    --Индикатор: E-Mail-адрес(а) определен(ы)
    flagcomm7 varchar(256),    --Индикат.: адрес(а) дистанц. электр. почты (R/Mail) введен(ы)
    flagcomm8 varchar(256),    --Индикатор: X.400-адрес(а) введен(ы)
    flagcomm9 varchar(256),    --Индикатор: RFC-адрес(а) назначения введен(ы)
    flaggroups varchar(256),    --Индикатор: существуют другие присвоения к группам адресов
    floor varchar(256),    --Этаж в здании
    home_city varchar(256),    --Местожительство (отличается от почтового нас. пункта)
    house_num1 varchar(256),    --Номер дома
    house_num2 varchar(256),    --Дополнение к номеру дома
    id_category varchar(256),    --Категория ид. адреса
    langu varchar(256),    --Код языка
    langu_crea varchar(256),    --Язык оригинала при создании записи адреса
    location varchar(256),    --Наименование региона 2
    mc_city1 varchar(256),    --Название города прописными буквами для средства поиска
    mc_county varchar(256),    --Название округа прописными буквами для средства поиска
    mc_name1 varchar(256),    --Имя ПРОПИСНЫМИ БУКВАМИ для средства поиска (поле NAME1)
    mc_street varchar(256),    --Название улицы прописными буквами для средства поиска
    mc_township varchar(256),    --Название города прописными буквами для средства поиска
    name1 varchar(256),    --Имя 1
    name2 varchar(256),    --Имя 2
    name3 varchar(256),    --Имя 3
    name4 varchar(256),    --Имя 4
    name_co varchar(256),    --Наименование региона 1
    name_text varchar(256),    --Преобразованное поле имени (с обращением)
    nation varchar(256) NOT NULL,    --Идентификатор версии для международных адресов
    pers_addr varchar(256),    --Индикатор: речь идёт о личном адресе
    post_code1 varchar(256),    --Почтовый индекс города
    post_code2 varchar(256),    --Почтовый индекс почтового ящика
    post_code3 varchar(256),    --Почтовый индекс фирмы (для крупных клиентов)
    po_box varchar(256),    --Почтовый ящик
    po_box_cty varchar(256),    --Страна для почтового ящика
    po_box_lobby varchar(256),    --Отделение почтовых ящиков (PO Box Lobby)
    po_box_loc varchar(256),    --Город почтового ящика
    po_box_num varchar(256),    --Индикатор: указание почтового ящика без номера
    po_box_reg varchar(256),    --Регион к п/ящику (штат, фед. земля, провинция, область, ...)
    regiogroup varchar(256),    --Группировка региональной структуры
    region varchar(256),    --Регион (штат, федер. земля, провинция, область, графство)
    roomnumber varchar(256),    --Номер квартиры или помещения
    sort1 varchar(256),    --Критерий поиска 1
    sort2 varchar(256),    --Критерий поиска 2
    street varchar(256),    --Улица
    streetcode varchar(256),    --Кодировка улицы для файла города и улицы
    str_suppl1 varchar(256),    --Улица 2
    str_suppl2 varchar(256),    --Улица 3
    str_suppl3 varchar(256),    --Улица 4
    taxjurcode varchar(256),    --Место налогообложения
    tel_extens varchar(256),    --Первый номер телефона: внутренний номер
    tel_number varchar(256),    --Первый номер телефона: код + номер
    time_zone varchar(256),    --Часовой пояс адреса
    title varchar(256),    --Ключ обращения
    township varchar(256),    --Город
    township_code varchar(256),    --Код города
    transpzone varchar(256),    --Транспортная зона, в которую/из которой идет поставка
    uuid_belated varchar(256),    --Индикатор: UUID создан впоследствии дополнительно
    xpcpt varchar(256),    --Индикатор для окончания целевого назначения
    addrorigin varchar(256),    --(не поддерживается) Источник данных по адресу (ключ)
    house_num3 varchar(256),    --(не поддерживается) диапазон номеров домов
    pcode1_ext varchar(256),    --(не поддерж.) Расширение к п/инд. города,напр., код ZIP+4+2
    pcode2_ext varchar(256),    --(не поддерж.)Расшир. к п/индексу п/ящика, напр., код ZIP+4+2
    pcode3_ext varchar(256),    --(не поддерживается) Расширение к п/инд. крупного клиента
    postalarea varchar(256),    --(не поддерживается) почтовый участок
    sort_phn varchar(256),    --(не поддерж-ся) Поле сортировки для фонетического поиска
    streetabbr varchar(256),    --(не поддерживается) Сокращение для названия улицы
    tech_load_ts timestamp(6) NOT NULL,
    tech_job_id integer,
    tech_is_deleted integer,
    tech_delete_ts timestamp(6) NOT NULL,
    CONSTRAINT C_PRIMARY PRIMARY KEY (client, addrnumber, date_from, nation, tech_load_ts) DISABLED
)
ORDER BY
    client, addrnumber, date_from, nation, tech_load_ts
SEGMENTED BY hash(client, addrnumber, date_from, nation, tech_load_ts)
ALL NODES;