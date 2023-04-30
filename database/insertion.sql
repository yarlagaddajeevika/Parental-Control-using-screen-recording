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
INSERT INTO UserDetails VALUES('ab','ab')
select upassword from UserDetails where username='jeevika'
select * from UserDetails


drop database PARENTALCONTROL