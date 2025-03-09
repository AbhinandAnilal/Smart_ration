/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.5.8-log : Database - smart_ration
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`smart_ration` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `smart_ration`;

/*Table structure for table `buy` */

DROP TABLE IF EXISTS `buy`;

CREATE TABLE `buy` (
  `buy_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `tamount` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`buy_id`),
  KEY `user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `buy` */

/*Table structure for table `buydetails` */

DROP TABLE IF EXISTS `buydetails`;

CREATE TABLE `buydetails` (
  `bdetail_id` int(11) NOT NULL AUTO_INCREMENT,
  `buy_id` int(11) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  `quantity` varchar(100) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`bdetail_id`),
  KEY `buy_id` (`buy_id`),
  KEY `product_id` (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `buydetails` */

/*Table structure for table `complaints` */

DROP TABLE IF EXISTS `complaints`;

CREATE TABLE `complaints` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `complaint_title` varchar(100) NOT NULL,
  `description` varchar(1000) NOT NULL,
  `reply` varchar(1000) NOT NULL,
  `date` varchar(50) NOT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

/*Data for the table `complaints` */

insert  into `complaints`(`complaint_id`,`user_id`,`complaint_title`,`description`,`reply`,`date`) values 
(1,1,'sam','fog','helloo','2023-1-20'),
(2,2,'smpl2','fdfhdsfbgsdvgh','hi','2023-10-21'),
(3,1,'hi','helloi','NA','2023-10-27'),
(4,1,'hello','how r u','Pending','2023-10-30');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `feedback` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`feedback_id`),
  KEY `user_id` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`feedback_id`,`user_id`,`feedback`,`date`) values 
(1,1,'not good','23/02/2020');

/*Table structure for table `govtstaff` */

DROP TABLE IF EXISTS `govtstaff`;

