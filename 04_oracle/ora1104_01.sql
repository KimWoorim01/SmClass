drop table emp02;
drop table mem2;
select * from mem;
create table emp02(
empno number(4) not null,
ename varchar2(30) not null,
job varchar2(9),
deptno number(2)
);
insert into emp02 values(
1,'홍길동','clerk',2
);
-- null
insert into emp02 values(
2,'유관순',null,null
);
insert into emp02 values(
3,null,null,null
);
drop table emp02;
create table emp02(
empno number(4) unique,
ename varchar2(30) not null,
job varchar2(9),
deptno number(2)
);
insert into emp02 values(
1,'홍길동','clerk',2
);
insert into emp02 values(
2,'유관순',null,null
);
insert into emp02 values(
3,'이순신',null,null
);
insert into emp02 values(
null,'강감찬',null,null
);
-- unique 에러
insert into emp02 values(
2,'김구',null,null
);
select * from emp02;
delete emp02 where empno is null;
commit;
-- 제약조건 변경 alter
alter table emp02 modify empno not null;
alter table emp02 modify empno;
-- not null, pk_emp02_empno 별칭
alter table emp02 add constraint pk_emp02_empno primary key(empno);
alter table emp02 drop constraint pk_emp02_empno;
create table emp02(
empno number(4) primary key,
ename varchar2(30) not null,
job varchar2(9),
deptno number(2)
);
drop table mem;
create table mem (
id varchar2(30) primary key,
pw varchar2(30) not null,
name varchar2(100) default '무명',
gender varchar2(6) check(gender in ('Male','Female')) -- male,female,MALE,FEMALE 입력시 에러
);
insert into mem values(
'aaa','1111','홍길동','Male'
);
insert into mem values(
'bbb','1111','유관순','Female'  -- female 에러
);
commit;
create table board2 (
bno number(4) primary key,
btitle varchar2(1000) not null,
id varchar2(30),
constraint fk_board2_id foreign key(id) references mem(id)
);
select * from mem;
delete mem where id='aaa';
-- 외래키로 등록시 부모키에 해당 값이 없을시 에러
insert into board2 values(
4,'제목4','bbb'
);
-- 외래키 삭제
alter table board2 drop constraint fk_board2_id;
-- 부모키 삭제시, 외래키로 등록된 값들을 모두 삭제
alter table board2
add constraint fk_board2_id foreign key (id)
references mem(id) on delete cascade;  -- on delete set null
-- default : on delete restricted : 부모키 삭제시, 외래키에 등록된 값이 있으면, 삭제가 되지 않음.
-- on delete set null : 부모키 삭제시, 외래키로 등록된 값을 삭제는 하지 않고, 해당되는 컬럼값만 null 처리
-- 부모테이블의 aaa삭제시, 자식테이블의 aaa글이 모두 삭제
delete mem where id='aaa';
select * from mem;
select * from board2;
select id,pw,name,deptno, decode(deptno, 10, '총무부', 20 , '인사부', 30 , '마케팅') from mem;


select substr(job_id,4) j_id , salary,
decode (substr(job_id,4),
'CLERK',salary*1.05,
'REP', salary*1.1,
'MAN',salary*1.15
) sal
from employees
where substr(job_id,4) in ('CLERK','REP','MAN')
;


create table lavel_data (
	id VARCHAR2(50) primary key,
	lavel number(1) not null
);

