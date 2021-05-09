"""
In order to improve customer experience, Amazon has developed a system to provide recommendations to the customer regarding the item they can purchase. Based on historical customer purchase information, an item association can be defined as - If an item A is ordered by a customer, then item B is also likely to be ordered by the same customer (e.g. Book 1 is frequently orderered with Book 2). All items that are linked together by an item association can be considered to be in the same group. An item without any association to any other item can be considered to be in its own item association group of size 1.

Given a list of item association relationships(i.e. group of items likely to be ordered together), write an algorithm that outputs the largest item association group. If two groups have the same number of items then select the group which contains the item that appears first in lexicographic order.

Input
The itput to the function/method consists of an argument - itemAssociation, a list containing paris of string representing the items that are ordered together.

Output
Return a list of strings representing the largest association group sorted lexicographically.

Example
Input:
itemAssociation: [
[Item1, Item2],
[Item3, Item4],
[Item4, Item5]
]

Output:
[Item3, Item4, Item5]

Explanation:
There are two item association groups:
group1: [Item1, Item2]
group2: [Item3,Item4,Item5]
In the available associations, group2 has the largest association. So, the output is [Item3, Item4, Item5].

Helper Description in java
The following class is used to represent a Pair of strings and is already implemented in the default code (Do not write this definition again in your code):

class PairString
{
	String first;
	String second;
	
	PairString(String first, String second)
	{
		this.first = first;
		this.second = second;
	}
}
Method Signature to Implement in java
Java

List<String> LargestItemAssociation(List<PairString> itemAssociation)
{
}
"""



        class PairString:
            def __init__(self, first, second):
                self.first = first
                self.second = second
            
        def largestItemAssociation(itemAssociation):
            itemsMap = {}
            for i in itemAssociation:
                if i.first not in itemsMap.keys():
                    itemsMap[i.first] = []
                if i.second not in itemsMap.keys():
                    itemsMap[i.second] = []

                itemsMap[i.first].append(i.second)
                itemsMap[i.second].append(i.first)

            output = []
            visited = set()
            print(itemsMap)

            for i in itemsMap.keys():
                res = []
                if i not in visited:
                    dfs(i,res,visited, itemsMap)
                    res.sort()
                    if len(output)==0:
                        output.append(res)
                    elif (len(res)>len(output[0])):
                        output[0]=res
                    elif(len(res)==len(output)):
                        if (res[0] < output[0][0]):
                            output[0] = res
            return output

        def dfs(key,res,visited,itemsMap):
            if key not in visited:
                visited.add(key)
                res.append(key)
                for nei in itemsMap[key]:
                    if nei in visited:
                        continue
                    dfs(nei,res,visited,itemsMap)
            return res


        # arr1 = PairString("Item1", "Item2")
        # arr2 = PairString("Item3", "Item4")
        # arr3 = PairString("Item4", "Item5")


        a = PairString("Item1", "Item2")
        b =  PairString("Item2", "Item8")
        c = PairString("Item2", "Item10")
        d =  PairString("Item10", "Item12")
        e =  PairString("Item10", "Item4")
        f =  PairString("Item10", "Item3")
        g = PairString("Item3", "Item4")
        h = PairString("Item4", "Item5")

        itemAssociation = []
        itemAssociation.append(a)
        itemAssociation.append(b)
        itemAssociation.append(c)
        itemAssociation.append(d)
        itemAssociation.append(e)
        itemAssociation.append(f)
        itemAssociation.append(g)
        itemAssociation.append(h)

        out = largestItemAssociation(itemAssociation)
        print(out)
