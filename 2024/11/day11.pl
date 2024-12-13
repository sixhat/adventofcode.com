package Day11;

use strict;
use warnings;
use feature 'say';
use Readonly;

Readonly my $YEAR       => 2024;
Readonly my $MAX_RUNS   => 35;
Readonly my $PART_1_RUN => 25;

my $in = <>;
chomp $in;
my @stones = split q/ /, $in;

sub blink {
    my @sts = @_;
    my @new_line;
    for my $stone (@sts) {
        if ( !$stone ) {
            push @new_line, 1;
        }
        elsif ( length($stone) % 2 == 0 ) {
            push @new_line,
              ( substr $stone, 0, length($stone) / 2 ),
              ( 0 + substr $stone, length($stone) / 2 );
        }
        else {
            push @new_line, $stone * $YEAR;
        }
    }
    return @new_line;
}

# say "@stones";
for my $i ( 1 .. $MAX_RUNS ) {
    @stones = blink(@stones);
    if ( $i == $PART_1_RUN ) {
        say q/Part 1: /, $#stones + 1;
    }
    say $#stones+ 1;
}
say q/Part 2: /, $#stones + 1;
1;