insert into lavel_data (id, lavel) values ('Arlen', 4);
insert into lavel_data (id, lavel) values ('Catie', 4);
insert into lavel_data (id, lavel) values ('Adoree', 5);
insert into lavel_data (id, lavel) values ('Cher', 4);
insert into lavel_data (id, lavel) values ('Dorita', 5);
insert into lavel_data (id, lavel) values ('Zulema', 1);
insert into lavel_data (id, lavel) values ('Richy', 4);
insert into lavel_data (id, lavel) values ('James', 5);
insert into lavel_data (id, lavel) values ('Aeriel', 5);
insert into lavel_data (id, lavel) values ('Reinald', 3);
insert into lavel_data (id, lavel) values ('Bernardina', 1);
insert into lavel_data (id, lavel) values ('Tiertza', 2);
insert into lavel_data (id, lavel) values ('Carolyne', 5);
insert into lavel_data (id, lavel) values ('Jonis', 1);
insert into lavel_data (id, lavel) values ('Abigael', 5);
insert into lavel_data (id, lavel) values ('Pauli', 4);
insert into lavel_data (id, lavel) values ('Sheffie', 2);
insert into lavel_data (id, lavel) values ('Tully', 2);
insert into lavel_data (id, lavel) values ('Ricard', 5);
insert into lavel_data (id, lavel) values ('Jameson', 3);
insert into lavel_data (id, lavel) values ('Thorstein', 1);
insert into lavel_data (id, lavel) values ('Arlyne', 5);
insert into lavel_data (id, lavel) values ('Mela', 5);
insert into lavel_data (id, lavel) values ('Yetta', 3);
insert into lavel_data (id, lavel) values ('Corilla', 4);
insert into lavel_data (id, lavel) values ('Adoree', 1);
insert into lavel_data (id, lavel) values ('Sabine', 3);
insert into lavel_data (id, lavel) values ('Nelson', 3);
insert into lavel_data (id, lavel) values ('Isahella', 5);
insert into lavel_data (id, lavel) values ('Mandel', 5);
insert into lavel_data (id, lavel) values ('Sasha', 4);
insert into lavel_data (id, lavel) values ('Deanne', 1);
insert into lavel_data (id, lavel) values ('Thorny', 1);
insert into lavel_data (id, lavel) values ('Jacki', 3);
insert into lavel_data (id, lavel) values ('Sibby', 2);
insert into lavel_data (id, lavel) values ('Jack', 2);
insert into lavel_data (id, lavel) values ('Chandra', 2);
insert into lavel_data (id, lavel) values ('Cecilla', 5);
insert into lavel_data (id, lavel) values ('Saunder', 1);
insert into lavel_data (id, lavel) values ('Way', 4);
insert into lavel_data (id, lavel) values ('Velma', 3);
insert into lavel_data (id, lavel) values ('Keelia', 1);
insert into lavel_data (id, lavel) values ('Clay', 4);
insert into lavel_data (id, lavel) values ('Grace', 2);
insert into lavel_data (id, lavel) values ('Maura', 5);
insert into lavel_data (id, lavel) values ('Karolina', 4);
insert into lavel_data (id, lavel) values ('Mal', 5);
insert into lavel_data (id, lavel) values ('Annette', 4);
insert into lavel_data (id, lavel) values ('Issy', 2);
insert into lavel_data (id, lavel) values ('Reid', 2);
insert into lavel_data (id, lavel) values ('Dall', 4);
insert into lavel_data (id, lavel) values ('Sukey', 2);
insert into lavel_data (id, lavel) values ('Etty', 5);
insert into lavel_data (id, lavel) values ('Kendall', 5);
insert into lavel_data (id, lavel) values ('Gibby', 4);
insert into lavel_data (id, lavel) values ('Kylila', 2);
insert into lavel_data (id, lavel) values ('Orelia', 2);
insert into lavel_data (id, lavel) values ('Alexei', 4);
insert into lavel_data (id, lavel) values ('Iorgo', 1);
insert into lavel_data (id, lavel) values ('Clive', 1);
insert into lavel_data (id, lavel) values ('Roger', 1);
insert into lavel_data (id, lavel) values ('Halette', 3);
insert into lavel_data (id, lavel) values ('Clyve', 3);
insert into lavel_data (id, lavel) values ('Peadar', 1);
insert into lavel_data (id, lavel) values ('Mose', 4);
insert into lavel_data (id, lavel) values ('Raimundo', 3);
insert into lavel_data (id, lavel) values ('Glori', 1);
insert into lavel_data (id, lavel) values ('Merrel', 2);
insert into lavel_data (id, lavel) values ('Ulberto', 2);
insert into lavel_data (id, lavel) values ('Bren', 4);
insert into lavel_data (id, lavel) values ('Ker', 2);
insert into lavel_data (id, lavel) values ('Rosalinda', 1);
insert into lavel_data (id, lavel) values ('Delphinia', 5);
insert into lavel_data (id, lavel) values ('Johnette', 3);
insert into lavel_data (id, lavel) values ('Marilyn', 3);
insert into lavel_data (id, lavel) values ('Paddy', 2);
insert into lavel_data (id, lavel) values ('Antony', 3);
insert into lavel_data (id, lavel) values ('Kinna', 5);
insert into lavel_data (id, lavel) values ('Rogers', 5);
insert into lavel_data (id, lavel) values ('Zolly', 5);
insert into lavel_data (id, lavel) values ('Lance', 1);
insert into lavel_data (id, lavel) values ('Carroll', 2);
insert into lavel_data (id, lavel) values ('Geralda', 2);
insert into lavel_data (id, lavel) values ('Riobard', 2);
insert into lavel_data (id, lavel) values ('Sunshine', 4);
insert into lavel_data (id, lavel) values ('Betteanne', 2);
insert into lavel_data (id, lavel) values ('Andrea', 1);
insert into lavel_data (id, lavel) values ('Theresina', 3);
insert into lavel_data (id, lavel) values ('Koenraad', 4);
insert into lavel_data (id, lavel) values ('Eydie', 1);
insert into lavel_data (id, lavel) values ('Karolina', 2);
insert into lavel_data (id, lavel) values ('Sutton', 5);
insert into lavel_data (id, lavel) values ('Ikey', 5);
insert into lavel_data (id, lavel) values ('Ugo', 1);
insert into lavel_data (id, lavel) values ('Mallory', 4);
insert into lavel_data (id, lavel) values ('Mariska', 2);
insert into lavel_data (id, lavel) values ('Edmund', 3);
insert into lavel_data (id, lavel) values ('Twyla', 5);
insert into lavel_data (id, lavel) values ('Laney', 5);
insert into lavel_data (id, lavel) values ('Onida', 4);


