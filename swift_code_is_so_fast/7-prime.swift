func is_prime(N: Int) -> (Bool) {
    var tmp = N / 2
    if N <= 1 {
        return false
    } else if N <= 3 {
        return true
    }
    while tmp != 1 {
        if N % tmp == 0{
            return false
        }
        tmp -= 1
    }
    return true
}
