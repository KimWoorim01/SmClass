
drop table students;

create table students(
no number(4),
name varchar2(30),
kor number(3),
eng number(3),
math number(3),
total number(5),
avg number(5),
rank number(3)
);

select * from students;
commit;

insert all
into students (no, name, kor, eng, math, total , avg, rank)values(1,'Debor',51,73,79,203,67,0)
into students (no, name, kor, eng, math, total , avg, rank)values(2,'Carolyne',72,98,65,235,78,0)
into students (no, name, kor, eng, math, total , avg, rank)values(3,'Cornell',53,60,86,199,66,0)
into students (no, name, kor, eng, math, total , avg, rank)values(4,'Roslyn',72,60,97,229,76,0)
into students (no, name, kor, eng, math, total , avg, rank)values(5,'Gunner',78,83,63,224,74,0)
into students (no, name, kor, eng, math, total , avg, rank)values(6,'Griz',92,83,79,254,84,0)
into students (no, name, kor, eng, math, total , avg, rank)values(7,'Ida',69,72,85,226,75,0)
into students (no, name, kor, eng, math, total , avg, rank)values(8,'Standford',68,67,67,202,67,0)
into students (no, name, kor, eng, math, total , avg, rank)values(9,'Pier',57,84,96,237,79,0)
select * from dual;



create table no_tab (
no number,
name varchar2(20),
avg1 number,
avg2 number(5,2)
);



insert into no_tab values(
1, '홍길동', 1000/3, 1000/3
);


select * from no_tab;


create table date_tab(
no number(4),
s_date date,
s_date2 date
);

drop table date_tab;

insert into date_tab values(
 1, '2024-10-28', sysdate
);
 
select * from date_tab;

select to_char(s_date,'YYYY-MM-DD'),to_char(s_date2,'YYYY-MM-DD hh24:mi:ss') from date_tab;

--검색
--select 컬럼명 from 테이블명


select emp_name from employees where emp_name = 'Fat Fay';

select * from employees;

select employee_id, emp_name, phone_number, hire_date from employees;

select employee_id, emp_name, job_id from employees where job_id = 'SH_CLERK';

drop table member;

