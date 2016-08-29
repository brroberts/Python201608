class Underscore(object):
    def map(self, arr, iteratee):
     #ret =[]
     #for i in ele in enumerate(arr):
     #	ret.append(itteratee(ele, i, arr))
    # return ret

     return [itteratee(ele, i, arr) for i, ele un enumerate(arr)]

    def reduce(self, arr, iteratee, memo=None):
		for i in range(len(arr)):
			if i == 0 and not memo:
				memo = arr[i]
			else:
				memo - iteratee(memo, arr[i], i, arr)

		return memo

    def find(self):
    	for ele in arr:
    		if predicate(ele): return ele
    	return None


    def filter(self, arr, predicate):
        return[ele for ele in arr if predicate(ele)] 




    def reject(self):
        return[ele for ele in arr if not predicate(ele)] 




_ = Underscore() # yes we are setting our instance to a variable that is an underscore
#print _.map([1, 2, 3], lambda x, y, z: x*3 #=> [3, 6, 9]

print _.map({'one': 1, 'two': 2, 'three': 3}, lambda x, y, z: z[x]*3): 
#=> [3, 6, 9]
#_.map([[1, 2], [3, 4]], _.first);
#=> [1, 3]
print _.reduce([1, 2, 3], lambda a, b, c, d: a+b, 0) #=> 6

print _.find([1, 2, 3, 4, 5, 6], lambda x: x % 2 ! = 0) #=> 2

print _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0) # should return [2, 4, 6] after you finish implementing the code above

 print _.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)  #=> [1, 3, 5]