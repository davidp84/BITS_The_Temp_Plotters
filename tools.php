<?php
  session_start();
  error_reporting( E_ERROR | E_WARNING | E_PARSE);

  $alerts = getAlertsFromCSV();

  function topModule($title) {
  echo <<<"TOP"
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>$title</title>

<link id='stylecss' type="text/css" rel="stylesheet" href="style.css?t=<?= filemtime("style.css"); ?>
<script src='script.js'></script>

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@300&display=swap" rel="stylesheet">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@300&family=Belleza&family=Noto+Serif&display=swap"
rel="stylesheet">
</head>

<body>
  <div class='main-grid'>  
    <header class='logo-header'>
    <img class='logo-head' src='../../media/logo.jpg'>
      <h2 class='company-name'>The Temp Plotters</h2>
      <a href='index.php'>
      <img class='logo' src='../../media/Logo_Resized.png' alt='The Temp Plotters Company Logo'>
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
TOP;
}

function footerModule() {
  echo <<<"END"
</main>

<footer>
  <div id='footer-contact'>
    <p>The Temp Plotters - 02 9678 1234 - info@thetempplotters.com.au</p>
  </div>
  <div>Disclaimer: This website is not a real website and is being developed as part of a School of Science
  course at RMIT University in Melbourne, Australia.</div>
</footer>
</div>
</body>

</html>
END;
}

// Builds array of alerts from CSV File
function getAlertsFromCSV() {
  $alerts=[];
  if( ($fp = fopen('alerts.txt','r')) && flock($fp, LOCK_SH) ) {
    if (($headings = fgetcsv($fp)) !== false) {
      while ( $cells = fgetcsv($fp) ) {
        $numCols = count($cells);
        for ($c=1; $c<$numCols; $c++) {
          $alerts[$cells[0]][$headings[$c]] = $cells[$c];
        }
        $date=explode('|', $alerts[$cells[0]]['date'] );
        $temp=explode('|', $alerts[$cells[0]]['temp'] );
        $humidity=explode('|', $alerts[$cells[0]]['humidity'] );
        $alerted=explode('|', $alerts[$cells[0]]['alerted'] );
      }
    }
    flock($fp, LOCK_UN);
    fclose($fp);
    return($alerts);
  }
}

// Builds table rows from data collected from CSV file.
function tableModule() {
  foreach ($alerts as $alert => $range) {
  $date = $range['date'];
  $temp = $range['temp'];
  $humidity = $range['humidity'];
  $alerted = $range['alerted'];
  echo <<<"TABLE"
  <tr>
    <td class="table-row">$date</td>
    <td class="table-row">$temp</td>
    <td class="table-row">$humidity</td>
    <td class="table-row">$alerted</td>
  </tr>
TABLE;
}
}
