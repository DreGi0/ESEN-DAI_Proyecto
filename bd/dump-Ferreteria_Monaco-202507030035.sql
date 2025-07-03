/*M!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.19-11.8.2-MariaDB, for osx10.20 (arm64)
--
-- Host: localhost    Database: Ferreteria_Monaco
-- ------------------------------------------------------
-- Server version	11.8.2-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*M!100616 SET @OLD_NOTE_VERBOSITY=@@NOTE_VERBOSITY, NOTE_VERBOSITY=0 */;

--
-- Table structure for table `administrador`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `administrador` (
  `id_administrador` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_admin` varchar(25) NOT NULL,
  `contrasena_admin` varchar(25) NOT NULL,
  `usuario_admin` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`id_administrador`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `administrador`
--

LOCK TABLES `administrador` WRITE;
/*!40000 ALTER TABLE `administrador` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `administrador` VALUES
(1,'Alvin','Alvin123','Alvin123'),
(2,'Dana ','Dana456','Dana456'),
(3,'Andre','Andre246','Andre246'),
(4,'Susana','Susana789','Susana789'),
(5,'Debbie','Debbie135','Debbie135'),
(6,'Tiffany','Tiffany176','Tiffany176');
/*!40000 ALTER TABLE `administrador` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `categoria`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `categoria` (
  `id_categoria` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_categoria` varchar(25) NOT NULL,
  `descripcion_categoria` varchar(100) NOT NULL,
  PRIMARY KEY (`id_categoria`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categoria`
--

LOCK TABLES `categoria` WRITE;
/*!40000 ALTER TABLE `categoria` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `categoria` VALUES
(1,'Pinturas','Sustancia que proporciona color, proteccion o acabado decorativo'),
(2,'Herramientas','Instrumentos manuales de trabajo general'),
(3,'Electricidad','Instrumentos que foman parte del cableado electrico de una construccion'),
(4,'Fontaneria','Instrumentos relacionados con la instalacion y mantenimiento de alcantarillado'),
(5,'Jardineria','Productos relacionados con el cuido de plantas'),
(6,'Ferreteria general','Productos basicos ferreteros'),
(7,'Material de construcción','Productos para obras y proyectos');
/*!40000 ALTER TABLE `categoria` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `clientes`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `clientes` (
  `id_cliente` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_cliente` varchar(25) NOT NULL,
  `apellido_cliente` varchar(25) NOT NULL,
  PRIMARY KEY (`id_cliente`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `clientes` VALUES
(1,'Alvin','Portillo'),
(2,'Katherine','Melendez'),
(3,'Juancito','Martinez'),
(4,'Carla','Torres'),
(5,'Predro','Herrera'),
(6,'Louis','Tomlinson'),
(7,'Niall','Horan'),
(8,'Zayn','Malik'),
(9,'Liam','Payne'),
(10,'Harry','Styles');
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `contacto_clientes`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `contacto_clientes` (
  `id_contacto_cliente` int(11) NOT NULL AUTO_INCREMENT,
  `id_cliente` int(11) NOT NULL,
  `correo_cliente` varchar(25) NOT NULL,
  PRIMARY KEY (`id_contacto_cliente`),
  KEY `fk_id_cliente` (`id_cliente`),
  CONSTRAINT `fk_id_cliente` FOREIGN KEY (`id_cliente`) REFERENCES `clientes` (`id_cliente`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contacto_clientes`
--

LOCK TABLES `contacto_clientes` WRITE;
/*!40000 ALTER TABLE `contacto_clientes` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `contacto_clientes` VALUES
(1,1,'AlvinP@gmail.com'),
(2,2,'Khatomelendez@gmail.com'),
(3,3,'MartinezL@gmail.com'),
(4,4,'CarlaTTorres@gmail.com'),
(5,5,'HerreraP@gmail.com'),
(6,6,'It28@gmail.com'),
(7,7,'nh67@gmail.com'),
(8,8,'zm84@gmail.com'),
(9,9,'lp890@gmail.com'),
(10,10,'hs34@gmail.com');
/*!40000 ALTER TABLE `contacto_clientes` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `contacto_proveedor`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `contacto_proveedor` (
  `id_contacto_proveedor` int(11) NOT NULL AUTO_INCREMENT,
  `id_prov` int(11) NOT NULL,
  `correo_proveedor` varchar(25) NOT NULL,
  PRIMARY KEY (`id_contacto_proveedor`),
  KEY `fk_id_proveedor` (`id_prov`),
  CONSTRAINT `fk_id_proveedor` FOREIGN KEY (`id_prov`) REFERENCES `proveedor` (`id_prov`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contacto_proveedor`
--

LOCK TABLES `contacto_proveedor` WRITE;
/*!40000 ALTER TABLE `contacto_proveedor` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `contacto_proveedor` VALUES
(1,1,'SanchezGr@gmail.com'),
(2,2,'FernandezRo@gmail.com'),
(3,3,'PortilloGabi@gmail.com'),
(4,4,'MendezLau@gmail.com'),
(5,5,'sor234@gmail.com'),
(6,6,'alet234@gmail.com'),
(7,7,'valc@gmail.com'),
(8,8,'marl@gmail.com'),
(9,9,'camh@gmail.com'),
(10,10,'dang@gmail.com');
/*!40000 ALTER TABLE `contacto_proveedor` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `detalle_factura`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalle_factura` (
  `id_detalle` int(11) NOT NULL AUTO_INCREMENT,
  `id_factura` int(11) DEFAULT NULL,
  `id_producto_proveedor` int(11) DEFAULT NULL,
  `cantidad_detalle` int(11) NOT NULL,
  `precio_unitario_detalle` double(6,2) NOT NULL,
  PRIMARY KEY (`id_detalle`),
  KEY `Detalle_factura_Factura_FK` (`id_factura`),
  KEY `Detalle_factura_Producto_proveedor_FK` (`id_producto_proveedor`),
  CONSTRAINT `Detalle_factura_Factura_FK` FOREIGN KEY (`id_factura`) REFERENCES `factura` (`id_factura`),
  CONSTRAINT `Detalle_factura_Producto_proveedor_FK` FOREIGN KEY (`id_producto_proveedor`) REFERENCES `producto_proveedor` (`id_producto_proveedor`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalle_factura`
--

LOCK TABLES `detalle_factura` WRITE;
/*!40000 ALTER TABLE `detalle_factura` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `detalle_factura` VALUES
(1,1,1,30,5.00),
(2,2,1,10,9.00),
(3,3,2,15,11.00),
(4,4,2,5,8.00),
(5,5,5,18,4.00),
(6,6,6,15,14.00),
(7,7,6,5,20.00),
(8,8,7,20,1.50),
(9,9,7,3,3.00),
(10,10,8,10,5.00),
(11,11,8,4,8.00),
(12,12,9,15,2.00),
(13,13,9,8,3.40),
(14,14,8,3,8.00),
(15,15,3,10,2.50),
(16,16,4,10,0.30),
(17,17,10,10,3.50),
(18,18,3,5,4.80),
(19,19,4,5,0.50),
(20,20,10,5,7.00);
/*!40000 ALTER TABLE `detalle_factura` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `factura`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `factura` (
  `id_factura` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_factura` enum('Compra','Venta') NOT NULL,
  `fecha_factura` date NOT NULL,
  `id_cliente` int(11) DEFAULT NULL,
  `id_prov` int(11) DEFAULT NULL,
  `id_administrador` int(11) DEFAULT NULL,
  `metodo_pago` varchar(25) DEFAULT NULL,
  `total` double(6,2) DEFAULT NULL,
  PRIMARY KEY (`id_factura`),
  KEY `Factura_Clientes_FK` (`id_cliente`),
  KEY `Factura_Proveedores_FK` (`id_prov`),
  KEY `fk_factura_admin` (`id_administrador`),
  CONSTRAINT `Factura_Clientes_FK` FOREIGN KEY (`id_cliente`) REFERENCES `clientes` (`id_cliente`),
  CONSTRAINT `Factura_Proveedores_FK` FOREIGN KEY (`id_prov`) REFERENCES `proveedor` (`id_prov`),
  CONSTRAINT `fk_factura_admin` FOREIGN KEY (`id_administrador`) REFERENCES `administrador` (`id_administrador`),
  CONSTRAINT `chk_tipo_factura` CHECK (`tipo_factura` = 'Venta' and `id_cliente` is not null and `id_prov` is null or `tipo_factura` = 'Compra' and `id_prov` is not null and `id_cliente` is null)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `factura`
--

LOCK TABLES `factura` WRITE;
/*!40000 ALTER TABLE `factura` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `factura` VALUES
(1,'Compra','2024-03-20',NULL,1,1,'Efectivo',150.00),
(2,'Venta','2024-03-22',1,NULL,2,'Tarjeta',90.00),
(3,'Compra','2024-03-23',NULL,2,3,'Efectivo',165.00),
(4,'Venta','2024-03-24',2,NULL,4,'Transferencia',40.00),
(5,'Compra','2024-03-27',NULL,5,1,'Efcetivo',72.00),
(6,'Compra','2024-04-27',NULL,6,3,'Efectivo',210.00),
(7,'Venta','2024-04-27',3,NULL,4,'Tarjeta',100.00),
(8,'Compra','2024-04-28',NULL,7,6,'Transferencia',30.00),
(9,'Venta','2024-04-29',4,NULL,5,'Tarjeta',9.00),
(10,'Compra','2024-05-02',NULL,8,6,'Tarjeta',50.00),
(11,'Venta','2024-05-03',5,NULL,3,'Efectivo',32.00),
(12,'Compra','2024-05-06',NULL,9,4,'Efectivo',30.00),
(13,'Venta','2024-05-07',7,NULL,2,'Transferencia',27.20),
(14,'Venta','2024-05-10',6,NULL,2,'Transferencia',24.00),
(15,'Compra','2024-05-11',NULL,3,3,'Efectivo',25.00),
(16,'Compra','2024-05-11',NULL,4,4,'Efectivo',3.00),
(17,'Compra','2024-05-11',NULL,10,2,'Tarjeta',35.00),
(18,'Venta','2024-05-12',8,NULL,3,'Efectivo',24.00),
(19,'Venta','2024-05-12',9,NULL,4,'Efectivo',2.50),
(20,'Venta','2024-05-12',10,NULL,2,'Tarjeta',35.00);
/*!40000 ALTER TABLE `factura` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `inventario`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventario` (
  `id_inventario` int(11) NOT NULL AUTO_INCREMENT,
  `id_prod` int(11) DEFAULT NULL,
  `cantidad_disponible` int(11) NOT NULL,
  `fecha_actualizacion` date NOT NULL,
  `tipo_movimiento` enum('Entrada','Salida') NOT NULL,
  PRIMARY KEY (`id_inventario`),
  KEY `Inventario_Producto_FK` (`id_prod`),
  CONSTRAINT `Inventario_Producto_FK` FOREIGN KEY (`id_prod`) REFERENCES `producto` (`id_prod`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventario`
--

LOCK TABLES `inventario` WRITE;
/*!40000 ALTER TABLE `inventario` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `inventario` VALUES
(1,3,20,'2024-03-20','Entrada'),
(2,3,20,'2024-03-22','Salida'),
(3,4,15,'2024-03-23','Entrada'),
(4,4,10,'2024-03-24','Salida'),
(5,6,18,'2024-03-27','Entrada'),
(6,7,15,'2024-04-27','Entrada'),
(7,7,10,'2024-04-28','Salida'),
(8,8,20,'2024-04-28','Entrada'),
(9,8,17,'2024-04-28','Salida'),
(10,9,10,'2024-05-02','Entrada'),
(11,9,6,'2024-05-03','Salida'),
(12,2,15,'2024-05-06','Entrada'),
(13,2,7,'2024-05-07','Salida'),
(14,9,3,'2024-05-10','Salida'),
(15,1,10,'2024-05-11','Entrada'),
(16,5,10,'2024-05-11','Entrada'),
(17,10,10,'2024-05-11','Entrada'),
(18,1,5,'2024-05-12','Salida'),
(19,5,5,'2024-05-12','Salida'),
(20,10,5,'2024-05-12','Salida');
/*!40000 ALTER TABLE `inventario` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `producto`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `producto` (
  `id_prod` int(11) NOT NULL AUTO_INCREMENT,
  `id_categoria` int(11) DEFAULT NULL,
  `id_unidad_medida` int(11) DEFAULT NULL,
  `nombre_prod` varchar(50) NOT NULL,
  `descripcion_prod` varchar(75) NOT NULL,
  `ubicacion_prod` varchar(50) NOT NULL,
  `precio_unitario_prod` double(6,2) NOT NULL,
  PRIMARY KEY (`id_prod`),
  KEY `Producto_Categoria_FK` (`id_categoria`),
  KEY `Producto_Unidad_Medida_FK` (`id_unidad_medida`),
  CONSTRAINT `Producto_Categoria_FK` FOREIGN KEY (`id_categoria`) REFERENCES `categoria` (`id_categoria`),
  CONSTRAINT `Producto_Unidad_Medida_FK` FOREIGN KEY (`id_unidad_medida`) REFERENCES `unidad_medida` (`id_unidad_medida`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producto`
--

LOCK TABLES `producto` WRITE;
/*!40000 ALTER TABLE `producto` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `producto` VALUES
(1,1,3,'Celeste Cristal','Gl 1/4 Aceite','Bodega 1',4.80),
(2,1,3,'Rojo Oxido','1/48 Esmalte','Bodega 1',3.40),
(3,2,4,'Martillo','Mango de goma','Bodega 1',9.00),
(4,3,1,'Cable THHN','Negro 10m','Bodega 1',11.00),
(5,4,4,'Codo PVC','1/2\" ','Bodega 1',0.50),
(6,6,2,'Llave ajustable','Herramienta de precisión mediana','Bodega 1',5.50),
(7,5,3,'Maceta','Maceta grande de barro','Bodega 1',20.00),
(8,2,4,'Broca para concreto','Broca 3/8 X 12\"','Bodega 1',3.00),
(9,4,4,'Brocha Std','\'Brocha Std Expert 1/2\"','Bodega 1',8.00),
(10,7,5,'Cemento','Material de construccion básico en sacos de 20 kg','Bodega 1',7.00);
/*!40000 ALTER TABLE `producto` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `producto_proveedor`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `producto_proveedor` (
  `id_producto_proveedor` int(11) NOT NULL AUTO_INCREMENT,
  `id_prov` int(11) DEFAULT NULL,
  `id_prod` int(11) DEFAULT NULL,
  `precio_compra` double(6,2) NOT NULL,
  PRIMARY KEY (`id_producto_proveedor`),
  KEY `Producto_proveedor_Proveedor_FK` (`id_prov`),
  KEY `Producto_proveedor_Producto_FK` (`id_prod`),
  CONSTRAINT `Producto_proveedor_Producto_FK` FOREIGN KEY (`id_prod`) REFERENCES `producto` (`id_prod`),
  CONSTRAINT `Producto_proveedor_Proveedor_FK` FOREIGN KEY (`id_prov`) REFERENCES `proveedor` (`id_prov`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producto_proveedor`
--

LOCK TABLES `producto_proveedor` WRITE;
/*!40000 ALTER TABLE `producto_proveedor` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `producto_proveedor` VALUES
(1,1,3,5.00),
(2,2,4,8.00),
(3,3,1,2.50),
(4,4,5,0.30),
(5,5,6,4.00),
(6,6,7,14.00),
(7,7,8,1.50),
(8,8,9,5.00),
(9,9,2,2.00),
(10,10,10,3.50);
/*!40000 ALTER TABLE `producto_proveedor` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `proveedor`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `proveedor` (
  `id_prov` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_prov` varchar(25) NOT NULL,
  `apellido_prov` varchar(25) NOT NULL,
  PRIMARY KEY (`id_prov`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proveedor`
--

LOCK TABLES `proveedor` WRITE;
/*!40000 ALTER TABLE `proveedor` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `proveedor` VALUES
(1,'Gabriel','Sanchez'),
(2,'Roberto','Fernandez'),
(3,'Gabriela','Portillo'),
(4,'Laura','Mendez'),
(5,'Sofía','Ramírez'),
(6,'Alejandro','Torres'),
(7,'Valentina','Cruz'),
(8,'Martín','López'),
(9,'Camila','Hernández'),
(10,'Daniel','García');
/*!40000 ALTER TABLE `proveedor` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `unidad_medida`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `unidad_medida` (
  `id_unidad_medida` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_unidad` varchar(15) NOT NULL,
  `abreviatura_unidad` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id_unidad_medida`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `unidad_medida`
--

LOCK TABLES `unidad_medida` WRITE;
/*!40000 ALTER TABLE `unidad_medida` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `unidad_medida` VALUES
(1,'Metro','M'),
(2,'Litro','Lt'),
(3,'Galon','Gl'),
(4,'Unidad','Ud'),
(5,'Kilogramo','Kg'),
(6,'Pulgada','In');
/*!40000 ALTER TABLE `unidad_medida` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Dumping routines for database 'Ferreteria_Monaco'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*M!100616 SET NOTE_VERBOSITY=@OLD_NOTE_VERBOSITY */;

-- Dump completed on 2025-07-03  0:35:21
