-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: callorie
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `callorie_track`
--

DROP TABLE IF EXISTS `callorie_track`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `callorie_track` (
  `item` varchar(100) DEFAULT NULL,
  `category` varchar(80) DEFAULT NULL,
  `quantity` bigint DEFAULT NULL,
  `id` varchar(50) DEFAULT NULL,
  `carbohydrates` decimal(7,2) DEFAULT NULL,
  `fats` decimal(7,2) DEFAULT NULL,
  `protein` decimal(7,2) DEFAULT NULL,
  `fiber` decimal(7,2) DEFAULT NULL,
  `callories` bigint DEFAULT NULL,
  `date` date DEFAULT NULL,
  KEY `id` (`id`),
  CONSTRAINT `callorie_track_ibfk_1` FOREIGN KEY (`id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `callorie_track`
--

LOCK TABLES `callorie_track` WRITE;
/*!40000 ALTER TABLE `callorie_track` DISABLE KEYS */;
INSERT INTO `callorie_track` VALUES ('dosa','BreakFast',200,'eswarn',37.60,10.40,5.40,2.20,266,'2023-01-02'),('dosa','BreakFast',200,'eswarn',37.60,10.40,5.40,2.20,266,'2023-01-02'),('Eggs','BreakFast',100,'eswarn',1.10,11.00,13.00,0.00,66,'2023-01-02'),('Eggs','BreakFast',100,'eswarn',1.10,11.00,13.00,0.00,66,'2023-01-02'),('Brinjal Curry','BreakFast',100,'eswarn',7.92,7.82,2.45,5.71,115,'2023-01-02'),('Brinjal Curry','BreakFast',100,'eswarn',7.92,7.82,2.45,5.71,115,'2023-01-02'),('Poori','BreakFast',100,'eswarn',7.50,7.40,1.30,0.20,101,'2023-01-02'),('Nutella Milkshake','BreakFast',100,'eswarn',44.00,14.00,38.00,12.00,454,'2023-01-02'),('Pani Puri','Snacks',50,'eswarn',14.80,2.60,2.70,1.80,164,'2023-01-02'),('Vegetable Biryani','Lunch',200,'eswarn',121.60,36.40,17.80,11.40,482,'2023-01-02'),('dosa','BreakFast',50,'eswarn',9.40,2.60,1.35,0.55,66,'2023-01-02'),('dosa','BreakFast',50,'eswarn',9.40,2.60,1.35,0.55,66,'2023-01-02'),('Oreo Milkshake','Shakes',100,'eswarn',31.40,11.70,5.10,0.30,262,'2023-01-02'),('Veg Manchuria','Snacks',250,'eswarn',77.25,56.50,13.50,12.75,2092,'2023-01-02'),('Oats Idly','BreakFast',250,'eswarn',14.25,1.50,4.50,2.50,75,'2023-01-03'),('Poori','BreakFast',150,'eswarn',11.25,11.10,1.95,0.30,152,'2023-01-03'),('Tomato Dal','Lunch',150,'eswarn',45.45,10.65,14.55,7.50,336,'2023-01-03'),('Tomato Rice','Lunch',100,'eswarn',30.30,7.10,9.70,5.00,224,'2023-01-03');
/*!40000 ALTER TABLE `callorie_track` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `items`
--

DROP TABLE IF EXISTS `items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `items` (
  `item` varchar(30) NOT NULL,
  `category` varchar(50) DEFAULT NULL,
  `carbohydrates` float DEFAULT NULL,
  `fats` float DEFAULT NULL,
  `protein` float DEFAULT NULL,
  `fiber` float DEFAULT NULL,
  `calorie` float DEFAULT NULL,
  PRIMARY KEY (`item`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `items`
--

LOCK TABLES `items` WRITE;
/*!40000 ALTER TABLE `items` DISABLE KEYS */;
INSERT INTO `items` VALUES ('Beetroot&Coconut Sabzi','lunch',3.8,6.8,1.1,2,81),('Brinjal Curry','lunch',7.92,7.82,2.45,5.71,115.33),('Burger','Snacks',24,14,17,0.9,295),('Chocolate Blend Milkshake','MilkShakes',90,22,2.2,0.3,590),('dosa','breakfast',18.8,5.2,2.7,1.1,133),('Egg Noodles','Snacks',40,3,7,2,221),('Eggs','breakfast',1.1,11,13,0,66),('Nutella Milkshake','MilkShakes',44,14,38,12,454),('Oatmeal','breakfast',27,3,5,4,95),('Oats Idly','breakfast',5.7,0.6,1.8,1,30),('Oreo Milkshake','MilkShakes',31.4,11.7,5.1,0.3,262),('Pani Puri','Snacks',29.6,5.2,5.4,3.6,329),('Pizza','Snacks',33,10,14.2,2.3,266),('Poori','breakfast',7.5,7.4,1.3,0.2,101),('Strawberry Milkshake','MilkShakes',71,11,13,1.5,235),('Tomato Dal','lunch',30.3,7.1,9.7,5,224),('Tomato Rice','lunch',30.3,7.1,9.7,5,224),('Vanilla Milkshake','MilkShakes',33.9,9.5,8.2,0,350.6),('Veg Manchuria','Snacks',30.9,22.6,5.4,5.1,837),('Vegetable Biryani','lunch',60.8,18.2,8.9,5.7,241);
/*!40000 ALTER TABLE `items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `salary`
--

DROP TABLE IF EXISTS `salary`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `salary` (
  `salary` decimal(5,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `salary`
--

LOCK TABLES `salary` WRITE;
/*!40000 ALTER TABLE `salary` DISABLE KEYS */;
INSERT INTO `salary` VALUES (65.44);
/*!40000 ALTER TABLE `salary` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` varchar(50) NOT NULL,
  `name` varchar(150) DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  `mobile_no` varchar(10) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  `target` bigint DEFAULT '0',
  `consumed` bigint DEFAULT '0',
  `workouttarget` bigint DEFAULT '0',
  `workoutconsumed` bigint DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('eswarn','Eswar Nandivada','posieswarnandivada@gmail.com','9177806313','Eswar@2001',0,786,1000,724);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `workout`
--

DROP TABLE IF EXISTS `workout`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `workout` (
  `workout` varchar(150) DEFAULT NULL,
  `time` int DEFAULT NULL,
  `callories` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `workout`
--

LOCK TABLES `workout` WRITE;
/*!40000 ALTER TABLE `workout` DISABLE KEYS */;
INSERT INTO `workout` VALUES ('jogging',30,280),('cycling',30,298),('running',10,114),('jumping rope',15,300),('yoga',60,600);
/*!40000 ALTER TABLE `workout` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `workout_track`
--

DROP TABLE IF EXISTS `workout_track`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `workout_track` (
  `workout` varchar(50) DEFAULT NULL,
  `time` int DEFAULT NULL,
  `id` varchar(50) DEFAULT NULL,
  `callories` bigint DEFAULT NULL,
  `date` date DEFAULT NULL,
  KEY `id` (`id`),
  CONSTRAINT `workout_track_ibfk_1` FOREIGN KEY (`id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `workout_track`
--

LOCK TABLES `workout_track` WRITE;
/*!40000 ALTER TABLE `workout_track` DISABLE KEYS */;
INSERT INTO `workout_track` VALUES ('Jogging',25,'eswarn',233,'2023-01-05'),('Running',30,'eswarn',342,'2023-01-05'),('Cycling',15,'eswarn',149,'2023-01-05');
/*!40000 ALTER TABLE `workout_track` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-05  8:44:59
