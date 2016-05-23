func longest_word(text: String) -> (String) {
    // Change the string into an array of word.
    let textArr = text.characters.split{$0 == " "}.map(String.init)

     /* Set the first word as longest, then iterate through the array,
      comparing the current item in the array with the longest. Assign current
      array item as longest if length is greater. */
    var longest = textArr[0]
    var i = 0
    for word in textArr {
        if word.characters.count > longest.characters.count {
            longest = word
        }
        i += 1
    }
    return longest
}