commit;

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
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (1, '9122', 'Teggart', 'gteggart0@naver.com', '314-134-5080', 'Non-binary', 'golf', '2024-04-02');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (2, '7364', 'Petican', 'fpetican1@goo.ne.jp', '731-743-1711', 'Male', 'swim', '2024-05-16');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (3, '8334', 'Deboy', 'fdeboy2@acquirethisname.com', '363-559-1354', 'Male', 'run', '2024-03-23');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (4, '9072', 'Sparshott', 'hsparshott3@deviantart.com', '933-703-6077', 'Female', 'book', '2024-01-22');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (5, '1486', 'Esslemont', 'aesslemont4@ameblo.jp', '182-410-6079', 'Male', 'golf', '2024-03-23');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (6, '8345', 'McGlue', 'cmcglue5@cnn.com', '678-974-8579', 'Agender', 'run', '2024-02-19');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (7, '5550', 'Wendover', 'cwendover6@instagram.com', '884-243-7185', 'Female', 'golf', '2024-02-09');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (8, '2329', 'Lomasna', 'alomasna7@utexas.edu', '157-974-8607', 'Male', 'book', '2024-02-05');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (9, '6524', 'McCarthy', 'cmccarthy8@free.fr', '454-234-2735', 'Female', 'run', '2024-10-02');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (10, '6030', 'Springell', 'aspringell9@aboutads.info', '284-577-8307', 'Male', 'game', '2024-02-09');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (11, '7915', 'Thewles', 'ethewlesa@devhub.com', '123-774-9151', 'Female', 'golf', '2024-07-31');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (12, '4702', 'Spensley', 'aspensleyb@go.com', '482-791-1826', 'Male', 'swim', '2024-01-13');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (13, '4096', 'Joreau', 'ljoreauc@jigsy.com', '762-299-5988', 'Female', 'golf', '2024-04-20');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (14, '5685', 'Footitt', 'zfootittd@sphinn.com', '705-594-1128', 'Female', 'golf', '2024-09-03');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (15, '6465', 'Christophers', 'pchristopherse@altervista.org', '722-638-0335', 'Male', 'book', '2024-05-08');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (16, '1440', 'Bugge', 'abuggef@so-net.ne.jp', '317-418-3340', 'Male', 'golf', '2024-06-13');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (17, '9150', 'Lougheid', 'ylougheidg@elegantthemes.com', '277-334-3318', 'Female', 'golf', '2024-09-26');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (18, '1878', 'Harbar', 'hharbarh@ebay.com', '786-782-9399', 'Male', 'run', '2024-08-06');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (19, '3979', 'Rushford', 'mrushfordi@jimdo.com', '985-868-3424', 'Male', 'book', '2024-03-26');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (20, '5894', 'Widocks', 'nwidocksj@bloglovin.com', '984-688-1772', 'Female', 'golf', '2024-06-24');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (21, '3317', 'Stalley', 'hstalleyk@symantec.com', '746-583-7988', 'Male', 'run', '2024-02-27');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (22, '8571', 'Stains', 'cstainsl@nytimes.com', '178-305-0971', 'Female', 'golf', '2024-08-28');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (23, '2189', 'Caukill', 'kcaukillm@wikia.com', '354-518-7602', 'Male', 'game', '2024-06-06');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (24, '5875', 'Lange', 'glangen@ocn.ne.jp', '943-570-0643', 'Female', 'book', '2024-10-06');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (25, '9058', 'Handslip', 'chandslipo@ovh.net', '710-343-7346', 'Male', 'golf', '2024-05-17');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (26, '9749', 'Anstee', 'ransteep@yandex.ru', '359-558-1425', 'Female', 'book', '2024-08-08');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (27, '4430', 'Bairstow', 'kbairstowq@addthis.com', '367-528-9397', 'Male', 'book', '2024-03-17');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (28, '9381', 'McWard', 'mmcwardr@state.gov', '815-556-3420', 'Female', 'game', '2024-07-17');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (29, '5508', 'Preshous', 'mpreshouss@google.nl', '660-615-7093', 'Male', 'run', '2023-12-26');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (30, '4522', 'Masseo', 'cmasseot@va.gov', '981-131-1117', 'Female', 'book', '2024-05-21');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (31, '9617', 'Kembley', 'qkembleyu@walmart.com', '688-885-0908', 'Male', 'run', '2024-05-07');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (32, '8128', 'Kubicka', 'ckubickav@soundcloud.com', '377-246-0484', 'Female', 'run', '2024-08-04');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (33, '6202', 'Stallebrass', 'jstallebrassw@bloomberg.com', '398-373-2437', 'Male', 'book', '2024-05-12');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (34, '5102', 'Maffini', 'cmaffinix@nature.com', '633-787-3981', 'Female', 'swim', '2024-07-02');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (35, '5404', 'Astie', 'castiey@ibm.com', '642-371-2376', 'Female', 'game', '2023-12-08');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (36, '3786', 'McPake', 'fmcpakez@g.co', '800-428-6374', 'Polygender', 'swim', '2024-07-11');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (37, '4651', 'Feldhuhn', 'pfeldhuhn10@mtv.com', '826-518-0739', 'Female', 'game', '2024-06-06');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (38, '5627', 'O''Noulane', 'nonoulane11@xing.com', '876-914-4799', 'Male', 'game', '2024-07-07');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (39, '8206', 'Pinner', 'lpinner12@yahoo.com', '856-152-3537', 'Genderfluid', 'swim', '2024-03-17');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (40, '9400', 'Saul', 'csaul13@jigsy.com', '688-777-0057', 'Female', 'game', '2024-04-28');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (41, '9514', 'Nielson', 'nnielson14@deliciousdays.com', '491-516-9927', 'Female', 'run', '2023-11-05');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (42, '1090', 'McCullogh', 'cmccullogh15@reddit.com', '233-246-2286', 'Agender', 'swim', '2024-07-03');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (43, '7144', 'Kas', 'mkas16@yandex.ru', '775-392-3613', 'Male', 'game', '2024-01-27');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (44, '8002', 'Milella', 'cmilella17@bluehost.com', '156-373-3454', 'Male', 'run', '2024-05-08');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (45, '1787', 'Lejeune', 'olejeune18@seesaa.net', '504-886-6631', 'Male', 'golf', '2024-09-03');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (46, '3329', 'Belmont', 'wbelmont19@wiley.com', '652-321-8921', 'Female', 'book', '2023-11-04');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (47, '5417', 'Ashbridge', 'cashbridge1a@japanpost.jp', '431-652-4410', 'Male', 'golf', '2024-08-16');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (48, '7674', 'Rops', 'krops1b@census.gov', '124-901-6351', 'Male', 'game', '2024-08-24');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (49, '5672', 'Sample', 'asample1c@aol.com', '921-638-2655', 'Male', 'golf', '2024-05-01');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (50, '2587', 'Sexten', 'nsexten1d@networksolutions.com', '878-741-8952', 'Female', 'run', '2024-04-23');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (51, '4416', 'Heasley', 'rheasley1e@nbcnews.com', '686-692-4366', 'Genderfluid', 'book', '2024-09-07');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (52, '6980', 'Mungan', 'pmungan1f@paypal.com', '232-760-3193', 'Bigender', 'game', '2024-09-06');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (53, '6871', 'Gofton', 'sgofton1g@ucla.edu', '154-931-6115', 'Female', 'game', '2024-06-01');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (54, '4911', 'Simony', 'asimony1h@yandex.ru', '325-590-7386', 'Male', 'game', '2024-08-05');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (55, '3150', 'Maudson', 'gmaudson1i@angelfire.com', '442-889-7622', 'Male', 'swim', '2024-06-20');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (56, '5387', 'Sharply', 'rsharply1j@umich.edu', '537-258-4592', 'Genderfluid', 'run', '2024-09-20');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (57, '2395', 'Trunks', 'jtrunks1k@uol.com.br', '442-213-6558', 'Female', 'golf', '2024-08-13');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (58, '5089', 'Elvey', 'relvey1l@bbc.co.uk', '476-227-3208', 'Genderfluid', 'run', '2024-02-27');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (59, '5136', 'Joust', 'hjoust1m@people.com.cn', '438-991-4995', 'Male', 'swim', '2024-06-16');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (60, '7442', 'Hablet', 'lhablet1n@instagram.com', '993-986-6250', 'Female', 'game', '2024-04-06');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (61, '7894', 'Schrei', 'gschrei1o@abc.net.au', '519-200-3868', 'Female', 'swim', '2024-05-13');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (62, '5069', 'Soars', 'esoars1p@amazon.co.jp', '435-506-9351', 'Female', 'swim', '2024-08-09');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (63, '8033', 'Benstead', 'jbenstead1q@nhs.uk', '585-824-0375', 'Male', 'golf', '2024-01-18');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (64, '2753', 'Lorkins', 'elorkins1r@google.de', '519-193-6800', 'Male', 'book', '2024-10-01');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (65, '7226', 'Licciardiello', 'tlicciardiello1s@prweb.com', '664-676-7321', 'Male', 'book', '2024-01-25');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (66, '1102', 'Haskell', 'ghaskell1t@bloglines.com', '295-876-5471', 'Male', 'game', '2024-05-12');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (67, '8768', 'McGray', 'gmcgray1u@google.pl', '288-714-3094', 'Female', 'game', '2024-03-04');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (68, '2461', 'Blayney', 'ablayney1v@mtv.com', '693-821-1705', 'Male', 'swim', '2023-11-05');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (69, '6008', 'Cote', 'jcote1w@wsj.com', '951-734-8950', 'Female', 'game', '2023-12-12');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (70, '6837', 'Letson', 'cletson1x@europa.eu', '258-731-2804', 'Male', 'golf', '2023-11-27');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (71, '6181', 'Tocqueville', 'htocqueville1y@dedecms.com', '736-907-2300', 'Male', 'swim', '2024-06-24');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (72, '5013', 'Cushion', 'ecushion1z@phoca.cz', '269-323-6292', 'Female', 'swim', '2024-01-21');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (73, '2465', 'Cockrell', 'ecockrell20@vkontakte.ru', '883-135-6627', 'Female', 'game', '2024-06-09');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (74, '3229', 'Syred', 'csyred21@aol.com', '611-397-9842', 'Bigender', 'game', '2024-05-25');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (75, '4229', 'Sammut', 'rsammut22@privacy.gov.au', '718-516-8343', 'Female', 'book', '2024-04-09');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (76, '6858', 'Corbally', 'jcorbally23@zimbio.com', '947-420-6316', 'Female', 'run', '2024-05-27');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (77, '1074', 'Watton', 'jwatton24@google.de', '962-765-4866', 'Female', 'game', '2024-05-19');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (78, '7076', 'McLeoid', 'smcleoid25@buzzfeed.com', '813-998-5299', 'Genderqueer', 'book', '2024-01-17');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (79, '1878', 'Gallandre', 'jgallandre26@xrea.com', '555-996-6151', 'Male', 'swim', '2024-06-30');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (80, '2799', 'Allmann', 'eallmann27@over-blog.com', '817-538-0016', 'Female', 'run', '2024-01-19');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (81, '8371', 'Walworche', 'fwalworche28@wufoo.com', '499-262-1495', 'Male', 'run', '2023-12-11');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (82, '3029', 'Treffrey', 'atreffrey29@berkeley.edu', '627-352-1191', 'Non-binary', 'run', '2023-12-10');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (83, '9011', 'Buckham', 'tbuckham2a@alexa.com', '147-605-1197', 'Female', 'book', '2023-11-18');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (84, '4543', 'Birchenhead', 'lbirchenhead2b@hexun.com', '430-639-0295', 'Male', 'run', '2023-10-31');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (85, '4173', 'Vasyagin', 'rvasyagin2c@booking.com', '379-640-1240', 'Male', 'swim', '2024-01-17');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (86, '6357', 'Asee', 'masee2d@rakuten.co.jp', '418-819-9113', 'Female', 'swim', '2024-01-12');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (87, '9984', 'Attride', 'cattride2e@netvibes.com', '715-929-4856', 'Female', 'run', '2024-02-01');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (88, '9595', 'Prator', 'lprator2f@foxnews.com', '303-316-6497', 'Male', 'swim', '2024-10-11');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (89, '7606', 'Hulbert', 'shulbert2g@foxnews.com', '161-373-9499', 'Male', 'golf', '2024-07-21');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (90, '2533', 'Foyster', 'gfoyster2h@yahoo.com', '882-796-6680', 'Female', 'golf', '2024-03-31');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (91, '4431', 'Cardenas', 'mcardenas2i@simplemachines.org', '748-663-2548', 'Female', 'run', '2024-10-11');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (92, '9525', 'McNickle', 'cmcnickle2j@delicious.com', '865-811-2130', 'Female', 'golf', '2024-08-31');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (93, '5134', 'McCluskey', 'fmccluskey2k@kickstarter.com', '849-926-2501', 'Male', 'golf', '2023-12-21');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (94, '4198', 'Culcheth', 'vculcheth2l@samsung.com', '712-851-3794', 'Male', 'game', '2024-09-09');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (95, '2244', 'Hapke', 'chapke2m@pbs.org', '814-489-5565', 'Male', 'swim', '2024-08-06');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (96, '8767', 'Ledeker', 'dledeker2n@nhs.uk', '344-735-7762', 'Female', 'run', '2024-07-21');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (97, '2551', 'Diego', 'rdiego2o@hao123.com', '510-478-4282', 'Female', 'swim', '2024-02-26');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (98, '4667', 'Devereu', 'cdevereu2p@forbes.com', '925-279-9726', 'Female', 'book', '2024-02-23');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (99, '2663', 'Dedam', 'jdedam2q@cloudflare.com', '817-678-3688', 'Male', 'book', '2024-03-12');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (100, '1407', 'Vitler', 'rvitler2r@wikispaces.com', '500-376-6141', 'Male', 'game', '2024-03-20');


select * from member;



--연산자
--타입 : 숫자인경우
select * from students;

select (kor+eng) from students
