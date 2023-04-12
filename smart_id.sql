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
  `emergency_email` VARCHAR(150) NOT NULL,
  `emergency_affiliation` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`emergency_id`)
) ENGINE=INNODB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `emergencyinformation` */

INSERT  INTO `emergencyinformation`(`emergency_id`,`emergency_fname`,`emergency_mname`,`emergency_lname`,`emergency_suffix`,`emergency_gender`,`emergency_address`,`emergency_no`,`emergency_email`,`emergency_affiliation`) VALUES 
(1,'jose','mari','chan','','male','tungko','09234678921','mari01@gmail.com','Father'),
(2,'bogo','jori','jomai','','male','bulacan','09897862221','bogo@yahoo.com','Father'),
(3,'ewqewqe','','wqewqe','','wqewq','ewqe','wqewqewqewq','','Guardian'),
(4,'ewqeqw','','ewqewqewq','','Male','ewqewqewqe','wqeqwewq','','Guardian'),
(5,'eqwewqewqe','','qweqwew','','Male','qewq','ewqewqeqwew','','Guardian');

/*Table structure for table `error_logs` */

DROP TABLE IF EXISTS `error_logs`;

CREATE TABLE `error_logs` (
  `button_error_id` INT(20) NOT NULL AUTO_INCREMENT,
  `button_error_desc` VARCHAR(1000) NOT NULL,
  `button_error_date` VARCHAR(50) NOT NULL,
  `button_error_time` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`button_error_id`)
) ENGINE=INNODB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `error_logs` */

/*Table structure for table `personalinformation` */

DROP TABLE IF EXISTS `personalinformation`;

CREATE TABLE `personalinformation` (
  `personal_id` INT(10) NOT NULL AUTO_INCREMENT,
  `personal_fname` VARCHAR(100) NOT NULL,
  `personal_mname` VARCHAR(100) NOT NULL,
  `personal_lname` VARCHAR(100) NOT NULL,
  `personal_suffix` VARCHAR(10) NOT NULL,
  `personal_bdate` VARCHAR(100) NOT NULL,
  `personal_bplace` VARCHAR(100) NOT NULL,
  `personal_gender` VARCHAR(100) NOT NULL,
  `personal_address` VARCHAR(255) NOT NULL,
  `personal_age` INT(3) NOT NULL,
  `personal_no` VARCHAR(11) NOT NULL,
  `personal_email` VARCHAR(150) NOT NULL,
  PRIMARY KEY (`personal_id`)
) ENGINE=INNODB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `personalinformation` */

INSERT  INTO `personalinformation`(`personal_id`,`personal_fname`,`personal_mname`,`personal_lname`,`personal_suffix`,`personal_bdate`,`personal_bplace`,`personal_gender`,`personal_address`,`personal_age`,`personal_no`,`personal_email`) VALUES 
(1,'Raymark','Lacorte','Cruz','','2000/01/05','Bulacan','male','san jose',23,'09878542312','ray@yahoo.com'),
(2,'albert','chan','gojo','','2000/03/10','tungko','male','san jose',23,'09789898543','albert@yahoo.com'),
(3,'Raymark','dsadsa','ewqewqe','qwewq','17/03/2004','ewqewqeqw','eqwewq','ewqeqw',19,'',''),
(4,'ewqewq','','wqewqewq','','02/03/2023','ewqewq','Male','ewqeqweqw',0,'',''),
(5,'eqwewqeqw','','ewqewqe','','01/03/2023','wqewqe','Male','wqewqewqewqewq',0,'','');

/*Table structure for table `user_login` */

DROP TABLE IF EXISTS `user_login`;

