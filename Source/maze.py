from random import shuffle, randrange
 
def make_maze(w = 16, h = 16):
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    ver = [["1 "] * w + ['1'] for _ in range(h)] + [[]]
    hor = [["11"] * w + ['1'] for _ in range(h + 1)]
 
    def walk(x, y):
        vis[y][x] = 1
 
        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]: continue
            if xx == x: hor[max(y, yy)][x] = "1 "
            if yy == y: ver[y][max(x, xx)] = "  "
            walk(xx, yy)
 
    walk(randrange(w), randrange(h))
 
    s = ""
    for (a, b) in zip(hor, ver):
        s += ''.join(a + ['\n'] + b + ['\n'])

    out = s.strip().split("\n")
    for i in range(len(out)):
    	out[i] = list(out[i])
    
    return out
 
if __name__ == '__main__':
    maze = make_maze()
    print maze