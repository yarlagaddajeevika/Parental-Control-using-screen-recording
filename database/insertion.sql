IF OBJECT_ID('UserDetails', 'U') IS NULL
			 BEGIN
				PRINT ' UserDetails TABLE DOES NOT EXISTS'
			END
		   ELSE
			 BEGIN
				INSERT INTO UserDetails
				VALUES('jeevika','abc')
			 END

select userId from UserDetails where username='jeevika'

