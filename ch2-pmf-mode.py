from solutions import Pmf

hist = Pmf.MakeHistFromList([1, 1, 1, 1, 1, 3, 4, 8, 8, 8, 9, 0, 5, 5, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5])

print hist.Mode()