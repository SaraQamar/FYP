-- MySQL Administrator dump 1.4
--
-- ------------------------------------------------------
-- Server version	5.1.61-0ubuntu0.11.10.1


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


--
-- Create schema CONTACTS
--

CREATE DATABASE IF NOT EXISTS CONTACTS;
USE CONTACTS;

--
-- Definition of table `CONTACTS`.`calls`
--

DROP TABLE IF EXISTS `CONTACTS`.`calls`;
CREATE TABLE  `CONTACTS`.`calls` (
  `ids` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  `e_type` varchar(20) DEFAULT NULL,
  `datetime` varchar(30) DEFAULT NULL,
  `duration` int(11) DEFAULT NULL,
  `key` varchar(4) DEFAULT NULL,
  `e_from` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`ids`),
  KEY `name` (`name`)
) ENGINE=MyISAM AUTO_INCREMENT=29 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `CONTACTS`.`calls`
--

/*!40000 ALTER TABLE `calls` DISABLE KEYS */;
LOCK TABLES `calls` WRITE;
INSERT INTO `CONTACTS`.`calls` VALUES  (1,'PersonD','incoming','2012-01-31 5:30 PM',25,'c','03331233454'),
 (2,'PersonD','incoming','2012-01-31 5:30 PM',27,'c','03332233494'),
 (3,'PersonL','incoming','2012-01-31 5:30 PM',28,'c','03333233474'),
 (4,'PersonK','incoming','2012-01-31 5:30 PM',29,'c','03334233654'),
 (5,'PersonJ','incoming','2012-01-31 5:30 PM',22,'c','03335233454'),
 (6,'PersonI','incoming','2012-01-31 5:30 PM',12,'c','03336233451'),
 (7,'PersonH','incoming','2012-01-31 5:30 PM',30,'c','03337233452'),
 (8,'PersonG','incoming','2012-01-31 5:30 PM',40,'c','03338233453'),
 (9,'PersonE','incoming','2012-01-31 5:30 PM',50,'c','03339233456'),
 (10,'PersonF','incoming','2012-01-31 5:30 PM',960,'c','03339233454'),
 (11,'PersonD','incoming','2012-01-31 5:30 PM',70,'c','03338233459'),
 (12,'PersonB','incoming','2012-01-31 5:30 PM',80,'c','03337233458'),
 (13,'PersonC','incoming','2012-01-31 5:30 PM',20,'c','03336233457'),
 (14,'PersonA','incoming','2012-01-31 5:30 PM',10,'c','03335233456'),
 (15,'PersonA','incoming','2012-01-31 5:30 PM',25,'c','03331133454'),
 (16,'PersonD','incoming','2012-01-31 5:30 PM',27,'c','03332333494'),
 (17,'PersonL','incoming','2012-01-31 5:30 PM',28,'c','03333733474'),
 (18,'PersonK','incoming','2012-01-31 5:30 PM',29,'c','03334833654'),
 (19,'PersonJ','incoming','2012-01-31 5:30 PM',22,'c','03335933454'),
 (20,'PersonI','incoming','2012-01-31 5:30 PM',12,'c','03336633451'),
 (21,'PersonH','incoming','2012-01-31 5:30 PM',30,'c','03337533452'),
 (22,'PersonG','incoming','2012-01-31 5:30 PM',40,'c','03338433453'),
 (23,'PersonE','incoming','2012-01-31 5:30 PM',50,'c','03339333456'),
 (24,'PersonF','incoming','2012-01-31 5:30 PM',60,'c','03339233454'),
 (25,'PersonD','incoming','2012-01-31 5:30 PM',70,'c','03338233459'),
 (26,'PersonB','incoming','2012-01-31 5:30 PM',80,'c','03337233458'),
 (27,'PersonC','incoming','2012-01-31 5:30 PM',20,'c','03336233457'),
 (28,'PersonA','incoming','2012-01-31 5:30 PM',10,'c','03335213456');
UNLOCK TABLES;
/*!40000 ALTER TABLE `calls` ENABLE KEYS */;


--
-- Definition of table `CONTACTS`.`emails`
--

DROP TABLE IF EXISTS `CONTACTS`.`emails`;
CREATE TABLE  `CONTACTS`.`emails` (
  `ids` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  `e_type` varchar(20) DEFAULT NULL,
  `e_from` varchar(20) DEFAULT NULL,
  `datetime` varchar(30) DEFAULT NULL,
  `duration` int(11) DEFAULT NULL,
  `key` varchar(4) DEFAULT NULL,
  PRIMARY KEY (`ids`),
  KEY `name` (`name`)
) ENGINE=MyISAM AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `CONTACTS`.`emails`
--

