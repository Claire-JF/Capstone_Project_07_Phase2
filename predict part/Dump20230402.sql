-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: tempandhum
-- ------------------------------------------------------
-- Server version	5.7.36-log

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
-- Table structure for table `rain`
--

DROP TABLE IF EXISTS `rain`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rain` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `temperature` char(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `humidity` char(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `updata_time` char(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rain`
--

LOCK TABLES `rain` WRITE;
/*!40000 ALTER TABLE `rain` DISABLE KEYS */;
INSERT INTO `rain` VALUES (-4,'12.5℃','57.00%','Wed Mar 29 18:08:32 2023'),(-3,'15.3℃','57.00%','Wed Mar 29 18:08:32 2023'),(-2,'15.3℃','57.00%','Thu Mar 30 18:08:32 2023'),(-1,'9.7℃','57.00%','Thu Mar 30 18:08:32 2023'),(1,'16.3℃','57.00%','Fri Mar 31 18:08:32 2023'),(2,'10.70℃','57.00%','Fri Mar 31 18:08:32 2023'),(3,'19.50℃','57.00%','Sat Apr 01 18:08:32 2023'),(4,'11.60℃','57.00%','Sat Apr 01 18:08:32 2023'),(5,'13.3℃','57.00%','Sun Apr 02 18:08:32 2023'),(6,'21.6℃','57.00%','Sun Apr 02 18:08:34 2023'),(7,'23.2℃','57.00%','Mon Apr 03 18:08:30 2023'),(8,'15.7℃','57.00%','Mon Apr 03 18:08:28 2023'),(9,'23.2℃','57.00%','Tue Apr 04 18:08:26 2023'),(10,'12.50℃','57.00%','Tue Apr 04 18:08:24 2023');
/*!40000 ALTER TABLE `rain` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'tempandhum'
--

--
-- Dumping routines for database 'tempandhum'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-02 21:30:02
