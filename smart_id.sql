/*
SQLyog Community v13.2.0 (64 bit)
MySQL - 10.4.27-MariaDB : Database - smart_id
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`smart_id` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;

USE `smart_id`;

/*Table structure for table `emergencyinformation` */

DROP TABLE IF EXISTS `emergencyinformation`;

CREATE TABLE `emergencyinformation` (
  `emergency_id` int(10) NOT NULL AUTO_INCREMENT,
  `emergency_fname` varchar(100) NOT NULL,
  `emergency_mname` varchar(100) NOT NULL,
  `emergency_lname` varchar(100) NOT NULL,
  `emergency_suffix` varchar(10) NOT NULL,
  `emergency_gender` varchar(100) NOT NULL,
  `emergency_address` varchar(100) NOT NULL,
  `emergency_no` varchar(11) NOT NULL,
  `emergency_email` varchar(150) NOT NULL,
  `emergency_affiliation` varchar(100) NOT NULL,
  PRIMARY KEY (`emergency_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `emergencyinformation` */

/*Table structure for table `id_reg_settings` */

DROP TABLE IF EXISTS `id_reg_settings`;

CREATE TABLE `id_reg_settings` (
  `id_reg_id` int(15) NOT NULL AUTO_INCREMENT,
  `id_reg_hname` varchar(100) NOT NULL,
  `id_reg_uname` varchar(100) NOT NULL,
  `id_reg_password` varchar(100) NOT NULL,
  `id_reg_database` varchar(100) NOT NULL,
  `id_reg_port` varchar(100) NOT NULL,
  `id_reg_path` varchar(4000) NOT NULL,
  `id_reg_cname` varchar(150) NOT NULL,
  `id_reg_abbreviation` varchar(100) NOT NULL,
  `id_reg_photo` varchar(255) NOT NULL,
  PRIMARY KEY (`id_reg_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `id_reg_settings` */

/*Table structure for table `personalinformation` */

DROP TABLE IF EXISTS `personalinformation`;

CREATE TABLE `personalinformation` (
  `personal_id` int(10) NOT NULL AUTO_INCREMENT,
  `personal_fname` varchar(100) NOT NULL,
  `personal_mname` varchar(100) NOT NULL,
  `personal_lname` varchar(100) NOT NULL,
  `personal_suffix` varchar(10) NOT NULL,
  `personal_bdate` date NOT NULL,
  `personal_bplace` varchar(100) NOT NULL,
  `personal_gender` varchar(100) NOT NULL,
  `personal_address` varchar(255) NOT NULL,
  `personal_age` int(3) NOT NULL,
  `personal_no` varchar(11) NOT NULL,
  `personal_email` varchar(150) NOT NULL,
  PRIMARY KEY (`personal_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `personalinformation` */

insert  into `personalinformation`(`personal_id`,`personal_fname`,`personal_mname`,`personal_lname`,`personal_suffix`,`personal_bdate`,`personal_bplace`,`personal_gender`,`personal_address`,`personal_age`,`personal_no`,`personal_email`) values 
(2,'eqweqw','3qwe','wqewqewqeds','dasdsa','0000-00-00','wqedsad','asds','adasdsad',12,'321321421',''),
(3,'eqweqw3','3qwe','wqewqewqeds','dasdsa','0000-00-00','wqedsad','asds','adasdsad',12,'321321421','');

/*Table structure for table `user_login` */

DROP TABLE IF EXISTS `user_login`;

CREATE TABLE `user_login` (
  `user_id` int(10) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(100) DEFAULT NULL,
  `user_pass` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `user_login` */

insert  into `user_login`(`user_id`,`user_name`,`user_pass`) values 
(1,'asd','qwe'),
(2,'123','zxc');

/*Table structure for table `userinformation` */

DROP TABLE IF EXISTS `userinformation`;

CREATE TABLE `userinformation` (
  `user_id` int(10) NOT NULL AUTO_INCREMENT,
  `user_no` int(10) NOT NULL,
  `user_type` varchar(100) NOT NULL,
  `user_pos_gr_crs` varchar(100) NOT NULL,
  `user_dept_section` varchar(100) NOT NULL,
  `user_lrn_eno` varchar(100) NOT NULL,
  `user_card_id` varchar(100) NOT NULL,
  `user_photo` varchar(255) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `userinformation` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
