function is_equilateral(sides)
    (tri_is_valid(sides)) & (length(Set(sides))==1) ? true : false
end

function is_isosceles(sides)
    (tri_is_valid(sides)) & (length(Set(sides))<=2) ? true : false
end

function is_scalene(sides)
    (tri_is_valid(sides)) & (length(Set(sides))==3) ? true : false
end

#Helper

function tri_is_valid(sides)
    sides = sort(sides)
    length(sides)==3 && sides[1]>0 && sides[1]+sides[2]>sides[3] ? true : false
end
