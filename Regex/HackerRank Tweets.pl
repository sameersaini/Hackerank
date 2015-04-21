$n=<STDIN>;
$count=0;
while($n--)
{
 $tweet=<STDIN>;
 chomp($tweet);
 if($tweet =~ /.*hackerrank/i)
  {
   $count++;
  }
}
printf"$count"