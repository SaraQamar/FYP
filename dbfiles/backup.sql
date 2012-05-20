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
-- Create schema contacts
--

CREATE DATABASE IF NOT EXISTS contacts;
USE contacts;

--
-- Definition of table `contacts`.`calls`
--

DROP TABLE IF EXISTS `contacts`.`calls`;
CREATE TABLE  `contacts`.`calls` (
  `ids` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  `e_type` varchar(20) DEFAULT NULL,
  `datetime` datetime DEFAULT NULL,
  `duration` int(11) DEFAULT NULL,
  `key` varchar(4) DEFAULT NULL,
  `e_from` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`ids`),
  KEY `name` (`name`)
) ENGINE=MyISAM AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `contacts`.`calls`
--

/*!40000 ALTER TABLE `calls` DISABLE KEYS */;
LOCK TABLES `calls` WRITE;
INSERT INTO `contacts`.`calls` VALUES  (1,'PersonD','incoming','2012-01-11 01:03:01',25,'c','0989877123'),
 (2,'PersonD','incoming','2012-01-12 03:30:23',27,'c','0989877123'),
 (3,'PersonL','incoming','2012-01-11 02:30:17',28,'c','0989877123'),
 (4,'PersonK','incoming','2012-01-10 01:30:19',29,'c','03331233454'),
 (5,'PersonJ','incoming','2012-01-08 23:30:24',22,'c','03335233454'),
 (6,'PersonI','incoming','2012-01-07 22:30:23',12,'c','03331233454'),
 (7,'PersonH','incoming','2012-01-06 21:30:00',30,'c','03331233454'),
 (8,'PersonG','incoming','2012-01-05 20:30:10',40,'c','03331233474'),
 (9,'PersonE','incoming','2012-01-04 19:30:19',50,'c','03331233474'),
 (10,'PersonF','incoming','2012-01-03 18:30:18',60,'c','03331233474'),
 (11,'PersonD','incoming','2012-01-02 17:30:17',70,'c','03338233459'),
 (12,'PersonB','incoming','2012-12-01 16:30:16',80,'c','03337233458'),
 (13,'PersonC','incoming','2012-11-03 15:30:15',20,'c','03336233457'),
 (14,'PersonA','incoming','2012-10-03 14:30:14',10,'c','03335233456'),
 (15,'PersonD','incoming','2012-10-03 14:30:14',27,'c','03332333494'),
 (16,'PersonL','incoming','2012-11-03 15:30:15',28,'c','03333733474'),
 (17,'PersonK','incoming','2012-12-01 16:30:16',29,'c','03334833654'),
 (18,'PersonJ','incoming','2012-01-02 17:30:17',22,'c','03335933454'),
 (19,'PersonI','incoming','2012-01-03 18:30:18',12,'c','03336633451'),
 (20,'PersonH','incoming','2012-01-04 19:30:19',30,'c','03337533452'),
 (21,'PersonG','incoming','2012-01-06 21:30:06',40,'c','03331233451'),
 (22,'PersonE','incoming','2012-01-07 22:30:23',50,'c','03339333456'),
 (23,'PersonF','incoming','2012-01-08 23:30:24',60,'c','03339233454'),
 (24,'PersonD','incoming','2012-01-10 01:30:19',70,'c','03338233459'),
 (25,'PersonB','incoming','2012-01-09 02:30:15',80,'c','03337233458'),
 (26,'PersonC','incoming','2012-01-11 02:30:17',20,'c','03331233451'),
 (27,'PersonA','incoming','2012-01-12 03:30:23',10,'c','03331233494');
UNLOCK TABLES;
/*!40000 ALTER TABLE `calls` ENABLE KEYS */;


--
-- Definition of table `contacts`.`emails`
--

DROP TABLE IF EXISTS `contacts`.`emails`;
CREATE TABLE  `contacts`.`emails` (
  `ids` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  `e_type` varchar(30) DEFAULT NULL,
  `e_from` varchar(20) DEFAULT NULL,
  `datetime` datetime DEFAULT NULL,
  `duration` int(11) DEFAULT NULL,
  `key` varchar(4) DEFAULT NULL,
  PRIMARY KEY (`ids`),
  KEY `name` (`name`)
) ENGINE=MyISAM AUTO_INCREMENT=26 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `contacts`.`emails`
--

