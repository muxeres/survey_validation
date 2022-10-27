-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema dojo_survey
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `dojo_survey` ;

-- -----------------------------------------------------
-- Schema dojo_survey
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `dojo_survey` DEFAULT CHARACTER SET utf8 ;
USE `dojo_survey` ;

-- -----------------------------------------------------
-- Table `dojo_survey`.`locations`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dojo_survey`.`locations` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `location_name` VARCHAR(45) NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT NOW(),
  `updated_at` DATETIME NOT NULL DEFAULT NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dojo_survey`.`languages`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dojo_survey`.`languages` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `language_name` VARCHAR(45) NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT NOW(),
  `updated_at` DATETIME NOT NULL DEFAULT NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dojo_survey`.`surveys`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dojo_survey`.`surveys` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `comment` TEXT NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT NOW(),
  `updated_at` DATETIME NOT NULL DEFAULT NOW(),
  `location_id` INT NOT NULL,
  `language_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_surveys_locations_idx` (`location_id` ASC) VISIBLE,
  INDEX `fk_surveys_languages1_idx` (`language_id` ASC) VISIBLE,
  CONSTRAINT `fk_surveys_locations`
    FOREIGN KEY (`location_id`)
    REFERENCES `dojo_survey`.`locations` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_surveys_languages1`
    FOREIGN KEY (`language_id`)
    REFERENCES `dojo_survey`.`languages` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
