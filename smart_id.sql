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
  `emergency_id` INT(10) NOT NULL AUTO_INCREMENT,
  `emergency_fname` VARCHAR(100) NOT NULL,
  `emergency_mname` VARCHAR(100) NOT NULL,
  `emergency_lname` VARCHAR(100) NOT NULL,
  `emergency_suffix` VARCHAR(10) NOT NULL,
  `emergency_gender` VARCHAR(100) NOT NULL,
  `emergency_address` VARCHAR(100) NOT NULL,
  `emergency_no` VARCHAR(11) NOT NULL,
  `emergency_email` VARCHAR(100) NOT NULL,
  `emergency_affiliation` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`emergency_id`),
  UNIQUE KEY `emergency_email` (`emergency_email`)
) ENGINE=INNODB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `emergencyinformation` */

/*Table structure for table `id_reg_settings` */

DROP TABLE IF EXISTS `id_reg_settings`;

CREATE TABLE `id_reg_settings` (
  `id_reg_id` INT(15) NOT NULL AUTO_INCREMENT,
  `id_reg_hname` VARCHAR(100) NOT NULL,
  `id_reg_uname` VARCHAR(100) NOT NULL,
  `id_reg_password` VARCHAR(100) NOT NULL,
  `id_reg_database` VARCHAR(100) NOT NULL,
  `id_reg_port` VARCHAR(100) NOT NULL,
  `id_reg_path` VARCHAR(4000) NOT NULL,
  `id_reg_cname` VARCHAR(150) NOT NULL,
  `id_reg_abbreviation` VARCHAR(100) NOT NULL,
  `id_reg_photo` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id_reg_id`)
) ENGINE=INNODB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `id_reg_settings` */

/*Table structure for table `personalinformation` */

DROP TABLE IF EXISTS `personalinformation`;

CREATE TABLE `personalinformation` (
  `personal_id` INT(10) NOT NULL AUTO_INCREMENT,
  `personal_fname` VARCHAR(100) NOT NULL,
  `personal_mname` VARCHAR(100) NOT NULL,
  `personal_lname` VARCHAR(100) NOT NULL,
  `personal_suffix` VARCHAR(10) NOT NULL,
  `personal_bdate` DATE NOT NULL,
  `personal_bplace` VARCHAR(100) NOT NULL,
  `personal_gender` VARCHAR(100) NOT NULL,
  `personal_address` VARCHAR(255) NOT NULL,
  `personal_age` INT(3) NOT NULL,
  `personal_no` VARCHAR(11) NOT NULL,
  `personal_email` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`personal_id`),
  UNIQUE KEY `personal_email` (`personal_email`)
) ENGINE=INNODB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `personalinformation` */

INSERT  INTO `personalinformation`(`personal_id`,`personal_fname`,`personal_mname`,`personal_lname`,`personal_suffix`,`personal_bdate`,`personal_bplace`,`personal_gender`,`personal_address`,`personal_age`,`personal_no`,`personal_email`) VALUES 
(2,'eqweqw','3qwe','wqewqewqeds','dasdsa','0000-00-00','wqedsad','asds','adasdsad',12,'321321421','ewqewq@yahoo.com'),
(3,'eqweqw3','3qwe','wqewqewqeds','dasdsa','0000-00-00','wqedsad','asds','adasdsad',12,'321321421','ewqeq@yahoo.com');

/*Table structure for table `userinformation` */

DROP TABLE IF EXISTS `userinformation`;

CREATE TABLE `userinformation` (
  `user_id` INT(10) NOT NULL AUTO_INCREMENT,
  `user_no` INT(10) NOT NULL,
  `user_type` VARCHAR(100) NOT NULL,
  `user_pos_gr_crs` VARCHAR(100) NOT NULL,
  `user_dept_section` VARCHAR(100) NOT NULL,
  `user_lrn_eno` VARCHAR(100) NOT NULL,
  `user_card_id` VARCHAR(100) NOT NULL,
  `user_photo` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=INNODB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `userinformation` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

CREATE TABLE user_login (
user_id INT(10) PRIMARY KEY NOT NULL AUTO_INCREMENT,
user_name VARCHAR(100),
user_pass VARCHAR(100)
);

INSERT INTO user_login(user_name, user_pass) VALUES ('asd', 'qwe');
INSERT INTO user_login(user_name, user_pass) VALUES ('123', 'zxc');