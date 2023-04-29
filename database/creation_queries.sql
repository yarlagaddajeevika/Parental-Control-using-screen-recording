IF NOT EXISTS(SELECT name FROM sys.databases WHERE name='PARENTALCONTROL')
     BEGIN
	   CREATE DATABASE PARENTALCONTROL
	 END
GO
  USE PARENTALCONTROL

---------------------------------------------------------------
------------------ CREATE TABLES ---------------------------
---------------------------------------------------------------
---------------- Table 1. Login----------------------------
----------User Id: start:8000000 -------------------------------
IF OBJECT_ID('User', 'U') IS NOT NULL
   BEGIN
		PRINT 'User TABLE ALREADY EXISTS'
   END
ELSE
   BEGIN
		CREATE TABLE UserDetails(
		  userId Integer IDENTITY(8000000,1) NOT NULL PRIMARY KEY,
		  username varchar(40) NOT NULL UNIQUE,
		  upassword varchar(10) NOT NULL CHECK(len(upassword)<=10)
		  )
   END

IF OBJECT_ID('Statistics', 'U') IS NOT NULL
   BEGIN
		PRINT 'Statistics TABLE  ALREADY EXISTS'
   END
ELSE
   BEGIN
		CREATE TABLE StatisticsData(
		  userId Integer NOT NULL FOREIGN KEY REFERENCES UserDetails(userId),
		  youtubeId Integer NOT NULL,
		  view_count Integer NOT NULL,
		  PRIMARY KEY (userId,youtubeId)
		  )
   END