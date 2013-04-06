#!C:\Perl64\bin\perl.exe

use CGI;
use Data::Dumper;

my $cgi=CGI->new;


# my $code=$cgi->param('code');
my $data = $cgi->param('textcontent');
# $data =~ s/\r\n//g;
my @pairs = split(/\n/, $data);

my %df;
for ($i=0; $i<=$#pairs; $i++) {
  $pairs[$i] =~ s/\r//g;
  my @coords = split(/\s/, $pairs[$i]);
  
  $df{$i}->{"x"} = $coords[0];
  $df{$i}->{"y"} = $coords[1];
}


open(OUT, "> test.txt");
print OUT Dumper(\%df);
close(OUT);

print $cgi->header(),
      $cgi->start_html(-title=>'Wow!'),
      $cgi->h1('Wow!'),
      'Look Ma, no hands!',
      $data,
      $cgi->end_html();
# $time_exec = gettimeofday() - $time_start;
# $logger->write(">> TIME TO DUMP client xml: $time_exec");

# $total_time_exec = gettimeofday() - $total_time_start;
# $logger->write(">> TOTAL EXECUTION TIME: $total_time_exec");