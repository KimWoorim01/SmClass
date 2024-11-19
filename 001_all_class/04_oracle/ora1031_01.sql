

select * from member;

commit;

select hire_date,round(hire_date,'Month') from employees;
select hire_date, trunc(hire_date,'month') from employees;

select sysdate, add_months(trunc(sysdate,'month'),1) from dual;


select hire_date, add_months(trunc(hire_date,'month'),1) from employees;

select sysdate, add_months(sysdate,12) from dual;

select hire_date, add_months(hire_date,12) from employees;

select hire_date, add_months(hire_date,12), last_day(add_months(hire_date,12)) from employees;


select hire_date, last_day(add_months(hire_date,12)) from employees where last_day(add_months(hire_date,12)) in ('07/08/31','08/08/31','07/09/30','07/10/31');


select sysdate from dual;

select extract(year from sysdate) from dual;
select extract(month from sysdate) from dual;
select extract(day from sysdate) from dual;

select systimestamp from dual;
select extract(hour from systimestamp) from dual;
select extract(minute from systimestamp) from dual;
select extract(second from systimestamp) from dual;


select sysdate, substr(sysdate,4,2) from dual;

select to_char(sysdate,'yyyy-mm-dd') from dual;

select to_char(hire_date,'yyyy-mm-dd') from employees;



create table chartable(
no number(4),
kor number(10),
kor_char varchar2(10),
kor_mark varchar2(10)
);

drop table chartable1;

insert into chartable values(
1,10000,to_char(10000,'00000000'),to_char(10000,'0,000,000')
);

select * from chartable;



select salary from employees;


select sum(salary) from employees;

select round(avg(salary),4) from employees;
select trunc(avg(salary),4) from employees;

select max(salary) from employees;
select min(salary) from employees;

select count(salary) from employees where salary >= (select round(avg(salary),4) from employees);


--단일함수와 그룹함수를 같이 사용할수 없음


select sum(salary), avg(salary), max(salary), min(salary) from employees where department_id = 50;


select department_id, max(salary) from employees group by department_id;

select count(salary), max(salary), min(salary) from employees where salary >= (select avg(salary) from employees);



--수학함수 abs: 절대값:ceil 올림:floor 버림 round:반올림 trunc:절사 mod:나머지 power:제곱 sqrt:제곱근

--initcap: 첫글자 대문자 취환
--lpad , rpad 자리수 채우기
select 'joHn',lpad('john',10,'#'),rpad('john',10,'#') from dual;

--trim 공백 없애기


select * from employees where substr(hire_date,4,2) = 03;

select * from students where  length(name) >= 5;

select sum(eng), round(avg(eng),2), max(eng), min(eng) from students;

select * from students;

select * from employees;

select emp_name, to_char(hire_date,'"등록일 : "yyyy"년 "mm"월 "dd"일"') from employees; 




