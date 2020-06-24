function clean(phone_number)
    phone_number = strip(phone_number)
    reg = r"^(?:\+?1)?\s?\(?([2-9]\d{2})\)?[\-\. ]*([2-9]\d{2})[\-\. ]*(\d{4})$"
    found_match = match(reg, phone_number)
    if typeof(found_match) == RegexMatch
        str = found_match[1]*found_match[2]*found_match[3]
        return str
    end
    return nothing
end

