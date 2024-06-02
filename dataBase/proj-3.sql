-- phpMyAdmin SQL Dump
-- version 5.2.1deb1ubuntu1
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost:3306
-- Généré le : dim. 02 juin 2024 à 13:48
-- Version du serveur : 8.0.36-0ubuntu0.23.10.1
-- Version de PHP : 8.2.10-2ubuntu2.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `proj`
--

-- --------------------------------------------------------

--
-- Structure de la table `background`
--

CREATE TABLE `background` (
  `id` int NOT NULL,
  `civilization` int NOT NULL,
  `image` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `camps`
--

CREATE TABLE `camps` (
  `id` int NOT NULL,
  `name` varchar(50) NOT NULL,
  `xpCost` int NOT NULL,
  `passiveGold` int NOT NULL,
  `image` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `civilization`
--

CREATE TABLE `civilization` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `xpCost` int NOT NULL,
  `passiveGold` int NOT NULL,
  `image` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `civilization`
--

INSERT INTO `civilization` (`id`, `name`, `xpCost`, `passiveGold`, `image`) VALUES
(1, 'Primitive Age', 0, 0, 0),
(2, 'Medieval Age', 0, 0, 0),
(3, 'Modern Age', 0, 0, 0),
(4, 'Future Age', 0, 0, 0);

-- --------------------------------------------------------

--
-- Structure de la table `economy`
--

CREATE TABLE `economy` (
  `id` int NOT NULL,
  `gold` int NOT NULL,
  `xp` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `game`
--

CREATE TABLE `game` (
  `id` int NOT NULL,
  `player1Id` int NOT NULL,
  `player2Id` int DEFAULT NULL,
  `player1Civilization` int NOT NULL,
  `player2Civilization` int NOT NULL,
  `player1HPCamp` int NOT NULL,
  `player2HPCamp` int NOT NULL,
  `field` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `player1SpecialCapacity` int DEFAULT NULL,
  `player2SpecialCapacity` int DEFAULT NULL,
  `player1Turrets1` int DEFAULT NULL,
  `player1Turrets2` int DEFAULT NULL,
  `player1Turrets3` int DEFAULT NULL,
  `player2Turrets1` int DEFAULT NULL,
  `player2Turrets2` int DEFAULT NULL,
  `player2Turrets3` int DEFAULT NULL,
  `waitingListPlayer1` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `waitingListPlayer2` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `player`
--

CREATE TABLE `player` (
  `id` int NOT NULL,
  `name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `specialCapacity`
--

CREATE TABLE `specialCapacity` (
  `id` int NOT NULL,
  `name` varchar(50) NOT NULL,
  `civilization` int NOT NULL,
  `cost` int NOT NULL,
  `reloadTime` int NOT NULL,
  `image` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `specialCapacity`
--

INSERT INTO `specialCapacity` (`id`, `name`, `civilization`, `cost`, `reloadTime`, `image`) VALUES
(1, 'Lightning Strike', 1, 500, 30, 0),
(2, 'Healing', 2, 800, 35, 0),
(3, 'Freeze', 3, 1500, 40, 0),
(4, 'Nuclear Bomb', 4, 2000, 60, 0);

-- --------------------------------------------------------

--
-- Structure de la table `troops`
--

CREATE TABLE `troops` (
  `id` int NOT NULL,
  `name` varchar(20) NOT NULL,
  `hp` int NOT NULL,
  `damage` int NOT NULL,
  `civilization` int NOT NULL COMMENT '0=stoneAge; 1=gallic; 2=modern OR 3=furistic',
  `type` int NOT NULL COMMENT '1=light; 2=range OR 3=heavy',
  `image` int NOT NULL COMMENT 'Id of image on the image table',
  `goldDrop` int DEFAULT NULL,
  `cost` int NOT NULL,
  `xpDrop` int DEFAULT NULL,
  `spawnTime` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `troops`
--

INSERT INTO `troops` (`id`, `name`, `hp`, `damage`, `civilization`, `type`, `image`, `goldDrop`, `cost`, `xpDrop`, `spawnTime`) VALUES
(1, 'Clubman', 10, 3, 1, 1, 0, NULL, 20, NULL, 1),
(2, 'Spear Thrower', 15, 5, 1, 2, 0, NULL, 40, NULL, 2),
(3, 'Warrior', 20, 8, 1, 3, 0, NULL, 10, NULL, 3),
(4, 'Knight', 50, 30, 2, 1, 0, NULL, 150, NULL, 1),
(5, 'Crossbowman', 40, 20, 2, 2, 0, NULL, 100, NULL, 2),
(6, 'Wizard', 60, 25, 2, 3, 0, NULL, 200, NULL, 3),
(7, 'Tank', 150, 50, 3, 1, 0, NULL, 400, NULL, 1),
(8, 'Sniper', 80, 40, 3, 2, 0, NULL, 250, NULL, 2),
(9, 'Bazooka', 120, 45, 3, 3, 0, NULL, 300, NULL, 3),
(10, 'Mech', 80, 80, 4, 1, 0, NULL, 800, NULL, 1),
(11, 'Laser', 100, 70, 4, 2, 0, NULL, 500, NULL, 2),
(12, 'Cyborg', 180, 90, 4, 3, 0, NULL, 700, NULL, 3);

-- --------------------------------------------------------

--
-- Structure de la table `turrets`
--

CREATE TABLE `turrets` (
  `id` int NOT NULL,
  `name` varchar(50) NOT NULL,
  `damage` int NOT NULL,
  `civilization` int NOT NULL,
  `image` int NOT NULL,
  `goldCost` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `turrets`
--

INSERT INTO `turrets` (`id`, `name`, `damage`, `civilization`, `image`, `goldCost`) VALUES
(1, 'Tribal Hut', 4, 1, 0, 50),
(2, 'Cave', 6, 1, 0, 100),
(3, 'Totem Pole', 10, 1, 0, 150),
(4, 'Castle', 40, 2, 0, 350),
(5, 'Cannon Tower', 50, 2, 0, 450),
(6, 'Wizard Tower', 60, 2, 0, 600),
(7, 'Bunker', 70, 3, 0, 450),
(8, 'Missile Silo', 80, 3, 0, 550),
(9, 'Laser Turret', 90, 3, 0, 650),
(10, 'Forcefield', 100, 4, 0, 700),
(11, 'Plasma Cannon', 120, 4, 0, 900),
(12, 'Death Ray', 150, 4, 0, 1200);

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `background`
--
ALTER TABLE `background`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `camps`
--
ALTER TABLE `camps`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `civilization`
--
ALTER TABLE `civilization`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `game`
--
ALTER TABLE `game`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `player`
--
ALTER TABLE `player`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `specialCapacity`
--
ALTER TABLE `specialCapacity`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `troops`
--
ALTER TABLE `troops`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `turrets`
--
ALTER TABLE `turrets`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `background`
--
ALTER TABLE `background`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `camps`
--
ALTER TABLE `camps`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `civilization`
--
ALTER TABLE `civilization`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT pour la table `game`
--
ALTER TABLE `game`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=174;

--
-- AUTO_INCREMENT pour la table `player`
--
ALTER TABLE `player`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT pour la table `specialCapacity`
--
ALTER TABLE `specialCapacity`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT pour la table `troops`
--
ALTER TABLE `troops`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT pour la table `turrets`
--
ALTER TABLE `turrets`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
