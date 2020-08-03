

CREATE TABLE DM_SALES.ORDER_MONITOR
(
    supplementary_gtm_num varchar(32),
    position_num varchar(16) NOT NULL,
    position_vol numeric(18,3),
    order_num varchar(32) NOT NULL,
    order_vol numeric(18,3),
    supplementary_delta_vol numeric(18,3),
    order_status_code varchar(8),
    order_status_descr varchar(128)
);


ALTER TABLE DM_SALES.ORDER_MONITOR ADD CONSTRAINT c_pk PRIMARY KEY (position_num, order_num) DISABLED;

CREATE PROJECTION DM_SALES.ORDER_MONITOR /*+createtype(P)*/ 
(
 supplementary_gtm_num,
 position_num,
 position_vol,
 order_num,
 order_vol,
 supplementary_delta_vol,
 order_status_code,
 order_status_descr
)
AS
 SELECT ORDER_MONITOR.supplementary_gtm_num,
        ORDER_MONITOR.position_num,
        ORDER_MONITOR.position_vol,
        ORDER_MONITOR.order_num,
        ORDER_MONITOR.order_vol,
        ORDER_MONITOR.supplementary_delta_vol,
        ORDER_MONITOR.order_status_code,
        ORDER_MONITOR.order_status_descr
 FROM DM_SALES.ORDER_MONITOR
 ORDER BY ORDER_MONITOR.supplementary_gtm_num
SEGMENTED BY hash(ORDER_MONITOR.position_num, ORDER_MONITOR.order_num) ALL NODES KSAFE 1;


SELECT MARK_DESIGN_KSAFE(1);
