def originalDigits(self, s: str) -> str:
        """
        credit to ZitaoWang for being a beast (adapted sol.)
        The key to this solution is in the set-up in identifying
        that each number has its own unique character that defines
        it. Some don't have this characteristic but they become 
        defined as the ones before it do
        """
        char2word = {'z': 'zero', 'w': 'two', 'u': 'four', 'x': 'six', 'g': 'eight', 'o': 'one', 'r': 'three',                      'f': 'five', 's': 'seven','i': 'nine'}
        word2int = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', \
                    'four': '4', 'five': '5', 'six': '6', 'seven': '7', \
                    'eight': '8', 'nine': '9'}
        kei = list(char2word.keys())
        arr = []
        all = dict()
        
        # fill dict with all letters
        for letter in s:
            if letter in all:
                all[letter] += 1
            else:
                all[letter] = 1
        
        #iterate through each key
        for key in kei:
            if key in all:
                while all[key] != 0:
                    # take the key and output it to an array while subtracting the letters from all
                    for i in range(len(char2word[key])):
                        print(char2word[key][i])
                        all[char2word[key][i]] -= 1
                    arr.append(word2int[char2word[key]])
        arr.sort()
        return ''.join(arr)