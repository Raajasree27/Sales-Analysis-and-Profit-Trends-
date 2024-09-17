--Loading the data
create warehouse ecommerce;
create database sales;
create schema analytics;
create table products(product_name varchar, product_price varchar, product_review varchar);
create table suppliers(supplier_id varchar, supplier_name varchar, Product_name varchar, city varchar);
create table customer(first_name varchar, last_name varchar, customer_id varchar, city varchar, states varchar, country varchar, email varchar);
create table returnes(product_name varchar, order_id varchar, refund_amount int, return_date date, return_id varchar, return_reason varchar);
create table orders(customer_id varchar, order_id varhcar, product_name varchar, quantity int, unir_price int, order_date date, order_total int);
create table customer
