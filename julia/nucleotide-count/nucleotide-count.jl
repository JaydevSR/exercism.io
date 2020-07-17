"""
    count_nucleotides(strand)

The frequency of each nucleotide within `strand` as a dictionary.

Invalid strands raise a `DomainError`.

"""
function count_nucleotides(strand)
    nucsn = Dict([nuc, count(==(nuc), strand)] for nuc in "ATGC")
    if sum(values(nucsn)) != length(strand)
        throw(DomainError("Invalid nucleotide sequence."))
    end
    return nucsn
end