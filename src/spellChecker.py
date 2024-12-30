import os
file_path = os.path.join(os.getcwd(), './src/words.txt')

def load_dictionary(file_path):
    with open(file_path, 'r') as lines:
        return [line.strip() for line in lines]
    
def wagner_fischer(s1, s2):
    len_s1, len_s2 = len(s1), len(s2)
    
    matrix = [[0 for _ in range(len_s2+1)] for _ in range(len_s1+1)]

    for i in range(len_s1+1):
        matrix[i][0] = i
    for j in range(len_s2+1):
        matrix[0][j] = j

    for i in range(1, len_s1+1):
        for j in range(1, len_s2+1):
            cost = 0 if s1[i-1] == s2[j-1] else 1
            insertion, deletion, substitution = matrix[i][j-1]+1, matrix[i-1][j]+1, matrix[i-1][j-1]+cost
            matrix[i][j] = min(insertion, deletion, substitution)

    return matrix[len_s1][len_s2]
    
class SpellChecker:
    def __init__(self, file_path=file_path):
        self.words = load_dictionary(file_path)
    
    def spell_check(self, w, max_suggestions=10):
        if w in self.words:
            return None
        
        suggestions = []
        for word in self.words:
            distance = wagner_fischer(w, word)
            suggestions.append((word, distance))

        suggestions.sort(key=lambda x: x[1])
        return suggestions[:max_suggestions]