/*!40000 ALTER TABLE `emails` DISABLE KEYS */;
LOCK TABLES `emails` WRITE;
INSERT INTO `contacts`.`emails` VALUES  (1,'PersonD','incoming','0989877123','2012-01-11 01:30:01',25,'e'),
 (2,'PersonD','incoming','0989877123','2012-01-21 02:30:02',27,'e'),
 (3,'PersonL','incoming','0989877123','2012-01-31 03:30:03',28,'e'),
 (4,'PersonK','incoming','0989877123','2012-01-31 04:30:04',29,'e'),
 (5,'PersonJ','incoming','0989877123','2012-01-31 05:30:05',22,'e'),
 (6,'PersonI','incoming','03331233454','2012-02-03 06:30:06',12,'e'),
 (7,'PersonH','incoming','03331233454','2012-03-31 07:30:07',30,'e'),
 (8,'PersonF','incoming','03331233454','2012-06-01 10:30:10',60,'e'),
 (9,'PersonD','incoming','03331233454','2012-01-01 11:30:11',70,'e'),
 (10,'PersonB','incoming','03331233494','2012-02-01 12:30:12',80,'e'),
 (11,'PersonC','incoming','03331233451','2012-03-01 13:30:13',20,'e'),
 (12,'PersonA','incoming','03331233494','2012-04-01 14:30:14',10,'e'),
 (13,'PersonD','incoming','03331233454','2012-05-01 15:30:15',25,'e'),
 (14,'PersonD','incoming','03332233494','2012-02-01 16:30:16',27,'e'),
 (15,'PersonL','incoming','03331233494','2012-01-02 17:30:17',28,'e'),
 (16,'PersonK','incoming','03334233654','2012-01-03 18:30:18',29,'e'),
 (17,'PersonJ','incoming','03335233454','2012-01-04 19:30:19',22,'e'),
 (18,'PersonI','incoming','03331233474','2012-01-05 20:30:10',12,'e'),
 (19,'PersonH','incoming','03331233474','2012-01-06 21:30:00',30,'e'),
 (20,'PersonG','incoming','03331233474','2012-01-07 22:30:23',40,'e'),
 (21,'PersonE','incoming','03339233456','2012-01-08 23:30:24',50,'e'),
 (22,'PersonF','incoming','03339233454','2012-01-09 04:30:15',60,'e'),
 (23,'PersonD','incoming','03338233459','2012-01-10 01:30:19',70,'e'),
 (24,'PersonB','incoming','03337233458','2012-01-11 02:30:17',80,'e'),
 (25,'PersonC','incoming','03331233451','2012-01-12 03:30:23',20,'e');
UNLOCK TABLES;
/*!40000 ALTER TABLE `emails` ENABLE KEYS */;


--
-- Definition of table `contacts`.`msgs`
--

DROP TABLE IF EXISTS `contacts`.`msgs`;
CREATE TABLE  `contacts`.`msgs` (
  `ids` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  `e_type` varchar(20) DEFAULT NULL,
  `datetime` datetime DEFAULT NULL,
  `duration` int(11) DEFAULT NULL,
  `key` varchar(4) DEFAULT NULL,
  `e_from` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`ids`),
  KEY `name` (`name`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `contacts`.`msgs`
--

/*!40000 ALTER TABLE `msgs` DISABLE KEYS */;
LOCK TABLES `msgs` WRITE;
INSERT INTO `contacts`.`msgs` VALUES  (1,'PersonA','incoming','2012-01-12 03:30:23',25,'m','03331233451'),
 (2,'PersonD','incoming','2012-01-11 02:30:17',27,'m','0989877123'),
 (3,'PersonL','incoming','2012-01-09 23:30:15',28,'m','03331233454'),
 (4,'PersonK','incoming','2012-01-10 01:30:19',29,'m','03331233454'),
 (5,'PersonJ','incoming','2012-01-08 23:30:24',22,'m','03335933454'),
 (6,'PersonI','incoming','2012-01-07 22:30:23',12,'m','03331233474'),
 (7,'PersonH','incoming','2012-01-06 21:30:06',30,'m','03331233474'),
 (8,'PersonG','incoming','2012-01-04 19:30:19',40,'m','03331233474'),
 (9,'PersonE','incoming','2012-01-03 18:30:18',50,'m','03339333456'),
 (10,'PersonF','incoming','2012-12-01 16:30:16',60,'m','03339233454'),
 (11,'PersonD','incoming','2012-10-31 14:30:14',70,'m','03338233459'),
 (12,'PersonC','incoming','2012-01-04 19:30:19',20,'m','03331233451'),
 (13,'PersonA','incoming','2012-01-04 19:30:19',10,'m','03335213456');
UNLOCK TABLES;
/*!40000 ALTER TABLE `msgs` ENABLE KEYS */;


--
-- Definition of table `contacts`.`persons`
--

DROP TABLE IF EXISTS `contacts`.`persons`;
CREATE TABLE  `contacts`.`persons` (
  `id_number` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(25) DEFAULT NULL,
  `email_id` varchar(40) DEFAULT NULL,
  `phone_no` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`id_number`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `contacts`.`persons`
--

/*!40000 ALTER TABLE `persons` DISABLE KEYS */;
LOCK TABLES `persons` WRITE;
INSERT INTO `contacts`.`persons` VALUES  (1,'PersonA','azx','0989877123'),
 (2,'PersonB','zxc','03331233454'),
 (3,'PersonC','sdf','03331233494'),
 (4,'PersonD','poi','03331233474'),
 (5,'PersonE','rty','03331233451'),
 (6,'PersonF','qwe','03337233452'),
 (7,'PersonG','dfg','03335213456'),
 (8,'PersonH','kjh','03335933458'),
 (9,'PersonI','kjh','03338233459'),
 (10,'PersonJ','lpo','03337233452'),
 (11,'PersonK','kli','03337233456'),
 (12,'PersonL','mnb','03337233466');
UNLOCK TABLES;
/*!40000 ALTER TABLE `persons` ENABLE KEYS */;




/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
