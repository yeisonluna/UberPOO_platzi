<?php

require_once('car.php');
require_once('account.php');
require_once('uberX.php');
require_once('uberPool.php');

$uberX = new UberX("UBS532", new Account("Andres Herrera", "AND3452"), "Chevrolet", "Spark");
$uberX->printDataCar();

$uberPool = new UberPool("AFO987", new Account("Felipe Barrera", "FB5778"), "Dodge", "Attitude");
$uberPool->printDataCar();

?>