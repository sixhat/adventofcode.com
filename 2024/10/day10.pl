package Day10;
# https://adventofcode.com/2024/day/10

use strict;
use warnings;
use feature 'say';

# procedure DFS(G, v) is
#     label v as discovered
#     for all directed edges from v to w that are in G.adjacentEdges(v) do
#         if vertex w is not labeled as discovered then
#             recursively call DFS(G, w)

# for each 0 process a DFS for 9s and mark all thar are visitable

sub p2d {
    for my $e (@_) {
        say join( ',', @$e );
    }
}

# Read the map
my @map;
while ( my $line = <> ) {
    chomp($line);
    my @vec = split( '', $line );
    push( @map, [@vec] );
}

p2d(@map);

# DFS
my @discovered;
my $nines = 0;


sub dfs_grid {
    my ($grid, $row, $col, $visited) = @_;

    # Boundary and visited checks
    return if $row < 0 || $row >= $rows;       # Out of bounds (row)
    return if $col < 0 || $col >= $cols;       # Out of bounds (col)
    return if $visited->[$row][$col];          # Already visited
    return if $grid->[$row][$col] == 0;        # Not a valid cell (e.g., 0)

    # Mark the cell as visited
    $visited->[$row][$col] = 1;
    print "Visited cell ($row, $col)\n";

    # Recur for all neighboring cells
    for my $dir (@directions) {
        my ($dr, $dc) = @$dir;
        dfs_grid($grid, $row + $dr, $col + $dc, $visited);
    }
}


sub dfs {
    say @_;
    my $v = $_[0];
    push( @discovered, $v );
    my $cv = @map[ @$v[0], @$v[1] ];

    if ( $cv == 9 ) {
        $nines++;
        return 1;
    }

    if ( @$v[0] > 0 && @map[ @$v[0] - 1, @$v[1] ] == ( $cv + 1 ) ) {
        return dfs( [ @$v[0] - 1, @$v[1] ] );
    }
    say @discovered;
}

dfs( [ 0, 2 ] );

1;