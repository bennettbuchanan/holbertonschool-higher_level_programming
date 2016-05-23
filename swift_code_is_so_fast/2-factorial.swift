func factorial(N: Int) -> (Int) {
    if N < 2 {
        return 1
    }
    else {
        return N * factorial(N-1)
    }
}
