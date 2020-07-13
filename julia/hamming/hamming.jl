"""
    distance(a::AbstractString, b::AbstractString)

The hamming distance between the two strands.

Strands of unequal length throw "ArgumentError".
"""
function distance(a::AbstractString, b::AbstractString)
    if length(a) != length(b)
        throw(ArgumentError("Unequal strands!"))
    end
    diffs = [i != j for (i, j) = collect(zip(a, b))]
    return count(diffs)
end
