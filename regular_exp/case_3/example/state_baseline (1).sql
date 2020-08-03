

CREATE TABLE DM_MTOIR.BEACON
(
    id int NOT NULL,
    name varchar(255),
    has_equipment boolean,
    id_machine int,
    machine_name varchar(255)
);

ALTER TABLE DM_MTOIR.BEACON ADD CONSTRAINT c_primary PRIMARY KEY (id) DISABLED;

CREATE PROJECTION DM_MTOIR.BEACON /*+createtype(P)*/ 
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
