CREATE DATABASE IF NOT EXISTS `tortix`;

use tortix;

CREATE TABLE IF NOT EXISTS `tortix_scanner` (
  `sid` int(11) NOT NULL auto_increment,
  `id` int(11) NOT NULL default '0',
  `type` varchar(60) NOT NULL default '',
  `stype` varchar(60) NOT NULL default '',
  PRIMARY KEY  (`sid`),
  UNIQUE KEY `its` (`id`,`type`,`stype`)
) ENGINE=MyISAM AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;

