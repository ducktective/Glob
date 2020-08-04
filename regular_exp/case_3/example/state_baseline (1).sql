

CREATE TABLE FMU_TEST_OBJECTS.FMU_TEST_TABLE_1
(
    test int,
    up1 varchar(256),
	up2 varchar(256)
);










SELECT MARK_DESIGN_KSAFE(0);
﻿


CREATE TABLE ODS_SAPERP.ADRC
(
    address_id varchar(256),    
    addrnumber varchar(256) NOT NULL,    
    addr_group varchar(256),    
    adrc_err_status varchar(256),    
    adrc_uuid varchar(256),    
    building varchar(256),    
    chckstatus varchar(256),    
    city1 varchar(256),    
    city2 varchar(256),    
    cityh_code varchar(256),    
    cityp_code varchar(256),    
    city_code varchar(256),    
    city_code2 varchar(256),    
    client integer NOT NULL,    
    country varchar(256),    
    county varchar(256),    
    county_code varchar(256),    
    date_from date NOT NULL,    
    date_to date,    
    deflt_comm varchar(256),    
    deli_serv_number varchar(256),    
    deli_serv_type varchar(256),    
    dont_use_p varchar(256),    
    dont_use_s varchar(256),    
    duns varchar(256),    
    dunsp4 varchar(256),    
    extension1 varchar(256),    
    extension2 varchar(256),    
    fax_extens varchar(256),    
    fax_number varchar(256),    
    flagcomm10 varchar(256),    
    flagcomm11 varchar(256),    
    flagcomm12 varchar(256),    
    flagcomm13 varchar(256),    
    flagcomm2 varchar(256),    
    flagcomm3 varchar(256),    
    flagcomm4 varchar(256),    
    flagcomm5 varchar(256),    
    flagcomm6 varchar(256),    
    flagcomm7 varchar(256),    
    flagcomm8 varchar(256),    
    flagcomm9 varchar(256),    
    flaggroups varchar(256),    
    floor varchar(256),    
    home_city varchar(256),    
    house_num1 varchar(256),    
    house_num2 varchar(256),    
    id_category varchar(256),    
    langu varchar(256),    
    langu_crea varchar(256),    
    location varchar(256),    
    mc_city1 varchar(256),    
    mc_county varchar(256),    
    mc_name1 varchar(256),    
    mc_street varchar(256),    
    mc_township varchar(256),    
    name1 varchar(256),    
    name2 varchar(256),    
    name3 varchar(256),    
    name4 varchar(256),    
    name_co varchar(256),    
    name_text varchar(256),    
    nation varchar(256) NOT NULL,    
    pers_addr varchar(256),    
    post_code1 varchar(256),    
    post_code2 varchar(256),    
    post_code3 varchar(256),    
    po_box varchar(256),    
    po_box_cty varchar(256),    
    po_box_lobby varchar(256),    
    po_box_loc varchar(256),    
    po_box_num varchar(256),    
    po_box_reg varchar(256),    
    regiogroup varchar(256),    
    region varchar(256),    
    roomnumber varchar(256),    
    sort1 varchar(256),    
    sort2 varchar(256),    
    street varchar(256),    
    streetcode varchar(256),    
    str_suppl1 varchar(256),    
    str_suppl2 varchar(256),    
    str_suppl3 varchar(256),    
    taxjurcode varchar(256),    
    tel_extens varchar(256),    
    tel_number varchar(256),    
    time_zone varchar(256),    
    title varchar(256),    
    township varchar(256),    
    township_code varchar(256),    
    transpzone varchar(256),    
    uuid_belated varchar(256),    
    xpcpt varchar(256),    
    addrorigin varchar(256),    
    house_num3 varchar(256),    
    pcode1_ext varchar(256),    
    pcode2_ext varchar(256),    
    pcode3_ext varchar(256),    
    postalarea varchar(256),    
    sort_phn varchar(256),    
    streetabbr varchar(256),    
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

CREATE TABLE DM_MTOIR.BEACON
(
    id int NOT NULL,
    name varchar(255),
    has_equipment boolean,
    id_machine int,
    machine_name varchar(255)
);

ALTER TABLE DM_MTOIR.BEACON ADD CONSTRAINT c_primary PRIMARY KEY (id) DISABLED;

CREATE PROJECTION DM_MTOIR.BEACON 
 
(
 id,
 name,
 has_equipment,
 id_machine,
 machine_name
)
AS
 SELECT BEACON.id,
        BEACON.name,
        BEACON.has_equipment,
        BEACON.id_machine,
        BEACON.machine_name
 FROM DM_MTOIR.BEACON
 ORDER BY BEACON.id
SEGMENTED BY hash(BEACON.id) ALL NODES KSAFE 1;


SELECT MARK_DESIGN_KSAFE(1);
