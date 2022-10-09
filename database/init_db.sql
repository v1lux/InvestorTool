CREATE TABLE public."InvestorTool"(
	id serial4 primary key,
	company_name varchar(50) NULL,
	ticker varchar(10) NULL,
	exchange varchar(20) NULL,
	industry varchar(50) null,
	company_location varchar(80) null,
	file_url varchar(80) null
);
