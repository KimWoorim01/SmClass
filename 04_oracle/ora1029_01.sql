

update member set name = '홍길동' where id = 1;

commit;



--테이블 생성하면서 복사
create table emp2 as select * from employees;

--테이블 구조만 복사
create table emp2 as select * from employees where 1=2;

commit;


select * from emp2;

drop table emp2;


--테이블이 존재할경우 데이터만 복사
create table member2 as select * from member where 1=2;

select * from member2;

--테이블 내용을 복사
insert into member2 select * from member;

--컬럼데이터 타입, 길이 변경 (내용은 비어 있어야 한다.)
alter table member modify pw number(10);

delete member;

desc member;


--테이블 구조
desc employees;



select * from employees;

select employee_id, emp_name, hire_date from employees;

--연산자 : 산술연산자, +,-,*,/

drop table member;
drop table member2;
drop table emp2;


create table member (
	id number,
	pw varchar2(4),
	name VARCHAR2(50),
	email VARCHAR2(50),
	phone VARCHAR2(50),
	gender VARCHAR2(50),
	hobby varchar2(100),
	mdate DATE
);



select * from member;


--concat 명령어
select concat(employee_id,emp_name) from employees;

select emp_name,salary, salary*1384 from employees;

create table stu(
    no number(4),
    name varchar(20),
    kor number(3)
);

insert into stu values(1, '홍길동', 100);
insert into stu values(2, '유관순', 90);

commit;

insert into stu values(3,'',0);
insert into stu values(4,null,null);

select * from stu;

select commission_pct from employees where commission_pct is not null;

--nvl함수 :kor 컬럼에 null 값이 있으면 0으로 표시
select no,name,kor,nvl(kor,0)+100 from stu;


select salary, salary*12 as year_salary from employees;


select * from students;

select name as 이름, kor as 국어, eng as 영어, math as 수학, total as 합계, avg as 평균 from students;


select * from employees;

select employee_id || emp_name || email from employees;
select concat(concat(employee_id, emp_name), email) from employees;
select emp_name || ' is a ' || job_id from employees;

select department_id from employees;
--중복제거 distinct
select distinct department_id from employees;

--순차정렬 생략가능
select distinct department_id from employees order by department_id asc;
--역순정렬
select distinct department_id from employees order by department_id desc;

select substr(job_id,0,2) from employees;


--where절 : 조건 비교 연산자
select * from employees;
select * from employees where manager_id = 124;


select * from students;

select * from students where total > 250;

select * from students where eng > 70 and eng < 90;


select * from employees where salary > 5000 and salary < 8000;

select * from employees where salary != 8000;

select count(*) from employees where department_id != 50;

select count(*) from employees where department_id is null;

select employee_id as 사원번호, emp_name as 이름 , salary as 월급 from employees where salary <= 4000;


select * from employees where hire_date <= '1999/12/31';


select * from employees where department_id = 80 and job_id like '%MAN%';  


select * from employees where commission_pct = 0.2 or commission_pct = 0.3 or commission_pct = 0.5;

select * from employees where commission_pct in (0.2, 0.3);

select * from employees where employee_id in (110, 120, 130);


select hire_date from employees where hire_date in ('2004/02/17','2002/06/07');
select hire_date from employees where hire_date between '2004/02/17' and '2004/12/31';

select * from employees where job_id like '%MAN';























