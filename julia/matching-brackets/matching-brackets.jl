"""
    matching_brackets(input_string)

--- Check whether the input string has correct form
    of matching brackets.
"""
function matching_brackets(input)
    stack = []
    for char in input
        if isleftbracket(char)
            push!(stack, char)
        elseif isrightbracket(char)
            (length(stack) > 0) ? (left = pop!(stack)) : (return false)
            matchpair(left, char) ? (continue) : (return false)
        end
    end
    isempty(stack) ? true : false
end


function isleftbracket(char)
    char in ('[', '(', '{')
end


function isrightbracket(char)
    char in (']', ')', '}')
end


function matchpair(left, right)
    pairs = Dict('[' => ']', '(' => ')', '{' => '}')
    (pairs[left] == right) ? true : false
end
