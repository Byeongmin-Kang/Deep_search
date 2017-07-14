use pnudb;
select count(*) from gisa;

create table test(
	id varchar(20) not null,
    pw varchar(8) not null, 
    user_name varchar(30) not null
);

select * from test;
desc test;

insert into test(id,pw,user_name) values('admin','1234','kim');
insert into test(id,pw,user_name) values('dev','1234','park');
insert into test(id,pw,user_name) values('tester','1234','lee');
insert into test(id,pw,user_name) values('user1','1234','kang');
insert into test(id,pw,user_name) values('user2','1234','choi');
#지우기 
delete from test where id = 'user2' ;
#수정하기
update test set pw='2345' where id = 'admin';