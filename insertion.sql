IF OBJECT_ID('UserDetails', 'U') IS NULL
			 BEGIN
				PRINT ' UserDetails TABLE DOES NOT EXISTS'
			END
		   ELSE
			 BEGIN
				INSERT INTO UserDetails
				VALUES('jeevika','yarlagadda','jeevika@gmail.com','jeevika','abc')
			 END