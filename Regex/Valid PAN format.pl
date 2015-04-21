$n=<STDIN>;
while($n--)
{
 $word=<STDIN>;
 if($word =~ /^[A-Z]{5}[0-9]{4}[A-Z]/)
   {
     printf "YES\n";
   }
   else
   { 
     printf "NO\n";
     }
}