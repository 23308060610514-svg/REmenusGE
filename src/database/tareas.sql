-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 30-05-2026 a las 19:29:15
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `tareas`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `restaurantechin`
--

CREATE TABLE `restaurantechin` (
  `ID_comidaChin` int(11) NOT NULL,
  `ID_usuario` int(11) NOT NULL,
  `PrecioChin` int(11) NOT NULL,
  `MezaNum2` int(11) NOT NULL,
  `Menu` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `restaurantemaris`
--

CREATE TABLE `restaurantemaris` (
  `ID_comidaMar` int(11) NOT NULL,
  `ID_usuario` int(11) NOT NULL,
  `PrecioMari` int(11) NOT NULL,
  `MezaNum3` int(11) NOT NULL,
  `Menu` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `restaurantemex`
--

CREATE TABLE `restaurantemex` (
  `ID_comidaMex` int(11) NOT NULL,
  `ID_usuario` int(11) NOT NULL,
  `PrecioMex` int(11) NOT NULL,
  `MezaNum1` int(11) NOT NULL,
  `Menu` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `ID_usuario` int(11) NOT NULL,
  `User` varchar(50) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `Password` varchar(255) NOT NULL,
  `Fecha_Registro` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `restaurantechin`
--
ALTER TABLE `restaurantechin`
  ADD PRIMARY KEY (`ID_comidaChin`),
  ADD KEY `fk_chin_usuario` (`ID_usuario`);

--
-- Indices de la tabla `restaurantemaris`
--
ALTER TABLE `restaurantemaris`
  ADD PRIMARY KEY (`ID_comidaMar`),
  ADD KEY `fk_maris_usuario` (`ID_usuario`);

--
-- Indices de la tabla `restaurantemex`
--
ALTER TABLE `restaurantemex`
  ADD PRIMARY KEY (`ID_comidaMex`),
  ADD KEY `fk_mex_usuario` (`ID_usuario`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`ID_usuario`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `restaurantechin`
--
ALTER TABLE `restaurantechin`
  MODIFY `ID_comidaChin` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `restaurantemaris`
--
ALTER TABLE `restaurantemaris`
  MODIFY `ID_comidaMar` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `restaurantemex`
--
ALTER TABLE `restaurantemex`
  MODIFY `ID_comidaMex` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `ID_usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `restaurantechin`
--
ALTER TABLE `restaurantechin`
  ADD CONSTRAINT `fk_chin_usuario` FOREIGN KEY (`ID_usuario`) REFERENCES `usuarios` (`ID_usuario`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `restaurantemaris`
--
ALTER TABLE `restaurantemaris`
  ADD CONSTRAINT `fk_maris_usuario` FOREIGN KEY (`ID_usuario`) REFERENCES `usuarios` (`ID_usuario`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `restaurantemex`
--
ALTER TABLE `restaurantemex`
  ADD CONSTRAINT `fk_mex_usuario` FOREIGN KEY (`ID_usuario`) REFERENCES `usuarios` (`ID_usuario`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
