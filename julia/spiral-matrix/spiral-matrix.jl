function spiral_matrix(n)
    rotate_90 = Dict(
        ( 0,  1) => [ 1,  0],
        ( 1,  0) => [ 0, -1],
        ( 0, -1) => [-1,  0],
        (-1,  0) => [ 0,  1]
        )
    spi_mat = zeros(Int64, n, n)
    pos, vel = [1, 1], [0, 1]
    for i ∈ 1:n^2
        spi_mat[pos...] = i
        pos_next = pos + vel
        # Last condition in `if` exploits short circuiting
        if !(1 <= pos_next[1] <= n) || !(1 <= pos_next[2] <= n) || spi_mat[pos_next...] != 0
            vel = rotate_90[Tuple(vel)]
        end
        pos = pos + vel
    end
    return spi_mat
end