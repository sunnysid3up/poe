DROP TABLE IF EXISTS `class`;

CREATE TABLE `class` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(10) DEFAULT NULL,
  `announced_date` date DEFAULT NULL,
  `core_attribute` varchar(10) DEFAULT NULL,
  `combat_focuses` varchar(50) DEFAULT NULL,
  `lore` longtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4