--주석
--실행단축키 f9 or ctrl + enter
--계정 이름 앞에 c## 생략 코드
alter session set "_ORACLE_SCRIPT" = true;


--사용자 생성
create user ora_user identified by 1111;

--권한부여
grant connect,resource,dba to ora_user;

--권한해제
revoke connect,resource,dba from ora_user;

drop user ora_user