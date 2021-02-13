-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 13, 2021 at 07:55 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `codeupload`
--

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

CREATE TABLE `contact` (
  `sno` int(4) NOT NULL,
  `name` text NOT NULL,
  `email` varchar(25) NOT NULL,
  `msg` varchar(200) NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contact`
--

INSERT INTO `contact` (`sno`, `name`, `email`, `msg`, `date`) VALUES
(1, 'hry', 'this@gmail.com', 'vhyhj', '2021-02-11 17:13:48'),
(4, 'Pallavi Bobde', 'pallavibobde1@gmail.com', 'Shanti colony, Borgaon, Tehsil Sausar', '2021-02-12 14:38:21'),
(5, 'Pallavi Bobde', 'pallavibobde1@gmail.com', 'Shanti colony, Borgaon, Tehsil Sausar', '2021-02-12 16:01:05'),
(6, 'Pallavi Bobde', 'pallavibobde1@gmail.com', 'Shanti colony, Borgaon, Tehsil Sausar', '2021-02-12 16:02:36'),
(7, 'Pallavi Bobde', 'pallavibobde1@gmail.com', 'Shanti colony, Borgaon, Tehsil Sausar', '2021-02-12 16:03:52'),
(8, 'Pallavi Bobde', 'pall111111111@gmail.com', 'Shanti colony, Borgaon, Tehsil Sausar', '2021-02-12 16:04:35'),
(9, 'oj', 'ojhuij@gmail.com', 'what to say', '2021-02-12 16:05:52'),
(10, 'Pallavi Bobde', 'pallavibobde1@gmail.com', 'Shanti colony, Borgaon, Tehsil Sausar', '2021-02-13 18:45:21');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `sno` int(3) NOT NULL,
  `title` text NOT NULL,
  `content` text NOT NULL,
  `author` text NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp(),
  `image` varchar(20) NOT NULL,
  `slug` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`sno`, `title`, `content`, `author`, `date`, `image`, `slug`) VALUES
(1, '1 post', 'Hey, this is Pallavi. I am a web designer.', 'Hey', '2021-02-13 22:23:16', 'first.jpg', 'first post'),
(2, '2', 'Hey, this is Pallavi. I am a web designer.', 'Hey', '2021-02-13 22:23:37', 'first.png', '2nd'),
(3, '333333333', '3333333333333333', 'b', '2021-02-13 22:24:20', 'first.jpg', '3'),
(4, 'bvv', 'gfvd', 'bdddddddddd', '2021-02-13 22:24:44', 'first.jpg', '4'),
(5, 'fbc', 'dbbbbbbbbbg', 'gbbbg', '2021-02-13 22:25:18', 'first.jpg', '5'),
(6, '6', '6666666666666666666666666666666666666666', '6gg', '2021-02-13 22:25:41', 'first.jpg', '6'),
(7, '777777777777', '777777777777777', '777777ehvg', '2021-02-13 22:26:10', 'abc.png', '7gn');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contact`
--
ALTER TABLE `contact`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contact`
--
ALTER TABLE `contact`
  MODIFY `sno` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `sno` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
