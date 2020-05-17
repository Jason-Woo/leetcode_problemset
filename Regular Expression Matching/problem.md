Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false

我们假设当前问题是考虑 s 的第 i 个字母，p 的第 j 个字母，所以这时的子问题是 s[0...i] 和 p[0...j] 是否匹配：

* p[j] 是字母，并且 s[i] == p[j]，当前子问题成立与否取决于子问题 s[0...i-1] 和 p[0...j-1] 是否成立
* p[j] 是 '.'，当前子问题成立与否取决于子问题 s[0...i-1] 和 p[0...j-1] 是否成立
* p[j] 是字母，并且 s[i] != p[j]，当前子问题不成立
* p[j] 是 '*'，s[i] == p[j - 1]，或者 p[j - 1] == '.'， 当前子问题成立与否取决于子问题 s[0...i-1] 和 p[0...j] 是否成立
* p[j] 是 '*'，s[i] != p[j - 1]，当前子问题正确与否取决于子问题 s[0...i] 是否匹配 p[0,...j-2]

作者：P.yh
链接：https://juejin.im/post/5d39f62bf265da1b6a34d9fb
来源：掘金
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。