use strict;
use warnings;
use feature 'say';

my $in = <>;
chomp($in);
my @stones = split( ' ', $in );

sub blink {
    my @stones = @_;
    my @new_line;
    for my $stone (@stones) {
        if ( $stone == 0 ) {
            push( @new_line, 1 );
            next;
        }
        elsif ( length($stone) % 2 == 0 ) {
            push( @new_line, 0 + substr( $stone, 0, length($stone) / 2 ) );
            push( @new_line, 0 + substr( $stone, length($stone) / 2 ) );
            next;
        }
        else {
            push(@new_line, $stone * 2024 );
        }
    }
    return @new_line;
}

for ( 1 .. 25 ) {
    @stones = blink(@stones);
}
say "Part 1: ",$#stones+1;