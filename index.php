<!DOCTYPE html>
<html lang='en'>

<?php 

include ('tools.php');
topModule("The Temp Plotters");
    
?>


<body>
<div class='main-grid'>  
<header class='logo-header'>
<!-- <img class='logo-head' src='../../media/logo.jpg'> -->
  <h2 class='company-name'>The Temp Plotters</h2>
  <a href='index.php'>
    <!-- img used for educational purposes only, note this will be relpaced with a new logo -->
  <img class='logo' src='https://i.pinimg.com/564x/74/94/ed/7494ed64686f16ed0535873c1c2790e1.jpg' alt='The Temp Plotters Logo' width="750" height="350">
  </a>
</header>

<nav id="nav">
  <div>
    <ul>
      <li><a href="index.php" id="home__link">Home</a></li>
      <li><a href="about.php" class="nav_link">About</a></li>
    </ul>
  </div>
</nav>

<main>

<h1> ALERTS <h1>

<article> 

<table  class="main-table" style="width:70%">
  <tr>
    <th class="table-header">Date</th>
    <th class="table-header" >Temperature</th>
    <th class="table-header">Humidity</th>
    <th class="table-header">Alert Sent</th>
  </tr>
    <?= tableModule() ?>
</table>

</artcile>

</main>

<?= footerModule() ?>
<?= debugModule() ?>
