The params.ctl file contains general parameters:
Length of the mitochondrial sequence;
The length of the nuclear sequence;
Average number of children;
Maximum life time of an individual (time is measured in reproductive cycles);
Probability of mutation of nucleotide and mitochondrial sequences;
The duration of the simulation, expressed in the number of reproductive cycles.
The environmental impact on each nursing species (realized through the capacity of the environment) is described separately in two files, envi.ctl and
envi1.ctl
The first column expresses the number of reproductive cycles;
The next is the initial number of organisms;
The third column contains the final number of organisms.
The gene flow script is in the file
swing.ctl
The first line shows the number of segments.
Each segment is defined by three values:
the first is the length, which is expressed as the number of reproductive cycles.
The second value is the probability that females of the form 1 form pairs with males of the form 2. And the same relation works for type 2 (third value).
