use strict;
use warnings;

my @haystack = <>;
my $rows     = $#haystack;
my $cols     = length( $haystack[0] ) - 2;

my $num_xmas = 0;

sub l {
    return "Z" if ( $_[0] < 0 || $_[0] > $rows || $_[1] < 0 || $_[1] > $cols );
    return substr( $haystack[ $_[0] ], $_[1], 1 );
}

for my $row ( 0 .. $rows ) {
    for my $col ( 0 .. $cols ) {
        my $letter = l( $row, $col );

        if ( $letter eq 'A' ) {

            if (   ( l( $row - 1, $col - 1 ) eq 'M' )
                && ( l( $row + 1, $col + 1 ) eq 'S' )
                && ( l( $row - 1, $col + 1 ) eq 'M' )
                && ( l( $row + 1, $col - 1 ) eq 'S' ) )
            {
                $num_xmas++;
            }

            if (   ( l( $row - 1, $col - 1 ) eq 'M' )
                && ( l( $row + 1, $col + 1 ) eq 'S' )
                && ( l( $row - 1, $col + 1 ) eq 'S' )
                && ( l( $row + 1, $col - 1 ) eq 'M' ) )
            {
                $num_xmas++;
            }

            if (   ( l( $row - 1, $col - 1 ) eq 'S' )
                && ( l( $row + 1, $col + 1 ) eq 'M' )
                && ( l( $row - 1, $col + 1 ) eq 'S' )
                && ( l( $row + 1, $col - 1 ) eq 'M' ) )
            {
                $num_xmas++;
            }

            if (   ( l( $row - 1, $col - 1 ) eq 'S' )
                && ( l( $row + 1, $col + 1 ) eq 'M' )
                && ( l( $row - 1, $col + 1 ) eq 'M' )
                && ( l( $row + 1, $col - 1 ) eq 'S' ) )
            {
                $num_xmas++;
            }

        }
    }
}

print "Part 2: $num_xmas \n";
