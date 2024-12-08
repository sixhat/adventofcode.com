# part 1 run with 
# perl a.pl input | grep "#" | sort | uniq | wc -l
use strict;
use warnings;
use feature 'say';

my @map;
my @antenas;
my @antinodes;
my $i = -1;
my $dim;
while ( my $line = <> ) {
    chomp($line);
    push( @map, $line );
    $i++;
    $dim = length($line);
    for my $c ( 0 .. ( $dim - 1 ) ) {
        my $letter = substr( $line, $c, 1 );
        if ( $letter ne '.' ) {
            push( @antenas, [ $letter, $i, $c ] );
        }
    }
}

for my $row (@antenas) {
    say join( ",", @{$row} );
}

for my $r ( 0 .. $#antenas ) {
    my $a = $antenas[$r][0];
    if ( $a ne '.' ) {
        for my $c ( 0 .. $#antenas ) {
            my $b = $antenas[$c][0];
            if ( $r != $c && $a eq $b ) {
                my @vec = [
                    "#",
                    2 * $antenas[$c][1] - $antenas[$r][1],
                    2 * $antenas[$c][2] - $antenas[$r][2]
                ];
                
                if (   $vec[0][1] >= 0
                    && $vec[0][2] >= 0
                    && $vec[0][1] <= $#map
                    && $vec[0][2] < $dim )
                {

                    push( @antinodes, @vec );
                }
            }
        }
    }
}

for my $row (@antinodes) {
    say join( ",", @{$row} );
}
