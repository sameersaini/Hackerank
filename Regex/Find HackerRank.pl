$n=<STDIN>;
while($n--)
{
 $input=<STDIN>;
 chomp($input);

 if($input =~ /^hackerrank$/)
  {
   printf "0\n";
  }
  elsif($input =~ /hackerrank$/)
  {
   printf "2\n";
  }
  elsif($input =~ /^hackerrank/)
  {
   printf "1\n";
  }
  else
  {
   printf "-1\n";
  }
}