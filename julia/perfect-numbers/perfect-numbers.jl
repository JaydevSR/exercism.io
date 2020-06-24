function isperfect(number::Int)
    if number <= 0
        throw(DomainError(number, "Only Natural Numbers!"))
    end
    factors = [i for i in 1:number÷2 if number % i == 0]
    return sum(factors) == number
end

function isabundant(number::Int)
    if number <= 0
        throw(DomainError(number, "Only Natural Numbers!"))
    end
    factors = [i for i in 1:number÷2 if number % i == 0]
    return sum(factors) > number
end

function isdeficient(number::Int)
    if number <= 0
        throw(DomainError(number, "Only Natural Numbers!"))
    end
    factors = [i for i in 1:number÷2 if number % i == 0]
    return sum(factors) < number
end