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
select count(*) from gisa;

select std_no,eng_score+kor_score as temp
from gisa
where acc_code = 'A' or acc_code = 'B'
order by temp desc,std_no asc
limit 4,1;

