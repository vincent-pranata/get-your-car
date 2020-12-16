-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema ppdb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema ppdb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `ppdb` DEFAULT CHARACTER SET utf8 ;
USE `ppdb` ;

-- -----------------------------------------------------
-- Table `ppdb`.`customer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ppdb`.`customer` (
  `cust_id` INT NOT NULL,
  `cust_first_name` VARCHAR(45) NOT NULL,
  `cust_last_name` VARCHAR(45) NOT NULL,
  `cust_DOB` DATE NOT NULL,
  `cust_email` VARCHAR(45) NOT NULL,
  `cust_phone` VARCHAR(45) NOT NULL,
  `cust_password` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`cust_id`),
  UNIQUE INDEX `cust_id_UNIQUE` (`cust_id` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ppdb`.`licence`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ppdb`.`licence` (
  `licence_number` INT NOT NULL,
  `licence_country` VARCHAR(45) NOT NULL,
  `licence_state` VARCHAR(45) NOT NULL,
  `licence_issue_date` DATE NOT NULL,
  `licence_expiry_date` DATE NOT NULL,
  PRIMARY KEY (`licence_number`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ppdb`.`car`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ppdb`.`car` (
  `car_id` INT NOT NULL,
  `car_name` VARCHAR(45) NOT NULL,
  `car_colour` VARCHAR(45) NOT NULL,
  `car_description` VARCHAR(45) NOT NULL,
  `car_capacity` INT NOT NULL,
  `car_registration_plate` VARCHAR(45) NOT NULL,
  `car_fuel_type` VARCHAR(45) NOT NULL,
  `car_transmission` VARCHAR(45) NOT NULL,
  `car_status` BINARY(1) NOT NULL,
  PRIMARY KEY (`car_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ppdb`.`booking`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ppdb`.`booking` (
  `booking_id` INT NOT NULL,
  `customer_cust_id` INT NOT NULL,
  `car_car_id` INT NOT NULL,
  `booking_start_date` DATE NOT NULL,
  `booking_start_time` TIME NOT NULL,
  `booking_end_date` DATE NOT NULL,
  `booking_end_time` TIME NOT NULL,
  `booking_cost` FLOAT NOT NULL,
  `booking_status` INT NOT NULL,
  PRIMARY KEY (`booking_id`, `customer_cust_id`, `car_car_id`),
  INDEX `fk_booking1_customer1_idx` (`customer_cust_id` ASC) VISIBLE,
  INDEX `fk_booking1_car1_idx` (`car_car_id` ASC) VISIBLE,
  CONSTRAINT `fk_booking1_customer1`
    FOREIGN KEY (`customer_cust_id`)
    REFERENCES `ppdb`.`customer` (`cust_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_booking1_car1`
    FOREIGN KEY (`car_car_id`)
    REFERENCES `ppdb`.`car` (`car_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ppdb`.`drivers_licence`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ppdb`.`drivers_licence` (
  `customer_cust_id` INT NOT NULL,
  `licence_licence_number` INT NOT NULL,
  PRIMARY KEY (`customer_cust_id`, `licence_licence_number`),
  INDEX `fk_drivers_licence_licence1_idx` (`licence_licence_number` ASC) VISIBLE,
  CONSTRAINT `fk_drivers_licence_customer1`
    FOREIGN KEY (`customer_cust_id`)
    REFERENCES `ppdb`.`customer` (`cust_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_drivers_licence_licence1`
    FOREIGN KEY (`licence_licence_number`)
    REFERENCES `ppdb`.`licence` (`licence_number`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ppdb`.`address`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ppdb`.`address` (
  `address_id` INT NOT NULL,
  `address_street_number` INT NOT NULL,
  `address_street_name` VARCHAR(45) NOT NULL,
  `address_city` VARCHAR(45) NOT NULL,
  `address_state` VARCHAR(45) NOT NULL,
  `address_postcode` VARCHAR(45) NOT NULL,
  `address_latitude` FLOAT NOT NULL,
  `address_longitude` FLOAT NOT NULL,
  PRIMARY KEY (`address_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ppdb`.`customer_address`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ppdb`.`customer_address` (
  `customer_cust_id` INT NOT NULL,
  `address_address_id` INT NOT NULL,
  PRIMARY KEY (`customer_cust_id`, `address_address_id`),
  INDEX `fk_customer_address_address1_idx` (`address_address_id` ASC) VISIBLE,
  CONSTRAINT `fk_customer_address_customer1`
    FOREIGN KEY (`customer_cust_id`)
    REFERENCES `ppdb`.`customer` (`cust_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_customer_address_address1`
    FOREIGN KEY (`address_address_id`)
    REFERENCES `ppdb`.`address` (`address_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ppdb`.`location`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ppdb`.`location` (
  `location_id` INT NOT NULL,
  `car_car_id` INT NOT NULL,
  `location_description` VARCHAR(45) NOT NULL,
  `location_latitude` FLOAT NOT NULL,
  `location_longitude` FLOAT NOT NULL,
  PRIMARY KEY (`location_id`, `car_car_id`),
  INDEX `fk_location_car1_idx` (`car_car_id` ASC) VISIBLE,
  CONSTRAINT `fk_location_car1`
    FOREIGN KEY (`car_car_id`)
    REFERENCES `ppdb`.`car` (`car_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