commit;

select * from lavel_data;

select id, lavel,decode(lavel, 1, '100point', 2 , '1000point', 3 , '5000point', 4, '10000point', 5 , '20000point') as point from lavel_data;


select id,lavel, case 
when lavel >= 1 and lavel <= 3 then 5000
when lavel >= 4 then 20000
en point
from lavel data;

drop table stu;

create table stu as select * from students;

select * from stu;

alter table stu add result varchar2(2);

update stu set result = (
case
when avg >= 90 then 'A'
when avg >= 80 then 'B'
when avg >= 70 then 'C'
when avg >= 60 then 'D'
when avg < 60 then 'F'
end);

select no,name,total, rank() over (order by total desc) from stu order by no;

select no,name,total, dense_rank() over(order by total desc) from stu;

update stu a set rank = (
    select ranks from ( select no,rank() over (order by total desc) as ranks from stu)b 
    where b.no = a.no
);


select emp_name, salary, 
case
when salary <= 5000 then salary * 1.15
when salary > 5000 and salary <= 8000 then salary * 1.10
when salary > 8000 then salary * 1.05
end salary_up
 from employees;


select count(*) from employees where salary <= (select avg(salary) from employees) group by department_id;

select department_id, count(salary) from employees group by department_id having avg(salary)> 6000;

select department_id, count(salary) from employees group by department_id 
having avg(salary)> 6000;


select department_id, count(*) from employees group by department_id;



select department_id, count(*) from employees a 
where salary <
(
select salarys from (
select department_id,avg(salary) salarys from employees
group by department_id
)b
where a.department_id = b.department_id
)
group by department_id
;



select min(salary), max(salary), department_id from employees group by department_id having max(salary) > 5000;


select emp_name, department_id from employees where emp_name ='Donald OConnell';


select * from employees, departments
where employees.department_id = departments.department_id(+);


select bno, btitle, bcontent,id from board;

select * from board;


select bno,btitle,bcontent, a.id, bgroup, bstep, bindent, bhit, bdate, bfile
from member a, board b
where a.id = b.id;


select employee_id, emp_name, a.job_id ,job_title from employees a, jobs b
where a.job_id = b.job_id;


select * from employees;
select * from departments;
select * from jobs;

select a.employee_id, a.emp_name, a.department_id, b.department_name, a.job_id, c.job_title from employees a, departments b, jobs c
where a.department_id = b.department_id and a.job_id = c.job_id order by department_id;


select a.employee_id, a.emp_name, a.salary, a.department_id, b.department_name from employees a, departments b
where a.department_id = b.department_id 
and salary < (select avg(salary) from employees)
;


select department_id, avg(salary) from employees group by department_id;

select employee_id, emp_name, salary, a.department_id, department_name from employees a, departments b
where a.department_id = b.department_id;


--select emp_name , salary, grade from employees, salgrade where salary between losal and hisal;

create table stu_grade(
grade varchar2(10),
loavg number(8),
hiavg number(8)
);

insert into stu_grade values( 'F', 0,59.99);
insert into stu_grade values( 'D', 60,69.99);
insert into stu_grade values( 'C', 70,79.99);
insert into stu_grade values( 'B', 80,89.99);
insert into stu_grade values( 'A', 90,100);

select * from stu;


update stu a set result = (
select results from (
select no,grade as results from stu,stu_grade
where avg between loavg and hiavg
)b
where a.no = b.no
);


select a.employee_id, a.emp_name, a.manager_id, b.emp_name
from employees a, employees b
where a.manager_id = b.employee_id;



