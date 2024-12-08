# part 2 run with
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
                    $antenas[$c][1] - $antenas[$r][1],
                    $antenas[$c][2] - $antenas[$r][2]
                ];

                my $n = 1;
                while (1) {
                    my @nvec = [
                        "#",
                        $antenas[$c][1] + $vec[0][1] * $n,
                        $antenas[$c][2] + $vec[0][2] * $n
                    ];

                    if (   $nvec[0][1] >= 0
                        && $nvec[0][2] >= 0
                        && $nvec[0][1] <= $#map
                        && $nvec[0][2] < $dim )
                    {

                        push( @antinodes, @nvec );
                        $n++;
                    }
                    else {
                        last;
                    }
                }

            }
        }
    }
}

for my $row (@antinodes) {
    say join( ",", @{$row} );
}
for my $row (@antinodes) {
    my $r = @{$row}[1];
    my $c = @{$row}[2];
    substr($map[$r], $c, 1, "#");
}

my $count = 0;
for my $r (0 .. $#map){
    for my $c ( 0 .. ( $dim - 1 ) ) {
        if (substr($map[$r], $c, 1) ne '.'){
            $count++;
        }
    }
}
say "Part 2: $count";
