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

        if ( $letter eq 'A' ) {

            if (   ( get_letter( $row - 1, $col - 1 ) eq 'M' )
                && ( get_letter( $row + 1, $col + 1 ) eq 'S' )
                && ( get_letter( $row - 1, $col + 1 ) eq 'M' )
                && ( get_letter( $row + 1, $col - 1 ) eq 'S' ) )
            {
                $num_xmas++;
            }

            if (   ( get_letter( $row - 1, $col - 1 ) eq 'M' )
                && ( get_letter( $row + 1, $col + 1 ) eq 'S' )
                && ( get_letter( $row - 1, $col + 1 ) eq 'S' )
                && ( get_letter( $row + 1, $col - 1 ) eq 'M' ) )
            {
                $num_xmas++;
            }

            if (   ( get_letter( $row - 1, $col - 1 ) eq 'S' )
                && ( get_letter( $row + 1, $col + 1 ) eq 'M' )
                && ( get_letter( $row - 1, $col + 1 ) eq 'S' )
                && ( get_letter( $row + 1, $col - 1 ) eq 'M' ) )
            {
                $num_xmas++;
            }

            if (   ( get_letter( $row - 1, $col - 1 ) eq 'S' )
                && ( get_letter( $row + 1, $col + 1 ) eq 'M' )
                && ( get_letter( $row - 1, $col + 1 ) eq 'M' )
                && ( get_letter( $row + 1, $col - 1 ) eq 'S' ) )
            {
                $num_xmas++;
            }

        }
    }
}

print "Part 2: $num_xmas \n";
