create database community_center;
create user vgst_group@localhost identified by 'VGST';
grant all privileges on community_center.* to vgst_group@localhost;


