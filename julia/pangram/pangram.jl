"""
    ispangram(input)

Return `true` if `input` contains every alphabetic character (case insensitive).

"""
function ispangram(input)
        alphs = Set("abcdefghijklmnopqrstuvwxyz")
        if isempty(setdiff!(alphs, Set(lowercase(input))))
            return true
        end
        return false
end

