/*
 Navicat Premium Data Transfer

 Source Server         : local-mamp
 Source Server Type    : MySQL
 Source Server Version : 50723
 Source Host           : localhost
 Source Database       : Simple-data-visualization

 Target Server Type    : MySQL
 Target Server Version : 50723
 File Encoding         : utf-8

 Date: 07/13/2019 22:33:46 PM
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `activity`
-- ----------------------------
DROP TABLE IF EXISTS `activity`;
CREATE TABLE `activity` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `position` int(11) NOT NULL,
  `activity` varchar(25) NOT NULL,
  `duration` float NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `activity`
-- ----------------------------
BEGIN;
INSERT INTO `activity` VALUES ('2', '2', 'Tennis', '1'), ('4', '4', 'Soccer', '1'), ('5', '5', 'Tennis', '1.5'), ('7', '7', 'Badminton', '2'), ('13', '8', 'Soccer', '2'), ('16', '1', 'Hiking', '3');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
