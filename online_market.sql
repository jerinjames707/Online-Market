-- phpMyAdmin SQL Dump
-- version 4.1.6
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Jul 19, 2023 at 10:55 AM
-- Server version: 5.6.16
-- PHP Version: 5.5.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `online_market`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=61 ;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add booking', 7, 'add_booking'),
(26, 'Can change booking', 7, 'change_booking'),
(27, 'Can delete booking', 7, 'delete_booking'),
(28, 'Can view booking', 7, 'view_booking'),
(29, 'Can add category', 8, 'add_category'),
(30, 'Can change category', 8, 'change_category'),
(31, 'Can delete category', 8, 'delete_category'),
(32, 'Can view category', 8, 'view_category'),
(33, 'Can add payment', 9, 'add_payment'),
(34, 'Can change payment', 9, 'change_payment'),
(35, 'Can delete payment', 9, 'delete_payment'),
(36, 'Can view payment', 9, 'view_payment'),
(37, 'Can add reportss', 10, 'add_reportss'),
(38, 'Can change reportss', 10, 'change_reportss'),
(39, 'Can delete reportss', 10, 'delete_reportss'),
(40, 'Can view reportss', 10, 'view_reportss'),
(41, 'Can add subcategory', 11, 'add_subcategory'),
(42, 'Can change subcategory', 11, 'change_subcategory'),
(43, 'Can delete subcategory', 11, 'delete_subcategory'),
(44, 'Can view subcategory', 11, 'view_subcategory'),
(45, 'Can add user_feedback', 12, 'add_user_feedback'),
(46, 'Can change user_feedback', 12, 'change_user_feedback'),
(47, 'Can delete user_feedback', 12, 'delete_user_feedback'),
(48, 'Can view user_feedback', 12, 'view_user_feedback'),
(49, 'Can add userregg', 13, 'add_userregg'),
(50, 'Can change userregg', 13, 'change_userregg'),
(51, 'Can delete userregg', 13, 'delete_userregg'),
(52, 'Can view userregg', 13, 'view_userregg'),
(53, 'Can add wrkr_feedback', 14, 'add_wrkr_feedback'),
(54, 'Can change wrkr_feedback', 14, 'change_wrkr_feedback'),
(55, 'Can delete wrkr_feedback', 14, 'delete_wrkr_feedback'),
(56, 'Can view wrkr_feedback', 14, 'view_wrkr_feedback'),
(57, 'Can add wrkregg', 15, 'add_wrkregg'),
(58, 'Can change wrkregg', 15, 'change_wrkregg'),
(59, 'Can delete wrkregg', 15, 'delete_wrkregg'),
(60, 'Can view wrkregg', 15, 'view_wrkregg');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `city360_auction`
--

