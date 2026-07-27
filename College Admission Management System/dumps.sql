-- MySQL dump 10.13  Distrib 8.0.45, for Win64 (x86_64)
--
-- Host: localhost    Database: college_admission_db
-- ------------------------------------------------------
-- Server version	8.0.45

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `course`
--

DROP TABLE IF EXISTS `course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `course` (
  `course_id` int NOT NULL AUTO_INCREMENT,
  `course_name` varchar(50) NOT NULL,
  `duration` varchar(30) NOT NULL,
  `course_fee` decimal(10,2) NOT NULL,
  PRIMARY KEY (`course_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `course`
--

LOCK TABLES `course` WRITE;
/*!40000 ALTER TABLE `course` DISABLE KEYS */;
INSERT INTO `course` VALUES (1,'BCA','3 Years',60000.00),(2,'BBA','3 Years',70000.00),(3,'B.Com','3 Years',50000.00),(4,'MCA','2 Years',80000.00),(5,'MBA','2 Years',90000.00);
/*!40000 ALTER TABLE `course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `student_id` int NOT NULL AUTO_INCREMENT,
  `student_name` varchar(100) NOT NULL,
  `father_name` varchar(100) NOT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `mobile` varchar(15) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `address` text,
  `admission_date` date DEFAULT NULL,
  `course_id` int DEFAULT NULL,
  `fee_paid` decimal(10,2) DEFAULT NULL,
  `fee_status` varchar(20) DEFAULT NULL,
  `pending_fee` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`student_id`),
  KEY `course_id` (`course_id`),
  CONSTRAINT `student_ibfk_1` FOREIGN KEY (`course_id`) REFERENCES `course` (`course_id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES (14,'Berlin','Irving','Male','1954-09-04','6578945678','berlin@gmail.com','London','1975-10-07',1,60000.00,'Paid',0.00),(15,'Tokyo','Moscow','Female','1998-12-09','4535678976','tokyo@gmail.com','Japan','2025-09-08',1,60000.00,'Paid',0.00),(18,'Kanika','Shiv Kumar','Female','2006-09-08','8765678976','kanika@gmail.com','Rewari','2024-09-05',1,30000.00,'Pending',30000.00),(19,'Albus Potter','Harry Potter','Male','1998-03-17','5678987656','albuspotter@gmail.com','Hogwarts, London','2005-12-07',1,40000.00,'Pending',20000.00),(20,'Rose','Lotus','Male','2003-09-02','6758987654','rose@gmail.com','Russia','2022-03-05',4,80000.00,'Paid',0.00),(21,'Sheetal','Ramesh','Female','2006-07-28','2345678987','sheetalkumari@gmail.com','Sector-18, Rewari','2024-03-04',2,20000.00,'Pending',50000.00),(22,'Junior While','Whitter White','Male','1998-12-08','9876543456','juniorwhite@gmail.com','Albuquerque, New Mexico','2022-03-04',4,34000.00,'Pending',46000.00),(23,'Anna','Sunatol','Male','2000-10-23','7685645678','anna@gmail.com','Paris, France','2022-05-12',4,45000.00,'Pending',35000.00);
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-07-27 21:50:07
