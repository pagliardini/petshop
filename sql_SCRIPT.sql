-- -----------------------------------------------------
-- Schema petShop
-- -----------------------------------------------------

CREATE SCHEMA IF NOT EXISTS `petShop` DEFAULT CHARACTER SET utf8;
USE `petShop`;

-- -----------------------------------------------------
-- Table `petShop`.`Categoria`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `petShop`.`Categoria` (
  `ID_Categoria` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(45) NOT NULL,
  `Descripcion` VARCHAR(45) NULL,
  PRIMARY KEY (`ID_Categoria`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `petShop`.`Productos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `petShop`.`Productos` (
  `Codigo_de_barras` VARCHAR(45) NOT NULL,
  `Nombre` VARCHAR(30) NOT NULL,
  `Precio_Unitario` DECIMAL(10,2) NOT NULL,
  `Stock` INT NOT NULL,
  `ID_Categoria` INT NOT NULL,
  `Descripcion` VARCHAR(45) NOT NULL,
  `En_Promocion` BOOLEAN NOT NULL DEFAULT FALSE,
  PRIMARY KEY (`Codigo_de_barras`),
  INDEX `fk_Productos_Categoria1_idx` (`ID_Categoria` ASC) VISIBLE,
  CONSTRAINT `fk_Productos_Categoria1`
    FOREIGN KEY (`ID_Categoria`)
    REFERENCES `petShop`.`Categoria` (`ID_Categoria`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `petShop`.`Proveedores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `petShop`.`Proveedores` (
  `ID_Proveedor` INT NOT NULL AUTO_INCREMENT,
  `CUIT` VARCHAR(45) NOT NULL,
  `Nombre` VARCHAR(45) NOT NULL,
  `Apellido` VARCHAR(45) NOT NULL,
  `Telefono` VARCHAR(25) NOT NULL,
  PRIMARY KEY (`ID_Proveedor`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `petShop`.`Clientes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `petShop`.`Clientes` (
  `ID_Cliente` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(45) NOT NULL,
  `Apellido` VARCHAR(45) NOT NULL,
  `Telefono` VARCHAR(30) NOT NULL,
  `Email` VARCHAR(45) NULL,
  PRIMARY KEY (`ID_Cliente`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `petShop`.`Sucursales`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `petShop`.`Sucursales` (
  `ID_Sucursal` INT NOT NULL AUTO_INCREMENT,
  `Ciudad` VARCHAR(45) NOT NULL,
  `Direccion` VARCHAR(45) NOT NULL,
  `Telefono` VARCHAR(30) NOT NULL,
  `Email` VARCHAR(45) NULL,
  PRIMARY KEY (`ID_Sucursal`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `petShop`.`Ventas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `petShop`.`Ventas` (
  `ID_Venta` INT NOT NULL AUTO_INCREMENT,
  `Fecha` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `Forma_Pago` VARCHAR(45) NULL,
  `Descuento` DECIMAL(5,2) NULL,
  `Total_Venta` DECIMAL(10,2) NOT NULL,
  `ID_Cliente` INT NOT NULL,
  `ID_Sucursal` INT NOT NULL,
  PRIMARY KEY (`ID_Venta`),
  INDEX `fk_Ventas_Clientes1_idx` (`ID_Cliente` ASC) VISIBLE,
  INDEX `fk_Ventas_Sucursales1_idx` (`ID_Sucursal` ASC) VISIBLE,
  CONSTRAINT `fk_Ventas_Clientes1`
    FOREIGN KEY (`ID_Cliente`)
    REFERENCES `petShop`.`Clientes` (`ID_Cliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Ventas_Sucursales1`
    FOREIGN KEY (`ID_Sucursal`)
    REFERENCES `petShop`.`Sucursales` (`ID_Sucursal`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `petShop`.`Detalle_Ventas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `petShop`.`Detalle_Ventas` (
  `ID_Detalle` INT NOT NULL AUTO_INCREMENT,
  `ID_Venta` INT NOT NULL,
  `Codigo_de_barras` VARCHAR(45) NOT NULL,
  `Cantidad_Unidades` INT NOT NULL,
  `Precio_Unitario` DECIMAL(10,2) NOT NULL,
  `Descuento` DECIMAL(5,2) NOT NULL,
  `Total_Item` DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (`ID_Detalle`),
  INDEX `fk_Detalle_Ventas_Productos1_idx` (`Codigo_de_barras` ASC) VISIBLE,
  INDEX `fk_Detalle_Ventas_Ventas1_idx` (`ID_Venta` ASC) VISIBLE,
  CONSTRAINT `fk_Detalle_Ventas_Productos1`
    FOREIGN KEY (`Codigo_de_barras`)
    REFERENCES `petShop`.`Productos` (`Codigo_de_barras`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Detalle_Ventas_Ventas1`
    FOREIGN KEY (`ID_Venta`)
    REFERENCES `petShop`.`Ventas` (`ID_Venta`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `petShop`.`Empleados`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `petShop`.`Empleados` (
  `CUIL_Empleado` VARCHAR(45) NOT NULL,
  `Nombre` VARCHAR(45) NOT NULL,
  `Apellido` VARCHAR(45) NOT NULL,
  `Telefono` VARCHAR(30) NOT NULL,
  `Email` VARCHAR(45) NOT NULL,
  `Direccion` VARCHAR(45) NULL,
  `ID_Sucursal` INT NOT NULL,
  INDEX `fk_Empleados_Sucursales1_idx` (`ID_Sucursal` ASC) VISIBLE,
  PRIMARY KEY (`CUIL_Empleado`),
  CONSTRAINT `fk_Empleados_Sucursales1`
    FOREIGN KEY (`ID_Sucursal`)
    REFERENCES `petShop`.`Sucursales` (`ID_Sucursal`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `petShop`.`Pedidos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `petShop`.`Pedidos` (
  `ID_Pedido` INT NOT NULL AUTO_INCREMENT,
  `Fecha` DATETIME NOT NULL,
  `ID_Proveedor` INT NOT NULL,
  `Estado` VARCHAR(45) NOT NULL,
  `ID_Sucursal` INT NOT NULL,
  PRIMARY KEY (`ID_Pedido`),
  INDEX `fk_Pedidos_Proveedores1_idx` (`ID_Proveedor` ASC) VISIBLE,
  INDEX `fk_Pedidos_Sucursales1_idx` (`ID_Sucursal` ASC) VISIBLE,
  CONSTRAINT `fk_Pedidos_Proveedores1`
    FOREIGN KEY (`ID_Proveedor`)
    REFERENCES `petShop`.`Proveedores` (`ID_Proveedor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Pedidos_Sucursales1`
    FOREIGN KEY (`ID_Sucursal`)
    REFERENCES `petShop`.`Sucursales` (`ID_Sucursal`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `petShop`.`Detalle_Pedidos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `petShop`.`Detalle_Pedidos` (
  `ID_Detalle` INT NOT NULL AUTO_INCREMENT,
  `ID_Pedido` INT NOT NULL,
  `Codigo_de_barras` VARCHAR(45) NOT NULL,
  `Cantidad` INT NOT NULL,
  `Precio_Unitario` DECIMAL(10,2) NOT NULL,
  `Total` DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (`ID_Detalle`),
  INDEX `fk_Detalle_Pedidos_Productos1_idx` (`Codigo_de_barras` ASC) VISIBLE,
  INDEX `fk_Detalle_Pedidos_Pedidos1_idx` (`ID_Pedido` ASC) VISIBLE,
  CONSTRAINT `fk_Detalle_Pedidos_Productos1`
    FOREIGN KEY (`Codigo_de_barras`)
    REFERENCES `petShop`.`Productos` (`Codigo_de_barras`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Detalle_Pedidos_Pedidos1`
    FOREIGN KEY (`ID_Pedido`)
    REFERENCES `petShop`.`Pedidos` (`ID_Pedido`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;
