-- MySQL dump 10.13  Distrib 5.7.30, for Linux (x86_64)
--
-- Host: localhost    Database: mydb
-- ------------------------------------------------------
-- Server version	5.7.30-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Cars`
--

DROP TABLE IF EXISTS `Cars`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Cars` (
  `idCars` int(11) NOT NULL AUTO_INCREMENT,
  `Transmition` varchar(45) DEFAULT NULL,
  `Mileage` varchar(45) DEFAULT NULL,
  `PTC` varchar(45) DEFAULT NULL,
  `Price` varchar(45) DEFAULT NULL,
  `Year_of_issue` varchar(45) DEFAULT NULL,
  `Engine_capacity` varchar(10) DEFAULT NULL,
  `Color_idColor` int(11) DEFAULT NULL,
  `Body_type_idBody_type` int(11) DEFAULT NULL,
  `Model_idModel` int(11) DEFAULT NULL,
  PRIMARY KEY (`idCars`),
  KEY `fk_Cars_1_idx` (`Color_idColor`),
  KEY `fk_Cars_2_idx` (`Body_type_idBody_type`),
  KEY `fk_Cars_4_idx` (`Model_idModel`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Cars`
--

LOCK TABLES `Cars` WRITE;
/*!40000 ALTER TABLE `Cars` DISABLE KEYS */;
INSERT INTO `Cars` VALUES (1,'АКПП','120000','5465F8GJ4G5','3500000','2018','2.1',1,2,4),(2,'АКПП','240000','SD546123JR8','2780000','2017','1.9',1,2,2),(3,'МКПП','120000 ','GFJ99721KS8','2910000','2018','1.9',2,3,3),(4,'МКПП','357000','687687YH7S1','1470000','2016','1.8',3,4,1),(5,'АКПП','180000','F4564J6FJ866','3010000','2017','1.8',4,1,2),(6,'МКПП','96000','GF5JF6526123','2980000','2018','1.8',3,2,3),(7,'АКПП','57000','8464DH897SR','4700000','2019','2.1',4,3,1),(8,'АКПП','250000','3487FK968479','3200000','2017','1.5',3,4,3),(9,'АКПП','230000','245346356','2300000','2014','1.2',2,2,1),(10,'АКПП','10000','D4J56H356N435','4300000','2019','1.2',1,2,1),(11,'МКПП','450000','46367GTJG557','1200000','2015','1.9',7,4,2),(12,'МКПП','250000','478FGTU3576','120000000','2018','1.9',3,3,1);
/*!40000 ALTER TABLE `Cars` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-07-07 17:08:33
