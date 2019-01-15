#!/usr/bin/env perl

use warnings;
use strict;

use Getopt::Long;
use Pod::Usage;

use FindBin qw($RealBin);
use lib "$RealBin/../lib/";
use File::Basename;

use Verbose;
use Verbose::ProgressBar;

use List::Util 'sum';
use Bio::SeqIO;

our $VERSION = '1.00';

=head1 NAME

        counts2table - a tool to create a merged count matrix based on multiple incomplete unsorted count tables.

=head1 CHANGELOG

        see git log

=head1 SYNOPSIS

        list2venn --tbl <tbl>

=cut
    
=over

=cut
    
my %opt;

=item [--tbl=<TBL-FILE>]

        Input count table. Specify multiple count tables separated by comma.
=cut
    
$opt{'tbl=s'} = \(my $opt_tbl = '-');

=item [--verbose=<INT>]

        Toggle verbose level, default 2, which outputs statistics and progress.
        Set 1 for statistics only or 0 for no verbose output.

=cut
    
$opt{'verbose=i'} = \(my $opt_verbose = 2);

=item [--quiet]

        Omit all verbose messages. The same as --verbose=0, superceeds --verbose settings.

=cut
    
$opt{'quiet'} = \(my $opt_quiet);

=item [--help]

        Display this help

=cut
    
$opt{'help|?'} = \(my $opt_help);

=item [--version|-V]

        Display current version

=cut
    
$opt{'version|V'} = \(my $opt_version);

=back

=cut
    
GetOptions(%opt) or pod2usage(1);

pod2usage(1) if $opt_help;
if ($opt_version){
        print "$VERSION\n";
        exit(1);
}

$opt_verbose = 0 if $opt_quiet;

##------------------------------------------------------------------------##

my $V = Verbose->new(
    level => 1,
    report_level => $opt_verbose,
    line_width => 80,

    );

$V->verbose("$0-$VERSION");

##------------------------------------------------------------------------##

if(!$opt_tbl)
{
    $V->exit("Cannot find input file: $opt_tbl") if ! -f $opt_tbl;

    if( -s $opt_tbl == 0){
        $V->verbose("Empty input file: $opt_tbl");
        exit(0);
    }

}

##------------------------------------------------------------------------##

my @tbl = split(/,/,$opt_tbl);

##------------------------------------------------------------------------##

# Read tables

my %stbl = ();
my %sids = ();
my %data = ();

foreach my $tbl (@tbl)
{

    my $fh_tbl = opt2read($tbl,$V);
    $stbl{$tbl}++;
    while(<$fh_tbl>)
    {
	chomp($_);
	my @data = split(/\t+/, $_);
	$sids{$data[0]}++;
	$data{$tbl}{$data[0]} = $data[1];
    }
    close($fh_tbl);
}

foreach my $id (sort keys %sids)
{
    my @pa = ();
    foreach my $tbl (sort keys %stbl)
    {
	my $entry = (exists $data{$tbl}{$id}) ? $data{$tbl}{$id} : 0;
	push(@pa,$entry);
    }
    print $id,"\t",join("\t",@pa),"\n";
}

##------------------------------------------------------------------------##

=head1 Methods

=cut

=head2 opt2read

    Open read file handle to any file given and report to log.

=cut
    
sub opt2read {
    my ($v, $V) = @_;
    my $h;
    return unless $v;
    if(-f $v)
    {
        $V->verbose("Using $v");
        open($h, "<", $v) or $V->exit("$!: $v");
    }
    return $h;
}