CREATE TABLE `govtstaff` (
  `staff_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `fname` varchar(50) DEFAULT NULL,
  `lname` varchar(50) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `designation` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`staff_id`),
  KEY `login_id` (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `govtstaff` */

insert  into `govtstaff`(`staff_id`,`login_id`,`fname`,`lname`,`place`,`phone`,`email`,`designation`) values 
(2,3,'anju','m','ernakulam','2345678908','abi@gmail.com','nkjnn');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `usertype` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`login_id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values 
(1,'admin','admin','admin'),
(2,'anu','12345','govtstaff'),
(3,'a','a','govtstaff'),
(4,'shop','shop','shop'),
(5,'jd','khdkj','shop'),
(6,'s','s','shop'),
(7,'hotel1','12334','hotel');

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `notification_id` int(11) NOT NULL AUTO_INCREMENT,
  `notification` varchar(100) DEFAULT NULL,
  `details` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`notification_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

insert  into `notification`(`notification_id`,`notification`,`details`,`date`) values 
(2,'noti2','ghvghv','2024-03-08');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `buy_id` int(11) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`payment_id`),
  KEY `buy_id` (`buy_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

/*Table structure for table `products` */

DROP TABLE IF EXISTS `products`;

CREATE TABLE `products` (
  `product_id` int(11) NOT NULL AUTO_INCREMENT,
  `product` varchar(100) DEFAULT NULL,
  `details` varchar(100) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `products` */

insert  into `products`(`product_id`,`product`,`details`,`amount`) values 
(2,'product1','ghvghv','6000');

/*Table structure for table `rating` */

DROP TABLE IF EXISTS `rating`;

CREATE TABLE `rating` (
  `rating_id` int(11) NOT NULL AUTO_INCREMENT,
  `shop_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `rated` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`rating_id`),
  KEY `shop_id` (`shop_id`),
  KEY `user_id` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `rating` */

insert  into `rating`(`rating_id`,`shop_id`,`user_id`,`rated`,`date`) values 
(1,2,1,'4.0','4/2/24');

/*Table structure for table `rationcard` */

DROP TABLE IF EXISTS `rationcard`;

CREATE TABLE `rationcard` (
  `rationcard_id` int(11) NOT NULL AUTO_INCREMENT,
  `cardnumber` varchar(50) DEFAULT NULL,
  `request_id` int(11) DEFAULT NULL,
  `type_id` int(11) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`rationcard_id`),
  KEY `request_id` (`request_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `rationcard` */

insert  into `rationcard`(`rationcard_id`,`cardnumber`,`request_id`,`type_id`,`date`) values 
(1,'68768687687',1,2,'2024-03-09');

/*Table structure for table `requestdetail` */

DROP TABLE IF EXISTS `requestdetail`;

CREATE TABLE `requestdetail` (
  `rdetail_id` int(11) NOT NULL AUTO_INCREMENT,
  `request_id` int(11) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `relation` varchar(50) DEFAULT NULL,
  `designation` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`rdetail_id`),
  KEY `request_id` (`request_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `requestdetail` */

insert  into `requestdetail`(`rdetail_id`,`request_id`,`name`,`relation`,`designation`) values 
(1,1,'anu1','hhh','ndmns,');

/*Table structure for table `requestrationcard` */

DROP TABLE IF EXISTS `requestrationcard`;

CREATE TABLE `requestrationcard` (
  `request_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`request_id`),
  KEY `user_id` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `requestrationcard` */

insert  into `requestrationcard`(`request_id`,`user_id`,`status`) values 
(1,1,'upload'),
(2,1,'reject');

/*Table structure for table `setproducttotype` */

DROP TABLE IF EXISTS `setproducttotype`;

CREATE TABLE `setproducttotype` (
  `ptype_id` int(11) NOT NULL AUTO_INCREMENT,
  `type_id` int(11) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  `kiloorlitter` varchar(20) DEFAULT NULL,
  `forthemonth` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`ptype_id`),
  KEY `type_id` (`type_id`),
  KEY `product_id` (`product_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `setproducttotype` */

insert  into `setproducttotype`(`ptype_id`,`type_id`,`product_id`,`kiloorlitter`,`forthemonth`) values 
(1,2,2,'10','2024-02'),
(2,2,2,'10','2024-03');

/*Table structure for table `shop` */

DROP TABLE IF EXISTS `shop`;

CREATE TABLE `shop` (
  `shop_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `fname` varchar(50) DEFAULT NULL,
  `lname` varchar(50) DEFAULT NULL,
  `shop` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`shop_id`),
  KEY `login_id` (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `shop` */

insert  into `shop`(`shop_id`,`login_id`,`fname`,`lname`,`shop`,`place`,`phone`,`email`) values 
(1,4,'shop1','nd','nkjdn','sakjn','6876876','e@gmail.com'),
(2,6,'shop1','j','shopname','ernakulam','2345678908','abi@gmail.com');

/*Table structure for table `staffdetail` */

DROP TABLE IF EXISTS `staffdetail`;

CREATE TABLE `staffdetail` (
  `sdetail_id` int(11) NOT NULL AUTO_INCREMENT,
  `request_id` int(11) DEFAULT NULL,
  `detail` varchar(100) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`sdetail_id`),
  KEY `request_id` (`request_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `staffdetail` */

insert  into `staffdetail`(`sdetail_id`,`request_id`,`detail`,`status`) values 
(1,1,'det','ration card');

/*Table structure for table `stock` */

DROP TABLE IF EXISTS `stock`;

CREATE TABLE `stock` (
  `stock_id` int(11) NOT NULL AUTO_INCREMENT,
  `shop_id` int(11) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`stock_id`),
  KEY `shop_id` (`shop_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `stock` */

insert  into `stock`(`stock_id`,`shop_id`,`date`) values 
(1,2,'23/02/24'),
(2,2,'2024-03-08'),
(3,2,'2024-03-08');

/*Table structure for table `stockdetail` */

DROP TABLE IF EXISTS `stockdetail`;

CREATE TABLE `stockdetail` (
  `detail_id` int(11) NOT NULL AUTO_INCREMENT,
  `stock_id` int(11) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  `kiloorlitter` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`detail_id`),
  KEY `stock_id` (`stock_id`),
  KEY `product_id` (`product_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `stockdetail` */

insert  into `stockdetail`(`detail_id`,`stock_id`,`product_id`,`kiloorlitter`) values 
(1,1,2,'10'),
(2,2,2,'60');

/*Table structure for table `timeallocate` */

DROP TABLE IF EXISTS `timeallocate`;

CREATE TABLE `timeallocate` (
  `time_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `shop_id` int(11) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `time` varchar(100) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`time_id`),
  KEY `user_id` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `timeallocate` */

insert  into `timeallocate`(`time_id`,`user_id`,`shop_id`,`date`,`time`,`status`) values 
(1,1,2,'5/4/2024','3.00','Reject');

/*Table structure for table `type` */

DROP TABLE IF EXISTS `type`;

CREATE TABLE `type` (
  `type_id` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(50) DEFAULT NULL,
  `details` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`type_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `type` */

insert  into `type`(`type_id`,`type`,`details`) values 
(2,'APL','ghvghv'),
(3,'BPL','ghvghv');

/*Table structure for table `users` */

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `fname` varchar(50) DEFAULT NULL,
  `lname` varchar(50) DEFAULT NULL,
  `hname` varchar(100) DEFAULT NULL,
  `ward` varchar(50) DEFAULT NULL,
  `hno` varchar(50) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `age` varchar(100) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `designation` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  KEY `login_id` (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `users` */

insert  into `users`(`user_id`,`login_id`,`fname`,`lname`,`hname`,`ward`,`hno`,`place`,`age`,`gender`,`phone`,`email`,`designation`) values 
(1,2,'fdm','dsnf','kjrfn','7687','65768','bdbsnmb','33','male','79878979','a@gmail.com','dsnf');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
