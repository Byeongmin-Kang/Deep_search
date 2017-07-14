use pnudb;
create table gisa(
	std_no integer primary key,
    email varchar(30) not null,
    kor_score integer not null,
    eng_score integer not null,
    math_score integer not null,
    sci_score integer not null,
    hist_score integer not null,
    total integer not null,
    manager_code char(1) not null,
    acc_code char(1) not null,
    loc_code char(1) not null
);
#7/13일 자료
#select * from gisa where email = 'addx';
#insert into gisa values (990001,'addx', 17, 29, 16, 49, 43,154,'C','A','C');
#insert into gisa values (990002,'addx', 17, 29, 16, 49, 43,154,'C','A','C');
select count(*) from gisa;
select * from gisa;
#7/14정보처리기사 문제 가져와서 풀기
select std_no,eng_score+kor_score as temp
from gisa
where acc_code = 'A' or acc_code = 'B'
order by temp desc, std_no asc
#limit 10; 10개 가져와라
limit 4,1; #4까지 가져오고 그 이후로 거기에 1만큼 추가해서 가져와서 하나만 보여줘 ,가 있으면 순서를 가리킴

select count(*) from gisa where acc_code = 'A' or acc_code = 'B';

create table install_game(
	install_date date,
	app_name varchar(10),
    user_id varchar(20) 
);
create table dpu_won(
	log_date date,
	app_name varchar(10),
    user_id varchar(20),
    payment integer 
    );

select * from dpu_won;
select * from install_game;

select sum(payment) from dpu_won where month(log_date) =7;

select max(eng_score+kor_score) as temp
from gisa
where acc_code = 'A' or acc_code = 'B'
order by temp desc;
#3번
select std_no,eng_score,
case acc_code 
	when'A' then eng_score +5
    when'B' then eng_score +15
    when'C' then eng_score +20
end as plus_score
from gisa
where total >=150;
#집계함수 사용
select
sum(case acc_code 
	when'A' then eng_score +5
    when'B' then eng_score +15
    when'C' then eng_score +20
end) as plus_score
from gisa
where total >=150;
#4번
select count(*) 
from
	(select case manager_code 
		when'A' then kor_score +10
		when'B' then kor_score +15
		when'C' then kor_score +20
	end as plus_score_K
	from gisa
	where loc_code = 'B') tbl
where tbl.plus_score_K >=50 ;
