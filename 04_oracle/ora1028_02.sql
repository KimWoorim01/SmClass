--select * from employees;
--
--select * from customers;
--
--select * from products;

create table students (
no number(4),
name varchar2(20),
kor number(3),
eng number(3),
math number(3),
total number(3),
avg number(10),
rank number(4)
);

insert into students (no, name, kor, eng, math, total, avg, rank) values (
1, '이순신', 80, 95, 100, 275, (275/3), 1
);

insert into students (no, name, kor, eng, math, total, avg, rank) values (
2, '홍길동', 90, 95, 100, 275, (285/3), 2
);

select * from students

commit;

rollback;

--테이블삭제
--drop table students;

select * from employees;

create table member(
id varchar2(20) primary key,
pw varchar2(20),
name varchar2(20),
phone varchar2(20)
);

insert into member (id,pw,name,phone) values(
'aaa',
'1111',
'홍길동',
'010-1111-4444'
);

select * from member;

commit;

insert into member values(
'eee','1111','유관순','010-3333-9999'
);

insert into member (id,pw) values(
'ffff','1111'
);


select id from member;

update member set name = '홍길자' where id = 'aaa';

delete member where id='ffff';

commit;



