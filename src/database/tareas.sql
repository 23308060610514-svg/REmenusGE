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
-- Crear la base de datos
--
CREATE DATABASE IF NOT EXISTS `tareas`;

--
-- Usar la base de datos
--
USE `tareas`;

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

--
-- Volcado de datos para la tabla `restaurantechin`
--

INSERT INTO `restaurantechin` (`ID_comidaChin`, `ID_usuario`, `PrecioChin`, `MezaNum2`, `Menu`) VALUES
(1, 1, 70, 1, 'Arroz Frito'),
(2, 1, 85, 2, 'Chop Suey'),
(3, 1, 60, 3, 'Wantanes'),
(4, 1, 95, 4, 'Pollo Agridulce'),
(5, 1, 110, 5, 'Ternera Mongoliana'),
(6, 1, 75, 6, 'Rollos Primavera'),
(7, 1, 65, 7, 'Sopa Wantán'),
(8, 1, 100, 8, 'Cerdo Agridulce'),
(9, 1, 80, 9, 'Tallarines Saltados'),
(10, 1, 25, 10, 'Té Chino');

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

--
-- Volcado de datos para la tabla `restaurantemaris`
--

INSERT INTO `restaurantemaris` (`ID_comidaMar`, `ID_usuario`, `PrecioMari`, `MezaNum3`, `Menu`) VALUES
(1, 1, 120, 1, 'Ceviche'),
(2, 1, 150, 2, 'Camarones al Ajillo'),
(3, 1, 180, 3, 'Pulpo a la Parrilla'),
(4, 1, 130, 4, 'Filete de Pescado'),
(5, 1, 140, 5, 'Coctel de Camarón'),
(6, 1, 200, 6, 'Pescado Zarandeado'),
(7, 1, 85, 7, 'Tostadas de Ceviche'),
(8, 1, 135, 8, 'Camarones Empanizados'),
(9, 1, 95, 9, 'Sopa de Mariscos'),
(10, 1, 110, 10, 'Ostiones');

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

--
-- Volcado de datos para la tabla `restaurantemex`
--

INSERT INTO `restaurantemex` (`ID_comidaMex`, `ID_usuario`, `PrecioMex`, `MezaNum1`, `Menu`) VALUES
(1, 1, 85, 1, 'Tacos al Pastor'),
(2, 1, 95, 2, 'Enchiladas Verdes'),
(3, 1, 110, 3, 'Chiles Rellenos'),
(4, 1, 120, 4, 'Mole Poblano'),
(5, 1, 75, 5, 'Quesadillas'),
(6, 1, 130, 6, 'Pozole'),
(7, 1, 60, 7, 'Tamales'),
(8, 1, 70, 8, 'Tostadas'),
(9, 1, 80, 9, 'Sopes'),
(10, 1, 45, 10, 'Flan Napolitano');

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
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`ID_usuario`, `User`, `Email`, `Password`, `Fecha_Registro`) VALUES
(1, 'admin', 'admin@remenus.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/X4.VTt2O9uH7FjZbi', '2026-06-03'),
(2, 'test', 'test@test.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/X4.VTt2O9uH7FjZbi', '2026-06-03');

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
  MODIFY `ID_comidaChin` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `restaurantemaris`
--
ALTER TABLE `restaurantemaris`
  MODIFY `ID_comidaMar` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `restaurantemex`
--
ALTER TABLE `restaurantemex`
  MODIFY `ID_comidaMex` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

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
