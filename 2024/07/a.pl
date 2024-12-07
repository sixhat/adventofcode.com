use strict;
use warnings;
use feature 'say';

# Recursive function

sub search {
    my $t  = $_[0];
    my $rt = $_[-1];
    my @e  = @_[ 1 .. ( $#_ - 1 ) ];

    if ( $#e == -1 ) {
        if ( $t == $rt ) {
            return 1;
        }
        else {
            return 0;
        }
    }

    my $plus = search( $t, @e[ 1 .. $#e ], $rt + $e[0] );
    my $mult = search( $t, @e[ 1 .. $#e ], $rt * $e[0] );
    my $orop = search( $t, @e[ 1 .. $#e ], $rt . $e[0] ); # comment this line for Part 1

    if ( $plus + $mult + $orop ) {
        return $t;
    }
    else {
        return 0;
    }
}

my $accum = 0;
while ( my $line = <> ) {
    chomp($line);
    say $line;
    my @el    = split( ' ', $line );
    my @total = split( ':', $el[0] );
    my $total = $total[0];
    @el = @el[ 1 .. $#el ];

    my $temp = search( $total, @el[ 1 .. $#el ], $el[0] );
    if ( $temp > 0 ) {
        say "found ", $line;
    }
    $accum += $temp;
}
say "Part 2: ", $accum;
