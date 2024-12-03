use strict;
use warnings;
use Scalar::Util qw(looks_like_number);

my $acc = 0;
my $do  = 1;
while ( my $line = <> ) {
    my @matches = $line =~ /mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))/gm;
    for ( my $i = 0 ; $i < $#matches ; $i++ ) {
        if ( !defined $matches[$i] ) {
            next;
        }
        if ( $matches[$i] eq "don't()" ) {
            $do = 0;
            next;
        }
        if ( $matches[$i] eq "do()" ) {
            $do = 1;
            next;
        }
        if (   $do
            && looks_like_number( $matches[$i] )
            && looks_like_number( $matches[ $i + 1 ] ) )
        {
            $acc += $matches[$i] * $matches[ $i + 1 ];
            $i++;
        }
    }
}
print "Part 2: $acc \n";