CREATE TABLE IF NOT EXISTS `city360_auction` (
  `item_name` varchar(225) NOT NULL,
  `price` varchar(225) NOT NULL,
  `disc` varchar(225) NOT NULL,
  `file` varchar(225) NOT NULL,
  `start_date` varchar(225) NOT NULL,
  `end_date` varchar(225) NOT NULL,
  `seller_id` varchar(225) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `city360_auction`
--

INSERT INTO `city360_auction` (`item_name`, `price`, `disc`, `file`, `start_date`, `end_date`, `seller_id`, `id`, `user_id`) VALUES
('jeans', '6000', '34rtghnth', '15.jpg', '2023-07-15T19:08', '2023-07-17T19:07', '2', 1, 2),
('shirts', '4000', 'qwertyuiop', '1 (1).jpg', '2023-07-15T09:17', '2023-07-16T11:10', '2', 2, 1);

-- --------------------------------------------------------

--
-- Table structure for table `city360_auctionpayment`
--

CREATE TABLE IF NOT EXISTS `city360_auctionpayment` (
  `user_id` varchar(111) NOT NULL,
  `seller_id` varchar(111) NOT NULL,
  `item_name` varchar(111) NOT NULL,
  `price` varchar(111) NOT NULL,
  `date` varchar(111) NOT NULL,
  `card_name` varchar(111) NOT NULL,
  `card_type` varchar(111) NOT NULL,
  `card_no` varchar(111) NOT NULL,
  `cvv` varchar(111) NOT NULL,
  `item_id` varchar(111) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `city360_auctionpayment`
--

INSERT INTO `city360_auctionpayment` (`user_id`, `seller_id`, `item_name`, `price`, `date`, `card_name`, `card_type`, `card_no`, `cvv`, `item_id`, `id`) VALUES
('2', '2', 'jeans', '6000', '2023-07-18', 'jerin', 'credit', '1268612681798733', '765', '1', 1);

-- --------------------------------------------------------

--
-- Table structure for table `city360_cartitem`
--

CREATE TABLE IF NOT EXISTS `city360_cartitem` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `item_name` varchar(225) NOT NULL,
  `price` varchar(225) NOT NULL,
  `description` varchar(225) NOT NULL,
  `image` tinytext NOT NULL,
  `user_id` int(11) NOT NULL,
  `quantity` int(225) NOT NULL,
  `p_id` int(11) NOT NULL,
  `total` varchar(225) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `city360_payment`
--

CREATE TABLE IF NOT EXISTS `city360_payment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `item_name` varchar(225) NOT NULL,
  `quantity` varchar(225) NOT NULL,
  `total_price` varchar(225) NOT NULL,
  `date` date NOT NULL,
  `card_name` varchar(225) NOT NULL,
  `card_type` varchar(225) NOT NULL,
  `card_no` varchar(225) NOT NULL,
  `cvv` varchar(225) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `city360_payment`
--

INSERT INTO `city360_payment` (`id`, `item_name`, `quantity`, `total_price`, `date`, `card_name`, `card_type`, `card_no`, `cvv`, `user_id`) VALUES
(1, 'jeans', '1', '5000', '2023-07-18', 'jerin', 'debit', '1268612681798733', '213', 2);

-- --------------------------------------------------------

--
-- Table structure for table `city360_product`
--

CREATE TABLE IF NOT EXISTS `city360_product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `item_name` varchar(225) NOT NULL,
  `price` varchar(225) NOT NULL,
  `date` varchar(225) NOT NULL,
  `disc` varchar(225) NOT NULL,
  `seller_id` int(11) NOT NULL,
  `file` tinytext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `city360_product`
--

INSERT INTO `city360_product` (`id`, `item_name`, `price`, `date`, `disc`, `seller_id`, `file`) VALUES
(1, 'iphone', '85000', '2023-07-07', 'qwertyuiop', 1, '1.png'),
(2, 'jeans', '5000', '2023-07-07', '34rtghnth', 2, 'Screenshot (7).png'),
(3, 'shirts', '1999', '2023-07-15', 'qwertyuiop', 2, '1 (1).jpg');

-- --------------------------------------------------------

--
-- Table structure for table `city360_ratings`
--

CREATE TABLE IF NOT EXISTS `city360_ratings` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `p_id` varchar(111) NOT NULL,
  `star` varchar(111) NOT NULL,
  `u_id` varchar(111) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `city360_ratings`
--

INSERT INTO `city360_ratings` (`id`, `p_id`, `star`, `u_id`) VALUES
(1, 'jeans', '4', 'akhil');

-- --------------------------------------------------------

--
-- Table structure for table `city360_returnitem`
--

CREATE TABLE IF NOT EXISTS `city360_returnitem` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `item_name` varchar(225) NOT NULL,
  `total_price` varchar(225) NOT NULL,
  `date` varchar(225) NOT NULL,
  `return_reasons` varchar(225) NOT NULL,
  `status` varchar(225) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `city360_returnitem`
--

INSERT INTO `city360_returnitem` (`id`, `item_name`, `total_price`, `date`, `return_reasons`, `status`, `user_id`) VALUES
(1, 'jeans', '5000', '2023-07-17', 'bad ', 'approved', 2),
(2, 'jeans', '25000', '2023-07-17', 'feel bad', 'approved', 1),
(3, 'jeans', '25000', '2023-07-17', 'bnmnb', 'Rejected', 1),
(4, 'shirts', '3998', '2023-07-17', 'fghj', 'pending', 1);

-- --------------------------------------------------------

--
-- Table structure for table `city360_sellerregg`
--

CREATE TABLE IF NOT EXISTS `city360_sellerregg` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  `email` varchar(150) NOT NULL,
  `phone` varchar(150) NOT NULL,
  `password` varchar(150) NOT NULL,
  `status` varchar(150) NOT NULL,
  `file` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `city360_sellerregg`
--

INSERT INTO `city360_sellerregg` (`id`, `name`, `email`, `phone`, `password`, `status`, `file`) VALUES
(2, 'annu', 'annu@gmail.com', '7764535264', 'Rr@12345', 'approved', '3.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `city360_selr_feedback`
--

CREATE TABLE IF NOT EXISTS `city360_selr_feedback` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `feedback` varchar(225) NOT NULL,
  `seller_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `city360_selr_feedback`
--

INSERT INTO `city360_selr_feedback` (`id`, `feedback`, `seller_id`) VALUES
(1, 'sdfg', 2);

-- --------------------------------------------------------

--
-- Table structure for table `city360_upd_bid`
--

CREATE TABLE IF NOT EXISTS `city360_upd_bid` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `item_name` varchar(225) NOT NULL,
  `disc` varchar(225) NOT NULL,
  `price` varchar(225) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `city360_userregg`
--

CREATE TABLE IF NOT EXISTS `city360_userregg` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  `email` varchar(150) NOT NULL,
  `phone` varchar(150) NOT NULL,
  `password` varchar(150) NOT NULL,
  `status` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `city360_userregg`
--

INSERT INTO `city360_userregg` (`id`, `name`, `email`, `phone`, `password`, `status`) VALUES
(1, 'davood', 'a@gamil.com', '9876543210', 'Ee@12345', 'approved'),
(2, 'akhil', 'akhil@gmail.com', '9898746553', 'aA@12345', 'approved'),
(3, 'anu', 'anu@gmail.com', '7896543233', 'Vv@12345', 'pending');

-- --------------------------------------------------------

--
-- Table structure for table `city360_user_feeback`
--

CREATE TABLE IF NOT EXISTS `city360_user_feeback` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `feedback` varchar(225) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `city360_user_feeback`
--

INSERT INTO `city360_user_feeback` (`id`, `feedback`, `user_id`) VALUES
(1, 'good', 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=16 ;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(7, 'city360', 'booking'),
(8, 'city360', 'category'),
(9, 'city360', 'payment'),
(10, 'city360', 'reportss'),
(11, 'city360', 'subcategory'),
(13, 'city360', 'userregg'),
(12, 'city360', 'user_feedback'),
(15, 'city360', 'wrkregg'),
(14, 'city360', 'wrkr_feedback'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=22 ;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-04-18 12:09:54.368913'),
(2, 'auth', '0001_initial', '2023-04-18 12:09:55.245055'),
(3, 'admin', '0001_initial', '2023-04-18 12:09:55.420491'),
(4, 'admin', '0002_logentry_remove_auto_add', '2023-04-18 12:09:55.433484'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2023-04-18 12:09:55.448485'),
(6, 'contenttypes', '0002_remove_content_type_name', '2023-04-18 12:09:55.567536'),
(7, 'auth', '0002_alter_permission_name_max_length', '2023-04-18 12:09:55.629424'),
(8, 'auth', '0003_alter_user_email_max_length', '2023-04-18 12:09:55.691074'),
(9, 'auth', '0004_alter_user_username_opts', '2023-04-18 12:09:55.703065'),
(10, 'auth', '0005_alter_user_last_login_null', '2023-04-18 12:09:55.765583'),
(11, 'auth', '0006_require_contenttypes_0002', '2023-04-18 12:09:55.770576'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2023-04-18 12:09:55.782579'),
(13, 'auth', '0008_alter_user_username_max_length', '2023-04-18 12:09:55.842591'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2023-04-18 12:09:55.903070'),
(15, 'auth', '0010_alter_group_name_max_length', '2023-04-18 12:09:55.968037'),
(16, 'auth', '0011_update_proxy_permissions', '2023-04-18 12:09:55.979999'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2023-04-18 12:09:56.044261'),
(18, 'city360', '0001_initial', '2023-04-18 12:09:56.465489'),
(19, 'city360', '0002_auto_20230418_1616', '2023-04-18 12:09:56.864365'),
(20, 'sessions', '0001_initial', '2023-04-18 12:09:56.939962'),
(21, 'city360', '0003_wrkregg_file', '2023-05-20 06:56:27.436957');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('021fj6ocxy9o64erz51din33kih2t9v1', 'e30:1qLN9q:nUO087xUvgUt02qjmdRLVdRJMIrqgiv7_7OgU2uq05U', '2023-07-31 12:16:54.130557'),
('0auz5jxdgyr51ged0rk4wt9b0gefns16', '.eJxNyrEKgzAQgOF3uVmEOGYybiItHewDhPOQYJKD60mQ0ndvsrn-3_-FEjawxnRQsk8EFgrLQTIMUBNSVmlxei-Le7l1frpHA0o-xNs87i30yKkqeqWd5aqOnD8qJ2rg3FEkVAnoI_z-Iv8oXA:1q2QtB:zrpDxXi2f51_KLIIBiXcEV7WzsBQQqbDJsBVLT7keaI', '2023-06-09 06:25:25.835102'),
('1axygluccix1tyspt54jfkz5ip3qls00', 'e30:1qLoOD:7TqP23MHJ55dJcKelg60-kMpPlzV9hg1Hj0a5YmsuZQ', '2023-08-01 17:21:33.381956'),
('2jp3slw6xphgql2i7kgf23cvejzyum7l', '.eJyrVsrJT8_MK0lJLUnMzFGyUkpMyc3Mc0jPBfL0kvNzlXQgIjAZpVoAy3IRew:1q1KUh:LYzMRRz4eRj3BzV3IjFDJKWOJ07YTNV5vwvETCWvRyY', '2023-06-06 05:23:35.369797'),
('33d219act46e4dz6f7ugsinau2u9u7u3', '.eJyrVirNTFGyMtdRKs1LzE1VslIqLU4tMjJSAgqk5iZm5sBFHNJBXL3k_FygXHJpMVACRNYCALO1FOA:1pryWB:2Ff4Z67IfuHh-rgFaC8pVeS3IFy1rrku7tVX8c3y0M8', '2023-05-11 10:06:27.184925'),
('bq7krer7x3p50ehzwk26jq2ubvz1docw', '.eJyrVsrJT8_MK0lJLUnMzFGyUkpMyc3Mc0jPBfL0kvNzlXQgIjAZpVoAy3IRew:1q5Nw8:D3ijOGE1s0nNiobshEfIgHJIn8xm27NxcPZyWINB9OM', '2023-06-17 09:52:40.859803'),
('c8cqxhdlwfcy81hj9pvb6t1vh9dgtmvp', '.eJyrVirPTFGyMtJRKs9LzE1VslIqzy_KTi0yckjPTczM0UvOz1UCyqWCODgkkxNLUtPziyqB0gU5pblJqUVKtQD9SB2p:1pokZ6:eNSjbp7rr1jUYyX_kDtDRwPz5QXWEwugQdTEJk-fq9c', '2023-05-02 12:36:08.737756'),
('le3rnpd8hteo1nnr2szsepz075uapfn6', 'eyJ1aWQiOjEsInVuYW1lIjoiZGF2b29kIiwidWVtYWlsIjoiYUBnYW1pbC5jb20iLCJjdXMiOiJjdXMifQ:1qLnUh:wvZikItaoOdLMBhcmKNzeVCCVeuLZtKnEqYT1-uaAsk', '2023-08-01 16:24:11.657062'),
('p2cla9v0p2sju8lgvwoupqrqm7u6xkf4', '.eJyrVsrJT8_MK0lJLUnMzFGyUkpMyc3Mc0jPBfL0kvNzlXQgIjAZpVoAy3IRew:1q0yTq:WMWdXqiz3XMiLC83Z64IZyQkXWpy28rKi6x5yzfVe5U', '2023-06-05 05:53:14.242114'),
('pf8p045zn6vwxtz7tpkmuhrew3rxb6za', '.eJyrVirPTFGyMjTTUSrPS8xNVbJSKkktLlECclMyi4E8P1cfH_8gV5BAam5iZg5UgUM6iKOXnJ8LlElOLElNzy-qBMoVJGbmlaQW6RTklOYmpRYBJQtyEpNBxjqFens7BjiGePo5-irVAgD2ziZP:1q7phc:dIfiO6O-Km82qxbd2_t_l8yz7LvyX4GZJ2uEQo606xY', '2023-06-24 03:55:48.025707'),
('r9nyqt1cdju6lqivp8i4zjxoxpfn11ir', 'e30:1qLJHZ:xQL7gTpPYZAvmg-k007PQ4wPeZ-ZqBKXdeiFec6pTOE', '2023-07-31 08:08:37.313978'),
('rq6v8u0glsml7xc4k7dtgo2yoi55gzr7', 'eyJ1aWQiOjEsInVuYW1lIjoiZGF2b29kIiwidWVtYWlsIjoiYUBnYW1pbC5jb20iLCJjdXMiOiJjdXMifQ:1qJRGJ:-39cf53k33E5gPVFafei-pE_KhXKuSjW4wIuIkSG08g', '2023-07-26 04:15:35.304691'),
('xepb02fbt9w5xh6f6916z751r996wcyb', 'eyJ1aWQiOjEsInVuYW1lIjoiZGF2b29kIiwidWVtYWlsIjoiYUBnYW1pbC5jb20iLCJjdXMiOiJjdXMifQ:1qHdgO:DqIlqQEmOgK2VLjZ008RNI-3qQA_xaqqAoPh8MUPslg', '2023-07-21 05:07:04.009089'),
('xvaxlxgtz8e2j5i1936841nquu98fdyq', '.eJyrVsrJT8_MK0lJLUnMzFGyUkpMyc3Mc0jPBfL0kvNzlXQgIjAZpVoAy3IRew:1q0H07:A78FHPjPqvdg5p7YzAXY68B9mPWTPt_AX1U5D-nDdSM', '2023-06-03 07:27:39.122513'),
('y90dak2rdqly6rf1jbaw2wksfhw6fipb', 'e30:1pzt3z:G8kwnkj1rDGAaHJ9fw0IetFEXLkzwpZwpgyhouiiapc', '2023-06-02 05:54:03.175351'),
('z1ypsrjlzirsj1gz6k42swn93i31bsgw', 'eyJ3aWQiOjIsInduYW1lIjoiYW5udSIsIndlbWFpbCI6ImFubnVAZ21haWwuY29tIn0:1qLiRd:QeDjKYA15ljQXc-62DSsFTZKxsigHDta778jRMuMBeQ', '2023-08-01 11:00:41.321848'),
('z3fm6yt19rcbe2vkunoodbiylxtyvo2l', 'e30:1q5OSz:XzYiU4gQOFKrj7iiSTW63E4oCvAAvSaKjP88Ds7H22U', '2023-06-17 10:26:37.383029');

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
