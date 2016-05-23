func fibonacci(N: Int) -> (Int) {
    if N < 2 {
        return N
    }
    else {
        return fibonacci(N-1) + fibonacci(N-2)
    }
}
