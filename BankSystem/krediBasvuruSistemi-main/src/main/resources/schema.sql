drop database IF EXISTS `test`;

create database test;
use  test;

DROP TABLE IF EXISTS `user`;
 SET character_set_client = utf8mb4 ;

CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `identity` bigint(20) NOT NULL,
  `phone` varchar(100) NOT NULL,
  `in_come` int(100) NOT NULL,
  `credit_score` int(100) NOT NULL,
  `credit_amount` bigint(20) NOT NULL,
  `credit_status` bit(1) DEFAULT NULL,
   PRIMARY KEY (`id`)
)