CREATE TABLE `user_login` (
  `user_id` INT(10) NOT NULL AUTO_INCREMENT,
  `user_name` VARCHAR(100) DEFAULT NULL,
  `user_pass` VARCHAR(100) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=INNODB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `user_login` */

INSERT  INTO `user_login`(`user_id`,`user_name`,`user_pass`) VALUES 
(1,'asd','qwe'),
(2,'123','zxc');

/*Table structure for table `user_status` */

DROP TABLE IF EXISTS `user_status`;

CREATE TABLE `user_status` (
  `user_status_id` INT(10) NOT NULL,
  `user_status_action` VARCHAR(255) NOT NULL,
  `user_action_timestamp` VARCHAR(255) NOT NULL
) ENGINE=INNODB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `user_status` */

INSERT  INTO `user_status`(`user_status_id`,`user_status_action`,`user_action_timestamp`) VALUES 
(1,'User 1 has logged in','23/03/2023 10:00:27'),
(1,'User 1 has cleared all information','23/03/2023 10:00:28'),
(1,'User 1 has queried for a search','23/03/2023 10:00:28'),
(1,'User 1 has cleared all information','23/03/2023 10:00:36'),
(1,'User 1 has clicked Save/Update','23/03/2023 10:00:36'),
(1,'User 1 has cleared all information','23/03/2023 10:01:11'),
(1,'User 1 has clicked Save/Update','23/03/2023 10:01:11'),
(1,'User 1 has logged in','24/03/2023 13:09:33'),
(1,'User 1 has logged in','24/03/2023 13:09:43'),
(1,'User 1 has cleared all information','24/03/2023 13:09:49'),
(1,'User 1 has queried for a search','24/03/2023 13:09:49'),
(1,'User 1 has cleared all information','24/03/2023 13:11:13'),
(1,'User 1 has cleared all information','24/03/2023 13:11:16'),
(1,'User 1 has cleared all information','24/03/2023 13:11:28'),
(1,'User 1 has cleared all information','24/03/2023 13:11:31'),
(1,'User 1 has cleared all information','24/03/2023 13:11:33'),
(1,'User 1 has queried for a search','24/03/2023 13:11:33'),
(1,'User 1 has cleared all information','24/03/2023 13:11:40'),
(1,'User 1 has queried for a search','24/03/2023 13:11:40'),
(1,'User 1 has cleared all information','24/03/2023 13:11:43'),
(1,'User 1 has queried for a search','24/03/2023 13:11:43'),
(1,'User 1 has cleared all information','24/03/2023 13:11:47'),
(1,'User 1 has queried for a search','24/03/2023 13:11:47'),
(1,'User 1 has cleared all information','24/03/2023 13:11:54'),
(1,'User 1 has queried for a search','24/03/2023 13:11:54'),
(1,'User 1 has logged in','11/04/2023 14:24:36'),
(1,'User 1 has logged in','11/04/2023 14:26:18'),
(1,'User 1 has logged in','11/04/2023 15:34:51'),
(1,'User 1 has logged in','11/04/2023 15:55:56'),
(1,'User 1 has logged in','11/04/2023 16:05:05'),
(1,'User 1 has logged in','11/04/2023 16:15:12'),
(1,'User 1 has logged in','11/04/2023 16:20:27'),
(1,'User 1 has logged in','11/04/2023 16:33:07'),
(1,'User 1 has logged in','11/04/2023 16:33:56'),
(1,'User 1 has logged in','11/04/2023 16:46:56'),
(1,'User 1 has logged in','11/04/2023 16:47:11'),
(1,'User 1 has logged in','11/04/2023 16:50:59'),
(1,'User 1 has logged in','11/04/2023 16:54:53'),
(1,'User 1 has logged in','12/04/2023 08:47:02'),
(1,'User 1 has logged in','12/04/2023 08:49:05'),
(1,'User 1 has logged in','12/04/2023 08:54:30'),
(1,'User 1 has logged in','12/04/2023 09:37:51');

/*Table structure for table `userinformation` */

DROP TABLE IF EXISTS `userinformation`;

CREATE TABLE `userinformation` (
  `user_id` INT(10) NOT NULL AUTO_INCREMENT,
  `user_no` VARCHAR(15) NOT NULL,
  `user_type` VARCHAR(100) NOT NULL,
  `user_pos_gr_crs` VARCHAR(100) NOT NULL,
  `user_dept_section` VARCHAR(100) NOT NULL,
  `user_lrn_eno` VARCHAR(100) NOT NULL,
  `user_card_id` VARCHAR(100) NOT NULL,
  `user_photo` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=INNODB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `userinformation` */

INSERT  INTO `userinformation`(`user_id`,`user_no`,`user_type`,`user_pos_gr_crs`,`user_dept_section`,`user_lrn_eno`,`user_card_id`,`user_photo`) VALUES 
(1,'2023-023412','Student - Tertiary','crs1','clg1','','','C:/xampp/htdocs/SMART-ID-REGISTRATION-MODULE-v2/img/pug.jpg'),
(2,'2023-405233','Student - Tertiary','crs2','clg3','','','C:/xampp/htdocs/SMART-ID-REGISTRATION-MODULE-v2/img/Sad-pug.jpg'),
(3,'2023-214551','User Type','Pos/Gr/Crs','Dept/Section','','','C:/xampp/htdocs/SMART-ID-REGISTRATION-MODULE-v2/img/Sad-pug.jpg'),
(4,'0000-000000','User Type','Pos/Gr/Crs','Dept/Section','','',''),
(5,'0000-000000','User Type','Pos/Gr/Crs','Dept/Section','','','');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
