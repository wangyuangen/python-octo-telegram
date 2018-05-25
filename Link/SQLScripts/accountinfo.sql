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

 Date: 25/05/2018 10:31:12
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for accountinfo
-- ----------------------------
DROP TABLE IF EXISTS `accountinfo`;
CREATE TABLE `accountinfo`  (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Account` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `Pwd` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `HeadImg` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `FontColorId` int(11) NOT NULL,
  PRIMARY KEY (`Id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 13 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

SET FOREIGN_KEY_CHECKS = 1;
