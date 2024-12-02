use strict;
use warnings;

if ( $#ARGV + 1 != 1 ) {
    print "> Enter input data file's name!!! \n";
    exit;
}

open( my $in, "<", "$ARGV[0]" ) or die $!;

sub sign {
    return ( $_[0] > 0 ) - ( $_[0] < 0 );
}

sub process_report {
    my @levels = @_;
    my $dir    = sign( $levels[1] - $levels[0] );

    for my $i ( 1 .. $#levels ) {
        my $dif = $levels[$i] - $levels[ $i - 1 ];
        if ( sign($dif) != $dir || abs($dif) > 3 ) {
            return 0;
        }
    }
    return 1;
}

sub problem_dampener {
    my @levels = @_;

    for my $i ( 0 .. $#levels ) {
        my @nl = @levels;
        splice( @nl, $i, 1 );
        my $pp = process_report(@nl);
        if ($pp) {
            return 1;
        }
    }
    return 0;
}

my $valid_reports = 0;
my $extra_reports = 0;

while ( my $report = <$in> ) {
    unless ( $report =~ /^\s$/ ) {
        my @levels = split( ' ', $report );
        my $pr     = process_report(@levels);
        $valid_reports += $pr;
        unless ($pr) {
            $extra_reports += problem_dampener(@levels);
        }
    }
}

print "Part 1: $valid_reports\n";
print "Part 2: ($valid_reports+$extra_reports): ",
  $valid_reports + $extra_reports, "\n";

close($in);