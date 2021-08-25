-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 24 Agu 2021 pada 12.54
-- Versi server: 10.1.40-MariaDB
-- Versi PHP: 7.3.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `babak_belur`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('c4b3ff75c443');

-- --------------------------------------------------------

--
-- Struktur dari tabel `course_subject`
--

CREATE TABLE `course_subject` (
  `id_course` bigint(20) NOT NULL,
  `course_name` varchar(50) NOT NULL,
  `description` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `course_subject`
--

INSERT INTO `course_subject` (`id_course`, `course_name`, `description`) VALUES
(1, 'Math', 'Matematika adalah Queen of scince'),
(2, 'Natural Science', 'IPA adalah'),
(3, 'Physics', 'Physics is a science wherein it learns about the nature and natural phenomena or natural phenomena and all the interactions that occur in them');

-- --------------------------------------------------------

--
-- Struktur dari tabel `detail_user`
--

CREATE TABLE `detail_user` (
  `id_detail_user` bigint(20) NOT NULL,
  `age` bigint(20) DEFAULT NULL,
  `genre` enum('Male','Female') DEFAULT NULL,
  `internet` enum('Yes','No') DEFAULT NULL,
  `fjob` varchar(50) DEFAULT NULL,
  `mjob` varchar(50) DEFAULT NULL,
  `pstatus` enum('Yes','No') DEFAULT NULL,
  `id_user` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `detail_user`
--

INSERT INTO `detail_user` (`id_detail_user`, `age`, `genre`, `internet`, `fjob`, `mjob`, `pstatus`, `id_user`) VALUES
(1, 22, 'Female', 'Yes', 'Driver', 'Housewife', 'Yes', 1),
(2, 22, 'Female', 'Yes', 'Driver', 'Housewife', 'Yes', 2),
(3, 22, 'Female', 'Yes', 'Driver', 'Housewife', 'Yes', 3);

-- --------------------------------------------------------

--
-- Struktur dari tabel `evaluation`
--

CREATE TABLE `evaluation` (
  `id_evaluation` bigint(20) NOT NULL,
  `id_user` bigint(20) DEFAULT NULL,
  `date` date NOT NULL,
  `grade` int(11) NOT NULL,
  `study_time` enum('1','2','3','4') NOT NULL,
  `freetime` enum('1','2','3','4','5') NOT NULL,
  `id_target` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `evaluation`
--

INSERT INTO `evaluation` (`id_evaluation`, `id_user`, `date`, `grade`, `study_time`, `freetime`, `id_target`) VALUES
(1, 2, '2021-08-01', 99, '4', '3', 1),
(2, 1, '2021-08-02', 80, '2', '1', 1),
(3, 1, '2021-08-03', 85, '1', '2', 1),
(4, 1, '2021-08-03', 85, '1', '2', 1);

-- --------------------------------------------------------

--
-- Struktur dari tabel `target`
--

CREATE TABLE `target` (
  `id_target` bigint(20) NOT NULL,
  `id_user` bigint(20) DEFAULT NULL,
  `id_course` bigint(20) DEFAULT NULL,
  `g1` int(11) NOT NULL,
  `grade_target` int(11) NOT NULL,
  `target_time` date NOT NULL,
  `achived` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `target`
--

INSERT INTO `target` (`id_target`, `id_user`, `id_course`, `g1`, `grade_target`, `target_time`, `achived`) VALUES
(1, 1, 1, 90, 99, '2022-03-15', 0),
(2, 2, 3, 90, 99, '2022-03-15', 0),
(3, 2, 1, 80, 95, '2021-10-12', 0),
(4, 2, 1, 80, 95, '2021-10-12', 1),
(5, 2, 1, 80, 95, '2021-10-12', 1),
(6, 2, 1, 80, 95, '2021-10-12', 1),
(7, 2, 1, 80, 95, '2021-10-12', 1),
(8, 2, 1, 80, 97, '2021-10-12', 1),
(9, 2, 1, 80, 97, '2021-10-12', 1),
(10, 2, 1, 80, 97, '2021-10-12', 1);

-- --------------------------------------------------------

--
-- Struktur dari tabel `users`
--

CREATE TABLE `users` (
  `id_user` bigint(20) NOT NULL,
  `name` varchar(250) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role` enum('Admin','User') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `users`
--

INSERT INTO `users` (`id_user`, `name`, `username`, `password`, `role`) VALUES
(1, 'betha', 'betha', 'pbkdf2:sha256:260000$ad2MzFmqLRIWghRb$953053299aed379eb6c75eefdadb62835d73c696cf2a4dc18ea064aeabfb71fc', 'Admin'),
(2, 'agung', 'agung', 'pbkdf2:sha256:260000$SHzmRPXfs3rCA114$ce1fa61c124e59919974aae0aa34815db594bde9ec5d4b08fc05228354bcf2f7', 'Admin'),
(3, 'nana', 'nana', 'pbkdf2:sha256:260000$n6kn0zLjfYH5fAia$b39959bef382e774f0a05e37290b80e1a77f458e9e9c9312271e108a82e06adb', 'Admin');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Indeks untuk tabel `course_subject`
--
ALTER TABLE `course_subject`
  ADD PRIMARY KEY (`id_course`);

--
-- Indeks untuk tabel `detail_user`
--
ALTER TABLE `detail_user`
  ADD PRIMARY KEY (`id_detail_user`),
  ADD KEY `id_user` (`id_user`);

--
-- Indeks untuk tabel `evaluation`
--
ALTER TABLE `evaluation`
  ADD PRIMARY KEY (`id_evaluation`),
  ADD KEY `id_user` (`id_user`),
  ADD KEY `id_target` (`id_target`);

--
-- Indeks untuk tabel `target`
--
ALTER TABLE `target`
  ADD PRIMARY KEY (`id_target`),
  ADD KEY `id_course` (`id_course`),
  ADD KEY `id_user` (`id_user`);

--
-- Indeks untuk tabel `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id_user`),
  ADD UNIQUE KEY `ix_users_username` (`username`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `course_subject`
--
ALTER TABLE `course_subject`
  MODIFY `id_course` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT untuk tabel `detail_user`
--
ALTER TABLE `detail_user`
  MODIFY `id_detail_user` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT untuk tabel `evaluation`
--
ALTER TABLE `evaluation`
  MODIFY `id_evaluation` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT untuk tabel `target`
--
ALTER TABLE `target`
  MODIFY `id_target` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT untuk tabel `users`
--
ALTER TABLE `users`
  MODIFY `id_user` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `detail_user`
--
ALTER TABLE `detail_user`
  ADD CONSTRAINT `detail_user_ibfk_1` FOREIGN KEY (`id_user`) REFERENCES `users` (`id_user`);

--
-- Ketidakleluasaan untuk tabel `evaluation`
--
ALTER TABLE `evaluation`
  ADD CONSTRAINT `evaluation_ibfk_2` FOREIGN KEY (`id_user`) REFERENCES `users` (`id_user`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `evaluation_ibfk_3` FOREIGN KEY (`id_target`) REFERENCES `target` (`id_target`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ketidakleluasaan untuk tabel `target`
--
ALTER TABLE `target`
  ADD CONSTRAINT `target_ibfk_1` FOREIGN KEY (`id_course`) REFERENCES `course_subject` (`id_course`),
  ADD CONSTRAINT `target_ibfk_2` FOREIGN KEY (`id_user`) REFERENCES `users` (`id_user`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
