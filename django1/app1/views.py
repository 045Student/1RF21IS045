from django.shortcuts import render

def generate_combinations(s):
    if len(s) == 1:
        return [s]
    result = []
    for i, c in enumerate(s):
        rest = s[:i] + s[i+1:]
        for p in generate_combinations(rest):
            result.append(c + p)
    return result

def home(request):
    word = "eat"  # You can change this word as needed
    combinations = generate_combinations(word)
    
    return render(request, 'index.html', {'combinations': combinations, 'word': word})