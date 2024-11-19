


select last_day(hire_date) from employees;


select hire_date, add_months(hire_date,-6), add_months(sysdate,-6) from employees;


select substr(last_day(m_date),1,5) md, count(*) from member group by last_day(m_date) order by md;


create table emp4
as select * from employees where 1=2;

insert into emp4 select * from employees;

alter table member add constraint id_pk primary key(id);

select * from member;

drop table board;

create table board(
bno number(4) primary key,
btitle varchar2(100) not null,
bcontent clob,
id varchar2(30),
bgroup number(4),
bstep number(4),
bindent number(4),
bhit number(4),
bdate date,
bfile varchar2(100)
);

insert into board values(
board_seq.nextval,'제목1' ,'내용1', 'aaa', board_seq.currval, 0,0,0,sysdate,''
);


select employee_id, emp_name, email,salary, employees.department_id, department_name from employees, departments where employees.department_id = departments.department_id;





