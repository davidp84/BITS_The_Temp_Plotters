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


<article> 

<h1>Team Members</h1>
<p>Timothy Hall - s3851553</p>
<p>John Rehill - s3828158</p>
<p>David Pulvirenti - s3858853</p>
<p>Jacob Hooper - s3903479</p>
<p>Mitchell Abrahams - s3792975</p>

<h1>The Motivation</h1>

<p>The motivation for the Temp Plotters team was that everyone in 
  the team wanted to develop, design, and produce a small IT project 
  that implemented a microcomputer along with some form of sensor. 
  Everyone already had some experience with coding; however, 
  implementing something based around hardware was exciting and 
  provided additional learning that could complement our existing 
  coding experience. 
  </p>
  
<p>
After initial discussion, the idea of making a HVAC control unit 
utilising a Raspberry Pi and a temperature and a humidity sensor 
would be a great starting point for the project. Through research 
into the hardware, components, and discussion amongst each other 
it was decided to expand this to include a website component to 
round out the project and provide a user interface. </p>

</artcile>

</main>

<?= footerModule() ?>