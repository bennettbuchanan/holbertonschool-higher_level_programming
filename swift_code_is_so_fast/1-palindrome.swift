func is_palindrome(s: String) -> (Bool) {
    let reversed = String(s.characters.reverse())
    if reversed == s {
        return true
    } else {
        return false
    }
}
