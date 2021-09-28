<!DOCTYPE html>
<html lang='en'>

<?php 

include ('tools.php');
topModule("The Temp Plotters");
    
?>

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

<?= footerModule() ?>
<?= debugModule() ?>