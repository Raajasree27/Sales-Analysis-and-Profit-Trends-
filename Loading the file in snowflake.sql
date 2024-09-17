--Loading the data
create warehouse ecommerce;
create database sales;
create schema analytics;
create table products(product_name varchar, product_price varchar, product_review varchar);
create table suppliers(supplier_id varchar, supplier_name varchar, Product_name varchar, city varchar);
create table customer(first_name varchar, last_name varchar, customer_id varchar, city varchar, states varchar, country varchar, email varchar);
create table eturns(product_name varchar, order_id varchar, refund
