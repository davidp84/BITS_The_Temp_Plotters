<!DOCTYPE html>
<html lang='en'>

<?php 

include ('tools.php');
topModule("The Temp Plotters");
    
?>


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


<table class="main-table">
  <tr>
    <th class="table-header">Date</th>
    <th class="table-header">Temperature</th>
    <th class="table-header">Humidity</th>
    <th class="table-header">Alert Sent</th>
  </tr>
    <?= tableModule() ?>
</table>

<<<<<<< HEAD
<h1> DUMMY HEADING <h1>

<p> dummy text </p>
<p> dummy text </p>
<p> dummy text </p>
<p> dummy text </p>
<p> dummy text </p>
<p> dummy text </p>
<p> dummy text </p>
<p> Testing update across all redundancies.<p>

<?= footerModule() ?>
=======
<?= footerModule() ?>
<?= debugModule() ?>
>>>>>>> 08bb349f578776fba31b833baec1c0d7c7cf2ddb
