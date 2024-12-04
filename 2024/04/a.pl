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

        if ( $letter eq 'X' ) {

            # check east west.
            if ( substr( $haystack[$row], $col, 4 ) eq 'XMAS' ) {
                $num_xmas++;
            }

            if ( substr( $haystack[$row], $col - 3, 4 ) eq 'SAMX' ) {
                $num_xmas++;
            }

            # south
            if (   ( l( $row + 1, $col ) eq 'M' )
                && ( l( $row + 2, $col ) eq 'A' )
                && ( l( $row + 3, $col ) eq 'S' ) )
            {
                $num_xmas++;
            }

            # north
            if (   ( l( $row - 1, $col ) eq 'M' )
                && ( l( $row - 2, $col ) eq 'A' )
                && ( l( $row - 3, $col ) eq 'S' ) )
            {
                $num_xmas++;
            }

            # sw
            if (   ( l( $row + 1, $col - 1 ) eq 'M' )
                && ( l( $row + 2, $col - 2 ) eq 'A' )
                && ( l( $row + 3, $col - 3 ) eq 'S' ) )
            {
                $num_xmas++;
            }

            # se
            if (   ( l( $row + 1, $col + 1 ) eq 'M' )
                && ( l( $row + 2, $col + 2 ) eq 'A' )
                && ( l( $row + 3, $col + 3 ) eq 'S' ) )
            {
                $num_xmas++;
            }

            #nw
            if (   ( l( $row - 1, $col - 1 ) eq 'M' )
                && ( l( $row - 2, $col - 2 ) eq 'A' )
                && ( l( $row - 3, $col - 3 ) eq 'S' ) )
            {
                $num_xmas++;
            }

            #ne
            if (   ( l( $row - 1, $col + 1 ) eq 'M' )
                && ( l( $row - 2, $col + 2 ) eq 'A' )
                && ( l( $row - 3, $col + 3 ) eq 'S' ) )
            {
                $num_xmas++;
            }
        }
    }
}

print "Part 1: $num_xmas \n";
