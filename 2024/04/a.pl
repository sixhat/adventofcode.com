use strict;
use warnings;

my @haystack = <>;
my $rows     = $#haystack;
my $cols     = length( $haystack[0] ) - 2;

my $num_xmas = 0;

sub get_letter {
    return "Z" if ( $_[0] < 0 || $_[0] > $rows || $_[1] < 0 || $_[1] > $cols );
    return substr( $haystack[ $_[0] ], $_[1], 1 );
}

for my $row ( 0 .. $rows ) {
    for my $col ( 0 .. $cols ) {
        my $letter = get_letter( $row, $col );

        if ( $letter eq 'X' ) {

            # check east west.
            if ( substr( $haystack[$row], $col, 4 ) eq 'XMAS' ) {
                $num_xmas++;
            }

            if ( substr( $haystack[$row], $col - 3, 4 ) eq 'SAMX' ) {
                $num_xmas++;
            }

            # south
            if (   ( get_letter( $row + 1, $col ) eq 'M' )
                && ( get_letter( $row + 2, $col ) eq 'A' )
                && ( get_letter( $row + 3, $col ) eq 'S' ) )
            {
                $num_xmas++;
            }

            # north
            if (   ( get_letter( $row - 1, $col ) eq 'M' )
                && ( get_letter( $row - 2, $col ) eq 'A' )
                && ( get_letter( $row - 3, $col ) eq 'S' ) )
            {
                $num_xmas++;
            }

            # sw
            if (   ( get_letter( $row + 1, $col - 1 ) eq 'M' )
                && ( get_letter( $row + 2, $col - 2 ) eq 'A' )
                && ( get_letter( $row + 3, $col - 3 ) eq 'S' ) )
            {
                $num_xmas++;
            }

            # se
            if (   ( get_letter( $row + 1, $col + 1 ) eq 'M' )
                && ( get_letter( $row + 2, $col + 2 ) eq 'A' )
                && ( get_letter( $row + 3, $col + 3 ) eq 'S' ) )
            {
                $num_xmas++;
            }

            #nw
            if (   ( get_letter( $row - 1, $col - 1 ) eq 'M' )
                && ( get_letter( $row - 2, $col - 2 ) eq 'A' )
                && ( get_letter( $row - 3, $col - 3 ) eq 'S' ) )
            {
                $num_xmas++;
            }

            #ne
            if (   ( get_letter( $row - 1, $col + 1 ) eq 'M' )
                && ( get_letter( $row - 2, $col + 2 ) eq 'A' )
                && ( get_letter( $row - 3, $col + 3 ) eq 'S' ) )
            {
                $num_xmas++;
            }
        }
    }
}

print "Part 1: $num_xmas \n";