/*!40000 ALTER TABLE `emails` DISABLE KEYS */;
LOCK TABLES `emails` WRITE;
INSERT INTO `CONTACTS`.`emails` VALUES  (1,'PersonD','incoming','03331233454','2012-01-31 5:30 PM',1523,'e'),
 (2,'PersonD','incoming','03331233494','2012-01-31 5:30 PM',27,'e'),
 (3,'PersonL','incoming','03331233474','2012-01-31 5:30 PM',28,'e'),
 (4,'PersonK','incoming','03331233654','2012-01-31 5:30 PM',29,'e'),
 (5,'PersonJ','incoming','03331233454','2012-01-31 5:30 PM',22,'e'),
 (6,'PersonI','incoming','03331233451','2012-01-31 5:30 PM',12,'e'),
 (7,'PersonH','incoming','03331233452','2012-01-31 5:30 PM',30,'e'),
 (8,'PersonG','incoming','03331233453','2012-01-31 5:30 PM',40,'e'),
 (9,'PersonE','incoming','03331233456','2012-01-31 5:30 PM',50,'e'),
 (10,'PersonF','incoming','03331233454','2012-01-31 5:30 PM',60,'e'),
 (11,'PersonD','incoming','03331233459','2012-01-31 5:30 PM',70,'e'),
 (12,'PersonB','incoming','03331233458','2012-01-31 5:30 PM',80,'e'),
 (13,'PersonC','incoming','03331233457','2012-01-31 5:30 PM',20,'e'),
 (14,'PersonA','incoming','03331233456','2012-01-31 5:30 PM',10,'e'),
 (15,'PersonD','incoming','03331233454','2012-01-31 5:30 PM',25,'e'),
 (16,'PersonD','incoming','03332233494','2012-01-31 5:30 PM',27,'e'),
 (17,'PersonL','incoming','03333233474','2012-01-31 5:30 PM',28,'e'),
 (18,'PersonK','incoming','03334233654','2012-01-31 5:30 PM',29,'e'),
 (19,'PersonJ','incoming','03335233454','2012-01-31 5:30 PM',22,'e'),
 (20,'PersonI','incoming','03336233451','2012-01-31 5:30 PM',12,'e'),
 (21,'PersonH','incoming','03337233452','2012-01-31 5:30 PM',30,'e'),
 (22,'PersonG','incoming','03338233453','2012-01-31 5:30 PM',40,'e'),
 (23,'PersonE','incoming','03339233456','2012-01-31 5:30 PM',50,'e'),
 (24,'PersonF','incoming','03339233454','2012-01-31 5:30 PM',60,'e'),
 (25,'PersonD','incoming','03338233459','2012-01-31 5:30 PM',70,'e'),
 (26,'PersonB','incoming','03337233458','2012-01-31 5:30 PM',80,'e'),
 (27,'PersonC','incoming','03336233457','2012-01-31 5:30 PM',20,'e');
UNLOCK TABLES;
/*!40000 ALTER TABLE `emails` ENABLE KEYS */;


--
-- Definition of table `CONTACTS`.`msgs`
--

DROP TABLE IF EXISTS `CONTACTS`.`msgs`;
CREATE TABLE  `CONTACTS`.`msgs` (
  `ids` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  `e_type` varchar(20) DEFAULT NULL,
  `datetime` varchar(30) DEFAULT NULL,
  `duration` int(11) DEFAULT NULL,
  `key` varchar(4) DEFAULT NULL,
  `e_from` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`ids`),
  KEY `name` (`name`)
) ENGINE=MyISAM AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `CONTACTS`.`msgs`
--

/*!40000 ALTER TABLE `msgs` DISABLE KEYS */;
LOCK TABLES `msgs` WRITE;
INSERT INTO `CONTACTS`.`msgs` VALUES  (1,'PersonA','incoming','2012-01-31 5:30 PM',25,'m','03331133454'),
 (2,'PersonD','incoming','2012-01-31 5:30 PM',27,'m','03332333494'),
 (3,'PersonL','incoming','2012-01-31 5:30 PM',28,'m','03333733474'),
 (4,'PersonK','incoming','2012-01-31 5:30 PM',29,'m','03334833654'),
 (5,'PersonJ','incoming','2012-01-31 5:30 PM',22,'m','03335933454'),
 (6,'PersonI','incoming','2012-01-31 5:30 PM',12,'m','03336633451'),
 (7,'PersonH','incoming','2012-01-31 5:30 PM',30,'m','03337533452'),
 (8,'PersonG','incoming','2012-01-31 5:30 PM',40,'m','03338433453'),
 (9,'PersonE','incoming','2012-01-31 5:30 PM',50,'m','03339333456'),
 (10,'PersonF','incoming','2012-01-31 5:30 PM',60,'m','03339233454'),
 (11,'PersonD','incoming','2012-01-31 5:30 PM',70,'m','03338233459'),
 (12,'PersonB','incoming','2012-01-31 5:30 PM',80,'m','03337233458'),
 (13,'PersonC','incoming','2012-01-31 5:30 PM',20,'m','03336233457'),
 (14,'PersonA','incoming','2012-01-31 5:30 PM',10,'m','03335213456');
UNLOCK TABLES;
/*!40000 ALTER TABLE `msgs` ENABLE KEYS */;


--
-- Definition of table `CONTACTS`.`persons`
--

DROP TABLE IF EXISTS `CONTACTS`.`persons`;
CREATE TABLE  `CONTACTS`.`persons` (
  `id_number` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(25) DEFAULT NULL,
  `email_id` varchar(40) DEFAULT NULL,
  `phone_no` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`id_number`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `CONTACTS`.`persons`
--

/*!40000 ALTER TABLE `persons` DISABLE KEYS */;
LOCK TABLES `persons` WRITE;
INSERT INTO `CONTACTS`.`persons` VALUES  (1,'PersonA','azx',NULL),
 (2,'PersonB','zxc',NULL),
 (3,'PersonC','sdf',NULL),
 (4,'PersonD','poi',NULL),
 (5,'PersonE','rty',NULL),
 (6,'PersonF','qwe',NULL),
 (7,'PersonG','dfg',NULL),
 (8,'PersonH','kjh',NULL),
 (9,'PersonI','kjh',NULL),
 (10,'PersonJ','lpo',NULL),
 (11,'PersonK','kli',NULL),
 (12,'PersonL','mnb',NULL);
UNLOCK TABLES;
/*!40000 ALTER TABLE `persons` ENABLE KEYS */;




/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
