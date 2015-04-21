$n=<STDIN>;
while($n--)
{
 $num=<STDIN>;
 ($CountryCode,$LocalAreaCode,$Number) = $num =~ /([0-9]{1,3})[- ]([0-9]{1,3})[- ]([0-9]{4,10})/;
 printf"CountryCode=$CountryCode,LocalAreaCode=$LocalAreaCode,Number=$Number\n";
}