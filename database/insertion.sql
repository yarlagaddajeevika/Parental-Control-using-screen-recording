USE PARENTALCONTROL
IF OBJECT_ID('UserDetails', 'U') IS NULL
			 BEGIN
				PRINT ' UserDetails TABLE DOES NOT EXISTS'
			END
		   ELSE
			 BEGIN
				INSERT INTO UserDetails
				VALUES('jeevika','abc')
			 END

USE PARENTALCONTROL
select * from UserDetails

insert into StatisticsData values (8000000,'6Hyr45l',2)


drop database PARENTALCONTROL
