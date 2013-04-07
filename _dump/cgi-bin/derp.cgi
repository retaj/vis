#!C:\Perl64\bin\perl.exe
use CGI;

$cgi = new CGI;

$secretword = $cgi->param('w');
$remotehost = $cgi->remote_host();

print $cgi->header,
      $cgi->start_html(-title=>'Wow!'),
      $cgi->h1('Wow!'),
      $cgi->p("<p>The secret word is <b>$secretword</b> and your IP is <b>$remotehost</b>.</p>"),
      "<p>The secret word is ur IP .</p>",
      '<script type="text/javascript" src="../js/test.js"></script>',
      # $cgi->script(
              # -type=>'text/javascript',
              # -src=>'../js/test.js'),
      $cgi->end_html();
# print "<p>The secret word is <b>$secretword</b> and your IP is <b>$remotehost</b>.</p>";
# print "<p>The secret word is <b>$secretword</b> and your IP is <b>$remotehost</b>.</p>";
