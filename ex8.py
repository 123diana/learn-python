formatter = "%r %r %r %r"
# %r gives you the raw data, or the programmer's version of the variable, also known as the "representation."

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four",)
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight.",
)