
class Solution:
    def compress(self, chars) -> int:
        last_char = None
        result = []
        count = 1
        appending_int = False
        for char in chars:
            if char == last_char:
                appending_int = True
                count += 1
            elif (char != last_char and appending_int):
                str_count = [i for i in str(count)]
                result.extend(str_count)
                result.append(char)
                count = 1
                appending_int = False
            else:
                result.append(char)
                appending_int = False
            last_char = char
        if count > 1:
            result += str(count)
        
        length = len(result)
        for i in range(length):
            chars[i] = result[i]
        
        return length

if __name__ == '__main__':
    foo = Solution()
    print(foo.compress(["a","a","b","b","c","c","c"]))
