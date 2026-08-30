import numpy as np

def P(t, v): print(f"[{t}] {v}")

# Part S checks
P("S.6", (np.log2(8), np.log2(1), np.log2(0.5)))
P("S.6b", (np.log(np.e), np.log10(1000)))
P("S.6c", (np.log2(4*8), np.log2(4)+np.log2(8)))
P("S.2", (sum([4,7,2]), np.sum([4,7,2])))
P("R.9", (np.array([2,4,4,9]).mean(), np.median([2,4,4,9]),
          np.array([2,4,4,9]).var(), np.array([2,4,4,9]).std()))
P("S.7 mse", np.mean((np.array([3,5])-np.array([2,5]))**2))

# Part 1 exercise answers
P("1.30-1", (17//5, 17%5, -17//5, -17%5, 2**2**3))
P("1.30-4", (len("deep learning"), "deep learning"[0], "deep learning"[-1],
             "deep learning"[:4].upper(), "deep learning".split()))
counts={}
for ch in "mississippi": counts[ch]=counts.get(ch,0)+1
P("1.30-6", counts)
P("1.30-5", [x**2 for x in range(1,6)])

def evens(n):
    for i in range(n):
        if i%2==0: yield i
g=evens(6)
P("1.30-13", (list(g), list(g)))

# Part 2 exercise material
a = np.arange(12).reshape(3,4)
P("2ex a", a)
P("2ex sum0", a.sum(axis=0))
P("2ex sum1", a.sum(axis=1))
P("2ex keepdims", a.sum(axis=1, keepdims=True).shape)
P("2ex col", a[:,2])
P("2ex block", a[1:3, 1:3])
P("2ex mask", a[a % 3 == 0])
P("2ex norm rows", np.round(a / a.sum(axis=1, keepdims=True), 3))
b = np.array([1,2,3,4])
P("2ex bcast", a + b)
try:
    a + np.array([1,2,3])
except ValueError as e:
    P("2ex bcast err", str(e))
v = np.array([1.,2.,3.])
P("2ex outer", np.outer(v, v))
P("2ex einsum outer", np.einsum('i,j->ij', v, v))
P("2ex softmax", np.round(np.exp(v - v.max())/np.exp(v - v.max()).sum(), 6))
x = np.arange(6)
sl = x[1:4]; sl[0] = 99
P("2ex view", x)
y = np.arange(6); cp = y[[1,2,3]]; cp[0] = 99
P("2ex fancy copy", y)
P("2ex argmax", (np.array([[1,9],[7,3]]).argmax(), np.array([[1,9],[7,3]]).argmax(axis=1)))
rng = np.random.default_rng(7)
P("2ex rng", np.round(rng.random(3), 6))
P("2ex dtype", (np.array([1,2]).dtype, np.array([1,2]).astype(np.float32).dtype))
P("2ex flat", np.arange(6).reshape(2,3).ravel())
P("2ex where", np.where(np.array([1,-2,3]) > 0, 1, 0))
P("2ex clip", np.clip(np.array([-1.,0.5,2.]), 0, 1))
P("2ex allclose", np.allclose([0.1+0.2], [0.3]))
