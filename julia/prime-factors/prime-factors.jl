function prime_factors(number::Real)
    factors = []
    max_factor = number
    factor = 2
    while number > 1 && factor < max_factor
        while number % factor == 0
            number /= factor
            push!(factors, factor)
            max_factor = sqrt(number)
        end
        factor += 1
    end
    return factors
end
