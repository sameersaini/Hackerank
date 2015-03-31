$n=<STDIN>;

foreach $i (1..$n)
{
 $temp=<STDIN>;
 chomp($temp);
 ($key,$val)=(split " ",$temp);
 if($i <= $n/2)
 {
  $val= "-" ;
 }
 $hash{$key}=$hash{$key}."$val ";
}

@keys = sort {$a <=> $b} keys %hash;
foreach $a (@keys)
{
 print "$hash{$a}";
}