/*
this script uses MySql to add tables and populate them with data for an inventory database.
The database already exists and is named 'inventory'
*/

use inventory;

create table products (
    product_id int not null auto_increment primary key,
    product_name varchar(50) not null,
    product_description varchar(255),
    product_price decimal(10,2) not null
);