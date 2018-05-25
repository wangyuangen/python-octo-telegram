/*
 Navicat Premium Data Transfer

 Source Server         : mysql-local
 Source Server Type    : MySQL
 Source Server Version : 50527
 Source Host           : localhost:3306
 Source Schema         : link

 Target Server Type    : MySQL
 Target Server Version : 50527
 File Encoding         : 65001

 Date: 25/05/2018 10:31:43
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for relationship
-- ----------------------------
DROP TABLE IF EXISTS `relationship`;
CREATE TABLE `relationship`  (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `OwnerId` int(11) NOT NULL,
  `CustomerId` int(11) NOT NULL,
  `RelationDes` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `Note` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`Id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

SET FOREIGN_KEY_CHECKS = 1;
